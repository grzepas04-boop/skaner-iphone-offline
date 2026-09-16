const CACHE="skaner-studio-offline-release-51-topology-phase2";
const SHELL=["./?offline=1","./manifest.webmanifest","./assets/skaner-icon.png"];
self.addEventListener("install",event=>event.waitUntil((async()=>{
  const cache=await caches.open(CACHE),response=await fetch("./"),html=await response.text();
  await cache.put("./",new Response(html,{headers:{"Content-Type":"text/html;charset=utf-8"}}));
  const discovered=[...html.matchAll(/(?:src|href)=["']([^"']+)["']/g)].map(match=>match[1]).filter(path=>path.startsWith("./")||path.startsWith("/"));
  const scripts=discovered.filter(path=>path.endsWith(".js"));
  const wasm=[];for(const script of scripts){const source=await (await fetch(script)).text();for(const match of source.matchAll(/assets\/[A-Za-z0-9_.-]+\.wasm/g))wasm.push(`./${match[0]}`);}
  await cache.addAll([...new Set([...SHELL,...discovered,...wasm])]);
  await self.skipWaiting();
})()));
self.addEventListener("activate",event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",event=>{
  const req=event.request,url=new URL(req.url);if(req.method!=="GET"||url.origin!==location.origin||url.pathname.includes("/api/"))return;
  if(req.mode==="navigate"){
    event.respondWith(fetch(req).then(response=>{
      if(response.ok){const copy=response.clone();caches.open(CACHE).then(cache=>cache.put("./",copy));}
      return response;
    }).catch(()=>caches.match("./").then(hit=>hit||Response.error())));
    return;
  }
  event.respondWith(caches.match(req).then(hit=>hit||fetch(req).then(response=>{if(response.ok){const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(req,copy));}return response;})));
});
