---
name: pixel-art-motion
description: Pixel art in motion - a fixed low-resolution grid scaled by whole numbers, limited palettes (Game Boy, PICO-8, Sweetie 16, Endesga 32) with hue-shifted ramps, clean 1-px lines, manual anti-aliasing, dithering, consistent pixel size (no mixels), pixel fonts and game UI - with motion rules (frame-by-frame at 8-12 fps, timing by holds, whole-pixel movement, sub-pixel animation, smears, palette cycling, hit flashes, pixel screen shake, stepped parallax, dither and mosaic transitions). Includes Aseprite, After Effects, Blender (3D-to-pixel), HyperFrames/canvas, Python cleanup and Higgsfield recipes. Use when the user asks for pixel art, 8-bit, 16-bit, retro game style, sprite animation, Game Boy look, arcade, pixel UI, dithering, or palette cycling.
---

# Pixel art motion

Pixel art is drawn on a **fixed low-resolution grid** where every pixel is a deliberate choice, then scaled up by whole numbers so pixels stay square and crisp. Its beauty is constraint: few colours, few pixels, few frames. Motion is mostly **frame-by-frame**, with timing carried by holds rather than smooth tweening.

Pair with: `flat-2d-motion` (shape and character design thinking), `typography` (legibility at tiny sizes), `synthwave-motion` / `vaporwave-motion` (arcade and early-web cousins), `higgsfield-generate`. Design key frames (sprites and scenes) at native resolution first ([[motion-is-graphic-design]]).

References:
- `references/aseprite-and-cleanup.md`: canvas sizes, palettes, Aseprite workflow and CLI export, Python cleanup for AI or scaled art.
- `references/after-effects.md`: native-res comps, whole-pixel snapping, nearest-neighbour upscale, palette cycling, pixel transitions.
- `references/blender-code-ai.md`: 3D-to-pixel rendering, HyperFrames/canvas, sprite sheets, Higgsfield prompts.
- `references/history.md`: background and sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Grid | Pick one native resolution and never mix pixel sizes ("mixels"). Scale only by whole numbers (×2, ×3, ×4, ×6, ×8) with nearest-neighbour. |
| Palette | Limited: 4 (Game Boy) to 16–32 colours. Build hue-shifted ramps: shadows shift toward cool/purple, highlights toward warm/yellow, not just darker/lighter. |
| Lines | Clean 1-px lines, no doubles or orphan pixels; curves step in consistent increments (1-1-2-3, not 1-3-1). Selective outlines (darker, coloured) often beat black everywhere. |
| Anti-aliasing | Manual and sparing: a few mid-tone pixels on jaggy curves; never against unknown backgrounds (halos). |
| Dithering | Checkerboard or pattern dithers for gradients and textures; sparingly, or it turns muddy. |
| Readability | Silhouettes read at 1×; strong value contrast; no noisy detail. |
| Light | One light direction for the whole scene. |
| Type | Pixel fonts at their native size (Press Start 2P, Silkscreen, Pixelify Sans, VT323, m5x7): never scaled by fractions. |
| UI | Game UI vocabulary: 9-slice dialog boxes, health bars, score counters, cursors, menus. |
| No | Rotation by arbitrary angles, non-integer scaling, smooth blur, soft gradients, mixed resolutions. |

**Canvas suggestions:** 16:9 → 320×180 (×6 = 1920×1080) or 480×270 (×4); 9:16 → 180×320 (×6) or 270×480 (×4); 1:1 → 270×270 (×4 = 1080) or 180×180 (×6). Never pick a size that needs a fractional scale (240×240 → 1080 would be ×4.5).

**Palettes:** Game Boy `#0F380F #306230 #8BAC0F #9BBC0F`; PICO-8 (16), Sweetie 16, Endesga 32, Resurrect 64 (load from Lospec).

## 2. Motion principles

1. **Frame by frame at 8–12 fps.** Most pixel animation runs "on twos" (12 fps) or slower; cycles use few frames (walk 4–8, idle 2–6, run 4–6).
2. **Timing by holds.** Spacing can't be fine-tuned within a pixel, so ease with frame duration: hold anticipation and key poses longer, in-betweens shorter. Uniform durations look like a metronome.
3. **Whole-pixel movement.** Everything moves in whole native pixels, including the camera. No half pixels (they blur or jitter).
4. **Sub-pixel animation** for subtle motion (idle breathing, cloth, glints): shift colour values along edges so the eye reads movement smaller than a pixel.
5. **Smears and squash.** Fast actions use smear frames (stretched shapes, multiples) and pixel-level squash and stretch.
6. **Palette cycling.** Animate by rotating colours through a palette ramp (waterfalls, fire, water, neon, loading bars), the classic Mark Ferrari / Amiga technique.
7. **Hit feedback.** Impact = 1–2 white/flash frames, hit-stop (hold 2–4 frames), screen shake in whole pixels, particles as single pixels or tiny squares.
8. **Stepped parallax.** Background layers scroll at different whole-pixel rates; distant layers fewer pixels per frame.
9. **Game-like UI timing.** Text types on with a per-character blip; menus snap; cursors blink at a steady rate.

## 3. Signature moves

| Move | How |
|---|---|
| Sprite cycle | Character walk/run/idle loop with bob and secondary motion. |
| Palette cycle | Waterfall, lava, neon sign or rainbow driven by colour rotation. |
| Hit flash + shake | White frame, hit-stop, 2–4 px shake, pixel particles. |
| Dialog box | 9-slice box opens (grows in steps), text types with blips, a ▼ cursor blinks. |
| Parallax scroll | Layers of sky, mountains, trees scroll at different pixel rates. |
| Level transition | Mosaic/pixelate out and in, or a stepped iris (circle) wipe, or a dither fade. |
| Coin/pickup | Spin (4-frame cycle) + sparkle pixels + score pop. |
| Glitch/CRT | Optional scanlines, slight curvature, colour bleed for arcade nostalgia. |
| Pixel type reveal | Big pixel letters build block by block. |
| Isometric build | Pixel isometric scene assembles tile by tile. |

## 4. Build process

1. **Choose native resolution, scale factor and palette** (lock all three).
2. **Key frames at 1×:** design sprites/scenes/UI pixel by pixel (Aseprite or similar). Check silhouettes and readability at 1×.
3. **Animate frame by frame** (or 3D-to-pixel in Blender for complex motion).
4. **Composite** at native res in AE/HyperFrames, snapping all positions to whole pixels; add palette cycles, transitions, UI.
5. **Upscale** by an integer with nearest-neighbour as the final step.
6. **Check:** zoom to 100% of the output: every pixel the same size, no blur, no stray AA halos, palette respected.

## 5. Critique checklist

- One pixel size everywhere (no mixels, no fractional scaling)?
- Palette within the chosen limit, with hue-shifted ramps?
- Clean lines (no doubles/orphans), sparing AA and dithering?
- Silhouettes readable at 1×?
- Motion on whole pixels, timing by holds, not uniform frame lengths?
- Nearest-neighbour upscale, no blur or smoothing anywhere?
- Pixel fonts at native size and legible on a phone?
