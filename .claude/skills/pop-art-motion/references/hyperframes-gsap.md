# Pop art: HyperFrames / GSAP

Same rules as `../SKILL.md`. One paused GSAP timeline (read `hyperframes-core` first). Keep it seek-safe: no `Math.random()` at runtime; precompute seeded values.

## CSS building blocks

```css
:root { --red:#E4002B; --yellow:#FFE600; --blue:#0077C8; --ink:#111; --paper:#F4EBD9; --line:10px; }
/* Ben-Day dots */
.dots { background-color: var(--paper);
  background-image: radial-gradient(var(--red) 30%, transparent 31%),
                    radial-gradient(var(--red) 30%, transparent 31%);
  background-size: 24px 24px; background-position: 0 0, 12px 12px; }
/* outlined comic object with hard shadow */
.pop { border: var(--line) solid var(--ink); box-shadow: 14px 14px 0 var(--ink); }
/* SFX lettering */
.sfx { font: 400 180px/0.9 "Bangers", sans-serif; color: var(--yellow);
  -webkit-text-stroke: 10px var(--ink); paint-order: stroke fill;
  text-shadow: 10px 10px 0 var(--ink); transform: rotate(-8deg); }
/* starburst */
.burst { clip-path: polygon(50% 0%,58% 30%,85% 10%,70% 40%,100% 45%,72% 58%,90% 88%,60% 72%,50% 100%,40% 72%,10% 88%,28% 58%,0% 45%,30% 40%,15% 10%,42% 30%); }
```
Variable halftone: an SVG `<pattern>` of circles with radius driven per cell, or a CSS mask with `radial-gradient` whose stop % is animated via a CSS variable.

## Eases

| Use | GSAP ease |
|---|---|
| Pop-in | `back.out(2.5)` |
| Bouncy landing | `elastic.out(1, 0.45)` |
| Slam | `power4.in` into an impact, then `back.out(3)` |
| Stepped comic timing | `"steps(6)"` on short moves (on-2s feel at 12 fps over 0.5 s) |
| Colour flips | `set()` calls on beats (no tween) |

## Moves

```js
const beat = 0.5, at = n => n * beat;
// pop-in with tilt
tl.fromTo(".hero", { scale: 0, rotation: -12 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, at(1));
// SFX slam + impact flash + shake
tl.fromTo(".burst", { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(3)" }, at(2))
  .fromTo(".sfx", { scale: 3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.18, ease: "power4.in" }, at(2) + 0.05)
  .set(".flash", { opacity: 1 }, at(2) + 0.23).set(".flash", { opacity: 0 }, at(2) + 0.3);
const shake = [8,-10,6,-7,4,-3,2,0];             // precomputed, seek-safe
shake.forEach((x, i) => tl.set(".scene", { x, y: -x * 0.6 }, at(2) + 0.23 + i / 24));
// Warhol colour cycle on beats
const pal = ["#FF3FA4","#FFE600","#00D1C1","#FF7A00"];
for (let b = 0; b < 16; b++) document.querySelectorAll(".cell").forEach((c, i) =>
  tl.set(c, { "--plate": pal[(b + i) % pal.length] }, at(4 + b)));
// dot wipe: grow dot radius in the mask
tl.to(".next", { "--dot": "75%", duration: 0.6, ease: "power2.in" }, at(8));
```
