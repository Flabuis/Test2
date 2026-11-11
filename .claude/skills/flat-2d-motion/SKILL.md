---
name: flat-2d-motion
description: Flat 2D illustration and animation - geometric construction, solid fills, limited 60-30-10 palettes, flat cel shading, silhouettes, rounded consistent forms, and the motion rules that bring them alive (eased transforms, overlap and follow-through, shape morphs, stroke draw-ons, trim-path bursts, idle loops, parallax and infinite zooms, Duik character rigs). Covers strict flat, flat 2.0 / Kurzgesagt-style semi-flat, corporate explainer and mid-century variants, with After Effects and HyperFrames/GSAP recipes. Use when the user asks for flat design, flat 2D, vector animation, explainer animation, Kurzgesagt style, corporate explainer, character animation with shape layers, icon animation, or clean illustrated motion graphics.
---

# Flat 2D motion

Flat 2D builds everything from simple geometric shapes and solid colour, with little or no depth. It reads fast, scales to any size, and animates cleanly, which is why it rules explainers, UI and brand motion. Its quality comes from **construction** (clean shapes, a consistent system) and **animation craft** (easing, overlap, appeal), not effects.

Pair with: `design-principles` (colour, hierarchy), `layout-composition` (staging), `typography`, `explainer-documentary` (script and scene plan), `higgsfield-generate` (style frames). Design each hold frame as a finished illustration first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: shape-layer builds, easing, overlap expressions, morphs, bursts, idle loops, parallax, Duik rigging.
- `references/hyperframes-gsap.md`: the same in SVG/GSAP.
- `references/history.md`: sources, studios and variants.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Construction | Build every object from circles, rectangles, triangles and rounded rects. A tree = circle + rectangle. |
| Fills | Solid, opaque fills. No transparency, multiply or overlapping semi-transparent shapes (strict flat). |
| Palette | 3–5 colours plus neutrals, split 60 / 30 / 10 (base / secondary / accent). Test contrast. |
| Shading | Optional flat cel shadow: one darker tone shape clipped to the object, from one light direction for the whole scene. |
| Depth | Through colour value and scale, not rendering. Background lighter and less saturated; foreground stronger. |
| Outlines | None, or one consistent stroke weight for everything (icon style). Never mixed. |
| Corners | One corner radius system (e.g. 0, 8, 24 px). Same rounding everywhere. |
| Detail | Minimal. Shapes ≥ 8 px; anything thinner reads as a line. Remove detail that doesn't help the read. |
| Silhouette | Every object and character pose must read as a solid black silhouette. |
| Characters | Simple proportions (big head or bean body), dot or simple eyes, limbs as tapered rects or strokes. One style for every character. |
| Type | A clean geometric or humanist sans (Poppins, Manrope, Inter, Gilroy, Circular, Montserrat). Flat colour, no effects. |
| Long shadow (optional) | 45° flat shadow, one darker tone of the background, clipped to the background shape. Use sparingly; it dates fast. |

**Starter palettes**
- Friendly explainer: `#1E2A4A` ink, `#F5F1E8` base, `#3D7BF7` blue, `#FFB547` amber, `#FF6B6B` coral, `#3DD6A3` mint.
- Dark science (semi-flat): `#0E1530` night, `#1D2B5C` deep, `#4AC6FF` cyan, `#FFD447` yellow, `#FF4F7A` pink, `#9B6BFF` violet.

## 2. Motion principles

