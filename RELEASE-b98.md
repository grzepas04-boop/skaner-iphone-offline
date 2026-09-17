# b98 web — brush width, transformed sculpt and stable group shapes

Includes b97 fixes plus:
- Explicit Zwęź pędzlem / Rozszerz pędzlem tools, with radius-bound tangential
  deformation and live preview, independent of tiny cap triangle edges.
- Sculpt computes in world millimetres for rotated/scaled objects and returns
  geometry to object coordinates. Each new layer stroke records its frame
  for repeatable replay; legacy strokes keep their previous local frame.
- Group pivots retain the affine residual caused by non-uniform scaling of
  rotated solids. Rendering, subsequent moves and export keep the full matrix.
- Obsolete asynchronous scene rebuilds cannot replace a newer scene.

Passed: type check, production build, closed stroke preview, group order and
idempotence tests, affine render/store agreement, consecutive sculpt on drawn
outline, subtract/union after sculpt, narrowing/widening brushes, world-space
sculpt equivalence on a rotated non-uniformly scaled object, offline manifest
and service-worker simulation. Public file checks performed after deployment.

Not tested: physical iPhone gestures/performance, user's specific project,
large-mesh exhaustive coverage or full Blender/Nomad parity. The Windows EXE
has not been replaced by this web release. Save projects before refreshing.
