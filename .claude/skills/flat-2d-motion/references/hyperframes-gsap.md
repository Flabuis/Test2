# Flat 2D: HyperFrames / GSAP

Same rules as `../SKILL.md`. Inline SVG artwork (exported from Illustrator with named groups) + one paused GSAP timeline (read `hyperframes-core` first). GSAP plugins MorphSVG, DrawSVG and MotionPath are free in current GSAP releases.

## SVG prep

- Export from Illustrator as SVG, Styling: Presentation Attributes, Object IDs: Layer Names, Decimal 2.
- Set each part's pivot with `transformOrigin` in GSAP (e.g. `"50% 0%"` for a hanging arm).

## Eases

| Use | GSAP ease |
|---|---|
| Default move | `power2.inOut` |
| Snappy UI | `power3.out` |
| Soft pop | `back.out(1.4)` |
| Settle into pose | `power3.out` with a slightly longer duration |
| Mechanical | `none` |

## Moves

```js
gsap.registerPlugin(MorphSVGPlugin, DrawSVGPlugin, MotionPathPlugin);
const beat = 0.5, at = n => n * beat;
// assemble in reading order with soft pops
tl.from("#scene1 .part", { scale: 0, transformOrigin: "50% 100%", duration: 0.4, ease: "back.out(1.4)", stagger: 0.08 }, at(0));
// stroke draw-on then fill
tl.from("#route", { drawSVG: "0%", duration: 0.8, ease: "power2.inOut" }, at(2))
  .from("#pin", { scale: 0, transformOrigin: "50% 100%", duration: 0.35, ease: "back.out(1.6)" }, at(2) + 0.65);
// morph circle -> icon
tl.to("#blob", { morphSVG: "#icon-shape", duration: 0.6, ease: "power2.inOut" }, at(4));
// follow-through: child lags the parent
tl.to("#arm", { rotation: -40, duration: 0.4, ease: "power2.inOut" }, at(5))
  .to("#hand", { rotation: -25, duration: 0.4, ease: "power2.inOut" }, at(5) + 0.08);
// arc throw
tl.to("#ball", { motionPath: { path: "#arc", align: "#arc", alignOrigin: [0.5, 0.5] }, duration: 0.7, ease: "power1.inOut" }, at(6));
// circle wipe
tl.fromTo("#wipe", { attr: { r: 0 } }, { attr: { r: 1300 }, duration: 0.6, ease: "power2.inOut" }, at(8));
```

## Idle loops (seek-safe: derive from timeline time)

```js
tl.to("#char", { scaleY: 1.015, transformOrigin: "50% 100%", duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: 7 }, 0);
[1.2, 4.9, 8.6].forEach(t => tl.to("#eyes", { scaleY: 0.1, transformOrigin: "50% 50%", duration: 0.06, yoyo: true, repeat: 1 }, t));
```
