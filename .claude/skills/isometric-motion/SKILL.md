---
name: isometric-motion
description: Isometric design in motion - true isometric (30 degrees, 120-degree axes) vs 2:1 dimetric projection, isometric grids, three-tone face shading from one light, dioramas and floating islands, cut-away and exploded views, isometric infographics, cities and tech illustrations - with motion rules (movement only along the three axes, drop-in assembly, extrusion growth, exploded and re-assembled views, flow lines along paths, orthographic camera pans and zooms, 90-degree turntables, seamless loops). Includes After Effects (2D SSR method and 3D iso camera), Blender (orthographic 54.736/45 camera, auto three-tone shader), Illustrator, CSS/GSAP and Higgsfield recipes. Use when the user asks for isometric, isometric illustration or animation, iso city, diorama, 2.5D, axonometric, isometric infographic, exploded view, or isometric game-style scenes.
---

# Isometric motion

Isometric (axonometric) drawing shows three sides of an object with **no perspective**: parallel lines stay parallel, nothing shrinks with distance, every unit of the grid is equal. It reads as clear, "explainable" space, ideal for systems, products, cities, data and processes. Motion keeps that clarity: **everything moves along the three axes**.

Pick a projection and never mix:
- **True isometric:** axes 120° apart; ground lines at 30° to horizontal. Best for vector illustration and diagrams.
- **2:1 dimetric ("pixel isometric"):** ground lines rise 1 for every 2 across (≈26.565°); tiles twice as wide as tall. Best for pixel art and tile-based scenes (see `pixel-art-motion`).

Pair with: `flat-2d-motion` (shape and character style), `clay-3d-motion` (soft iso dioramas), `pixel-art-motion` (2:1 pixel iso), `design-principles`, `layout-composition`. Design hero frames as finished illustrations first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: 2D SSR transforms, iso grid expressions, 3D iso camera, drop-in, extrusion, exploded views, flow lines, loops.
- `references/blender-illustrator-code.md`: Blender ortho iso camera and auto three-tone shader, Illustrator iso workflow, CSS/GSAP, Higgsfield prompts.
- `references/history.md`: projection maths, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Projection | One projection for everything; no vanishing points; verticals stay vertical. |
| Grid | Everything sits on the iso grid: one base unit; heights in whole or half units. |
| Light | One light for the whole scene, usually from the top-left. |
| Three tones | Each material gets three values: top face lightest, left (light-facing) face mid, right face darkest (or swap left/right to match the light). Same value steps for every object. |
| Palette | 4–6 hues × 3 tones + a background; soft, friendly or brand colours. Accents for focal objects. |
| Forms | Simple blocks, cylinders, slabs; rounded corners optional but consistent; details small and few. |
| Scale cues | Tiny people, trees, cars and props set the scale. |
| Composition | Diorama/floating-island base slab, or a cut-away showing inside; clear focal object; generous negative space. |
| Shadows | Flat shadows cast along one iso axis (opposite the light), soft or hard but consistent; ambient occlusion in corners optional. |
| Lines | No outlines (pure tones) or one consistent thin outline. |
| Type | Flat in screen space for labels/titles (readable), or set on an iso plane for signage (sparingly; legibility first). |

## 2. Motion principles

1. **Axis-only movement.** Objects move along the three iso axes: vertical, and the two ground diagonals (screen angles 30°/150° for true iso, ≈26.6° for 2:1). Never arbitrary screen directions.
2. **Build the world.** Scenes assemble: base slab appears, blocks drop in from above (Z axis) with a small bounce, details pop on last. Order follows construction logic.
3. **Extrusion growth.** Buildings, bars and charts grow up from the ground (scale height from the base), staggered.
4. **Exploded views.** Parts separate along the axes to reveal insides, hold, then reassemble.
5. **Flow along paths.** Dashed lines, pipes and conveyors carry packets, cars, data along axis-aligned paths with 90° turns.
6. **Orthographic camera.** Pans along the axes and zooms by scaling (not dolly perspective). True-3D builds may rotate in 90° steps (turntable) to show another side.
7. **Friendly easing.** Ease-out drops with a 5–10% overshoot settle; mechanical linear for conveyors and loops.
8. **Seamless loops.** Iso cities and systems loop well: cars circulating, lights blinking, packets flowing.
9. **Light changes.** Day/night or highlight shifts recolour the three tones together; keep relationships intact.

## 3. Signature moves

| Move | How |
|---|---|
| Drop-in build | Blocks fall in on Z one by one and bounce-settle; props pop last. |
| Rise up | Buildings/bars extrude upward from the grid in a wave. |
| Tile cascade | Floor tiles pop in from one corner diagonally. |
| Explode / assemble | Product layers separate vertically, labels appear, then snap back. |
| Cut-away | A wall slides away along an axis to reveal the inside. |
| Flow network | Data packets or cars run along iso paths and pipes. |
| Iso camera glide | Orthographic pan along an axis from one diorama to the next. |
| 90° turntable | The whole diorama rotates a quarter turn (true 3D only). |
| Day to night | Tones shift, windows light up, lamp glows appear. |
| Iso chart | 3D bars/blocks grow to values with counters. |

**Transitions:** glide along an axis to the next island, tile wipe (floor tiles flip in the next scene), zoom out to reveal the island is part of a bigger map, explode-to-next.

## 4. Build process

1. **Choose projection, grid unit, light direction and three-tone palette.**
2. **Hero frames:** design 2–4 complete iso illustrations (Illustrator, Blender, or AE 3D).
3. **Separate parts** for animation (each block/prop its own layer or object, pivots at their base).
4. **Animate** construction, flows and camera along axes; add loops for life.
5. **Check:** any element moving off-axis? Any wrong face tone? Any perspective sneaking in?

## 5. Critique checklist

- One projection, no perspective, verticals vertical?
- Every object on the grid, consistent unit and scale?
- Three tones per material, consistent with one light?
- Shadows along one axis, consistent?
- All movement along the three axes?
- Clear focal object, readable labels?
- Loops seamless?
