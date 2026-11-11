# Isometric: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

Two approaches: **2D iso** (flat art drawn or transformed into iso; crisp, fast, the usual motion-design method) and **3D iso** (real 3D layers with an isometric camera; true rotations and extrusion).

## 2D: the SSR method (flat art onto iso faces)

Draw a face flat (front view), then apply Scale → Shear (Skew) → Rotate. With the Transform effect (Skew available) on each face layer (true isometric):

| Face | Scale (height) | Skew | Rotation |
|---|---|---|---|
| Top | 86.602% | 30° | −30° |
| Left | 86.602% | −30° | −30° |
| Right | 86.602% | 30° | 30° |

(Check the visual result once; sign conventions differ between apps. In Illustrator, use the same values with Object > Transform.) Use this for signage, screens and textures on faces.

## 2D: iso grid positioning

Place and move objects by grid coordinates so movement stays on-axis. Add three Slider controls (gx, gy, gz) to a layer, Position:
```js
var u = 60;                              // grid unit in px (half tile width)
var gx = effect("gx")("Slider"), gy = effect("gy")("Slider"), gz = effect("gz")("Slider");
var iso = true;                          // false for 2:1 dimetric
var k = iso ? Math.tan(Math.PI / 6) : 0.5;   // vertical factor per unit (0.577 true iso, 0.5 for 2:1)
var origin = [thisComp.width / 2, thisComp.height / 2];
var L = u * Math.sqrt(1 + k * k);        // on-screen length of one grid unit (vertical uses the same length)
origin + [(gx - gy) * u, (gx + gy) * u * k - gz * L];
```
Animate gx/gy/gz instead of Position: moves are axis-aligned by construction. Depth order: lower `gx + gy` behind; reorder layers or sort by an index if objects pass each other.

## 2D: drop-in, rise, tile cascade

- **Drop-in:** gz from 6 → 0 over 8–10 f with ease-out, then a bounce (0 → 0.15 → 0 over 4–6 f); stagger blocks 3–4 f in build order.
- **Rise (extrusion):** build buildings as precomps with the anchor at the base; Scale Y 0 → 100 (a box's side faces stretch correctly only if the top face moves, so animate the top face Position up and side faces' height together, or use the 3D method for true extrusion).
- **Tile cascade:** tiles' In points or Scale from the base offset by `(gx + gy) * 2` frames.

## 3D: isometric camera

1. Comp with 3D layers (Classic 3D or Advanced 3D renderer).
2. Null `ISO_RIG` at the comp centre: Orientation/Rotation **X = −35.264°**, **Y = 45°** (true isometric; 35.264° = 90° − 54.736°). For 2:1 dimetric use X = −30°.
3. Camera (one-node), parented to ISO_RIG, Position (0, 0, −20000), Zoom 20000+ (a very long lens approximates orthographic; AE has no orthographic render camera). Frame by moving/scaling the rig, not dollying.
4. Build objects from 3D shape layers with **Extrusion Depth** (Advanced 3D renderer) or six-sided precomp cubes.
5. **Flat three-tone look without lights:** colour each face manually (top light, left mid, right dark) with lights off. **Lit look:** one Parallel light (from top-left) + Ambient light 40–60%, shadows on.
6. Turntable: rotate ISO_RIG Y by 90° steps (ease in-out) to show other sides.
Shortcuts: Loop's "Angle" script or the Isomatic FX plugin automate iso cameras if installed.

## Exploded view

Each layer of the product/stack on its own 3D layer (or grid gz slider). Animate Z (or gz) apart with staggered ease-out, add leader lines + labels in screen space, hold, reassemble with a slight overshoot.

## Flow lines

Paths along iso axes (draw with the grid expression or snap to the iso grid in Illustrator): Stroke with Dashes, Offset `time * -40`; packets along paths via a mask path pasted into Position (Creative Bloq tip), or Trim Paths-driven position.

## Loops

Make cars, packets and lights cycle with `loopOut("cycle")` or modulo time; match first and last frame.

## Finish

- Light motion blur on moving blocks; none on static.
- Optional soft AO/shadow layers (Multiply, flat shapes along the shadow axis).
- Render ProRes / high-quality H.264.
