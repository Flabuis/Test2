---
name: swiss-style-motion
description: Swiss Style (International Typographic Style) in motion - grid systems, asymmetric layout, grotesque type, flat limited colour, objective hierarchy, and how each becomes motion rules (grid-locked movement, beat-locked timing, snap easing, cell and column wipes, type-as-image). Includes After Effects and HyperFrames/GSAP recipes. Use when the user asks for Swiss style, International Typographic Style, Müller-Brockmann, grid-based, modernist, Helvetica-style, minimal kinetic typography, or clean editorial motion design.
---

# Swiss style motion

Swiss style was never designed to move. It works in motion because its rules are *systems*: a grid, a type scale, a colour limit. Turn each system into a motion rule and the animation designs itself.

Core belief: **the grid governs space and time.** Every position, distance, size and duration is a multiple of a module.

Pair with: `typography` (type details), `layout-composition` (grids, eye flow), `design-principles` (critique). Design key frames as posters first, then animate between them ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: grid setup, snap expressions, reveals, wipes, counters, via the `after-effects` MCP.
- `references/hyperframes-gsap.md`: the same moves as GSAP for HyperFrames/HTML.
- `references/history.md`: the movement, its designers, and their variants to borrow from.

## 1. Static principles (every key frame must pass)

| Principle | Rule |
|---|---|
| Grid | Modular grid with fixed margins and gutters. Everything aligns to it, including image edges and baselines. |
| Asymmetry | Anchor content to one side (usually the left column). The empty side is active space, not leftover. Centre only on purpose. |
| Type | One grotesque family, at most 2–3 weights. Flush left, ragged right. No justified text, no centred paragraphs. |
| Hierarchy | Made by size, weight and position only. No boxes, shadows, icons or decoration doing hierarchy work. |
| Scale contrast | Pair one huge element (headline, numeral, shape) with small, precise text. Ratio ≥ 1:6. |
| Colour | Black, white, plus one accent. Flat fills only. No gradients, glows, bevels or textures. |
| Imagery | Objective: B&W or duotone photography, geometric shapes, diagrams. Cropped to grid cells. |
| White space | Generous. At least 30–40% of the frame is empty. |
| Objectivity | Content first. The design explains; it does not decorate. |

**Type picks:** Neue Haas Grotesk / Helvetica Now, Akzidenz-Grotesk, Univers, Suisse Int'l, Aktiv Grotesk. Free: Inter / Inter Display, Archivo, Geist.
**Display setting:** leading 0.9–1.0, tracking −2% to −4%, sentence case or all-lowercase. Small text: tracking 0 to +2%, leading 1.3.
**Size steps:** modular scale (×1.5 or ×2, or Fibonacci 8/13/21/34/55/89/144). Align baselines to a baseline grid. Mixed sizes in one line share a baseline (Ruder).
**Accent colours:** Swiss red `#E30613` or `#FF2D1A`, signal yellow `#FFD400`, blue `#0047FF`. Paper white `#F2F0EB`, ink `#111111`.

## 2. Motion principles (Swiss rules translated)

1. **Grid-locked movement.** Elements move on x or y only, along grid lines. Travel distance = whole modules (1 column, 2 rows). Start and end positions are grid positions.
2. **Beat-locked time.** Pick a time module (one beat; 120 BPM = 0.5 s = 15 f @ 30 fps). Durations are ½, 1 or 2 modules. Keyframes land on beat markers.
3. **Snap easing.** Fast start, long precise settle (expo/quart out). Or a sharp in-out for moves between two layouts. Never bounce, elastic, overshoot or wobble. Pure linear only for continuous scrolls and tickers.
4. **Reading order stagger.** Stagger left→right, top→bottom, by 2–4 frames per item. The motion teaches the hierarchy: biggest thing first.
5. **Reveal, don't fly.** Type appears through masks: lines rise out of their own baseline box, columns wipe open, cells fill. Things don't fly in from off-screen.
6. **Geometry only.** Rotation only in 90° steps. Scale on one axis from an edge (a bar growing from its left edge), not from the centre.
7. **Readable holds.** Every layout rests long enough to read: about 0.3 s per word, at least 0.75 s for a headline. Readable before anything overlaps it.
8. **Type stays type.** No letter distortion, melting, warp or wiggle. Kerning stays optically even in every frame.
9. **Clean finish.** Motion blur on (180° shutter) for fast moves. No grain, glow, chromatic aberration, camera shake or 3D fly-throughs. This is the opposite of the Vox/collage finish.
10. **Overlap within the system.** Each move starts before the last ends ([[overlapping-motion]]), but all overlaps stay on the time grid.

## 3. Signature moves

| Move | How |
|---|---|
| Line rise | Each text line slides up 100% of its height inside its own matte. Stagger 3 f. |
| Column wipe | A flat colour field grows across 1–N columns from an edge, revealing or hiding content. |
| Cell fill | Grid cells fill with colour or image in reading order or a pattern (checker, diagonal). |
| Rule draw | Hairline rules (2–4 px) draw on with Trim Paths, then type sits on them. |
| Scale jump | A word cuts between 2–3 type-scale sizes on the beat (hard cut, no tween). |
| Counter | Large numeral counts up with an ease-out, tabular figures, then locks. |
| Layout morph | Shared elements move to their grid slots in the next layout; the rest masks out. |
| Grid push | The whole layout slides one full column/frame, the next layout follows flush behind. |
| Shape system | Circles, bars and squares sized to modules (Müller-Brockmann posters) scale and slide in sync. |

**Transitions:** cut on the beat, column wipe, grid push, layout morph, colour-field flood from one cell. No dissolves, no whip pans.

## 4. Variants

- **Classic (Müller-Brockmann):** strict grid, red/black/white, geometric shapes, very calm. Default.
- **Hofmann:** point/line/plane, high B&W contrast, bolder play with the grid.
- **Swiss New Wave (Weingart):** layered, broken grid, bigger mixed type, more energy. Still grid-aware.
- **Contemporary kinetic (Experimental Jetset, Mat Voyce, brand systems):** a moving grid, heavy type, beat-locked snaps. Best for reels.

## 5. Build process

1. **Content and hierarchy:** list the message as levels (H1, H2, data, caption).
2. **Grid:** choose the frame grid (see AE reference for 9:16, 16:9, 1:1) and the time module from the music BPM.
3. **Key frames:** design 3–6 still layouts as posters. Each must pass section 1 on its own.
4. **Paths:** decide how each element gets from layout N to N+1 (morph, wipe, cut). Write it as a beat sheet.
5. **Animate:** snap easing, stagger in reading order, holds long enough to read.
6. **Check:** scrub frame by frame. Every paused frame should still look like a designed poster.

## 6. Critique checklist

- Is every edge on the grid? (Turn the guides on and check.)
- Is there one clear largest element per frame?
- Is the colour limited to black/white + 1 accent?
- Does any move bounce, overshoot, rotate oddly or distort type? Remove it.
- Does every keyframe land on the time grid?
- Is every layout readable before the next move starts?
- Is the composition asymmetric with active white space?
- Does any decoration (shadow, gradient, texture, icon) remain? Remove it.
