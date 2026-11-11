# Line art: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## Setup

- Illustrator art: import as Composition – Retain Layer Sizes, then Layer > Create > **Create Shapes from Vector Layer**. Each path becomes a group.
- Stroke only (Fill off), Line Cap Round, Line Join Round (friendly) or Butt/Miter (technical). Stroke width consistent.
- If a path draws backwards, reverse it: select the path > right-click > Mask and Shape Path > Reverse Path Direction (or reverse it in Illustrator before import).

## Draw-on with Trim Paths

- Add > **Trim Paths** after the paths in a group: End 0 → 100%.
- Several paths in one group: Trim Multiple Shapes = **Individually** (all draw at once) or **Simultaneously** (one after another along the group order).
- Erase: animate Start 0 → 100% after End finishes (or both, Start lagging End for a travelling segment; Offset slides it).
- **Speed proportional to length** (seek-safe expression on End, with a "Delay" and "Speed" slider on the layer):
```js
var len = 0, p = content("Group 1").content("Path 1").path;
var pts = p.points(); for (var i = 1; i < pts.length; i++) len += length(pts[i - 1], pts[i]);   // approx (straight segments)
var speed = effect("Speed")("Slider");        // px per second, e.g. 900
var t = time - inPoint - effect("Delay")("Slider");
var dur = Math.max(0.15, len / speed), x = clamp(t / dur, 0, 1);
x = x < .5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2;   // easeInOutQuad at stroke ends only
x * 100;
```
(For curved paths the point-to-point length underestimates; increase Speed slightly or sample with `pointOnPath`.)
- Stagger strokes 2–4 f; order layers/groups in drawing order.

## Taper and wave (AE 2020+ stroke options)

Stroke > **Taper**: Start Length / End Length 10–40%, Start/End Width 0–20%, Start/End Ease 50%: pen-like strokes. Animate taper lengths with the draw-on for a brush feel. Stroke > **Wave** adds a sine wiggle along the line (Amount, Units, Phase): animate Phase for flowing lines.

## Pen tip following the drawing

A small dot/pen layer, Position:
```js
var L = thisComp.layer("Line");
var g = L.content("Group 1"), path = g.content("Path 1").path;
var e = g.content("Trim Paths 1").end / 100;
L.toComp(path.pointOnPath(e));
```
Rotation for a pen graphic: `var tg = path.tangentOnPath(e); radiansToDegrees(Math.atan2(tg[1], tg[0]))`. Fade the tip out when End reaches 100.

## Continuous line (one-line story)

Draw the whole sequence as one long path in Illustrator (subject A → connecting stroke → subject B). In AE, animate Trim End 0 → 100 over the whole piece and Trim Start trailing behind (so subject A erases as B draws), or keep A and pan the camera along the line (a null following `pointOnPath` with smoothing via `valueAtTime(time - 0.2)`).

## Line boil (hand-drawn)

- **Wiggle Paths** (Add > Wiggle Paths): Size 1–3, Detail 2–5, Points Smooth, Wiggles/Second 0, and **Random Seed** stepped: `posterizeTime(8); Math.floor(time * 8) % 3` (cycles 3 drawings).
- Or Turbulent Displace (Amount 5–15, Size 30) with Evolution `posterizeTime(8); Math.floor(time*8)%3 * 100`.
- Use on holds; turn down during draw-ons for clarity.

## Morph

Path keyframes from drawing A to B on the same path property (match vertex counts and first vertex); ease 70%+. Or un-draw A (Trim Start) while B draws (Trim End) in the same spot.

## Draw + offset fill

Fill shapes on a layer below the lines, offset 6–20 px down-right, flat accent colours. After each line finishes: Scale 0 → 100 from the shape's centre (back ease) or a Linear Wipe (feather 0) in the drawing direction.

## Handwriting / signature write-on

Write-on needs single-stroke paths (not outlined font shapes): trace letters with the Pen tool in stroke order, or use a single-line font (Hershey, Relief SingleLine, other "SLF" fonts) converted to outlines that are open single paths. Trim Paths per stroke, Simultaneously; speed proportional to length. Dot the i and cross the t last.

## Blueprint build

Grid layer first (thin lines, 20–30% opacity), construction lines (dashed: Stroke > Dashes 8/8) draw fast, object lines draw at normal speed, dimension lines and labels last; white/cyan on deep blue; slight glow optional.

## Finish

- Motion blur off for thin lines (it softens them) unless strokes move fast as wholes.
- Render at full res; thin lines alias badly at low bitrate; use high-bitrate H.264 or ProRes.
