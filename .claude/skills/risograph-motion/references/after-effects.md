# Risograph: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## Structure

```
MAIN comp
 ├─ Posterize Time adjustment (12 fps or 8 fps)     ← last
 ├─ INK_Blue   (precomp, Multiply)                   ← riso stack per ink
 ├─ INK_Pink   (precomp, Multiply)
 └─ PAPER      (scanned paper texture, or solid #F3EEE3 + Noise)
```
Each `INK_x` precomp contains a **plate**: the artwork for that ink only, in black (ink) on transparent. Animate the artwork inside the plate (or in a shared "ART" comp and split plates with mattes).

## Riso stack per ink (on the INK precomp layer, top to bottom)

1. **Grain/halftone for tones (photos, gradients):** inside the plate, Black & White → Levels (contrast) → Color Halftone (Max Radius 4–8, all angles the same, a different angle per ink: e.g. pink 15°, blue 75°) or Noise-dither (Noise 40% → Threshold) for stochastic grain.
2. **Ink dropout speckle:** inside the plate, a top Fractal Noise layer (Fractal Type Basic, Contrast 250, Brightness +30, Scale 3–6, Complexity 2) with blend mode **Silhouette Luma** at 20–40% opacity, Evolution `posterizeTime(12); time*800`. Punches small random holes in the ink that change per step.
3. **Rough edges:** Roughen Edges (Edge Type Roughen, Border 2–4, Edge Sharpness 1–1.5, Fractal Influence 0.6, Scale 40–80, Complexity 3), Evolution `posterizeTime(12); time*400`.
4. **Ink colour:** Fill (colour = ink hex), or Tint (Map Black To ink, Map White To white) if the plate is black-on-white.
5. **Density:** opacity 85–95% (real riso solids are never perfect).
6. **Registration drift:** Transform effect (or Position):
```js
posterizeTime(12);
seedRandom(index, false);
var amp = effect("Drift")("Slider");      // 1–3 px on holds, 6–12 px on hits
value + [random(-amp, amp), random(-amp, amp)];
```
   Give each ink a different base offset as well (e.g. blue +4, +3 px).
7. **Blend mode Multiply** onto the paper (subtractive overprint). Riso inks are translucent and print darker-on-lighter, so use light paper stock; on dark stock most inks nearly vanish.

## Grain on solids

Add to the plate: Noise (Amount 20–35%, Colour Noise off) → Levels (crush to speckle) or a scanned grain texture set to Silhouette Luma 15–25%. Keep coarse: scale the texture up 150–300%.

## Paper

A scanned paper texture (fibers, slight tone variation) at the bottom; optional subtle second copy on top in Multiply at 10–20% so texture shows through the ink. No paper? Solid `#F3EEE3` + Noise 3% + Fractal Noise (Scale 600, Contrast 60) at 8% Overlay.

## Overprint check

With all inks on Multiply, overlaps produce the third colour automatically. Preview pairs: pink `#FF48B0` × blue `#0075BF` ≈ deep purple; yellow `#FFE800` × teal `#009DA5` ≈ green. If an overlap looks muddy, change one ink.

## Moves

- **Ink-pass build:** INK_Pink opacity cuts on (with a 2-step grain flicker: Fractal Noise Brightness high → normal), then 3–6 frames later INK_Blue cuts on with Drift at 10 → settles to 2 over 4 steps.
- **Registration snap:** keyframe the Drift slider or base offsets from 40 px apart → 3 px on a beat (hold keyframes).
- **Halftone bloom:** animate Color Halftone Max Radius or the plate's Levels so a tone grows from sparse dots to solid.
- **Paper feed:** precomp the whole sheet (inks + paper) and slide it in Y with a quick ease, stepped; the next sheet follows.
- **Roller wipe:** a band in the ink colour with grain/rough edges sweeping across (Linear Wipe with Feather 0 + Roughen Edges on the reveal edge).
- **Stamp:** Scale 112 → 100 in 2 steps with a dropout-free frame (Silhouette Luma off for 1 step) for a dense hit.

## Finish

- Posterize Time 12 fps (or 8) on top. No motion blur.
- Optional overall vertical feed streaks: Fractal Noise Scale Width 3000 / Height 40, very low opacity Multiply.
- Render ProRes master; H.264 at high bitrate (grain compresses badly).
