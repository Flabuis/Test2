# Pixel art: Blender (3D to pixel), HyperFrames/canvas, Higgsfield

## Blender 3D-to-pixel (via the `blender` MCP)

Used by games like Dead Cells for complex animation. Save to `C:\Users\basha\Motion Design\Cluads Work Folder\pixel\`.
1. Model low-poly; toon shading: Diffuse BSDF → Shader to RGB → ColorRamp (Constant interpolation, 2–4 stops from the palette) → Emission (EEVEE).
2. Outline: Solidify modifier with flipped normals and a black backface material (inverted hull), or Freestyle at 1 px.
3. Camera: Orthographic; output at native resolution (e.g. 64×64 per sprite or 320×180 scene); Film > Filter Size 0.00 (no AA); Color Management: Standard view (not AgX/Filmic, which shift palette colours).
4. Animate on twos (Stepped F-modifier, step 2) or render every other frame.
5. Compositor: Pixelate node or render small; optional palette quantisation in post (Python cleanup script) to snap to the exact palette.
6. Hand-clean key frames afterwards for the best result.

## HyperFrames / canvas

- Render at native resolution into a `<canvas width="320" height="180">`, then scale with CSS by an integer: `canvas { width: 1920px; height: 1080px; image-rendering: pixelated; }`. Disable smoothing: `ctx.imageSmoothingEnabled = false`.
- All draw positions `Math.round()`; time-step animation `const f = Math.floor(t * 12)` for 12 fps sprite frames (seek-safe).
- Sprite sheets: `ctx.drawImage(sheet, (f % frames) * w, row * h, w, h, x, y, w, h)`; or CSS `background-position` with GSAP `ease: "steps(n)"`.
- Palette cycling: draw indexed buffers (Uint8Array of palette indices) and map through a rotated palette each step `pal[(idx + Math.floor(t*10)) % n]` for cycling ranges.
- Pixel fonts: load the TTF and use exact multiples of its design size; or a bitmap font sprite sheet.

## Higgsfield prompts

- "pixel art scene, 320x180, 16-color PICO-8 palette, [scene], clean 1-pixel outlines, dithered sky gradient, consistent pixel size, side-view retro game, no anti-aliasing"
- "16-bit pixel art character sprite sheet, [character], walk cycle 6 frames, limited palette, transparent background"
AI pixel art often has inconsistent pixel sizes and too many colours: always run the Python cleanup (`aseprite-and-cleanup.md`) and hand-fix before animating.
