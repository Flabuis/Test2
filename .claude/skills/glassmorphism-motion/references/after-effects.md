# Glassmorphism: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## Living background (gradient orbs)

1. Dark or light base solid.
2. 3–5 ellipse shape layers (300–700 px) in palette colours.
3. Each drifts with a slow seamless loop on Position:
```js
var r = 120, p = 14 + index * 3;          // radius px, period s
value + [Math.sin(2*Math.PI*time/p) * r, Math.cos(2*Math.PI*time/(p*1.3)) * r * 0.7];
```
4. Precomp the orbs and apply Fast Box Blur (Radius 150–250, Iterations 3, Repeat Edge Pixels on), then a slight Noise (2%).
Alternatives: 4-Color Gradient with animated points, or real footage.

## Frosted glass panel (backdrop blur)

1. **Blur:** an Adjustment Layer with a rounded-rectangle mask (Mask Feather 0) = the panel shape. Effects: Fast Box Blur (Radius 30–50, Iterations 3, Repeat Edge Pixels) → Exposure +0.2 or Brightness +5. An adjustment layer blurs everything below it inside the mask, which is exactly a backdrop blur.
2. **Fill:** a shape layer with the same rounded rect, white fill 12–20% (or black 25–35% for dark).
3. **Edge:** the same shape, Stroke 2 px, Gradient Stroke white 60% → 10% from top-left to bottom-right. Or Layer Styles > Inner Glow / Stroke.
4. **Shadow:** Layer Styles > Drop Shadow: black, 12–18% opacity, distance 20–30, size 60–80, angle 90–120.
5. **Grain:** Noise 2–3% on the fill layer.
6. **Make the blur follow the panel:** a mask on the adjustment layer won't move with a parented null. Instead, skip the mask and set the adjustment layer's **Track Matte = Alpha Matte "Panel_Fill"** (AE 2023+ lets you pick any layer as the matte). Parent the fill, edge and shadow layers to one null and animate the null; the blur follows automatically.

## Edge lensing / refraction (Liquid Glass)

1. Precomp "Lens Map": the panel shape filled 50% grey, with Bevel Alpha (Edge Thickness 20–40, Light Intensity 1) or Inner Glow → then Fast Box Blur 10. This makes a height map that ramps at the edges.
2. On the adjustment layer (above the background, matted to the panel): Displacement Map → Map: Lens Map, Horizontal = Red, Vertical = Green (or Luminance), Max Displacement 20–40, Wrap off. Add a light Fast Box Blur (4–10) for Liquid Glass.
3. **Chromatic fringe:** duplicate the adjustment layer for R, G, B with Shift Channels and slightly different Max Displacement (e.g. 30 / 34 / 38), Screen blend. Keep it subtle.
4. Quick alternative: CC Lens or CC Glass (Bump Map = Lens Map, Softness 10, Height 30–60).

## Specular light sweep

Shape layer: a wide soft diagonal bar (white, Feather 60–100 via Fast Box Blur), Add blend at 30–50% opacity, Alpha matted to the panel. Animate it across the panel once over 0.6–1 s, ease in-out, timed just after the panel lands. A static edge highlight: Inner Glow 10–20% from the light side.

## Liquid merge (gooey)

1. Precomp the blobs/capsules (white shapes) that should merge.
2. On the precomp: Fast Box Blur (Radius 20–40) → Simple Choker (Choke Matte 20–40) or Levels on alpha (Input Black 100, Input White 160). Overlapping blurred shapes fuse into one smooth liquid outline.
3. Use the gooey precomp as the Track Matte for the glass blur/fill/edge layers.
4. Animate shapes with overshoot springs (`back`-style easing) so merges and splits jiggle.

## Glass type

Text layer as the Track Matte for a backdrop-blur adjustment layer, plus a duplicate text layer with Stroke 2 px white 50% and Inner Glow. Heavy weights (Bold/Black) work best.

## Parallax and tilt

- Make the panels 3D and use a camera with gentle moves; panels at Z −200 to −600, background far back (or 2D with position offsets × depth factor).
- Tilt: Rotation X/Y ±4–8° with ease; link the light sweep position to the rotation for a reacting highlight.

## Finish

- Motion blur on.
- Global Noise 1–2% on top to avoid banding in H.264.
- Render ProRes 422 HQ master, then H.264 at high bitrate (gradients band at low bitrates).
