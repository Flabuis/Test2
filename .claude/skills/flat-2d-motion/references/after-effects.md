# Flat 2D: After Effects recipes

Build through the `after-effects` MCP (`run_extendscript`, `preview_frame`, `render_comp`). Illustrator art through the `illustrator` MCP.
Save .ai files to `C:\Users\basha\Motion Design\Illustrator Projects\`, .aep files to `...\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## Artwork prep (Illustrator)

- One layer per moving part, clearly named (`arm_L_upper`, `arm_L_lower`, `hand_L`, `head`, `eye_L`...).
- Limb parts overlap at joints with round ends, so rotation hides the seam.
- Align to pixel grid; use whole-number sizes; keep shapes, not expanded strokes, where you will animate the stroke.
- In AE: import as Composition – Retain Layer Sizes, then right-click > Create > Create Shapes from Vector Layer for editable paths.

## Easing

- Default: F9, then in the speed graph set influence 66–80% on both sides.
- Snappy UI ease: outgoing 30%, incoming 85%.
- Character holds: ease into poses longer (incoming 85–90%) so poses "settle".
- Linear: rotations of wheels/gears, orbits, conveyor movements.

## Overshoot pop (soft)

Keyframes: Scale 0 → 108 (6 f) → 98 (3 f) → 100 (3 f). Or Scale 0 → 100 plus a light inertia expression:
```js
var amp = 0.04, freq = 2.5, decay = 6, n = 0;
if (numKeys > 0) { n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n > 0) { var t = time - key(n).time; var v = velocityAtTime(key(n).time - thisComp.frameDuration / 10);
  value + v * amp * Math.sin(freq * t * 2 * Math.PI) / Math.exp(decay * t); } else value;
```

## Overlap and follow-through (lag a child behind its parent)

On the child's Rotation (child is parented and has its own keys optional):
```js
var p = parent.transform.rotation;
var lag = 3 * thisComp.frameDuration;
value + (p.valueAtTime(time - lag) - p.value) * 0.6;
```
For a group stagger, offset layer In points by 2–3 f, or drive from one controller with `valueAtTime(time - index * delay)`.

## Idle loops

- Breathe (Scale): `var s = 100 + Math.sin(time * 2 * Math.PI / 3) * 1.5; [s, 100 + (s - 100) * 1.4];` (anchor at the feet).
- Float (Position): `value + [0, Math.sin(time * 2 * Math.PI / 2.5) * 6];`
- Blink (Scale Y of the eyes, seek-safe):
```js
var period = 3.7, d = 0.12, t = time % period;
var y = t < d ? 100 - 90 * Math.sin(Math.PI * t / d) : 100;
[value[0], y];
```
- Loop keyframed cycles: `loopOut("cycle")` or `loopOut("pingpong")`.

## Shape morph

1. One path keyframe per shape (paste the paths from Illustrator into the same Path property).
2. Match the vertex count and first vertex (right-click a vertex > Mask and Shape Path > Set First Vertex) to avoid twisting.
3. Ease 70%+ both sides; add a 1–2 f overshoot through scale for life.

## Stroke draw-on and bursts

- Draw-on: Trim Paths End 0 → 100 (ease), then fill opacity on, or fill scale from 0, 2 f before the stroke finishes.
- Burst: 8 short line paths (Repeater: Copies 8, Rotation 45°), Trim Paths Start/End animated 0 → 100 with End leading Start by 3 f, plus Offset; Round Cap. Add a ring: ellipse stroke, scale 0 → 140, stroke width 12 → 0.

## Circle wipe transition

Shape layer ellipse in the next scene's base colour, anchored at the focal point. Scale 0 → enough to cover the corners (≈ diagonal / diameter × 100), 12–18 f, ease in-out. Bring the next scene in under it, then cut the circle.

## Flat cel shadow and long shadow

- Cel shadow: duplicate the shape, darken 15–25% in the same hue, offset or reshape for one light direction, use the original as Alpha Matte (or Alpha Inverted for a highlight).
- Long shadow: duplicate the object as a solid shadow colour; Repeater Copies 200–400, Transform Position (1, 1), behind the object; clip it to the background shape with a matte.

## Parallax and zoom

- 2D: a Camera Control null; children use `value + (thisComp.layer("CAM").transform.position - [960,540]) * depth;` with depth 1.0 / 0.6 / 0.3.
- 3D: make layers 3D, spread Z (fg −300, mid 0, bg +800), and use a one-node camera parented to a null. Keep moves slow and eased.
- Infinite zoom: Scale the scene null exponentially so the speed feels constant: `var s = Math.pow(2, (time - inPoint) * 1.5) * 100; [s, s];`. Swap in the next scene inside the detail at about 400–800%.

## Character rigging (Duik Ángela)

1. Set the comp size and frame rate first. Changing the comp size after rigging breaks Duik.
2. Switch Duik from Rookie to Standard/Expert mode.
3. Create Structures (arm, leg, spine, head), align them to the artwork joints.
4. Link & Align the artwork layers to the structures, then Auto-rig (IK, foot roll, controllers).
5. Animate controllers pose to pose. Use the Walk Cycle tool for cycles; Kleaner adds overlap and follow-through automatically.
6. Lighter alternative: plain parenting chains plus the Puppet Pin tool for soft parts, and Joysticks 'n Sliders for face turns.

## Finish

- Motion blur on (shutter 180°) for fast moves.
- Optional subtle grain (Noise 1–2%) only for the mid-century variant.
- Render H.264 for review, ProRes 422 for the edit.
