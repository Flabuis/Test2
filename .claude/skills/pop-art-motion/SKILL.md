---
name: pop-art-motion
description: Pop Art in motion - Lichtenstein comic panels, Ben-Day dots and halftone, thick black outlines, flat primary and fluorescent colour, Warhol silkscreen repetition grids, misregistration, starbursts, speech balloons, onomatopoeia, speed lines - translated into motion rules (pose-to-pose pops with overshoot, stepped timing, impact frames, beat colour swaps, dot wipes, panel-to-panel camera). Includes After Effects and HyperFrames/GSAP recipes. Use when the user asks for pop art, comic book, Lichtenstein, Warhol, halftone, Ben-Day dots, retro comic, POW/BAM, or bold playful 60s ad-style motion.
---

# Pop art motion

Pop art took mass-produced images (comics, ads, packaging, celebrities) and blew them up with the *look of cheap printing*: dots, outlines, flat ink, repetition. In motion, think **printed comic come alive**: hard poses, punchy pops, impact frames and colour that flips on the beat.

Pop is the energetic opposite of `swiss-style-motion`: overshoot, tilt and shake are allowed. The design discipline is not optional, though. Every hold frame is a designed panel or poster ([[motion-is-graphic-design]]).

Pair with: `typography` (lettering quality), `layout-composition` (panel grids, focal points), `design-principles` (critique), `higgsfield-generate` (comic-style source art).

References:
- `references/after-effects.md`: dots, halftone, outlines, Warhol plates, overshoot, shake, bursts, speed lines, via the `after-effects` MCP.
- `references/hyperframes-gsap.md`: the same in GSAP/CSS.
- `references/history.md`: artists and what to borrow from each.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Outline | Thick black keylines (8–14 px at 1080 wide) on every figure and object. Uniform weight, round joins. |
| Flat ink | Flat colour fills. Shading only via dots, hatching or a second flat tone, never soft gradients or airbrush. |
| Ben-Day dots | Regular dot grid in one size per area (Lichtenstein), usually on a 45° staggered grid. Used for skin, sky and backgrounds. |
| Halftone | Variable-size dots for shading and fades (print look). |
| Palette | 3–5 inks per scene. Comic: red, yellow, blue, black, white. Warhol: fluorescent pink, orange, lime, turquoise, violet. |
| Crop | Dramatic close-ups: a face filling the frame, a hand, a product. Cut off at the edges. |
| Repetition | Same image repeated in a grid with different colour plates (Warhol). |
| Misregistration | Colour plate offset a few px from the black plate, like a cheap print. |
| Comic devices | Speech/thought balloons, yellow caption boxes, starbursts, onomatopoeia (POW, WHAAM), speed lines, panel borders. |
| Shadows | Hard offset shadows only (solid black, 0 blur). |
| Texture | Optional newsprint: warm off-white paper `#F4EBD9`, faint ink grain. Never grunge. |

**Type:** comic lettering (Bangers, Komika Axis, Badaboom, Luckiest Guy) for SFX and balloons. Uppercase comic hand-lettering (Comic Neue Bold, CC Wild Words) for dialogue. 60s ad faces (Futura Extra Bold, Cooper Black, Franklin Gothic Heavy) for headlines. SFX words: heavy, outlined, extruded or hard-shadowed, tilted, inside or bursting from a starburst.

**Core palette:** red `#E4002B`, yellow `#FFE600`, blue `#0077C8`, cyan `#00AEEF`, magenta `#EC008C`, black `#111111`, paper `#F4EBD9`. Warhol fluoro: `#FF3FA4` `#FF7A00` `#B6FF00` `#00D1C1` `#8A3FFC`.

## 2. Motion principles

