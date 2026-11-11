---
name: typography
description: Typography rules and systems for print, screen and video - choosing typefaces by tone, pairing fonts, sizes, leading, line length, tracking, kerning, type scales and hierarchy, readability, expressive type, plus logo and lettering quality checks. Use when picking or pairing fonts, setting headlines, body text, captions or on-screen titles, building a type system or brand typography, fixing text that looks amateur, or designing logos and lettering.
---

# Typography

From DesignSpo, Satori Graphics, Kittl, GraphiqVibe, Kole Jain, Juxtopposed and The Futur (Chris Do: type
rules, kerning, terminology, typography critiques, lettering, logos). Pair with `design-principles` and
`layout-composition`.
- `references/logos-and-lettering.md`: monoline logos, hand lettering, logo quality tests.
- `references/installed-fonts.md` (if present): pairings from fonts installed on this machine, with licence notes.

## Choose the typeface by tone
- **Serif:** tradition, stability, timeless (finance, law, jewellery, editorial, documentary quotes).
- **Sans-serif:** modern, clean, versatile, most legible on screen; UI, packaging, signage, body text.
- **Display:** logos, titles, short bursts only - never paragraphs, buttons or labels.
- **Script:** elegant, luxury, personal (short words only). Handwritten = playful.
- **Monospace:** code, data, typewriter-style captions.
- When unsure, pick a proven classic (Helvetica/Akzidenz-Grotesk, Avenir, Futura, Garamond, Bodoni, Caslon)
  or a free equivalent.

## Pairing
- One family with weight/size contrast is enough for most work. Two families max (plus a mono for captions).
- Never pair two of the same classification (two sans, two serifs, two scripts): pair for contrast.
- Classic: serif headline + sans body, or sans headline + serif body.
- **Skip a weight:** light -> bold, medium -> extra bold. Small weight steps go unnoticed.

## Numbers that work
| Setting | Rule |
|---|---|
| Body size | Print 9-12 pt (10-12 ideal; test-print below 9); web 16-18 px (15-25 range) |
| Leading | Body 120-145% of size; display ~100-115%; large x-height faces need more |
| Line length | 45-90 characters (~66 ideal); ~65 max for small x-height, ~52 for large x-height |
| Headings | H1 180-200% of body; H2/H3 130-150%; or simply double the size per level (3-4x for drama) |
| Tracking | Tighten large display type -2 to -3%; open up small text, all-caps labels and bold buttons |
| Sizes per project | Landing page ~6 max; poster 3-4; dashboard rarely above 24 px |
| Contrast | Text vs background 4.5:1 minimum, 7:1 ideal |
Size, line length and leading move together (triadic relationship): change one, rebalance the others.

## Setting text
- Left-align, ragged right by default; centre only short deliberate blocks; never force-justify (rivers).
- No first-line indent after headings; one space after punctuation; no hyphenated breaks in body.
- No widows/orphans; watch the shape of the rag.
- Avoid all-caps for anything long (kills word shapes); never stretch type or fake bold/italic.
- Align type to one strong axis (shared left edge, or a shared baseline/cap height).
- Group related blocks with proximity or thin rules; underline only headlines/links.
- **Kerning by shape:** curve-curve tightest (OO, CD); straight-straight most open (HI); straight-curve normal;
  diagonal-diagonal very tight (VA, WY). Always kern logos and big headlines by eye.

## Type systems
- Define styles for headings (2-3 levels), body, buttons and labels. Smaller = lighter and more open; buttons
  are bolder with a little extra tracking; labels smaller and lower-contrast.
- Use a type scale (e.g. 1.25 or 1.333 ratio); lock sizes to a baseline grid (headings at multiples of body leading).
- Web: rem units (16 px base). Print: points.

## Hierarchy with type
- Size, weight, colour, case, spacing, style. Change one or two per level, not all at once.
- When two lines compete, make one clearly bigger and the other clearly smaller.
- Expressive type: commit fully (offset, overlap, scale, tight crops, tension) and keep the information
  zone plain and findable. Negative space around a word makes it louder.

## Common faults (bad -> good)
- Too many sizes, weights, fonts, effects -> pick fewer and commit.
- Headline barely bigger than body -> double it or more.
- Centred paragraphs, tight leading, long lines -> left-aligned, 130-145% leading, 45-75 characters.
- Type jammed into corners or edges -> generous margins.
- Grey on grey, thin type at small sizes -> stronger contrast, regular weight or heavier.
- Pre-stretched-looking extended faces used for everything -> save them for display.

## Video and documentary use
- On-screen titles: condensed bold sans caps for labels, serif for quotes/headlines, mono for data captions.
- Large numbers: tighten tracking. Small captions: open tracking, mono or small caps, keep away from the
  platform's caption area.
- Check readability on a phone at real size, on light and dark footage (add a soft shadow or a backing shape).

## Kinetic type and captions in reels
Extends "Video and documentary use" for short-form reels, from a 30-reel study. Frames are at 30 fps.
- **Type classes:** two or three per reel. Heavy grotesque for the hero word, condensed or italic serif for
  sub-lines and numerals, mono or pixel caps for captions and HUD labels, thin light sans for quiet product
  lines, rounded UI sans for stickers and chat.
- **Size pairing:** one huge word with tiny connectors; escalate size word by word inside a line.
- **Cadence:** one word per 6 to 10 frames (median about 0.27 s). Hold a finished line 9 frames minimum, 15 for
  a seven-word headline. In loud type reels the first word is on screen by frame 12.
- **Build styles:** word by word with a 3 to 4 frame fade or blur-in; typed with a caret (14 to 32 characters
  per second in UI fields, 3 to 4 frames per letter in headlines); letter by letter at 2 to 3 frames. Exit by
  the build device, or morph into the next object.
- **Emphasis:** one device on one word per beat: accent colour (one hue per reel), size jump, underline draw
  over 10 to 12 frames, highlighter fill, or an italic serif swap inside mono captions.
- **Captions:** speech-synced, 1 to 3 words (one reel used uppercase letter-spaced mono), centred below
  mid-frame in 9:16 (measured 49 to 57 percent of height) and clear of the lowest 30 percent as a precaution. A phone-shot screen gets a fixed caption outside the shot. Never cover a face; on busy
  footage use a solid bar or pill. Platform safe areas were not measured, so check current guidance.
- **Numbers:** counters ease out over 30 to 42 frames with vertical blur; use tabular figures.

See also: reel-craft/references/kinetic-type-and-captions.md
