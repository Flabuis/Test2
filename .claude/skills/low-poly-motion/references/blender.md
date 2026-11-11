# Low poly: Blender recipes

Use the `blender` MCP (`get_scene_info`, `run_python`, `viewport_screenshot`, `render_preview`). Save .blend files to `C:\Users\basha\Motion Design\Cluads Work Folder\lowpoly\`. Blender 4.x.

## Modelling

- Model directly with few vertices (primitives with low segments: Ico Sphere subdivisions 1–2, Cylinder 6–8 sides, Cone 5–7), then shape.
- **Shade Flat** (Object > Shade Flat; or in Geometry Nodes Set Shade Smooth = off).
- **Decimate modifier:** Collapse with Triangulate on, Ratio 0.05–0.3; or Planar (angle 5–15°) to merge near-flat faces. Sculpted terrain decimates unevenly (dense at edges): prefer Remesh (Voxel, large size) + Decimate, or model low first.
- **Triangulate modifier** for consistent triangle facets.
- Exaggerate silhouettes; keep similar edge lengths across objects.

## Terrain

1. Grid (e.g. 60 × 60 subdivisions), Displace modifier with Clouds/Noise (strength 1–4, size 0.5–2), Triangulate, Shade Flat.
2. Colour by height: Geometry > Position (or Attribute) → Separate XYZ (Z) → Map Range → ColorRamp (Constant interpolation for banded water/sand/grass/rock/snow, or Linear for soft blends across facets) → Base Color.
3. Flat per-face colour jitter: in Geometry Nodes, Random Value on the **Face** domain → Store Named Attribute `jitter` → in the shader mix ±5% value/hue.

## Materials and light

- Principled BSDF: Roughness 0.6–0.9, Specular low, flat colours (or emission-free toon via Shader to RGB + Constant ColorRamp for stricter flat tones).
- Sun light (strength 2–4, angle 1–3°) from a 3/4 high direction + World colour/HDRI at low strength for fill. AgX, Medium Low Contrast.
- Fog: World Volume Scatter (low density) or Mist pass for depth layering.
- EEVEE for speed; Cycles for nicer bounce light.

## Animation

- **Turntable:** empty at the origin, objects parented, Z rotation 360° linear over the loop; or camera orbiting.
- **Vertex waves:** animate the Displace texture coordinates (Texture Coordinates = Object, animate an empty's location) or in Geometry Nodes Set Position with Noise Texture (4D, W = `#frame/48`) × strength; faces re-light every frame.
- **Water:** separate low-poly plane with a small wave displacement, slightly glossy (Roughness 0.3) and lighter blue.
- **Shatter:** Cell Fracture add-on (bundled extension) into ~50–300 shards, or Geometry Nodes: Split Edges → Translate each face along its normal × factor + random rotation (Rotate Instances on faces converted to instances) driven by an animated value; reverse for assemble.
- **Morph:** Shape Keys on the same mesh (Basis → Target), or Geometry Nodes point matching (same vertex count) with a mix factor.
- **Crystal growth:** shards scaled from their base (origin at base) with staggered keyframes or a GN delay by distance.
- **Sway:** trees with a Simple Deform (Bend) driven by `sin(frame/24)*0.05`.

## PS1 variant

Very low poly (100–500 tris per object), low-res textures (64–128 px) with Closest interpolation, render at 320×240 and upscale nearest; vertex snapping wobble via Geometry Nodes Set Position snapping (Snap to a grid in screen-ish space: `round(pos * 40) / 40`); 15–20 fps (stepped); fog; no AA (Film Filter Size 0).

## Render

PNG sequence (transparent if compositing). Motion blur light (0.3 shutter) for orbits; none for PS1.
