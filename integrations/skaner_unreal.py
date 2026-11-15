"""Read Skaner Studio static mesh packages inside Unreal Editor."""

from hashlib import sha256
from io import BytesIO
import json
import math
from pathlib import Path
from queue import Empty, Queue
import re
import secrets
from threading import Event, Thread
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener
from zipfile import ZipFile

import unreal


LIMIT=100*1024**2
BRIDGE=None


def checked_package(data):
    if not 30<=len(data)<=LIMIT:
        raise ValueError('Pakiet ma nieprawidłowy rozmiar.')
    with ZipFile(BytesIO(data)) as archive:
        names=archive.namelist()
        if len(names)!=len(set(names)) or sum(row.file_size for row in archive.infolist())>LIMIT:
            raise ValueError('Pakiet jest zbyt duży lub zawiera powielone pliki.')
        if archive.getinfo('manifest.json').file_size>64*1024:
            raise ValueError('Manifest jest zbyt duży.')
        manifest=json.loads(archive.read('manifest.json'))
        asset,folder=manifest['asset'],manifest['folder']
        if (manifest.get('schema')!='skaner.unreal-static.v1'
                or not re.fullmatch(r'SM_[A-Za-z0-9_]{1,56}',asset)
                or not re.fullmatch(r'/Game(?:/[A-Za-z0-9_]{1,48}){1,8}',folder)):
            raise ValueError('Nieprawidłowy typ pakietu, nazwa lub folder Unreal.')
        bounds=manifest['dimensions_cm']
        if (not isinstance(bounds,list) or len(bounds)!=3
                or any(type(value) not in (int,float) or not math.isfinite(value) or not 0<value<=1000000 for value in bounds)):
            raise ValueError('Nieprawidłowe wymiary modelu w cm.')
        rows=manifest['levels']
        if not isinstance(rows,list) or not 1<=len(rows)<=6:
            raise ValueError('Pakiet musi zawierać od 1 do 6 poziomów.')
        files=[]
        for i,row in enumerate(rows):
            filename=f'{asset}_LOD{i}.fbx'
            if row.get('file')!=filename or row.get('index')!=i:
                raise ValueError('Nieciągła numeracja poziomów LOD.')
            blob=archive.read(filename)
            if not blob.startswith(b'Kaydara FBX Binary  \0\x1a\0') or sha256(blob).hexdigest()!=row.get('sha256'):
                raise ValueError(f'Plik LOD{i} jest uszkodzony.')
            files.append((filename,blob))
    return manifest,files


def import_bytes(data):
    manifest,files=checked_package(data)
    asset,folder=manifest['asset'],manifest['folder']
    target=f'{folder}/{asset}'
    assets=unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
    static=unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem)
    if not assets or not static:
        raise RuntimeError('Potrzebne są podsystemy Editor Asset i Static Mesh.')
    if assets.does_asset_exist(target):
        raise ValueError(f'Zasób {target} już istnieje. Wybierz inną nazwę.')
    token=secrets.token_hex(8)
    # Source files remain in Saved for Unreal's own reimport tools.
    source=Path(unreal.Paths.convert_relative_path_to_full(unreal.Paths.project_saved_dir()))/'SkanerStudio'/token
    source.mkdir(parents=True,exist_ok=False)
    for filename,blob in files:
        (source/filename).write_bytes(blob)
    stage=f'/Game/Skaner_Import_{token}'
    task=unreal.AssetImportTask()
    task.filename=str(source/files[0][0])
    task.destination_path=stage
    task.destination_name=asset
    task.automated=True
    task.replace_existing=False
    task.save=False
    factory=getattr(unreal,'FbxFactory',None)
    if factory is not None:
        task.factory=factory()
    options=unreal.FbxImportUI()
    options.automated_import_should_detect_type=False
    options.mesh_type_to_import=unreal.FBXImportType.FBXIT_STATIC_MESH
    options.import_mesh=True
    options.import_as_skeletal=False
    options.import_materials=False
    options.import_textures=False
    options.import_animations=False
    settings=options.static_mesh_import_data
    settings.combine_meshes=True
    settings.convert_scene=True
    settings.convert_scene_unit=True
    settings.import_uniform_scale=1.0
    if hasattr(settings,'import_mesh_lods'):
        settings.import_mesh_lods=False
    else:
        settings.import_mesh_lo_ds=False
    settings.transform_vertex_to_absolute=True
    task.options=options
    moved=False
    try:
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
        found=task.get_objects()
        meshes=[item for item in found if isinstance(item,unreal.StaticMesh)]
        if len(meshes)!=1 or not meshes[0].get_path_name().startswith(stage+'/'):
            raise RuntimeError('Import FBX nie utworzył jednej siatki w folderze roboczym.')
        mesh=meshes[0]
        for index,(filename,_) in enumerate(files[1:],1):
            if static.import_lod(mesh,index,str(source/filename))!=index:
                raise RuntimeError(f'Unreal odrzucił LOD{index}.')
        if mesh.get_num_lods()!=len(files):
            raise RuntimeError('Unreal zwrócił nieoczekiwaną liczbę LOD.')
        bounds=mesh.get_bounds().box_extent
        expected=manifest['dimensions_cm']
        measured=(2*bounds.x,2*bounds.y,2*bounds.z)
        if (abs(measured[2]-expected[2])>max(.02,expected[2]*.01)
                or any(abs(a-b)>max(.02,b*.01) for a,b in zip(sorted(measured[:2]),sorted(expected[:2])))):
            raise RuntimeError(f'Import zmienił wymiary. Oczekiwano {expected} cm, otrzymano {measured}.')
        if assets.does_asset_exist(target) or not assets.rename_loaded_asset(mesh,target):
            raise RuntimeError('Nie udało się przenieść zasobu do folderu docelowego.')
        moved=True
        if not assets.save_loaded_asset(mesh,only_if_is_dirty=False):
            raise RuntimeError('Nie udało się zapisać zasobu w Unreal.')
        return f'{target} · {len(files)} poziomów · {measured[2]:.3g} cm wysokości'
    except Exception:
        if moved:
            assets.delete_asset(target)
        raise
    finally:
        if assets.does_directory_exist(stage):
            assets.delete_directory(stage)


