# Glassmorphism: CSS / SVG / GSAP (HyperFrames)

Same rules as `../SKILL.md`. HyperFrames renders in headless Chrome, which supports `backdrop-filter`. One paused GSAP timeline (read `hyperframes-core` first).

## Frosted panel

```css
.glass {
  background: rgba(255,255,255,0.14);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border-radius: 32px;
  border: 1.5px solid rgba(255,255,255,0.35);
  box-shadow: 0 30px 80px rgba(10,10,40,0.18), inset 0 1px 0 rgba(255,255,255,0.45);
}
.glass::after { /* frost grain */
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background-image: url("noise.png"); opacity: .05; mix-blend-mode: overlay; }
.glass.dark { background: rgba(12,14,30,0.32); border-color: rgba(255,255,255,0.18); }
```
Gradient edge: a pseudo-element with `padding: 1.5px; background: linear-gradient(135deg, rgba(255,255,255,.6), rgba(255,255,255,.1)); -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask-composite: exclude;`.

For live UI (not video): add `@media (prefers-reduced-transparency: reduce) { .glass { background: rgba(255,255,255,.85); backdrop-filter: none; } }` and an `@supports not (backdrop-filter: blur(1px))` fallback.

## Living background

```css
.orb { position: absolute; width: 600px; height: 600px; border-radius: 50%; filter: blur(120px); opacity: .9; }
```
```js
// seek-safe drift: tween on the timeline, yoyo
gsap.utils.toArray(".orb").forEach((o, i) =>
  tl.to(o, { x: 160 * (i % 2 ? 1 : -1), y: 120, duration: 8 + i * 2, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0));
```

## Liquid lensing (SVG filter)

```html
<svg width="0" height="0"><filter id="lens" x="-10%" y="-10%" width="120%" height="120%">
  <feImage href="lensmap.png" result="map"/>   <!-- grey with bright/dark ramps at edges -->
  <feDisplacementMap in="SourceGraphic" in2="map" scale="40" xChannelSelector="R" yChannelSelector="G"/>
</filter></svg>
```
Apply it to a copy of the background content clipped to the glass shape (more reliable for video than `backdrop-filter: url(#lens)`), then layer the frosted panel styles on top.

## Gooey merge

```html
<filter id="goo"><feGaussianBlur in="SourceGraphic" stdDeviation="14" result="b"/>
  <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 28 -12"/></filter>
```
Put the blobs in a group with `filter: url(#goo)`, then use that group as a mask for the glass layer.

## Moves

```js
const beat = 0.5, at = n => n * beat;
// panel rise with blur ramp
tl.fromTo(".card", { y: 100, opacity: 0, "--bl": "0px" },
  { y: 0, opacity: 1, "--bl": "24px", duration: 0.9, ease: "expo.out", stagger: 0.12 }, at(1));
// (CSS: .card { backdrop-filter: blur(var(--bl)); } with @property --bl registered as <length>)
// light sweep
tl.fromTo(".card .sheen", { xPercent: -120 }, { xPercent: 220, duration: 0.9, ease: "power2.inOut" }, at(2));
// tilt with parallax
tl.to(".card", { rotationY: 8, rotationX: -4, transformPerspective: 1200, duration: 1.2, ease: "power2.inOut" }, at(3));
// liquid split
tl.to(".drop", { x: (i) => [-140, 0, 140][i], duration: 0.7, ease: "back.out(2)" }, at(4));
```
