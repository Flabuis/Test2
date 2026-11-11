# Clay 3D: Blender recipes

Use the `blender` MCP: `get_scene_info` first, `run_python` for builds, `viewport_screenshot` for quick checks, `render_preview` (needs a camera) for look checks.
Save .blend files to `C:\Users\basha\Motion Design\Cluads Work Folder\clay\` and renders next to them. Blender 4.x node names below.

## Modelling

- **Rounded primitives:** Bevel modifier (Width 10–20% of object size, Segments 6–8, Limit Method Angle) + Subdivision Surface (Viewport 1, Render 2). Shade Smooth / Auto Smooth.
- **Blobby organic shapes:** Remesh (Voxel, size small) + Smooth / Corrective Smooth, or Metaballs for merging blobs.
- **Inflated 2D logos and type:** text or SVG curve → Extrude 0.1–0.3 + Bevel Depth 0.05–0.15 (Round, Resolution 6–8) → convert to mesh → Remesh + Smooth. Or Geometry Nodes: Fill Curve → Extrude Mesh → Subdivide → Blur Attribute on position.
- **Clay noodles:** a curve with Bevel Depth (round) and Fill Caps; animate Bevel End (Geometry > Start & End Mapping) 0 → 1 for a noodle draw.
- **Handmade imperfection:** a Displace modifier with a Clouds texture, strength 0.005–0.02 of object size. Keep it subtle.

## Clay material (Principled BSDF)

| Setting | Smooth clay | Claymation |
|---|---|---|
| Roughness | 0.5–0.6 | 0.65–0.8 |
| Specular IOR Level | 0.3 | 0.2 |
| Subsurface Weight | 0.15–0.3 | 0.08–0.15 |
| Subsurface Radius | (1.0, 0.45, 0.25) × scale suited to object size | same |
| Sheen | 0.1 | 0.1–0.2 |
| Bump strength | 0.02–0.05 | 0.08–0.2 |

Detail layers, mixed into Normal via Bump nodes:
- **Lumps:** Noise Texture (Scale 4–8, Detail 2) → Bump, strength 0.05.
- **Grain:** Noise Texture (Scale 60–150, Detail 8) → Bump, strength 0.02–0.05.
- **Fingerprints:** Wave Texture (Rings, Scale 40–80, Distortion 3–6) masked by a large-scale Noise through a narrow ColorRamp so prints appear in patches; Bump strength 0.02–0.05.
- **Colour variation:** Noise (Scale 3) → ColorRamp between base colour and a ±5–8% value/hue variant → Base Color.

One master material, colour per object: use an Attribute node reading object colour (Object Info > Color, or Object Info > Random → ColorRamp of palette colours).

Python (create and assign a clay material):
```python
import bpy
def clay_mat(name, rgb, rough=0.6, sss=0.2, bump=0.04):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Specular IOR Level"].default_value = 0.3
    b.inputs["Subsurface Weight"].default_value = sss
    b.inputs["Subsurface Radius"].default_value = (1.0, 0.45, 0.25)
    b.inputs["Subsurface Scale"].default_value = 0.05
    n = nt.nodes.new("ShaderNodeTexNoise"); n.inputs["Scale"].default_value = 90; n.inputs["Detail"].default_value = 8
    bp = nt.nodes.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = bump
    nt.links.new(n.outputs["Fac"], bp.inputs["Height"]); nt.links.new(bp.outputs["Normal"], b.inputs["Normal"])
    return m
obj = bpy.context.active_object
obj.data.materials.clear(); obj.data.materials.append(clay_mat("Clay_Peach", (1.0, 0.55, 0.45)))
```
(Colour values are linear; convert sRGB hex with `(c/255)**2.2`.)

## Lighting and set

- **Cyc:** a plane with the back edge extruded up and a large bevel (curved backdrop), in the background clay colour, same clay material at higher roughness.
- **Key:** Area light, size 2–4 m (large and soft), 45° side/top, warm (≈ 4500 K). **Fill:** opposite side, cool (≈ 7000 K), 30–50% of key. **Rim:** behind and above, to separate silhouettes.
- Or a soft studio HDRI at low strength plus one area key.
- **Colour management:** AgX (Blender 4.x), Look: Medium Low Contrast or Punchy depending on palette.
- **AO:** Cycles gets it naturally; in EEVEE enable Ambient Occlusion / raytracing.

## Camera

- 50–85 mm lens, 20–35° high angle, camera on a null for slow dolly/slider moves.
- Depth of field on: f-stop 1.8–4 with the focus object set. Smaller f-stop = more miniature.
- Smooth clay: eased moves. Claymation: camera also on twos with micro-jitter.

## Animation

- **Squash and stretch with volume:** keyframe a driver or set scale as `(1/sqrt(s), 1/sqrt(s), s)` around a base pivot (set origin to the contact point).
- **Jiggle:** a Lattice deform with hooks animated with damped follow-through; or Shape Keys (squashed/stretched) driven by velocity; or a Wiggle Bones add-on on an armature; or Soft Body / Cloth simulation with pinned groups for heavy jiggle.
- **Ease:** Bezier interpolation, Auto Clamped handles, then tweak in the Graph Editor. Overshoot with Back/Elastic easing modes for pops.
- **Claymation on twos:** add a Stepped Interpolation F-modifier (Frame Step 2) to every F-curve:
```python
import bpy
for ob in bpy.data.objects:
    ad = ob.animation_data
    if ad and ad.action:
        for fc in ad.action.fcurves:
            if not any(m.type == 'STEPPED' for m in fc.modifiers):
                m = fc.modifiers.new('STEPPED'); m.frame_step = 2
```
- **Boil:** use 4D Noise/Voronoi (W input) for fingerprints, lumps and colour variation, and drive W with a stepped frame value: driver expression `floor(frame/2)*0.37`. Do the same for the Displace texture offset.
- **Micro-jitter:** per-object driver on location, e.g. `noise.random()` is not seek-stable; use `sin(floor(frame/2)*12.9898)*0.0003` style hashes instead.

## Render

- **Cycles:** 128–256 samples + denoise (OpenImageDenoise), Light Paths default. Best SSS and AO.
- **EEVEE (Next):** much faster; enable raytracing and shadows; SSS is approximate.
- Output PNG or EXR sequence; render passes (AO, Mist, Cryptomatte) if compositing in AE.
- Claymation: render at 24 fps with stepped keys (or 12 fps and conform). Motion blur off.
