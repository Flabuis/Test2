---
name: bauhaus-motion
description: Bauhaus style in motion - primary colours and black on off-white, circle/square/triangle geometry (Kandinsky's yellow triangle, red square, blue circle), asymmetric diagonal compositions, bars and rules, lowercase geometric sans (Bayer's Universal, Futura), red-and-black typography, photomontage, Albers colour squares, Schlemmer's geometric figures and modern Bauhaus tile patterns - with motion rules (shapes as actors, compass-and-ruler construction, 90-degree rotations, tile cascades, mechanical rhythm, colour interaction shifts, visual music). Includes After Effects, CSS/GSAP and Higgsfield recipes. Use when the user asks for Bauhaus, Bauhaus style, geometric primary-colour design, Kandinsky shapes, Triadic Ballet, Bayer/Universal type, modernist geometric animation, or Bauhaus tile patterns.
---

# Bauhaus motion

The Bauhaus (Weimar 1919, Dessau 1925–32, Berlin 1932–33, founded by Walter Gropius) taught that art, craft and industry unite through **function, geometry and reduction**. Its graphic language: basic shapes, primary colours plus black, asymmetric dynamic layouts, bars and rules, and lowercase geometric sans type. It's the parent of Swiss style but **more playful, more diagonal, more about shape and colour as actors**.

Pair with: `swiss-style-motion` (stricter grid descendant), `typography`, `layout-composition` (asymmetry, diagonals), `design-principles` (colour), `flat-2d-motion` (shape-layer craft). Design every key frame as a poster ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: tile pattern cascades, compass construction, Albers squares, Schlemmer figures, geometric type, finishing.
- `references/css-gsap-ai.md`: CSS shapes and tile grids, GSAP moves, Higgsfield prompts.
- `references/history.md`: teachers and what to borrow, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Shapes | Circle, square, triangle, semicircle, quarter circle, bars. Pure geometry, drawn as if by compass and ruler. |
| Colour | Primary red, yellow, blue + black on off-white. Flat. Kandinsky pairing as a motif: yellow triangle, red square, blue circle. |
| Composition | Asymmetric and dynamic: diagonals (often 15–45°), off-centre weight, overlapping shapes, strong tension; balanced, never static symmetric. |
| Bars and rules | Heavy black bars and thin rules divide, frame and point; type often sits on or along them. |
| Type | Geometric sans, often all lowercase (Bayer's Universal ideal): Futura, Jost, Architype Bayer, ITC Avant Garde, Josefin Sans; heavy grotesk for contrast. Red and black. Type set vertically or on diagonals. Avoid the "Bauhaus 93" font (a later pastiche that reads cheap). |
| Image | Photomontage / "typophoto" (Moholy-Nagy): high-contrast B&W photos combined with type and shapes. |
| Texture | Optional: faint paper grain, slight print imperfection. Mostly flat. |
| Function | Every element has a role; no ornament for its own sake. |

**Palette:** off-white `#F2EBDD`, red `#D62828`, yellow `#F7C600`, blue `#1D4E89`, black `#111111` (optional pink `#E8A0BF` from the Triadic Ballet, grey `#8C8C8C`).

## 2. Motion principles

1. **Shapes are actors.** Like Schlemmer's Triadic Ballet, geometric forms perform: enter, meet, balance, exit. Give each shape a role.
2. **Construction.** Things are built in front of the viewer: lines extend like a ruler, circles draw like a compass sweep, shapes assemble into figures and letters.
3. **Geometric moves.** Rotations in 90° steps (or full turns), slides along diagonals and bars, scale from edges and centres, shapes rolling along lines.
4. **Mechanical rhythm.** The machine age: regular, metronomic timing, eased in-out like gears and pistons. Moderate overshoot is fine for playfulness; nothing floaty.
5. **Tile cascades.** Modern Bauhaus patterns: a grid of shape tiles that rotate/flip/swap colour in waves (from a corner, centre or diagonal).
6. **Colour interaction.** Albers: colours change meaning beside each other; nested squares and fields shift colours in sequence, revealing new relationships.
7. **Visual music.** Kandinsky linked colour to sound; sync shape hits to beats and instruments (circle on kick, triangle on hi-hat, square on snare).
8. **Diagonal energy.** Movement along diagonals reads as dynamic; horizontals and verticals as rest. Resolve scenes into balanced asymmetric posters.
9. **Clean finish.** Flat, crisp, light or no motion blur. Optional stop-motion (12 fps) for a paper cut-out feel.

## 3. Signature moves

| Move | How |
|---|---|
| Compass draw | A circle draws on with a rotating radius line, then fills. |
| Ruler extend | Black bars and rules shoot out from a point, type slides along them. |
| Shape assembly | Circle, triangle and square fly in and lock into a figure, logo or letter. |
| Universal type | Letters built from circles and bars, assembling stroke by stroke. |
| Tile cascade | Grid of quarter-circle/semicircle tiles rotates 90° in a wave; colours swap. |
| Kandinsky trio | Yellow triangle, red square, blue circle pop on beats and rearrange. |
| Albers squares | Nested squares change colours one by one. |
| Schlemmer figure | A geometric puppet (circle head, cone body, disc arms) dances on beats. |
| Typophoto | B&W photo cut-outs slide in with bars and red type. |
| Diagonal sweep | The whole layout rotates/slides along a diagonal into the next poster. |

**Transitions:** colour-field wipe by a shape (a giant circle or bar sweeps across), tile cascade flip, shape zoom-through (into a circle), hard cut on the beat.

## 4. Build process

1. **Palette and shape vocabulary:** primaries + black on off-white; pick 3–5 shapes and one typeface.
2. **Hero posters:** 3–6 asymmetric key frames with a clear diagonal and one dominant shape each.
3. **Plan the performance:** how shapes travel between posters (construction, rotation, assembly, cascade).
4. **Animate to rhythm:** beat-locked mechanical timing; tile cascades and colour shifts on bars.
5. **Check:** every paused frame is a balanced Bauhaus poster.

## 5. Critique checklist

- Only primaries + black on off-white (plus a deliberate accent)?
- Pure geometric shapes, cleanly constructed?
- Asymmetric, dynamic composition with a clear diagonal or tension, but balanced?
- Geometric sans (lowercase where fitting); no Bauhaus 93 cliché?
- Do shapes have roles, and does motion feel mechanical and rhythmic, not floaty?
- Any decoration without function? Remove it.
