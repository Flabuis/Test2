# Bauhaus: CSS / GSAP (HyperFrames) and Higgsfield

## CSS shapes and tiles

```css
:root { --paper:#F2EBDD; --r:#D62828; --y:#F7C600; --b:#1D4E89; --k:#111; }
.stage { background: var(--paper); }
.circle { border-radius: 50%; background: var(--b); }
.square { background: var(--r); }
.tri { background: var(--y); clip-path: polygon(50% 0, 100% 100%, 0 100%); }
.bar { background: var(--k); height: 28px; transform-origin: 0 50%; }
.grid { display: grid; grid-template-columns: repeat(6, 180px); }
.tile { width: 180px; height: 180px; position: relative; overflow: hidden; }
.tile .q { position: absolute; width: 360px; height: 360px; border-radius: 50%; left: -180px; top: -180px; } /* quarter circle */
h1 { font: 500 160px/0.9 "Jost", "Futura", sans-serif; text-transform: lowercase; letter-spacing: -0.02em; color: var(--r); }
```

## GSAP moves

```js
const beat = 0.5, at = n => n * beat;
// tile cascade from top-left, 90° turns
tl.to(".tile", { rotation: "+=90", duration: 0.35, ease: "power3.inOut",
  stagger: { grid: [10, 6], from: "start", each: 0.04 } }, at(2));
// ruler extend + type slide
tl.from(".bar", { scaleX: 0, duration: 0.25, ease: "power4.out", stagger: 0.08 }, at(1))
  .from("h1", { xPercent: -30, opacity: 0, duration: 0.4, ease: "power3.out" }, at(1) + 0.15);
// Kandinsky trio on beats
tl.from(".tri", { y: -800, rotation: -90, duration: 0.4, ease: "back.out(1.4)" }, at(4))
  .from(".square", { x: 900, rotation: 90, duration: 0.4, ease: "back.out(1.4)" }, at(5))
  .from(".circle", { scale: 0, duration: 0.4, ease: "back.out(1.6)" }, at(6));
// compass draw (SVG circle)
tl.from("#compass", { drawSVG: "0%", duration: 0.6, ease: "power2.inOut" }, at(7));
```

## Higgsfield prompts

- "Bauhaus poster, asymmetric dynamic composition, yellow triangle, red square and blue circle, heavy black bars and thin rules, lowercase geometric sans-serif typography in red and black, off-white paper, flat colours, 1920s modernism"
- "modern Bauhaus geometric tile pattern, quarter circles and semicircles in red, yellow, blue and black on cream, flat vector"
- "Oskar Schlemmer Triadic Ballet inspired geometric figure, costume made of circles, cones and discs, yellow and black, flat stage"
Rebuild type and shapes natively; use generations as style frames.