1. **Pose to pose.** Motion jumps between strong held poses (like comic panels). Holds read; the move between is fast.
2. **Stepped timing.** Animate on 2s (12 fps feel) with a Posterize Time layer for print and comic texture. Keep impacts on the beat.
3. **Overshoot is the voice.** Pops scale 0 → 115% → 95% → 100% in about 8–10 frames. Use squash and stretch on landings. Tilt ±5–12° on entry.
4. **Impact frames.** Big hits get 1–2 frames of an inverted or flat-colour frame, a starburst flash and 3–6 frames of screen shake.
5. **Colour flips on the beat.** Backgrounds, Warhol plates and dots swap colours on beats (hold keyframes, hard cuts, no fades).
6. **Dots move.** Ben-Day backgrounds scroll slowly diagonally. Halftone dots grow and shrink for wipes, fades and shading.
7. **Speed and emphasis lines.** Radial lines for zoom and shock; parallel speed lines behind moving objects. They flicker per step.
8. **Panel logic.** Sequences read as a comic page: panels slam in, the camera travels panel to panel, borders draw on, objects break the panel border for emphasis.
9. **Type punches.** SFX words slam in with overshoot and a rotation snap, letters staggered 1–2 frames, sometimes shaking. Balloons pop from their tail.
10. **Overlap.** The next pop starts before the last settles ([[overlapping-motion]]), but each hit still gets its own beat.

## 3. Signature moves

| Move | How |
|---|---|
| Pop-in | Scale with overshoot + small rotation snap, hard shadow following. |
| SFX slam | Starburst scales in, word slams in on top, 2-frame impact flash, shake. |
| Dot wipe | Halftone dots grow from one corner until they fill the frame, revealing the next scene. |
| Warhol grid | Subject splits into a 2×2 / 3×3 grid; each cell's colour plates cycle on the beat. |
| Plate shift | Colour plate slides out of register then snaps back on a hit. |
| Panel slam | A comic panel drops into the page grid with overshoot; the camera pushes into it. |
| Balloon pop | The balloon scales from the tail point; text types on or pops in by word. |
| Zoom lines | Radial speed lines burst on a reveal; the subject scale-punches. |
| Close-up crash | Hard cut to an extreme crop (eye, lips, hand) on the beat. |
| Ben-Day fill | Shape fills with dots that ripple in from one side. |

**Transitions:** dot wipe, starburst wipe, panel slam, colour-flash cut, page turn (sparingly), push through a speech balloon.

## 4. Variants

- **Lichtenstein comic (default):** primaries, Ben-Day dots, outlines, balloons, melodrama or action.
- **Warhol silkscreen:** photo → 2–3 flat plates, fluoro colours, repetition grids, misregistration. Best for people and products.
- **British collage (Hamilton, Blake):** cut-out ads and photos collaged with flat colour. Pair with `vox-collage-design` cutout techniques, but use pop colour.
- **Billboard (Rosenquist):** giant fragments of ads at huge scale, cropped and overlapping.
- **Neo-pop / sticker:** clean vector, thick outlines, glossy flat colour, Y2K brand energy. Best for social reels.

## 5. Build process

1. **Story beats as panels:** list each beat as a comic panel (shot, crop, caption, SFX).
2. **Palette and inks:** choose a variant and 3–5 inks. Fix the outline weight and dot size for the whole piece.
3. **Key frames:** design every hold frame as a panel/poster. One focal point, a dramatic crop, clear lettering.
4. **Assets:** cut out subjects, add outlines, convert photos to plates (see AE reference). Generate comic art with Higgsfield if needed ("1960s comic book panel, Ben-Day dots, thick black ink outlines, flat primary colours, Lichtenstein style").
5. **Animate:** pose to pose on the beat, overshoot pops, impacts, colour flips. Posterize Time at 12 fps last.
6. **Check:** pause on random frames. Each should look like a printed comic panel or poster.

## 6. Critique checklist

- Are outlines a consistent weight everywhere?
- Are there any soft gradients, blurs or soft shadows? Replace with dots, flat tones or hard shadows.
- Is the palette within 3–5 inks per scene?
- Is there one clear focal point and a dramatic crop per panel?
- Are the dots a consistent size and grid (or deliberately graded)?
- Does every pop have overshoot, and does every big hit have an impact?
- Is the comic lettering readable at phone size (min ~48 px for SFX, ~36 px for balloons at 1080 wide)?
- Do the colour flips and hits land on beats?