def import_skaner_package(path):
    source=Path(path)
    if source.stat().st_size>LIMIT:
        raise ValueError('Pakiet przekracza 100 MB.')
    message=import_bytes(source.read_bytes())
    unreal.log('Skaner Studio: '+message)
    return message


class LocalOnly(HTTPRedirectHandler):
    def redirect_request(self,*_args,**_kwargs):
        return None


class Companion:
    def __init__(self,url,key):
        target=urlsplit(url)
        if (target.scheme!='http' or target.hostname!='127.0.0.1' or not target.port
                or target.username or target.password or target.query or target.fragment or target.path not in ('','/')
                or not re.fullmatch(r'[A-Za-z0-9_-]{32}',key)):
            raise ValueError('Skopiuj adres i kod lokalnego mostu z programu Studio.')
        self.base=f'http://127.0.0.1:{target.port}/api/unreal/'
        project=Path(unreal.Paths.project_dir().rstrip('/\\')).name
        self.headers={'X-Skaner-Unreal-Key':key,'X-Skaner-Unreal-Client':secrets.token_hex(12),
                      'X-Skaner-Unreal-Project':re.sub(r'[^A-Za-z0-9_. -]','',project)[:80]}
        self.stop=Event()
        self.pending=Queue(maxsize=1)
        self.results=Queue(maxsize=1)
        self.tick_id=unreal.register_slate_post_tick_callback(self.tick)
        Thread(target=self.poll,name='SkanerUnreal',daemon=True).start()

    def request(self,path,body=None,limit=8192):
        data=json.dumps(body).encode() if body is not None else None
        headers=dict(self.headers)
        if data:
            headers['Content-Type']='application/json'
        with build_opener(ProxyHandler({}),LocalOnly()).open(Request(self.base+path,data,headers),timeout=12) as response:
            received=response.read(limit+1)
        if len(received)>limit:
            raise ValueError('Odpowiedź Studio przekracza limit.')
        return received

    def poll(self):
        result=None
        pending=False
        while not self.stop.wait(.7):
            try:
                if pending and result is None:
                    try:
                        result=self.results.get_nowait()
                    except Empty:
                        continue
                if result:
                    self.request('result/'+result[0],result[1])
                    result=None
                    pending=False
                claimed=json.loads(self.request('claim')).get('job')
                if claimed and re.fullmatch(r'[a-f0-9]{24}',claimed):
                    data=self.request('package/'+claimed,limit=LIMIT)
                    self.pending.put_nowait((claimed,data))
                    pending=True
            except HTTPError as error:
                if error.code in (403,409):
                    self.stop.set()
            except (OSError,ValueError):
                continue

    def tick(self,_delta):
        if self.stop.is_set():
            self.close()
            return
        try:
            job,data=self.pending.get_nowait()
        except Empty:
            return
        try:
            result={'ok':True,'message':import_bytes(data)}
            unreal.log('Skaner Studio: '+result['message'])
        except Exception as error:
            result={'ok':False,'message':str(error)[:600]}
            unreal.log_error('Skaner Studio: '+result['message'])
        self.results.put_nowait((job,result))

    def close(self):
        self.stop.set()
        if self.tick_id is not None:
            unreal.unregister_slate_post_tick_callback(self.tick_id)
            self.tick_id=None


def connect_skaner(url,key):
    global BRIDGE
    if BRIDGE:
        BRIDGE.close()
    BRIDGE=Companion(url,key)
    unreal.log('Skaner Studio: uruchomiono lokalny odbiornik.')


def disconnect_skaner():
    global BRIDGE
    if BRIDGE:
        BRIDGE.close()
        BRIDGE=None
