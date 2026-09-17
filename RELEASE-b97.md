# b97 web — drawn-solid sculpt and multi-object transforms

Two reproduced regressions corrected:
- Group transform mutated and shared the accumulated delta matrix between
  objects. Each selected object now receives an independent delta × start.
- Short incidental cap diagonals restricted a 2 mm build-up brush to roughly
  0.05 mm on a drawn outline. Build-up brushes use a smooth brush-direction
  field capped by radius rather than the shortest triangulation edge.

Regression checks: translation, rotation and scale on three distinct objects;
selection-order independence; repeated preview idempotence; unchanged start
matrices. Draw an ellipse from 180 input points, apply inflate/clay/grab/deflate
consecutively, then boolean subtract and union with a positioned cutter.
Observed sculpt displacement after correction: 0.78/1.20/1.81/1.11 mm.
Before correction, build-up/deflate was only 0.05 mm.

Type checking, production build, geometry and preview tests passed.
Physical iPhone gesture validation remains unverified. These fixes address
reproduced causes, not a claim that every user model or tool is now verified.
The Windows executable is not updated by this web publication.
