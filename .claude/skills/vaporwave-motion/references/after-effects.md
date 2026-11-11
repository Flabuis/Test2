# Vaporwave: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`. Set the comp duration to the loop length first.

## Win95 window component

Precomp (e.g. 600 × 380):
- Body: rectangle `#C0C0C0`.
- Bevel: 2 px white lines top/left outside, 2 px `#808080` + 1 px black bottom/right (shape strokes or Bevel Alpha Edge 2, Light Angle −45, Intensity 1).
- Title bar: 26 px rectangle, Gradient Fill `#000080` → `#1084D0` (left to right), title text white bold 13–16 px system-like font (W95FA / Pixelated MS Sans Serif).
- Buttons: three small bevelled squares (_ □ ×).
- Content: text, an icon, or a precomp scene (window as a frame for footage).
Error dialog: smaller window with an icon (red circle ×, yellow triangle !), message text and an "OK" button.

## Error cascade

Duplicate the dialog layer N times. Position and In point by index:
```js
// Position
var step = 26; value + [(index - 1) * step, (index - 1) * step];
```
Offset each layer's In point by 2–4 frames (Sequence Layers, overlap) so they pop one after another; Scale 90 → 100 in 2 f, hold keyframes (no easing). Cursor moves in and Scale-clicks OK; the stack disappears instantly.

## Statues

- **3D (best):** render a rotating bust in Blender (see `blender-css-ai.md`) with transparency and import the sequence.
- **AE 2024+:** import a GLB statue model as a 3D layer (Advanced 3D renderer), add an environment light, rotate Y `time * 360 / 12`.
- **2D:** cut-out photo (public-domain scan or photo), pastel Tint/Gradient Map, slow float `value + [0, Math.sin(time * 2 * Math.PI / 6) * 12]`, slight rotation ±3°.

## Checkerboard floor and grid

- Solid 4000 × 4000, Effect > Generate > **Checkerboard** (Size 120, colours black/white or pink/cyan), 3D layer, X Rotation 90°, camera looking toward the horizon; scroll with Offset (loop one tile). Fade into a pastel gradient horizon.
- Pastel grid: Grid effect (as in `synthwave-motion`), but pastel pink/cyan with softer glow and no aggressive pulse.
- Sky: Gradient Ramp `#FBC2EB` → `#A6C1EE`; or a sunset photo with heavy pastel grade.

## Echo trails and ghosting

Effect > Time > **Echo**: Echo Time −0.03 to −0.08 s, Number of Echoes 4–10, Starting Intensity 1, Decay 0.5–0.7, Operator Maximum or Composite in Back. Or CC Wide Time. Slow crossfades (1–2 s) between scenes are fine here.

## Slowed footage

Time Stretch 150–300% (or Time Remapping), Frame Blending = Pixel Motion for dreamy smearing, or Frame Mix for ghosting. Use stock or original footage of malls, fountains, pools, palms, offices.

## Fullwidth / Japanese titles

Type fullwidth characters directly (ｖａｐｏｒｗａｖｅ, U+FF01–FF5E; ideographic space U+3000). Typewriter reveal: Text Animator with Opacity 0, Range Selector End 0 → 100 by Characters, stepped; a blinking cursor `Math.floor(time * 2) % 2 ? 100 : 0`. Japanese text vertical: separate characters stacked or a vertical-text precomp (AE doesn't set vertical Japanese natively for all fonts; check).

## Lo-fi textures

- **Pixelation:** Mosaic (Horizontal/Vertical blocks to 1/4–1/8 resolution) + Sharp Colors on; or render at low res and scale up with nearest-neighbour (Layer > Quality > Draft for pixel look).
- **Dither / posterize:** Posterize (Level 6–10) + Noise 8–15% before it for dither.
- **VHS (manual, after AEJuice's approach):** Add Grain (film-stock preset), precomp, three copies with Shift Channels (R / G / B) offset 2–6 px Screen/Add, tracking band (Displacement Map with a moving gradient), flicker (Exposure wiggle), Posterize Time for choppiness; scanlines via Venetian Blinds.
- **Datamosh look:** Displacement Map driven by a duplicated, Time-Displaced copy of the footage, or a dedicated datamosh plugin if installed.

## Screensaver bounce (DVD logo style)

```js
// Position: bounce inside the frame, seek-safe
var w = thisComp.width - 300, h = thisComp.height - 200, sx = 180, sy = 140;
function tri(t, L) { var m = t % (2 * L); return m < L ? m : 2 * L - m; }
[150 + tri(time * sx, w), 100 + tri(time * sy, h)];
```
Swap the fill colour on each bounce via a hold-keyed colour or an expression on `Math.floor(time * sx / w)`.

## Finish

- Pastel grade (lift blacks to lavender, push pinks/cyans), slight softness (Fast Box Blur 0.5–1).
- Check the loop: last frame flows into the first (Offset/loopOut("cycle") everything).
- Render H.264 and a GIF/WebP loop if wanted (export via Media Encoder/ffmpeg).
