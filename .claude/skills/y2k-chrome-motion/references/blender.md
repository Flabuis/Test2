# Y2K chrome: Blender recipes

Use the `blender` MCP (`get_scene_info`, `run_python`, `render_preview`). Save .blend files to `C:\Users\basha\Motion Design\Cluads Work Folder\y2k\`. Blender 4.2+ names.

## Materials (Principled BSDF)

| Material | Settings |
|---|---|
| Mirror chrome | Base Color white (0.9–1.0), Metallic 1, Roughness 0.0–0.08 |
| Brushed / satin steel | Metallic 1, Roughness 0.2–0.35, Anisotropic 0.5–0.8 (needs tangents/UVs) |
| Liquid mercury | Metallic 1, Roughness 0.02, a weak Noise bump (strength 0.02) for ripples |
| Iridescent chrome | Metallic 1, Roughness 0.05, Thin Film Thickness 300–700 nm, Thin Film IOR 1.33–1.5 (oil-slick / holographic) |
| Candy plastic | Transmission 0.6–0.9, Roughness 0.05, IOR 1.45, tinted Base Color, Coat 1.0 |

```python
import bpy
def chrome(name="Chrome", rough=0.04, film=0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (0.95, 0.96, 0.98, 1)
    b.inputs["Metallic"].default_value = 1.0
    b.inputs["Roughness"].default_value = rough
    if film and "Thin Film Thickness" in b.inputs:
        b.inputs["Thin Film Thickness"].default_value = film
    return m
bpy.context.active_object.data.materials.append(chrome(film=450))
```

## Forms

- **Chrome type:** Text object, Extrude 0.05–0.15, Bevel Depth 0.02–0.05 (Round, Resolution 6) for highlights on edges. Extended fonts.
- **Liquid metal:** Metaballs for merging blobs (convert to mesh to render cleanly), or Remesh (Voxel) + Smooth + Displace (Voronoi/Noise, low strength) + Subdivision for melted shapes.
- **Drips:** a Simple Deform/Displace driven by a gradient texture, or a fluid sim (Mantaflow liquid) for real drips (slow; small domains).
- **Inflated bubbles:** Cloth sim with pressure on a low-poly shape, or Bevel + Subdivision for quick inflation.

## Lighting (chrome is its environment)

- A strong studio HDRI (strength 1.5–3) plus long Area strip lights (size 0.1 × 3 m, strength high) left, right and above. The strips create the long white highlight bands.
- Black or very dark planes around the subject add the dark reflection bands chrome needs.
- Y2K tint: a gradient World (pastel lilac/ice blue) or coloured light strips (pink, cyan) for holo reflections.
- Animate the strips or rotate the HDRI (Mapping node Z rotation) so reflections move even when the object is still.

## Render and bloom

- **Cycles:** 256+ samples, denoise, Glossy bounces 8+. Best chrome.
- **EEVEE (Next):** enable raytracing; good for fast iterations.
- **Compositor:** Glare node, Fog Glow (bloom, Threshold 0.8–1.0, Size 7–9) and Streaks (4 streaks, Angle 45°) for star glints; or use AE glow in post.
- Render PNG/EXR with alpha (Film > Transparent) to composite over Y2K backgrounds in AE.
