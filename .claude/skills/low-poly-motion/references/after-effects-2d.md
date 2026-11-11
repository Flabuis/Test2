# Low poly: 2D triangulation and After Effects

Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## Python: image → low-poly SVG (tested 2026-10-10)

Pillow only (no scipy). Jittered-grid triangulation, each triangle filled with the image colour at its centroid. Output: SVG (one `<polygon>` per triangle, with data attributes for animation) + a PNG preview.
```python
# python -I lowpoly.py input.jpg out.svg --cell 40 --jitter 0.35 --shade 0.07
import sys, random
from PIL import Image, ImageDraw
src, dst = sys.argv[1], sys.argv[2]
cell = int(sys.argv[sys.argv.index("--cell") + 1]) if "--cell" in sys.argv else 40
jit = float(sys.argv[sys.argv.index("--jitter") + 1]) if "--jitter" in sys.argv else 0.35
shade = float(sys.argv[sys.argv.index("--shade") + 1]) if "--shade" in sys.argv else 0.07   # per-facet light variation
im = Image.open(src).convert("RGB"); W, H = im.size; random.seed(7)
cols, rows = W // cell + 1, H // cell + 1
P = [[(min(W - 1, max(0, c * cell + (random.uniform(-jit, jit) * cell if 0 < c < cols - 1 else 0))),
       min(H - 1, max(0, r * cell + (random.uniform(-jit, jit) * cell if 0 < r < rows - 1 else 0))))
      for c in range(cols + 1)] for r in range(rows + 1)]
tris = []
for r in range(rows):
    for c in range(cols):
        a, b, d, e = P[r][c], P[r][c + 1], P[r + 1][c], P[r + 1][c + 1]
        tris += [(a, b, e), (a, e, d)] if (r + c) % 2 == 0 else [(a, b, d), (b, e, d)]
prev = Image.new("RGB", (W, H)); dr = ImageDraw.Draw(prev); out = []
for i, t in enumerate(tris):
    cx, cy = sum(p[0] for p in t) / 3, sum(p[1] for p in t) / 3
    samples = [((cx * 2 + p[0]) / 3, (cy * 2 + p[1]) / 3) for p in t] + [(cx, cy)]   # average 4 points
    px = [im.getpixel((int(min(W - 1, x)), int(min(H - 1, y)))) for x, y in samples]
    k = 1 + random.uniform(-shade, shade)                                            # facet catches light
    col = tuple(max(0, min(255, int(sum(c[j] for c in px) / len(px) * k))) for j in range(3))
    dr.polygon(t, fill=col)
    pts = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in t)
    out.append(f'<polygon points="{pts}" fill="#{col[0]:02x}{col[1]:02x}{col[2]:02x}" data-cx="{cx:.0f}" data-cy="{cy:.0f}" data-i="{i}"/>')
open(dst, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" shape-rendering="crispEdges">' + "".join(out) + "</svg>")
prev.save(dst.replace(".svg", "_preview.png"))
```
Tips: smaller `--cell` on faces/hero areas (run twice and mask), or add points along edges for portraits (true Delaunay with edge points needs scipy or the open-source Triangler tool). Slight gaps between triangles? Add `stroke="same colour" stroke-width="0.6"` per polygon.

## SVG → After Effects shapes

Open the SVG in Illustrator (`illustrator` MCP), save as .ai, import into AE as Composition and **Create Shapes from Vector Layer**: each triangle becomes a shape group. Or ExtendScript-build shape layers directly from the polygon list (fine up to ~1,500 triangles; group by rows for performance).

## Facet wave reveal (2D)

Per triangle group, a delay by distance from a point:
```js
// on the group's Transform: Scale, inside the shape layer (or a layer per triangle)
var origin = [540, 960], d = length(content(thisProperty.propertyGroup(2).name).transform.position, origin);
var t = time - 1 - d / 900;                  // 900 px per second sweep
var p = clamp(t / 0.35, 0, 1); p = 1 - Math.pow(1 - p, 3);
[100 * p, 100 * p];
```
Simpler: keep triangles as separate layers (script) and offset In points by distance; animate Scale from the triangle centre or a 3D Y-rotation flip (cards flip in).

## Shatter (built in)

- **CC Pixel Polly:** Force, Gravity, Spinning, Force Center; Grid Spacing sets triangle size (match the facet size); Object = Polygon (triangles); reverse time for assemble.
- **Shatter effect:** Shape Pattern = Triangles, Repetitions, Extrusion Depth for thickness, Force 1/2 position and radius, Physics gravity; lights for facet shading.
- **Card Dance / Card Wipe** for grid flips (rectangular, but with triangle masks for facets).

## Low-poly background loop

Triangulated gradient (generate from a gradient image with the script), then a gentle vertex wave: easiest in Blender (plane + Displace) and render; or in AE apply Wave Warp/Turbulent Displace lightly to the flat triangle layer (keeps edges straight only at low amounts).

## Plexus / tech look

Plexus plugin (if installed): points + lines + triangles (Facets) from a grid with noise. Or Mattrunks' Isoscene approach / aw_Triangulator script (paid) for triangle-based scenes.

## 3D in AE

Advanced 3D renderer: import GLB low-poly models (flat-shaded in Blender before export), environment/parallel light, camera orbit.
