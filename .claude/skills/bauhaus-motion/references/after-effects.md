# Bauhaus: After Effects recipes

Build through the `after-effects` MCP; Illustrator shapes via the `illustrator` MCP if needed. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`. Beat markers first.

## Tile pattern cascade

1. Grid: N × M square tiles (e.g. 6 × 10 for 1080×1920, tile 180 px). Build with `run_extendscript`: for each cell, a shape layer containing a square background + one motif (quarter circle anchored at a corner, semicircle, circle, triangle, or half square) with colours picked from the palette by a seeded rule (e.g. `(row*7 + col*3) % 5`).
2. Each tile's anchor at its centre; rotation animated in 90° steps.
3. Cascade by distance from an origin (corner, centre or a moving point):
```js
// on Rotation of every tile layer
var origin = [0, 0], tile = 180, delay = 0.06, dur = 0.35;   // s
var d = length(transform.position, origin) / tile;
var t = time - (thisComp.marker.numKeys ? thisComp.marker.key(1).time : 0) - d * delay;
var p = clamp(t / dur, 0, 1); p = p < .5 ? 4*p*p*p : 1 - Math.pow(-2*p + 2, 3) / 2;   // easeInOutCubic
value + 90 * p;
```
4. Colour swap waves: Fill colour hold-keyed, or an expression switching palette index at the same delayed time.

## Compass draw and ruler extend

- **Compass:** circle path, Stroke 6–10 px, Trim Paths End 0 → 100 (Offset so it starts at the radius line) over 12–18 f, ease in-out; a thin radius line rotates with it (Rotation linked to `trim end * 3.6`). Fill pops on at the end.
- **Ruler:** a bar's Scale X 0 → 100 from an end anchor (5–8 f, power ease); rules stagger 2–3 f; type slides along the bar from behind a mask.

## Shape assembly / Kandinsky trio

Yellow triangle, red square, blue circle as separate shape layers. Positions animate from off-frame along diagonals to their poster slots, rotation settling to set angles; a small overshoot (5%) on arrival. Re-arrange on later beats into new compositions.

## Universal-style geometric type

Draw letters from circles (o, a, b, d, p, q from a circle + bar), bars (l, i, t) and arcs; each stroke is its own shape path. Build by stroke: bars Scale from an end, bowls Trim Paths. Lowercase only. Or use a geometric font (Jost/Futura) and reveal with rule-mask wipes.

## Albers squares

3–4 nested squares (centres offset downward slightly, as in *Homage to the Square*). Hold-keyed fill colour changes one square at a time on beats, or a slow crossfade (Fill colour keyframes with linear interpolation over 1–2 s) to show colour interaction.

## Schlemmer figure

Puppet from shapes: circle head, cone/trapezoid body, disc or cylinder arms, parented at joints (or rigged with Duik). Pose-to-pose dance on beats with mechanical in-out eases; colours from the yellow/pink/black acts of the Triadic Ballet.

## Typophoto

B&W photo (Black & White + Levels for high contrast), masked to a geometric shape or rectangle, slides in along a bar; red lowercase type and black rules follow.

## Diagonal layout transitions

Parent the whole poster to a null; rotate the null 15–45° and slide along the diagonal into the next poster (or a giant circle/bar wipes across in a primary colour).

## Finish

- Light motion blur or none; flat colours.
- Optional paper grain (Noise 2–3% + paper texture Multiply 10%) and Posterize Time 12 for a cut-paper variant.
- Render ProRes / high-quality H.264.
