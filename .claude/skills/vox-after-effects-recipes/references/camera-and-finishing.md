# Camera rigs, transitions, finishing

## Camera rigs
- Basic: Layer > New Camera (35mm) + 3D null "Camera Controller"; parent camera to null. Keyframe the
  null. Add a slow push on the camera itself for the whole comp so every scene drifts.
- Split rig: null "camera pan" (parent) -> null "camera zoom" -> camera. Key pans and zooms separately.
- Fly-through: null Z position cranked forward between scenes; F9, then Graph Editor handles to the
  middle (slow start, spike, quick settle). Time the spike to the cut.
- Z-space layering: background paper ~10000-20000 px back, scaled up to fill; mid elements 6000-9000;
  subject nearest. Randomise depths so the parallax feels organic. Parent a grey solid to the texture
  and push 2000 px back for a darker far layer.
- Letter portal: make a big word 3D, fly the camera through one letter (a paper strip) into the next scene.
- Lightweight alternative without a 3D camera: an adjustment layer with Transform; keyframe Scale
  100 -> 112 over the shot and put `posterizeTime(6); value + wiggle(1,4) - value` on Position.

## Transitions
- Ink-bleed matte: ink precomp, anchor at bottom, rotate 90 deg, duplicate and flip so it bleeds from the
  centre; use as an inverted track matte on the outgoing scene.
- Zoom-flip: hold ~10 frames, scale out + Rotation 180 + scale in; speed spike exactly at the flip;
  flip the precomp vertically so the next card reads upright.
- Displacement dissolve: Displacement Map sourcing an animated texture (horizontal/vertical = luminance),
  keyframed in ~6-frame bursts, with Levels keyed in sync; Roughen Edges + Fill on luma mattes for a
  torn-paper reveal.
- Mask expansion reveal: blobby pen mask around a texture (handwriting), Mask Expansion from hidden to full.
- Circle close: a shape grows to cover the frame and becomes the next background.
- Ink splash: organic white blob matte into a chart or photo; Black & White over the frame.

## Finishing stack (top to bottom)
1. Posterize Time 12 fps (adjustment layer).
2. Flicker: Curves (or Exposure) adjustment layer, opacity `posterizeTime(6); wiggle(2,100)`.
3. Grain: Add Grain intensity 1.2, size 1.3, blend ~0.2 (or a Kodak Vision 250D preset).
4. Camera Lens Blur adjustment keyed as focus breathing during fast zooms (blur 5-12, back to 0).
5. Vignette (optional), fog/dry-ice overlay (Screen, low opacity) for depth on maps.
6. Motion blur on all layers.
