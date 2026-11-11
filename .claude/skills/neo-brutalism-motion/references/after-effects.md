# Neo-brutalism: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`. Add beat markers first.

## Outlined card with linked hard shadow

1. `CARD`: shape layer, Rectangle (Roundness 0–12), flat Fill, Stroke black 8 px (Line Join Miter for sharp corners).
2. `SHADOW`: duplicate, Fill black, Stroke off, placed **below** CARD.
3. `CTRL`: a null. Parent CARD and SHADOW to it; all slams, slides and rotations go on CTRL, so card and shadow travel together.
4. SHADOW Position (relative to CTRL) = card position + `[12, 12]` (the offset). It never moves on its own.
5. On CTRL add a Slider `Press` (0–100). CARD Position expression:
```js
var off = 12, p = thisComp.layer("CTRL").effect("Press")("Slider") / 100;
value + [off, off] * p;      // the card slides into its shadow
```
   Animate `Press` 0 → 100 → 0 (2 f down, 3–4 f back with a small overshoot) for a button press.
Make it a precomp "component" with Essential Graphics properties (colour, text, press) to reuse.

Text inside cards: black (or white on dark fills), bold display face; labels in mono.

## Slam entrance

Position from off-frame to rest in 5–7 f, then overshoot: keyframes rest−40 px → rest+12 → rest. Or the inertia expression:
```js
var amp = 0.05, freq = 3.5, decay = 9, n = 0;
if (numKeys > 0) { n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n > 0) { var t = time - key(n).time; var v = velocityAtTime(key(n).time - thisComp.frameDuration / 10);
  value + v * amp * Math.sin(freq * t * 2 * Math.PI) / Math.exp(decay * t); } else value;
```
Impact shake (2 f) on a scene null, triggered by comp markers:
```js
var m = thisComp.marker, t = -1;
if (m.numKeys) { var k = m.nearestKey(time); t = time - k.time; }
(t >= 0 && t < 0.07) ? value + [6, -4] * (t < 0.035 ? 1 : -1) : value;
```
Rotation snap: −4° → 1° → 0° over 6 f.

## Snap mode (no easing)

Hold keyframes (Ctrl+Alt+H) for instant state changes, or 2-frame linear moves. Optionally Posterize Time 12 for the rawer variant.

## Sticker slap

Sticker shape (star/circle/pill) with outline + hard shadow component. Scale 0 → 115 → 100 (3 f + 3 f), Rotation start ±15° → settle at a fixed tilt (e.g. −8°). Land on a beat.

## Marquee band

Black rectangle full width. Text layer (white, mono or display, uppercase, with separators like ✦ or •). Duplicate it so two copies sit end to end; Position:
```js
var w = sourceRectAtTime().width + 60, speed = 160;   // px per second
var x = -((time * speed) % w);
value + [x, 0];
```
(Second copy: `+ [x + w, 0]`.) Slight rotation (−3°) on the band for energy.

## Spinning badge

Circle path text: Text layer > Path Options > Path = an ellipse mask; Rotation `time * 40`. Outline circle + star in the middle.

## Highlight swipe

Flat colour rectangle behind a word, anchor on its left edge, Scale X 0 → 100 in 4–6 f (snap or quick ease), outline optional.

## Cursor click

Big cursor arrow (black fill, white 4 px stroke, hard shadow). Move with a quick ease-out (8–12 f), then Scale 100 → 88 → 100 (2 f + 3 f) on the click; trigger the button's `Press` at the same frame.

## Window card

Card component with a top bar (stroke divider, three circles or a title in mono), content below. Pops on with Scale 92 → 102 → 100 or a slam.

## Panel wipe transition

Full-frame outlined colour panel (with a hard shadow edge) slides across in 6–8 f; the next scene is revealed behind it as it exits (or cut under it).

## Finish

- No motion blur, no glow, no grain (except a deliberate print-texture variant).
- Render ProRes or H.264 high quality (flat colours compress well; avoid chroma bleeding on thin black lines by rendering at 4:4:4 where possible).
