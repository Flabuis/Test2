# Low poly: SVG/canvas, Three.js (HyperFrames) and Higgsfield

## SVG triangles (from the Python script)

Inline the generated SVG; animate polygons by their `data-cx/cy` distance (seek-safe, timeline-driven):
```js
const polys = [...document.querySelectorAll("polygon")], O = { x: 540, y: 960 };
polys.forEach(p => {
  const d = Math.hypot(+p.dataset.cx - O.x, +p.dataset.cy - O.y);
  tl.from(p, { scale: 0, transformOrigin: `${p.dataset.cx}px ${p.dataset.cy}px`, duration: 0.35, ease: "back.out(1.6)" }, 0.5 + d / 900);
});
// shatter out: deterministic offsets from index
polys.forEach((p, i) => { const a = (i * 2.399) % 6.283, r = 200 + (i * 37) % 300;
  tl.to(p, { x: Math.cos(a) * r, y: Math.sin(a) * r + 200, rotation: (i * 53) % 360 - 180, opacity: 0, duration: 1.2, ease: "power2.in" }, 6 + (i % 20) * 0.01); });
```
Over ~2,000 polygons, draw to canvas instead (same maths per frame from `t`).

## Three.js (HyperFrames adapter)

```js
const mat = new THREE.MeshStandardMaterial({ color: 0x7cc47f, flatShading: true, roughness: 0.8 });
const geo = new THREE.PlaneGeometry(40, 40, 40, 40).toNonIndexed();   // non-indexed = per-face normals
// per frame from timeline time t: displace vertices with a deterministic noise, then geo.computeVertexNormals()
```
Directional light + hemisphere light; fog; camera orbit from `t`. Keep everything a pure function of time for seek safety.

## Higgsfield prompts

- "low poly 3D landscape, faceted flat-shaded triangles, mountains, pine trees and a lake, soft gradient sky from blue to peach, consistent polygon size, limited pastel palette, soft sunlight, clean render"
- "low poly portrait made of coloured triangles, Delaunay triangulation, flat facets, dark background"
- "low poly crystal cluster, faceted violet and cyan gems, flat shading, dark navy background, glowing highlights"
- "PS1 style low poly scene, wobbly low-res textures, fog, 1998 video game look"
Use as style frames; build animatable geometry in Blender/AE.
