---
name: low-poly-motion
description: Low poly in motion - faceted 3D models and 2D triangulated (Delaunay) illustrations, flat shading that shows every triangle, consistent polygon density, strong exaggerated silhouettes, limited palettes and height/light gradients across facets, crystals, terrains and low-poly portraits - with motion rules (facets flickering light as forms turn, rolling vertex-wave terrains, triangle shatter and assemble, same-topology morphs, facet flip reveals, slow orbits, faceted water). Includes Blender, After Effects, Python triangulation, CSS/SVG/Three.js and Higgsfield recipes, plus the retro PS1 variant. Use when the user asks for low poly, polygonal, faceted, triangulated, geometric 3D landscapes, low-poly portraits, crystal/gem looks, Delaunay backgrounds, or PS1-style retro 3D.
---

# Low poly motion

Low poly makes a feature of **few polygons**: forms are reduced to big flat facets, each a single tone, so light reads as a mosaic of triangles. It's stylised, clean and graphic, halfway between flat illustration and 3D. The rule that makes or breaks it: **show the facets** (flat shading) and keep them **consistent in size**.

Two families:
- **3D low poly (default):** flat-shaded models, landscapes, characters, crystals rendered in Blender (or AE 3D).
- **2D low poly:** images and backgrounds triangulated into coloured triangles (Delaunay or jittered grids), animated as shapes.
- Variant: **retro PS1 look** (very low poly, wobbly vertices, affine-warped low-res textures, no AA): nostalgic/eerie; see the Blender reference.

Pair with: `flat-2d-motion` (colour and staging), `isometric-motion` (iso low-poly dioramas), `clay-3d-motion` (soft 3D contrast), `pixel-art-motion` (PS1 cousin), `particle-motion` (shatter), `higgsfield-generate`. Design hero frames as finished stills first ([[motion-is-graphic-design]]).

References:
- `references/blender.md`: modelling, decimation, terrains, flat materials, facet colour variation, lighting, animation (waves, shatter, morph), PS1 variant.
- `references/after-effects-2d.md`: 2D triangulation (Python script, tested), SVG to AE shapes, facet waves, CC Pixel Polly / Shatter, Plexus, AE 3D.
- `references/code-ai.md`: SVG/canvas triangles and Three.js `flatShading`, GSAP, Higgsfield prompts.
- `references/history.md`: background, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Facets | Flat shading: every face one tone, edges visible through light change. Never smooth-shade low geometry ("cheap mobile game" look). |
| Density | Consistent polygon size across the scene; a bit smaller on the hero, never a jarring mix. |
| Silhouette | Model the silhouette first; exaggerate proportions (chunkier trunks, bolder rocks). |
| Palette | Limited, coordinated (often one palette texture): 5–8 hues; saturation reserved for the focal element. |
| Gradients | Across facets, not within them: colour by height (terrain), by light direction, or a soft background gradient. |
| Light | One key direction (sun) + soft fill/ambient; light is what draws the facets. |
| Detail | No photo textures (except PS1 variant); subtle per-face colour jitter for life. |
| Edges | Optional thin wireframe/outline accents for tech looks; most work uses no lines. |
| Background | Soft gradient sky or flat colour; fog/haze to separate depth layers. |

**Palettes**
- Nature: sky `#9ED8F5` → `#FCE3C2`, grass `#7CC47F` / `#5AA469`, rock `#8A8FA3`, sand `#F2D49B`, water `#3FA7D6`, wood `#9C6B4E`.
- Crystal tech: deep `#0E1A3A`, violet `#6B4DE6`, cyan `#3DE0FF`, magenta `#FF4FD8`, white highlights.
- Warm dusk: `#2B2D5C`, `#E85D75`, `#F7A072`, `#FCD581`, `#5B8E7D`.

## 2. Motion principles

1. **Facets sparkle as forms turn.** Slow rotations and camera orbits make each facet change brightness; that flicker is the style's signature. Keep moves slow enough to enjoy it.
2. **Vertex waves.** Terrains, water and backgrounds ripple by moving vertices (noise or sine), re-lighting facets as they move.
3. **Shatter and assemble.** Objects break into triangles that scatter (with physics or noise), or fly in and assemble into a form.
4. **Same-topology morphs.** Morph shape A to B by moving vertices of one mesh (shape keys / point matching): faceted transformation.
5. **Facet reveals.** 2D: triangles flip, pop or fade in sweeping by position (wave from a point). 3D: faces grow in from the ground or edges.
6. **Grounded easing.** Smooth ease in-out for camera and objects; small overshoot on pops; linear for continuous waves and orbits.
7. **Stylised life.** Trees sway, clouds drift, water ripples in low-poly cycles; loops for scenery.
8. **Light as storytelling.** Sun moves (day to dusk), colours shift across facets together.
9. **PS1 variant:** vertex snapping/wobble, low frame rate (15–20 fps) and low resolution.

## 3. Signature moves

| Move | How |
|---|---|
| Slow turntable | Hero (crystal, logo, character) rotates; facets flicker. |
| Terrain flythrough | Camera glides over a low-poly landscape with fog. |
| Wave field | Triangulated plane ripples like a sea or data field. |
| Triangle shatter | Logo/portrait bursts into triangles that drift, then reassembles. |
| Crystal growth | Shards extrude from the ground in a stagger. |
| Facet wipe | 2D triangles flip/pop in a sweep to reveal the next image. |
| Low-poly morph | One faceted form morphs into another. |
| Portrait build | 2D triangulated portrait assembles triangle by triangle. |
| Day cycle | Sun arcs; facet colours warm then cool. |

**Transitions:** shatter-to-next, facet wipe, fly through a low-poly tunnel, morph.

## 4. Build process

1. **Pick family (3D, 2D, PS1), palette and light direction.**
2. **Hero frames:** model/triangulate with consistent density; flat shade; light it; colour by height/face.
3. **Separate for animation:** objects/faces animatable (3D objects, or 2D triangles as individual shapes).
4. **Animate:** turntables, waves, shatters, reveals; loops for scenery.
5. **Check:** flat shading everywhere, consistent density, readable silhouettes, palette discipline.

## 5. Critique checklist

- Flat shading everywhere (no smoothed low geometry)?
- Consistent facet size?
- Strong, exaggerated silhouettes?
- Limited palette, saturation on the focal element only?
- Gradients across facets, not inside them?
- Does motion make facets catch light (slow turns, waves)?
- Shatter/assemble pieces consistent with the facet size?