1. **Ease everything.** Moves start and stop softly (ease in-out, 60–80% influence). Linear only for constant mechanical motion (wheels, conveyor belts, orbits).
2. **Overlap and follow-through.** Parts lag the main body by 2–4 frames (hair, ears, tails, antennas, ribbons, label tags). Nothing in a group stops at the same frame.
3. **Anticipation.** A small move opposite to the action before big actions (a crouch before a jump, a pull back before a throw).
4. **Moderate overshoot.** Pops overshoot about 5–10% and settle. Keep it softer than pop art. Strict corporate flat: little or no bounce.
5. **Squash and stretch** on soft or organic things (blobs, characters, drops), preserving volume. Never on type or rigid objects.
6. **Arcs.** Limbs and thrown objects move on arcs, not straight lines.
7. **Transform first.** Prefer position, rotation and scale. Use path morphs where the story needs one shape to become another, and keep the shape language intact through the morph.
8. **Staging.** Animate one focal group at a time. Big camera moves over the whole canvas distract; keep them motivated.
9. **Life in holds.** Idle loops keep held frames alive: breathing (1–3% scale), blinks every 3–5 s, floating (±6 px sine), subtle background motion.
10. **Smooth playback.** 24/25/30 fps, motion blur on for fast moves, no posterize. Overlap moves so there are no dead frames ([[overlapping-motion]]).

## 3. Signature moves

| Move | How |
|---|---|
| Pop-on | Scale 0 → 108 → 100 with ease; groups stagger 2–3 f. |
| Shape morph | Circle → icon → object via path keyframes, matching vertex count and first vertex. |
| Stroke draw-on | Trim Paths reveals lines, then the fill appears. |
| Burst | Trim-path rays and circles explode out on an accent. |
| Grow / build | Objects assemble from parts in reading order (base first, details last). |
| Circle wipe | A flat circle grows from the focal point to fill the frame in the next scene's base colour. |
| Infinite zoom | Push into a small detail that becomes the next scene (vector stays sharp). |
| Parallax pan | Layers move at different speeds (fg 100%, mid 60%, bg 30%). |
| Match cut | A shape in one scene becomes a similar shape in the next (a sun becomes a coin). |
| Character act | Rigged pose-to-pose acting with anticipation, overlap and a settle. |
| Icon loop | Small looping UI or icon animations (2–4 s, seamless). |

**Transitions:** circle or shape wipe, match cut, infinite zoom, push and parallax, morph. Avoid long cross-dissolves (they create messy overlaps of flat shapes).

## 4. Variants

- **Strict flat (default for UI and corporate):** solid opaque colour, no gradients or shadows, very simple shapes (IBM, Google, Material-style illustration).
- **Flat 2.0 / semi-flat (Kurzgesagt-like science style):** flat forms on dark backgrounds, with subtle radial gradients, soft glows, rim highlights and atmospheric depth. Rich, saturated, luminous.
- **Corporate explainer:** friendly people (stylised proportions, often with skin tones in a muted range), offices and devices, isometric-ish props, a soft palette.
- **Mid-century flat:** 1950s–60s flat, a limited retro palette, grain or stipple texture, offset colour shapes, angular characters (UPA style).
- **Geometric minimal:** pure shapes and colour fields with no characters; abstract explainers and logos.

## 5. Build process

1. **Script and boards:** a beat per scene (pair with `explainer-documentary` for longer pieces).
2. **Style frame:** design 1–3 hero frames that define the palette, shape language, character style and corner radius. Get them approved first.
3. **Illustrate in layers:** in Illustrator, one layer per moving part, named. Characters split at joints with overlapping round ends. Save to `Illustrator Projects\`.
4. **Import:** into AE, then Create Shapes from Vector Layer for editable paths; rig characters with Duik.
5. **Animate:** blocking (key poses on beats) → in-betweens and easing → overlap and secondary motion → idle loops.
6. **Check:** pause on any frame; it should be a clean illustration with a clear focal point. Watch silhouettes and tangents.

## 6. Critique checklist

- Is every object built from clean, simple shapes with consistent corner radii?
- Is the palette within 3–5 colours, with a clear accent used sparingly?
- Does shading come from one light direction across the scene?
- Do the silhouettes read?
- Is anything moving linearly that should ease?
- Do parts overlap, or does everything stop on the same frame?
- Are there idle loops in long holds?
- Are there stray transparencies, mismatched stroke weights or tangent edges?
