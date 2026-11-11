# Line art: Illustrator prep, SVG/GSAP (HyperFrames) and Higgsfield

## Illustrator (via the `illustrator` MCP)

Save to `C:\Users\basha\Motion Design\Illustrator Projects\`.
- Draw with the Pen or Curvature tool: few anchor points, smooth handles; one path per natural stroke, in drawing direction (reverse with Object > Path > Reverse Path Direction if needed).
- Stroke-only, Round cap/join; keep strokes as strokes (don't Expand), so AE and SVG can animate them.
- Variable weight: Width tool (Shift+W) / variable width profiles; note AE imports width profiles poorly; recreate with AE Taper or keep variable-width strokes as filled outlines (then animate with masks instead of Trim Paths).
- **Image Trace** for converting a drawing or AI image to lines: Mode Black and White, Method Abutting/Overlapping, **Strokes** enabled (Create: Strokes, Stroke max width small) + Ignore White; then clean up paths by hand. Aim for open single paths (centrelines) for draw-ons; if the trace gives outlined shapes instead, redraw key strokes with the Pen tool over the trace.
- Single-line fonts (Hershey, Relief SingleLine) for write-on text.
- Name paths/layers in drawing order (01_head, 02_body...).

## SVG / GSAP (HyperFrames)

```html
<svg viewBox="0 0 1080 1920"><path class="ln" d="..." pathLength="1" fill="none" stroke="#1B1B1B" stroke-width="6" stroke-linecap="round"/></svg>
```
```js
gsap.registerPlugin(DrawSVGPlugin, MotionPathPlugin);
// draw-on in order, duration proportional to length
gsap.utils.toArray(".ln").forEach((p, i) => {
  const len = p.getTotalLength ? p.getTotalLength() : 300;   // with pathLength="1", getTotalLength still returns real length
  tl.from(p, { drawSVG: "0%", duration: Math.max(0.15, len / 900), ease: "power1.inOut" }, i === 0 ? 0.3 : ">-0.08");
});
// grow from the middle
tl.fromTo("#swirl", { drawSVG: "50% 50%" }, { drawSVG: "0% 100%", duration: 1.2, ease: "power2.inOut" }, 3);
// pen tip
tl.to("#tip", { motionPath: { path: "#signature", align: "#signature", alignOrigin: [0.5, 0.5] }, duration: 2, ease: "none" }, 4);
// offset fills after lines
tl.from(".fill", { scale: 0, transformOrigin: "50% 50%", duration: 0.35, ease: "back.out(1.6)", stagger: 0.08 }, ">");
```
Without the plugin: `stroke-dasharray: 1; stroke-dashoffset: 1` (with `pathLength="1"`) and tween `strokeDashoffset` to 0. Path direction sets drawing direction. Line boil: SVG `feTurbulence` + `feDisplacementMap` (scale 2–3) with the turbulence `seed` attribute changed every 2–3 frames via `tl.set()`.

## Higgsfield prompts

- "single continuous line drawing of [subject], one unbroken black line on off-white paper, minimal, elegant, no shading"
- "monoline illustration of [subject], uniform 3px black line, round caps, minimal line art, white background, with offset flat coral and mustard colour shapes behind the lines"
- "blueprint technical line drawing of [object], white lines on deep blue, construction lines and dimensions"
Then Image Trace (strokes/centreline) in Illustrator and clean paths before animating; generated images are pixels, not animatable lines.
