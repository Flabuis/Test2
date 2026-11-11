# Glassmorphism: 3D glass in Blender

Use the `blender` MCP (`get_scene_info`, `run_python`, `render_preview`). Save .blend files to `C:\Users\basha\Motion Design\Cluads Work Folder\glass\`. Blender 4.2+ node names.

## Glass material (Principled BSDF)

| Setting | Clear glass | Frosted glass |
|---|---|---|
| Transmission Weight | 1.0 | 1.0 |
| Roughness | 0.0–0.05 | 0.2–0.45 |
| IOR | 1.45–1.52 | 1.45 |
| Base Color | white or a light tint | tinted pastel |
| Dispersion (4.2+, Cycles) | 0.02–0.1 for rainbow fringes | 0 |
| Thin Film Thickness (4.2+) | 300–600 nm for iridescence (optional) | 0 |
| Coat | 0.3–1.0 for a crisp top reflection | 0 |

Python:
```python
import bpy
m = bpy.data.materials.new("Glass_Clear"); m.use_nodes = True
b = m.node_tree.nodes["Principled BSDF"]
b.inputs["Transmission Weight"].default_value = 1.0
b.inputs["Roughness"].default_value = 0.02
b.inputs["IOR"].default_value = 1.5
if "Dispersion" in b.inputs: b.inputs["Dispersion"].default_value = 0.05
bpy.context.active_object.data.materials.append(m)
```

## Forms

Rounded, thick shapes: Bevel (large, 6–10 segments) + Subdivision; extruded and bevelled icons and logos (bevel depth gives the edge refraction). Combine glass with a solid coloured inner object or a frosted plate for "glass icon" layering.

## Lighting and background

- Glass shows its environment: the background and lights *are* the look.
- Background: a colourful gradient plane or emissive orbs behind the object (same palettes as the 2D variant), or a studio HDRI.
- Area strip lights (long thin, high strength) left and right/top for long specular highlights on the edges.
- AgX colour management, Look: Medium High Contrast or Punchy.

## Render settings

- **Cycles** (needed for real refraction and dispersion): 256–512 samples + denoise. Light Paths: Max Bounces 16+, Transmission 12+, Transparent 16+, Glossy 8. Caustics: Filter Glossy 1.0 to reduce noise.
- **EEVEE (Next):** enable raytracing (screen-trace refraction); set the material's Render Method to Dithered with "Raytraced Transmission"; faster, less accurate.
- Depth of field: slight, focus on the hero object.

## Motion

- Slow turntable or tilt (8–15° over 2–4 s) so refraction and highlights travel across the surface.
- Move the light strips or the background slowly to animate reflections without moving the object.
- Easing: smooth Bezier, gentle overshoot on entrance.
