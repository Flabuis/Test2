# Risograph: Photoshop / Illustrator stills, CSS/GSAP, Higgsfield

## Photoshop (via the `photoshop` MCP) - riso still from a photo or artwork

Save to `C:\Users\basha\Motion Design\Photoshop projects\`.
1. Duplicate the source per ink. Convert each to greyscale and push its tones (Levels/Curves) to decide what that ink carries (e.g. shadows to blue, mids/highlights to pink).
2. Halftone: Image > Mode > Bitmap > Halftone Screen (frequency 25–45 lpi at 1080, angle per ink, Round) or Filter > Pixelate > Color Halftone; or keep grain via Filter > Noise > Add Noise then Threshold.
3. Back to RGB; fill each plate with its ink colour (Color Fill layer clipped, or Gradient Map black → ink, white → white) and set the layer to Multiply.
4. Add grain/dropout (a noise layer as a mask), rough edges (Filter > Brush Strokes > Spatter or Ripple, small), and offset plates 2–8 px.
5. Paper texture underneath; flatten a copy for export. Keep the layered PSD for AE (import as Composition – Retain Layer Sizes, each ink a layer).

## Illustrator (via the `illustrator` MCP) - vector riso posters

Save to `C:\Users\basha\Motion Design\Illustrator Projects\`.
- One layer per ink, named `INK_Pink`, `INK_Blue`. Fill everything with its ink colour, Transparency: Multiply (or Attributes > Overprint Fill for print).
- Grainy gradients: Effect > Texture > Grain (Stippled) on gradients, or a grain image as an opacity mask.
- Rough edges: Effect > Distort & Transform > Roughen (Size 0.5–1%, Detail 20–40, Smooth).
- Keep plates as separate layers so AE can import them as separate ink precomps.

## CSS / SVG / GSAP (HyperFrames)

```html
<svg width="0" height="0">
  <filter id="riso" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="1" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.5" result="holes"/>
    <feComposite in="SourceGraphic" in2="holes" operator="in" result="speckled"/>
    <feTurbulence type="turbulence" baseFrequency="0.04" numOctaves="2" seed="3" result="r"/>
    <feDisplacementMap in="speckled" in2="r" scale="3"/>
  </filter>
</svg>
```
```css
.paper { background: #F3EEE3 url(paper.jpg); }
.ink { mix-blend-mode: multiply; filter: url(#riso); }
.ink.pink { color: #FF48B0; } .ink.blue { color: #0075BF; }
```
Stepped boil and drift (seek-safe): change the turbulence `seed` attribute and plate offsets with `set()` calls every 2 frames.
```js
const step = 1 / 12, offs = [[3,-2],[-2,1],[1,3],[-3,-1],[2,2],[-1,-3]];
for (let i = 0; i < 12 * 8; i++) {
  tl.set("#riso feTurbulence", { attr: { seed: i % 7 + 1 } }, i * step);
  tl.set(".ink.blue", { x: offs[i % 6][0], y: offs[i % 6][1] }, i * step);
}
// ink-pass build
tl.from(".ink.pink", { opacity: 0, duration: 0.01 }, 1).from(".ink.blue", { opacity: 0, x: 24, y: 12, duration: 0.25, ease: "steps(3)" }, 1.25);
```

## Higgsfield prompts

- "risograph print poster of [subject], two-colour riso in fluorescent pink and blue, overprinted translucent inks creating purple overlaps, slight misregistration, coarse grain and halftone dots, rough ink edges, off-white paper texture, bold grotesk typography, indie zine aesthetic"
- "riso print illustration, yellow and teal inks overprinting to green, grainy textured fills, misregistered layers, matte paper"
- Video: generate stills, then animate in AE with the riso stack (AI video tends to smooth away grain and registration).

Reject results with smooth full-colour gradients or more than 3 ink colours.
