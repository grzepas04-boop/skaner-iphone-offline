# b96 web — 2026-09-18

Open https://grzepas04-boop.github.io/skaner-iphone-offline/?offline=1

Includes direct sculpt gesture fixes, conforming local subdivision repair,
closed stroke previews, signed face inset preview correction, WASM loading
retry, and automatic on-device engine selection on GitHub Pages.

Offline installation now caches an explicit complete build asset list,
including workers and WASM kernels. Older version directories are retained.
No personal models or project data are included in this publication.

Passed before publication:
- TypeScript type check and production Vite build.
- Grab distance, radius bound, welded adjacency, closed tube preview tests.
- Offline Manifold sculpt displacement, smooth/flatten/scrape, zero strength,
  curved rod creation and OBJ/STL roundtrip tests.
- Static relative-path and complete asset manifest checks.
- Service-worker installation and offline asset/navigation simulation.

Limitations: no physical iPhone/Safari gesture, memory or installation test
was available. These automated checks do not establish full mobile usability
or parity with Nomad/Blender. Start with small projects and export backups.
