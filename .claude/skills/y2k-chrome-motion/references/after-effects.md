# Y2K chrome: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## 2D chrome type (no plugins)

1. Text layer (extended or techno face, white), precomposed.
2. **Bevel Alpha:** Edge Thickness 6–14, Light Angle −60°, Light Intensity 0.6–0.8.
3. **Curves (the chrome trick):** on the RGB channel, draw a zig-zag curve (3–4 peaks and valleys). This turns smooth bevel shading into metallic banding. Then Hue/Saturation: Saturation −100 (or tint it slightly cool).
4. **Reflection gradient:** a Gradient Ramp or the chrome gradient (SKILL.md) image set to Overlay/Soft Light, track-matted to the text; animate its position slowly so the reflections move.
5. **Edge:** Layer Styles > Stroke 2–3 px dark gunmetal; Inner Glow white 20%.
6. **Depth:** Drop Shadow (soft, 30–40%) or a faux extrusion: duplicate the text 8–15 times behind, each offset 1 px down-right and darker (or the Repeater on a shape-text version).

## 3D chrome (native)

- **Advanced 3D renderer (AE 2024+):** set the comp renderer to Advanced 3D, make text or shape layers 3D with Geometry Options > Extrusion Depth 20–60 px (bevel options depend on version). Add an **Environment Light** with a studio HDRI as its source. In Material Options set high reflection/metal values (names vary by version; check the layer's Material Options). Turn on Shadows and Reflections in the renderer settings.
- **Cinema 4D renderer (legacy):** extrusion + bevel + Reflection 100%, Reflection Sharpness 100, with an environment layer.
- **Plugin option:** Element 3D or Deep Glow make this much easier if installed.
- For best quality spins and liquid metal, render the chrome element in Blender (`blender.md`) and composite here.

## Sheen sweep

A narrow, soft white diagonal bar (shape layer, Fast Box Blur 30–60), Add blend 60–90%, Alpha matted to the chrome text. Animate it across once over 0.6–1 s (ease in-out), during the hold. A thin bright core line + a wider soft glow bar reads best.

## Liquid metal melt and wobble

- **Wobble:** Turbulent Displace (Amount 10–30, Size 60–120, Complexity 2) with Evolution `time * 60`; Wave Warp for ripples (Height 4–10, Width 80, Speed 1).
- **Melt/drip:** Liquify (Turbulence or Warp, brush size large), keyframed via Distortion %; or CC Mr. Mercury (Velocity 0, Gravity 1–2, Blob sizes small) for drips off chrome type.
- **Mercury morph:** chrome-ify a gooey matte: blobs → Fast Box Blur → Simple Choker (see `glassmorphism-motion` gooey recipe), then Bevel Alpha + zig-zag Curves on the result.

## Sparkles

Star shape: Points 4, Inner Radius 12–18% of Outer, roundness 0, white fill + Glow. Twinkle: Scale 0 → 120 → 100 with Rotation 0 → 45° over 6–8 f, then Opacity to 0 over 10 f. Stagger several across the hero; a few bigger ones on beats.

## Glow, bloom, flares

- **Glow stack:** Glow (Threshold 70–80%, Radius 15, Intensity 0.6) + a second Glow (Radius 80–120, Intensity 0.3). Deep Glow plugin if available.
- **Flares:** Lens Flare effect (105 mm Prime, brightness 80–130%) on a black solid in Screen/Add mode; animate the Flare Center with the camera or across on hits. Optical Flares plugin if available.

## Holographic gradient

4-Color Gradient (pastel holo colours, Blend 100–300) + Colorama (Input Phase = Intensity, Output Cycle = Golden/Rainbow preset, Phase Shift `time * 30`) on a matte of the target shape, Soft Light or Overlay over chrome.

## Glitch cut (2–6 frames)

- RGB split: three copies with Shift Channels (R / G / B only), offset ±8–20 px, Add blend.
- Scanlines: Venetian Blinds (Direction 0°, Width 2–4, Completion 40%) at low opacity.
- Blocky displacement: Displacement Map with a Fractal Noise (Block) map, Max Displacement 40.
Keep it on cuts only, then return to clean chrome.

## Wireframe globe / rings

CC Sphere with a grid texture (Grid effect on a solid as the source), or Shape ellipses with Repeater rotating in 3D. Thin white strokes + Glow.

## Finish

- Motion blur on for spins and fast moves.
- Slight chromatic aberration on edges (optional), light grain 1–2%.
- Render ProRes master; H.264 at high bitrate (black-to-white chrome banding compresses badly at low bitrate).
