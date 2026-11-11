---
name: vox-collage-design
description: Design system for Vox-style editorial collage graphics and Aevy TV-style documentary inserts - paper textures, B&W photo cutouts, accent colours, typography, hand-drawn ink marks, maps, charts, newspaper pages, archival prints and per-topic palettes, plus Higgsfield image prompts and Photoshop/Illustrator builds. Use when designing frames, stills, thumbnails or graphic inserts in a Vox, Aevy TV, paper collage, editorial, archival or documentary-explainer look.
---

# Vox collage design system

Distilled from 13 createdaley / Mapal After Effects tutorials, a Claude + Higgsfield Vox tutorial and
4 Aevy TV documentaries. For motion see vox-after-effects-recipes; for story see explainer-documentary.

## Canvas and texture
- Paper is the base: warm cream/off-white (#F2EBDD-#EFE6D2), light grey linen, newsprint, aged tan,
  dark brown paper, white cracked plaster, dark concrete or black marble for dramatic scenes.
- Always real scanned textures (4K paper, wall, concrete), not generated noise; generated noise reads
  as sand. Blend the texture with Overlay/Multiply, Levels for contrast, Invert/Black & White to tune.
- Faint dot grid, halftone dots or graph-paper grid behind charts; thin dotted page border; registration
  crosshairs when cards sit on a table.
- Photos blend into paper with Multiply so the texture shows through.

## Colour
- Small palette: paper + black ink + ONE accent per video (teal #2E7D6E, Vox yellow, gold, lime) +
  red ink (#C8382E) only for circles, arrows, underlines and emphasis.
- Use very dark grey (#1E1E1E), not pure black, for type and bars.
- Aevy TV gives every episode its own palette that fits the topic (see below) inside one shell.

## Cutouts and photos
- Black-and-white or sepia photo cutouts with a white paper border, rough/torn edge (Roughen Edges)
  and a soft drop shadow, as if cut with scissors.
- Prints: white-bordered photos, slightly rotated and overlapping, laid along a timeline or on a table.
- Cutouts stand on flat shapes (a teal circle behind a person, a black half-circle "sunrise").
- Rotoscope people out of archival photos so they can pop forward; add a blurred reflection under feet.
- Scraps: torn newspaper, stamps, tape, letters, handwriting, engravings, paper clouds, crumpled paper.
- Censor bar (yellow or black) over eyes for a "who is it?" reveal.

## Typography
- Condensed bold sans caps for labels and names (Bebas Neue, Oswald, Bahnschrift Condensed,
  Adobe condensed families); second colour on one word.
- Serif for titles, headlines and quotes (Caslon Pro Bold, Times-like, spaced serif caps like "SOLDIER");
  key word in italic with a marker highlight.
- Typewriter/mono for small captions, axes and data labels.
- Year/number cards: big bold numerals in a rough ink box with a tiny "YEAR" label.
- Signatures and handwriting traced as strokes so they can write on.
- Lots of negative space; text never fills the frame. Sans + italic contrast pairs
  ("SMART PHONE  dumb user").
- After Effects gotcha (some locales): set the text layer's digit set to default (DigitSet.DEFAULT_DIGITS)
  or numbers render as Arabic-Indic digits.

## Hand-drawn layer
- Red marker circles, arrows, question marks, underlines and brush strokes over the design.
- Ink-on-paper charts: thick rough line, dot markers, dashed vertical guide at the key year.
- Dashed connector/leader lines; dashed routes linking photos like a timeline.
- Gold or red paint-brush strokes as accents (King/royalty themes).

## Scene types (layouts)
- **Map:** antique map scan, focus region cut out and lifted, glowing outline, red callout dot + ring,
  city -> world zoom. Aevy variant: dark top-down city map, grey footprints, glowing icon pins,
  yellow travel-time routes ("10 MIN"), radius circles.
- **Bar chart:** off-white paper, serif title with blinking cursor, solid dark bars, dashed paper-coloured
  gridlines cutting across bars, rounded black year pill along the bottom, red circle + value callout.
- **Pie chart:** thick-stroke circle, one slice breaking away, photo seen through the slice, small serif
  caps label ("25 PERCENT").
- **Line chart:** ink line with dots, the cliff at the turning-point year circled, zoom-in "micro shot".
- **Newspaper front page:** masthead, huge year, serif headline, body columns, byline, rules, keyed
  archival group photo, signature writing on.
- **Archival collage:** sepia print on marble or paper, rotoscoped people, condensed white name labels,
  big title word.
- **Timeline:** white-bordered prints in a row, dashed yellow paths, labels in yellow serif caps.
- **Process flow:** row of cutout objects joined by hand-drawn arrows, colour-coded stage bars above.
- **Isometric diagram (Aevy):** grey isometric blocks on cream paper, coloured plot areas, serif caption.
- **Letter as portal:** huge serif word, one letter is a paper strip the camera flies through.

## Aevy TV per-topic palettes (examples)
- Science/brain: vintage anatomy illustrations on aged tan paper, botanical leaf watermarks,
  constellation dot-and-line networks, single-line drawings on teal paper, research headlines set as
  classic serif editorial pages.
- Cities: dark map + glowing pins + yellow routes; isometric cream diagrams; sketched portrait cards.
- Attention/tech: anime-style illustrated scenes, CRT-TV framed graphics with green diagrams,
  white-on-black minimal text, cute 3D characters.
- Money: light grey paper, chart and app screenshots, teal stat badges ("S&P500 +29.54%"), seals.

## Building it
- Higgsfield images (higgsfield-generate): "Vox documentary collage, cream paper texture with halftone
  dots, black and white photo cutout of [subject] with white paper border and drop shadow on a teal
  circle, typewriter label '[text]', red marker circle, scanned grain, flat lay, 16:9".
- Photoshop connector: cutouts (remove_background), Levels to B&W, torn edges, textures.
- Illustrator connector: maps, charts, routes, icons, type lockups, image trace of engravings.
- Then animate with vox-after-effects-recipes. Show the user designs before animating.
