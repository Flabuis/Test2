# Scene recipes

## Map reveal (antique map)
- Antique map scan (Library of Congress). Pen mask around the region, feather 15.
- Duplicates: "Region" (mask add), "Rest" (mask subtract, below), "Region Outline".
- Outline: Video Copilot Saber (free), Core Type = Layer Masks, glow bias 0.3, core size 3.5, blend
  Classic Difference; animate Offset 0 -> 100 over 1 s (easy ease). No Saber? Stroke effect on the mask
  + Glow, or a shape copy of the mask path with Trim Paths.
- Callout precomp 1080x1080: red filled circle scale 0 -> 100 easy ease; larger stroke ring duplicate
  fading in; centre anchor (Layer > Transform > Center Anchor Point); place on the region, Multiply.
- Lift the region (3D, slight Z forward) and fly through it into the next scene with an ink-bleed matte.
- Aevy city-map variant: dark top-down footprints, glowing icon pins, yellow route stroke drawing on
  with a travel-time label ("10 MIN"), radius circle.

## Bar chart
- 4K paper texture scaled to fit, `posterizeTime(6); wiggle(2,4)` on position; Levels + Invert to blend
  into a pale off-white background.
- Proportional grid (Edit > Preferences > Grids & Guides) to align bars and lines.
- Bars: shape rect positioned so its bottom sits on the layer anchor; Scale [100,0] -> [100,100] eased,
  staggered 0.18 s.
- Gridlines: shape stroke in paper colour with Dashes + Offset expression, Trim Paths draw-on staggered;
  they cut across the bars.
- Year labels in a rounded black pill along the baseline.
- Title: serif, built-in "Cursor" typewriter effect (blinking cursor only).
- Red circle draws on (Trim Paths) around the tallest bar; value callout ("300 MILLION") fades in.
- Displacement Map sourcing the animated paper so bars wobble with it; camera pushes in; lens blur pull.

## Pie chart
- White concrete texture at 50% with the paper boil expression.
- Base pie: ellipse with stroke width = radius, centred anchor; Trim Paths End 0 -> 100.
- Slice: duplicate in another colour; animate BOTH Trim Start and End (start 75, end 100 = last quarter).
- Break-away: move/rotate the slice outward (ease copied with the Flow plugin if installed).
- Photo inside the slice via track matte; ink-bleed turns the frame B&W; spaced serif label
  ("25 PERCENT") and a big word revealed letter by letter.

## Line chart
- Ink line with dot markers, thick rough stroke; draw on with Trim Paths; dashed vertical guide at the key
  year; red circle around it; camera zooms to a "micro shot" of that point.

## Timeline of prints
- Placeholder precomps in a row on the proportional grid; white border via Stroke effect (or shape rect
  stroke) drawn on in sync with the camera zoom-out, off on zoom-in.
- Background: desaturated old document (Tint, Levels) at Z 6000, low opacity.
- Prints tilt slightly in X/Y as the camera passes; jitter `posterizeTime(6); wiggle(10,30)`.
- Yellow dashed paths between cards (Dash 13, Offset `time*-10`), Trim Paths draw-on.
- Torn edges: Fill white + Roughen Edges.

## Newspaper front page
- Newsprint: brown paper texture + halftone, desaturated with Levels; Extract to clean scans.
- Masthead and headline in Caslon Pro Bold; huge year; body columns; byline; thin rules; text lines
  animate on one by one.
- Archival group photo keyed (Keylight if green-screen, else Extract/roto); reflection = flipped duplicate,
  Gaussian blur, low opacity, parented to the photo.
- Signature: trace as 2 shape layers (first/last name), Trim Paths End 0 -> 100, handle pulled to the
  start (fast start, ease in).
- 3D camera pushes across the page; layers at varied Z (6500-10000).

## Archival pop-out (outlaws)
- Graph-paper Grid effect background, jitter `posterizeTime(6); wiggle(1,10)`.
- Sepia print on black marble; rotoscoped people ease forward out of the photo; condensed white name labels
  left-justified; big title word.
- Displacement dissolve + Roughen Edges for gritty paper edges (see camera-and-finishing.md).

## Character collage
- Paper texture far back (Z 20000), character cutout near, yellow eye bar (shape) at Z 6000, building
  cutouts at Z 9000.
- Handwritten script texture revealed by Mask Expansion.
- Buildings pop up from below (chimney offset after building); B&W copies first, colour copies after.
- Name: Text Animator Tracking (start tight) + Opacity 0, range selector Start 0 -> 100 over 1 s; eye bar
  trims away in sync (the reveal).

## King / royalty collage
- Dark textured paper; outlined serif word with one letter as a gold paper portal; crown cutouts with
  Deep Glow; gold brush strokes; Roughen Edges on every stroke, border and diamond; strokes then fills;
  hold keyframes; Displacement Map from a stone-wall texture in bursts.
- Light linen variant: black circle splits into a half-circle "sunrise" on a horizon line; B&W helmet
  rises into it (shape matte); faint engraving watermark.

## Process-flow infographic (Mapal)
- Row of cutout objects joined by hand-drawn arrows drawing on; colour-coded stage bars above
  ("Production" lime, "Consumer" light blue); sequential pops with S-curve easing; camera pans along,
  then zooms out to the whole chain.

## Icon morphs (Nijat)
- Flat icon shapes morph by copying path keyframes between shapes; squash-and-stretch rotation pops.
