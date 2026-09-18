# b99 — touch face/edge handle ownership

Reproduced the reported selection conflict in the actual application's touch
handler: a handle-owned pointerdown still called selectFaceAt, replacing the
selection while TransformControls was starting the manipulation.

The face/edge/vertex gizmo now owns touches when dragging, when its axis was
hit, or while its drag anchor is active. Ordinary surface touches still select.
The shared selection entry point rejects selection during an active drag.
Synthetic clicks are suppressed throughout a drag and for 600 ms after release.

Regression test failed on b98 and passes with this patch. Type check,
group-transform regression, production build and offline-cache simulation pass.
No physical iPhone test performed; device gesture validation remains pending.
