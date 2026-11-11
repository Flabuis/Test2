# Clay 3D: After Effects finishing and AI generation

## After Effects compositing

Use the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`.

- Import the Blender image sequence (set its frame rate to the render rate).
- **Grade:** Lumetri: slight warmth, lift the blacks a little (clay rarely has crushed blacks), gentle saturation.
- **Grain:** Add Grain or Noise 1–3% for a photographed feel. Claymation can go to 3–5%.
- **Claymation extras:**
  - Posterize Time adjustment layer at 12 fps if the render wasn't stepped.
  - Exposure flicker: Exposure effect with `posterizeTime(12); wiggle(12, 0.03)` on Exposure.
  - Camera micro-jitter: Transform effect Position `posterizeTime(12); wiggle(12, 1.5)` (1–2 px at 1080).
- **2D clay overlays:** flat type or UI over clay renders should use rounded fonts and the clay palette. For a fake-clay look on 2D shapes: Bevel Alpha (Edge 8–20, light angle −60, intensity 0.3) + Inner/Drop Shadow layer styles (soft, low opacity) + Noise bump via Displacement Map. It's a cheap stand-in, not true 3D.
- Render H.264 for review, ProRes 422 for the edit.

## Higgsfield prompts (style frames and AI video)

Use `higgsfield-generate`. Image first, then image-to-video.

**Smooth clay still:**
> 3D clay render of [subject], soft matte plasticine material, chunky rounded shapes, pastel palette of [colours], subtle subsurface glow, soft large studio lights, gentle contact shadows, seamless curved [colour] backdrop, tilt-shift miniature depth of field, 85mm, cute toy-like proportions, clean minimal composition

**Claymation still:**
> handmade claymation scene of [subject], plasticine with visible fingerprints and slight lumps, saturated playful colours, miniature tabletop set, soft practical lighting, shallow depth of field, Aardman-inspired stop-motion look, photographed miniature

**Video (image-to-video):**
> smooth clay: "the clay [subject] bounces in with squash and stretch, jiggles and settles, slow camera push, soft studio light"
> claymation: "stop-motion claymation, choppy 12fps movement, clay surface subtly changes each frame, [action], static tabletop camera"

Check generated frames for clay-ness (matte, rounded, imperfect) before animating; reject glossy plastic results.
