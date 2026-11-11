---
name: risograph-motion
description: Risograph (riso) print style in motion - 2-3 translucent spot inks on paper, fluorescent pink and bright riso colours, subtractive overprint, misregistration, coarse grain and ink speckle, halftone tones, rough ink edges, matte paper texture, zine and indie-poster layouts - with motion rules (stepped on-2s/3s timing, per-step registration drift and grain boil, ink-plate layering, pass-by-pass print reveals, paper-feed and roller transitions). Includes After Effects, Photoshop/Illustrator separation, CSS/GSAP and Higgsfield recipes. Use when the user asks for risograph, riso, riso print, zine style, screen-print look, indie poster, grainy two-colour print, misregistered print, or tactile printed-paper motion.
---

# Risograph motion

Risograph is a stencil-duplicator printer that prints **one translucent soy-based spot ink per pass**. Each extra colour is another trip through the machine, so layers never line up perfectly. The look: **2–3 bright inks, overprinting into new colours, slightly misregistered, grainy, matte, on paper.** The imperfection is the point; it feels handmade although a machine made it.

Pair with: `typography`, `layout-composition` (poster and zine layouts), `pop-art-motion` (shares halftone and misregistration but with outlines and comic logic), `swiss-style-motion` (riso posters often use Swiss grids), `higgsfield-generate`. Design hero frames as posters first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: ink plates, overprint, grain and dropout, halftone, rough edges, registration drift, paper, transitions.
- `references/print-prep-css-ai.md`: Photoshop/Illustrator separations for stills, CSS/SVG/GSAP version, Higgsfield prompts.
- `references/history.md`: background, ink list with hex approximations, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Inks | 2–3 spot inks per piece (4 max). Every element is one ink or an overprint of inks. No full-colour images. |
| Overprint | Inks are translucent: where two overlap they multiply into a third colour (pink × blue = purple, yellow × blue = green). Design those overlaps on purpose. |
| Misregistration | Each ink layer offset 2–8 px (at 1080) from the others; colour fringes at edges. |
| Grain | Coarse, irregular grain in solid areas; small speckled dropouts where ink didn't take. |
| Halftone | Tones and photos as coarse halftone dots or stochastic grain per ink; no smooth gradients (use grainy gradients instead). |
| Edges | Slightly rough, soft ink edges. Not vector-crisp. |
| Paper | Off-white, cream, or coloured stock texture under everything. White = the paper (riso has no white ink). |
| Solids | Large solids look better broken up (texture, grain, 85–90% density) like real riso. |
| Type | Bold grotesks, condensed display faces, typewriter monos, hand lettering. Big and graphic; set type in one ink, often with an offset copy in a second ink. |
| Layout | Indie poster and zine: bold crops, cut-and-paste collage, big type, playful grids, stickers and stamps. |

**Ink palette (screen approximations; fluorescent inks are brighter in print)**
Fluorescent Pink `#FF48B0`, Bright Red `#F15060`, Flo-Orange `#FF7477`, Sunflower `#FFB511`, Yellow `#FFE800`, Lime `#D4E356`, Green `#00A75C`, Mint `#82D8D5`, Light Teal `#009DA5`, Cornflower `#62A8E5`, Blue `#0075BF`, Federal Blue `#3D5588`*, Purple `#5D5580`, Burgundy `#914E72`, Metallic Gold `#AC936E`, Black `#000000`.
Paper: natural `#F3EEE3`, cream `#F6EBD3`, kraft `#C9A57A`.
*Federal Blue value is the commonly used community approximation; not confirmed by a print shop source.

Classic pairs: Fluorescent Pink + Blue; Fluorescent Pink + Federal Blue; Yellow + Teal; Red + Blue; Orange + Purple; any + Black.

## 2. Motion principles

1. **Stepped timing.** Animate on twos or threes (8–12 fps feel). The piece looks like a sequence of printed sheets.
2. **Registration drift.** Each ink plate jitters a few pixels independently on every step, so fringes shimmer. Bigger offsets on accents and transitions.
3. **Grain boil.** The grain and speckle pattern changes every step (a new "print"), but the image itself holds.
4. **Plates move separately.** Animate inks as separate layers: a pink plate slides in, a blue plate lands on top; overprint colours appear where they cross.
5. **Print-pass reveals.** Build a frame ink by ink: first colour prints, then the second lands slightly off, like the sheet going through again.
6. **Paper physicality.** Paper slides through (feed), sheets stack, pages flip, a roller sweeps across. Camera like a flatbed or desk-top view.
7. **Graphic, not smooth.** Moves are simple (slides, scales, pops) with snappy eases, chunky on the stepped timing. No smooth gradients or soft blurs; no motion blur.
8. **Restraint in drift.** Holds must stay readable: keep drift small (1–3 px) on text plates; save big offsets for hits.

## 3. Signature moves

| Move | How |
|---|---|
| Ink-pass build | Plate 1 appears with a quick grain flicker, plate 2 lands offset, then both settle into slight drift. |
| Overprint collide | Two shapes in different inks slide over each other; the overlap shows the multiplied third colour. |
| Registration snap | Plates start far apart and snap almost into register on the beat. |
| Halftone bloom | A tone grows from coarse dots to solid (or the reverse for fades). |
| Paper feed | The whole sheet slides through the frame (like a printer feed) into the next layout. |
| Roller wipe | An ink roller or band sweeps across, laying the next colour. |
| Stamp | Type or shapes thump down like a rubber stamp: scale 110 → 100 with a dense-ink flash. |
| Zine flip | Page turn or fold into the next spread. |
| Cut-paper collage | Cut-out photo halftones and shapes pop on in steps. |

**Transitions:** paper feed, roller wipe, ink flood (one ink floods the frame then drains), hard step cut.

## 4. Build process

1. **Pick 2–3 inks and the paper** (check overprint colours look good together).
2. **Design separations:** each element assigned to one ink; plan which overlaps create the third colour.
3. **Hero frames:** design 2–4 posters/spreads in flat inks first, then add the riso treatment.
4. **Animate clean,** with each ink as its own layer/precomp.
5. **Apply the riso stack** per ink: halftone/grain, dropout, rough edges, registration drift, multiply over paper; set stepped timing.
6. **Check:** pause on a frame: does it look like a real riso print? Is the text readable?

## 5. Critique checklist

- Only 2–3 inks (+ their overprints)? No stray full-colour elements?
- Do overlaps multiply into believable third colours?
- Is there visible but tasteful misregistration?
- Is there grain and speckle in solids, rough edges, and a paper texture?
- Are gradients and photos done with halftone or grain, not smooth tones?
- Is the timing stepped, with grain and drift changing per step?
- Is the text readable during holds?
