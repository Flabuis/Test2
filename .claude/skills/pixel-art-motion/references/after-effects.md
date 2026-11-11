# Pixel art: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## Comp structure

```
OUTPUT 1080x1920 (or 1920x1080)
 └─ NATIVE (270x480 or 320x180) scaled to exactly 400% / 600%, Quality: DRAFT (nearest neighbour)
      ├─ UI, text, sprites (PNG sequences from Aseprite)
      ├─ effects (palette cycle, flashes)
      └─ background layers (parallax)
```
- Build everything inside NATIVE at 1×.
- In OUTPUT, the NATIVE layer: Scale = integer × 100%, Position on whole pixels, **Quality and Sampling switch = Draft** (nearest neighbour). Also set footage/precomp layers inside NATIVE to Draft if scaled.
- Frame rate: comp 24 or 30 fps; sprite timing comes from the PNG sequences (import as 12 fps) or Posterize Time 12 on motion layers.

## Whole-pixel snapping

On any moving layer inside NATIVE:
```js
// Position
[Math.round(value[0]), Math.round(value[1])];
```
Camera-like moves: animate a null and round the null's position too (and keep the anchor points on whole pixels). Avoid Rotation (except 90° steps) and Scale (except integer steps).

## Stepped parallax

Background layers parented to a scroll null; each layer:
```js
var s = thisComp.layer("SCROLL").transform.position[0];
var rate = 0.25;                          // 1 = foreground, 0.5 mid, 0.25 far
[Math.round(value[0] + s * rate), value[1]];
```

## Crisp vector or text at native res

AE anti-aliases shapes and text. To make them pixel-crisp at native res: precomp → Levels (Alpha channel: Input Black 120, Input White 136) or Simple Choker (0) to binarise alpha → **Posterize** or palette mapping for colours. Pixel fonts must be set at their design size (e.g. 8 px or 16 px) and positioned on whole pixels.

## Palette cycling

- **Indexed approach:** draw the cycling area (water, lava, neon) in greyscale "index" values (e.g. 8 distinct greys), then Colorama: Input Phase = Intensity, Output Cycle = custom with your palette colours (no interpolation: set Interpolate Palette off), **Phase Shift** stepped: `posterizeTime(10); time * 360 / 2` (cycles the colours every step).
- **Simple approach:** duplicate the layer per palette step with Hue/Change To Color and hold-key them in sequence.

## Hit flash, hit-stop, shake

- Flash: Fill effect white for 1–2 frames on the hit sprite (hold keys), or Invert for the whole screen 1 frame.
- Hit-stop: freeze the action layers for 2–4 frames (Time Remap hold).
- Shake (whole pixels): on the NATIVE scene null `var t = time - hitTime; t >= 0 && t < 0.2 ? value + [Math.round(Math.sin(t * 90) * 3), Math.round(Math.cos(t * 70) * 2)] : value`.

## Transitions

- **Mosaic out/in:** on OUTPUT, Mosaic Horizontal/Vertical Blocks stepped from the native count down to 1/8 and back up (hold keys), Sharp Colors on.
- **Iris wipe:** a circle mask/shape at native res with Levels-binarised alpha (pixel-stepped edge), radius animated in steps.
- **Dither fade:** a precomp of a Bayer-matrix dither pattern (4×4 thresholds) + Levels driven threshold used as Luma Matte; animate the threshold in 16 steps.

## Dialog box and typewriter

9-slice box (pixel border PNG) grows in 3–4 steps; text layer (pixel font) with Text Animator Opacity 0 and Range Selector End animated per character at 30–50 chars/s, stepped; a blinking ▼ at the end `Math.floor(time * 3) % 2 ? 100 : 0`.

## Finish

- Never add blur, glow (unless deliberately pixelated afterwards), motion blur or soft grain.
- Optional CRT: scanlines (every other output row darker by 20–30%, aligned to the scale factor), slight colour bleed; apply at OUTPUT size.
- Render PNG sequence or ProRes 4444; H.264 at high bitrate with 4:4:4 if possible (chroma subsampling blurs coloured pixel edges).
