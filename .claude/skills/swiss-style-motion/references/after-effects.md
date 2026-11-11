# Swiss style: After Effects recipes

Build through the `after-effects` MCP: `run_extendscript` for multi-layer builds, `preview_frame` to check, `render_comp` for test MP4s.
Save test projects to `C:\Users\basha\Motion Design\After Effects Projects\` and renders to `C:\Users\basha\Motion Design\Cluads Work Folder\`.

## Grids

| Format | Size | Margins | Columns | Rows | Gutter | Cell |
|---|---|---|---|---|---|---|
| Reel 9:16 | 1080×1920 | 80 | 4 | 8 | 40 | 200 × 185 |
| Reel fine | 1080×1920 | 80 | 8 | 16 | 20 | 97.5 × 91.25 |
| Square 1:1 | 1080×1080 | 80 | 6 | 6 | 24 | ~133.3 × ~133.3 |
| Landscape 16:9 | 1920×1080 | 96 | 12 | 6 | 24 | 122 × 128 |

Keep a guide layer: a shape layer of column/row rectangles at 15% opacity, set as a **guide layer** (Layer > Guide Layer) so it never renders.
Column x for column `c` (0-based): `margin + c * (cell + gutter)`.

Baseline grid: 8 px for small text (or match body leading).

## Time grid

- 30 fps comp. Module = one beat. 120 BPM → 15 f; 100 BPM → 18 f; 128 BPM → ~14 f (use 14).
- Add a comp marker on each beat (script: loop `comp.markerProperty.setValueAtTime(i*beat, new MarkerValue(""))`).
- Durations: moves ½–1 module, holds ≥ 1 module (headlines ≥ 0.75 s).

## Easing

Graph Editor (speed graph), after F9:
- **Snap out (default):** outgoing influence 10–20%, incoming influence 85–95%. Fast start, long precise settle (expo-out feel).
- **Snap in-out (layout to layout):** both influences 70–80%. Sharp, mechanical.
- **Linear:** tickers, scrolling type, continuous rotation of a circle element.
Never use overshoot expressions (bounce/inertia). Never `wiggle`.

Expo-out by expression (on a property with 2 keyframes), when keyframe handles are fiddly:
```js
if (numKeys > 1 && time >= key(1).time && time < key(2).time) {
  var t = (time - key(1).time) / (key(2).time - key(1).time);
  var e = t == 1 ? 1 : 1 - Math.pow(2, -10 * t);
  key(1).value + (key(2).value - key(1).value) * e;
} else value;
```

## Snap to grid

Position expression that rounds to cell steps. Animate a "Column" and "Row" slider instead of raw position:
```js
var m = 80, cw = 200, ch = 185, g = 40;
var c = effect("Column")("Slider"), r = effect("Row")("Slider");
[m + c * (cw + g), m + r * (ch + g)];
```
Keyframe the sliders with snap easing; whole numbers at rest.

## Line rise (signature type reveal)

1. One text layer per line, anchor at top-left of the line box.
2. A rectangle matte the exact size of the line box above it; set the text to **Alpha Matte**. Alternatively use a layer mask on a precomp.
3. Position Y: start = rest + line height (hidden below the matte), end = rest. Duration 10–14 f, snap out.
4. Stagger lines by 3 f (offset layers, or `inPoint` offset).

Per-character or per-word in one layer: Text Animator > Position (0, lineHeight) + Range Selector, Units: Index, Based on: Words, Shape: Ramp Up, Ease High 100 / Low 0, animate Offset −100%→100% or End 0→100. Add a mask on the text layer for the baseline box so words rise out of it.

## Column wipe / colour field

1. Solid or shape rectangle = N columns wide, full height (or row height).
2. Move the anchor to the starting edge (left edge: anchor x = 0 in layer space).
3. Scale X 0 → 100% (snap out, ~12 f). For a reveal, use the field as a matte, or follow with a second wipe of the background colour (wipe on, then wipe off from the same edge).
4. Stagger columns by 2–3 f for a multi-column wipe.

## Cell fill

Shape layer per cell (or one script loop). Opacity or Scale from the cell's top-left corner, staggered by reading order:
```js
// on scale, with layer index driving delay
var d = (index - 1) * 2 * thisComp.frameDuration;
var t = time - inPoint - d;
var p = linear(t, 0, 0.3, 0, 1);
var e = 1 - Math.pow(1 - p, 4);
[100 * e, 100 * e];
```

## Rule draw

Shape layer path (line) stroke 2–4 px, no fill. Trim Paths End 0→100 over 8–12 f, snap out. Type rises onto the rule 2–3 f after it finishes drawing (overlap).

## Counter

Text layer Source Text with a Slider:
```js
var v = effect("Value")("Slider");
Math.round(v).toLocaleString();
```
Animate the slider with snap out. Use tabular figures (OpenType tnum, or a font with fixed-width numerals) so digits don't jitter. Right- or left-align it to a column edge.

## Scale jump

Hold keyframes (Ctrl+Alt+H) on font size or Scale, landing on beat markers. Sizes come from the type scale only (e.g. 89 → 144 → 233 px).

## Finish

- Motion blur on for all moving layers, comp shutter 180°, phase −90°.
- No adjustment-layer effects, grain or glow by default.
- Render H.264 for review; ProRes 422 for the edit.
