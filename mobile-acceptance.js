/* Physical-device acceptance probe. It measures the real browser, not a
 * desktop throttle. Geometry actions remain manual because a synthetic touch
 * must never be reported as a successful sculpt stroke. */
(function () {
  const root = window;
  const metrics = { startedAt: 0, endedAt: 0, frames: 0, longFrames: 0, maxFrameMs: 0,
    touchSamples: 0, pointerSamples: 0, errors: [], device: {
      userAgent: navigator.userAgent, dpr: devicePixelRatio,
      width: innerWidth, height: innerHeight, touchPoints: navigator.maxTouchPoints || 0,
      webgl: false, worker: typeof Worker !== "undefined" } };
  try { const c = document.createElement("canvas"); metrics.device.webgl = !!(c.getContext("webgl2") || c.getContext("webgl")); } catch (_) {}
  let running = false, last = 0, raf = 0;
  function frame(now) { if (!running) return; if (last) { const ms = now - last; metrics.frames++; metrics.maxFrameMs = Math.max(metrics.maxFrameMs, ms); if (ms > 16.667) metrics.longFrames++; } last = now; raf = requestAnimationFrame(frame); }
  function onPointer(event) { if (event.pointerType === "touch") metrics.pointerSamples++; }
  function onTouch(event) { metrics.touchSamples += event.touches?.length || 1; }
  function onError(event) { metrics.errors.push(String(event.message || event.reason || "unknown error")).slice(-20); }
  async function run(durationMs = 5000) {
    if (running) return root.__skanerMobileQA.result();
    running = true; last = 0; metrics.startedAt = performance.now();
    addEventListener("pointermove", onPointer, { passive: true }); addEventListener("touchmove", onTouch, { passive: true }); addEventListener("error", onError);
    raf = requestAnimationFrame(frame); await new Promise(resolve => setTimeout(resolve, durationMs));
    running = false; cancelAnimationFrame(raf); metrics.endedAt = performance.now();
    removeEventListener("pointermove", onPointer); removeEventListener("touchmove", onTouch); removeEventListener("error", onError);
    return root.__skanerMobileQA.result();
  }
  function result() {
    const elapsed = Math.max(1, metrics.endedAt - metrics.startedAt);
    return { ...metrics, elapsedMs: elapsed, averageFps: metrics.frames * 1000 / elapsed,
      frameBudgetPass: metrics.maxFrameMs <= 50 && metrics.longFrames / Math.max(1, metrics.frames) < .15,
      geometrySmokeAvailable: typeof root.__skanerApi === "function" && typeof root.__skanerState === "function" };
  }
  root.__skanerMobileQA = { run, result, metrics, instructions: "Włącz Rzeźba, wykonaj pociągnięcie, Wygładź, Boolean i Fazowanie ręcznie; zapisz wyniki po każdym scenariuszu." };
  if (new URLSearchParams(location.search).get("qa") === "1") {
    const panel = document.createElement("pre"); panel.id = "mobile-qa-panel"; panel.style.cssText = "position:fixed;z-index:9999;left:8px;bottom:8px;max-width:calc(100vw - 16px);max-height:30vh;overflow:auto;background:#111d;color:#d8f5e5;padding:8px;font:11px monospace;border:1px solid #6c9;"; document.body.append(panel);
    const tick = () => { panel.textContent = JSON.stringify(root.__skanerMobileQA.result(), null, 2); if (!running) setTimeout(tick, 500); else requestAnimationFrame(tick); }; tick();
  }
})();
