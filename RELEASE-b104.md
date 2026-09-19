# b104 — logical surfaces of drawn rods

- Drawn rods with a saved curve path expose four continuous side regions and two end caps. Closed paths expose four sides.
- The whole-surface selector follows the local curve frame around bends rather than selecting individual render triangles.
- Face edits preserve the curve guide, including when the object's transform is baked; guides are included in project/recovery data.
- Exact face selection uses all selected source triangles, without the former 64-triangle seed limit. Additive selection no longer truncates at 64 triangles or 400 face IDs.
- Desktop face editing now uses the same local geometry engine as the web version.

Verification: TypeScript, production build, six-region bent-rod edits and repeated edits, rotation/translation invariance, serialized guide, GLB-to-OBJ triangle mapping, additive selection, touch handle ownership, brush displacement and consecutive strokes, subtraction/union, OBJ/STL roundtrip, group transforms, service-worker offline assets.

Limits: no physical iPhone or visual UI verification for this release. Logical rod regions require the original saved path or a retained surface guide; arbitrary imported meshes and legacy rods whose path was already discarded use normal surface selection. Topology-changing operations such as Boolean/sculpting can discard the guide. This is mesh editing, not a full CAD boundary-representation kernel.
