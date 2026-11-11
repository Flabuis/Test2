# Pop art: After Effects recipes

Build through the `after-effects` MCP: `run_extendscript` for multi-layer builds, `preview_frame` to check, `render_comp` for test MP4s.
Save test projects to `C:\Users\basha\Motion Design\After Effects Projects\` and renders to `C:\Users\basha\Motion Design\Cluads Work Folder\`.

## Ben-Day dot field (even dots)

Shape layer:
1. Ellipse 12×12 px, fill ink colour, no stroke.
2. Repeater 1: Copies 90, Offset 0, Transform Position (24, 0).
3. Repeater 2: Copies 160, Transform Position (12, 24). The x shift staggers rows into a 45° grid.
4. Centre it with Anchor Point. Use it as an **Alpha Matte** for the area that should be dotted (skin, sky, shape).
5. Scroll: Position expression `value + [time*20, time*20]`. Keep the travel under one dot period visible, or loop with `% 24`.

Dot size guide at 1080 wide: 8–14 px dots, spacing 2× dot. Bigger dots read better on phones.

## Halftone (variable dots)

- **Effect > Stylize > Color Halftone:** Max Radius 8–20. Channel angles C 105°, M 75°, Y 90° (or all the same for a single-ink look).
- **Single-ink halftone from a photo:** Black & White → Levels (contrast) → Color Halftone (all channels 45°) → Tint (black to ink colour). Set it to Multiply over a flat colour plate.
- **Shading on a shape:** a Gradient Ramp precomp → Color Halftone → use as a Luma Matte for an ink layer.

## Dot wipe transition

1. Precomp: a white solid with Gradient Ramp (linear, from corner to corner) → Color Halftone (Max Radius 30–60, all angles 45°) → Threshold 128.
2. Animate the Gradient Ramp start/end points across the frame (or Levels Input Black/White) over 12–18 f.
3. Use the precomp as a **Luma Matte** for the incoming scene. Dots grow from one corner and merge into solid.

## Thick outlines

- **Vector shapes:** stroke 8–14 px black, line join Round, cap Round.
- **Cut-out footage/photo:** Roto Brush or a PNG cutout → Layer > Layer Styles > Stroke (Outside, black, 10 px). Add Drop Shadow (distance 12–20, softness 0, opacity 100%, angle 135°) for the hard pop shadow.
- **Line art from a photo:** Find Edges → Levels → Threshold, then Multiply over flat colour plates. Or use Higgsfield to redraw the subject as comic line art.

## Warhol plates (photo → silkscreen)

1. Cut out the subject. Duplicate it 3 times.
2. Plate 1 (shadows): Threshold ~90 → black, Multiply.
3. Plate 2 (face/skin): solid fluoro colour shaped by a loose hand-drawn mask around the face (not exact).
4. Plate 3 (accents): lips, eyes, hair in a different flat colour, masked by hand.
5. Background: flat fluoro colour.
6. **Misregistration:** offset the colour plates 6–12 px from the black plate.
7. **Grid:** precomp the subject; place in a 2×2 / 3×3 grid; each cell gets its own palette (Tint, Tritone or Change To Color). Cycle colours with hold keyframes on beat markers.

Plate colour cycle by expression (on a Fill colour, with a `palette` of hex values):
```js
var pal = ["#FF3FA4","#FFE600","#00D1C1","#FF7A00","#8A3FFC"];
var beat = 0.5;                                   // 120 BPM
var i = (Math.floor(time / beat) + index) % pal.length;
hexToRgb(pal[i]);
```

## Overshoot pop

Keyframe Scale 0 → 100 over 6–8 f, then add this to Scale (or Position or Rotation):
```js
var amp = 0.06, freq = 3.0, decay = 7.0, n = 0;
if (numKeys > 0) { n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n > 0) {
  var t = time - key(n).time;
  var v = velocityAtTime(key(n).time - thisComp.frameDuration / 10);
  value + v * amp * Math.sin(freq * t * 2 * Math.PI) / Math.exp(decay * t);
} else value;
```
Or keyframe it by hand: 0 → 115 (5 f) → 95 (3 f) → 100 (3 f). Rotation: −10° → 4° → 0°.

## Impact shake

On a null parenting the scene (or a Transform effect on an adjustment layer):
```js
var m = thisComp.marker, hit = 0;
if (m.numKeys > 0) { hit = m.nearestKey(time).time; }
posterizeTime(24);
var t = time - hit;
if (t >= 0 && t < 0.2) value + (wiggle(30, 25) - value) * (1 - t / 0.2); else value;
```
Add a comp marker on each hit.

**Impact frame:** on the hit, 1–2 frames of an adjustment layer with Invert, or a flat yellow/red solid with the black line plate on top.

## Starburst

Star tool: Points 12–16, Inner Radius 55–65% of outer, roundness 0. Yellow fill, 10 px black stroke. Pop in with overshoot, then a small rotation wiggle `posterizeTime(12); value + wiggle(1, 4) - value`. Put a second, bigger red star behind it, offset 2 frames.

## Speed and zoom lines

- **Radial zoom lines:** Fractal Noise (Contrast 400, Scale Width 3000, Scale Height 20, Evolution `time*600`) → Polar Coordinates (Rect to Polar, 100%) → Threshold. Mask out the centre. Posterize Time 12.
- **Parallel speed lines:** the same Fractal Noise without Polar; rotate it to the direction of motion.
- **Vector option:** a line shape with Repeater (Copies 40, Rotation 9°) + Trim Paths with randomised start/end per step.

## Comic panels

- Page: 20–24 px white gutters, 8–10 px black panel borders.
- Panel slam: Scale 120 → 100 with overshoot + Position drop 40 px, 6 f. Border Trim Paths draws on 4 f earlier.
- Camera: a null-parented layout or 3D camera with one push per panel; cut or whip between panels on beats.

## Speech balloon

An ellipse + triangle tail merged (Merge Paths: Add), white fill, 8 px black stroke. Set the anchor at the tail tip; Scale 0 → 100 with overshoot. Text pops in by word (Text Animator Scale 0 → 100, Based on Words, 1 f stagger).

## Finish

- Posterize Time adjustment layer at 12 fps (below any layer that must stay smooth, like a scrolling dot field).
- Newsprint: paper texture on top, Multiply, 15–30%. Slight warm tint.
- Optional ink spread: Matte Choker / a slight Roughen Edges (Border 2, Scale 300) on the line plate.
- No motion blur on stepped animation (it smears the dots).
