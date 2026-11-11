# Isometric: Blender, Illustrator, CSS/GSAP and Higgsfield

## Blender (via the `blender` MCP)

Save to `C:\Users\basha\Motion Design\Cluads Work Folder\isometric\`.

Camera:
```python
import bpy, math
cam = bpy.data.objects.get("Camera") or bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
if cam.name not in bpy.context.scene.collection.objects: bpy.context.scene.collection.objects.link(cam)
cam.data.type = 'ORTHO'
cam.data.ortho_scale = 12                     # frame the scene by this, not by moving closer
cam.rotation_euler = (math.radians(54.736), 0, math.radians(45))   # true isometric; use 60° X for 2:1 dimetric
d = 30 / math.sqrt(3); cam.location = (d, -d, d)   # on the view axis, looking at the origin
bpy.context.scene.camera = cam
```
(With rotation (54.736°, 0, 45°) the camera looks along (−1, 1, −1), so placing it at (d, −d, d) centres the origin. Frame with `ortho_scale`, not by moving closer.)

**Auto three-tone flat shader** (consistent face tones without lighting):
Geometry > Normal → Separate XYZ; Z > 0.5 → top colour; else X > 0.5 (or the camera-left axis) → left colour; else → right colour (Math Greater Than + Mix nodes) → Emission (strength 1) in EEVEE. Colours: base hue at three values. Gives clean vector-like iso renders.

**Lit look:** Sun light from top-left (rotation matched to the light convention), soft shadows, World ambient; AgX Medium Low Contrast for soft illustration.

**Animation:** pieces drop in with keyframes on Z (ease-out + bounce via Graph Editor), extrusions by scaling Z from origin at the base, exploded views on Z; Geometry Nodes for cascades (delay by `(x + y)`). Turntable: rotate an empty parenting the diorama in 90° steps. Freestyle 1 px for optional outlines.

## Illustrator (via the `illustrator` MCP)

Save to `C:\Users\basha\Motion Design\Illustrator Projects\`.
- Iso grid: Polar/Rectangular Grid tool + SSR, or a pre-made isometric grid; turn on Smart Guides with 30°/90°/150° construction angles (Preferences > Smart Guides > Construction Guides: 30° Angles).
- Faces with SSR (Scale vertical 86.602%, Shear ±30°, Rotate ±30°); or Effect > 3D and Materials > Extrude with an Isometric preset (Isometric Top/Left/Right), then Object > Expand Appearance for flat faces.
- Name layers per part for AE import (Composition – Retain Layer Sizes).

## CSS / GSAP (HyperFrames)

```css
.world { transform: rotateX(54.736deg) rotateZ(-45deg); transform-style: preserve-3d; }   /* true iso; rotateX(60deg) for 2:1 */
.block { position: absolute; transform-style: preserve-3d; }
.block .top { background: var(--t); } .block .left { background: var(--l); } .block .right { background: var(--r); }
```
Build boxes from three faces (top translated by height on Z; sides rotated 90°). GSAP:
```js
const at = n => n * 0.5;
tl.from(".block", { z: 400, duration: 0.45, ease: "bounce.out", stagger: { each: 0.08, from: "start" } }, at(1));
tl.from(".bar", { scaleZ: 0, transformOrigin: "50% 50% 0", duration: 0.6, ease: "power3.out", stagger: 0.06 }, at(3));
tl.to(".packet", { motionPath: { path: "#isoPath" }, duration: 3, ease: "none", repeat: -1 }, 0); // flat SVG overlay alternative
```
SVG is often simpler: draw iso art in Illustrator, export SVG, animate groups along iso vectors (e.g. `x: 52, y: 30` per unit for true iso).

## Higgsfield prompts

- "isometric illustration of a [scene], true isometric projection, floating island diorama, three-tone flat shading with light from the top left, soft pastel palette, tiny people and trees for scale, clean vector style, white background"
- "isometric 3D render of a tech workspace, orthographic, soft clay-like materials, cut-away view, soft shadows"
- "2:1 pixel art isometric tile map of a village, 16-color palette"
Use as style frames; rebuild with separated parts for animation.
