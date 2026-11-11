---
name: neo-brutalism-motion
description: Neo-brutalism (neubrutalism) in motion - thick black outlines, hard zero-blur offset shadows, flat saturated clashing colours, oversized quirky display type with plain body text, visible structure, boxy cards, stickers, badges, marquees, cursors and UI chrome - with motion rules (press-into-shadow, slam and snap entrances, sticker slaps, tilts, tickers, hard cuts, instant or springy timing, never floaty). Includes After Effects, CSS/GSAP (HyperFrames) and Higgsfield recipes, plus the raw web-brutalism variant. Use when the user asks for neo-brutalism, neubrutalism, brutalist UI, Gumroad-style, bold flat black-outline design, hard shadow cards, sticker-style social graphics, or punchy anti-polish brand reels.
---

# Neo-brutalism motion

Neo-brutalism borrows the attitude of brutalist architecture (béton brut, "raw concrete": function over form, structure exposed) and makes it friendly: **visible structure, thick black outlines, hard offset shadows, flat loud colour and big type**, but with working hierarchy and affordances. It looks deliberately unpolished, never confusing.

Two related styles:
- **Neo-brutalism (default):** systematic, colourful, playful; borders + hard shadows + flat fills.
- **Raw web brutalism:** bare HTML look (system fonts, Times or mono, blue underlined links, grey/white, no shadows, exposed grids), confrontational and minimal.

Pair with: `typography` (display type quality), `layout-composition`, `design-principles` (contrast, hierarchy), `swiss-style-motion` (shares grids, not the polish), `pop-art-motion` (shares outlines and loud colour). Design hero frames as posters first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: outlined cards with linked hard shadows, press, slam, stickers, marquees, badges, cursors, highlights.
- `references/css-gsap-ai.md`: CSS components, GSAP moves for HyperFrames, Higgsfield prompts.
- `references/history.md`: background, accessibility notes, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Outlines | Solid black (`#000`) borders on every card, button, sticker and image: 2–5 px in UI, 6–10 px in 1080 video. One weight across the piece. |
| Shadows | Hard offset shadows, zero blur, solid black (or a dark colour): 4–8 px UI, 8–16 px video, usually down-right. One direction for everything. |
| Colour | Flat, saturated, often clashing fills: 3–5 colours + black + an off-white base. No gradients, no transparency. |
| Type | Oversized, quirky display (Archivo Black, Clash Display, Space Grotesk Bold, Lexend Mega, Syne ExtraBold, Rubik Black) + plain sans or mono for body and labels (Inter, Space Mono, JetBrains Mono). Text is black or white for contrast. |
| Shapes | Boxy rectangles with 0–12 px radius (one radius system), pills, circles, stars and squiggles as stickers. |
| Structure | Visible: grid lines, dividers, window bars, labels, tags, numbered sections. Layout logic stays clear. |
| Decoration | Stickers, rotated badges, emoji/hand-drawn doodles, arrows, cursors, highlighter boxes; used as accents, not everywhere. |
| Contrast | Text vs fill ≥ 4.5:1. Black on bright fills usually passes; check white-on-colour carefully. Avoid large areas of pure black + neon that strain the eye. |

**Palettes**
- Classic: cream `#FFF6E5`, yellow `#FFE14D`, pink `#FF6FB5`, blue `#5B8CFF`, lime `#B8FF5C`, black `#000000`.
- Warm: paper `#FDF1E3`, orange `#FF8A3D`, red `#FF4D4D`, lilac `#C4A1FF`, teal `#3DD6C6`, black.
- Raw brutalism: white `#FFFFFF`, grey `#E5E5E5`, link blue `#0000EE`, visited `#551A8B`, black.

## 2. Motion principles

1. **Physical, not floaty.** Elements feel like thick cardboard cut-outs: they slam, snap, press and pop. Never slow drifting fades.
2. **Press into the shadow.** The signature interaction: an element moves by its shadow offset while the shadow shrinks to 0, as if pushed into the page; it springs back on release.
3. **Two timing modes:** *snap* (instant or 2–4 frame moves, hold keyframes, steps) or *spring* (fast `back`-style overshoot). Choose one per piece; never long eases.
4. **Slam entrances.** Cards and type drop or slide in fast from off-frame with a small overshoot and a 1–2 frame shake; a slight rotation snap (±2–5°).
5. **Sticker slaps.** Badges and stickers land rotated with a quick scale overshoot (0 → 115 → 100%).
6. **Constant tickers.** Marquee bands scroll linearly; rotating circular badges spin slowly. They give life during holds.
7. **Cursor-led storytelling.** A big cursor arrow moves (quick ease), clicks (scale 90%), and buttons press: great for product and UI reels.
8. **Hard cuts and wipes.** Cut on beats; transitions are flat colour panels sliding in with outlines (a card covering the frame), not dissolves.
9. **Structure stays put.** Borders and shadow offsets don't animate thickness; move with transform/position only.
10. **No blur.** No motion blur or soft focus; crisp edges always.

## 3. Signature moves

| Move | How |
|---|---|
| Press | Button moves +offset, shadow collapses to 0, then springs back. |
| Slam card | Card drops in with overshoot + tiny shake; shadow lands with it. |
| Stack | Cards slam onto a pile, each slightly rotated, shadows stacking. |
| Sticker slap | Rotated badge pops on with overshoot. |
| Marquee | Black band with repeating text scrolls endlessly. |
| Spinning badge | Circular text badge rotates around a star or icon. |
| Highlight swipe | Flat colour box swipes behind a word (left to right, 4–6 frames). |
| Cursor click | Cursor travels, clicks, button presses, result pops. |
| Window pop | UI window cards with title bars pop open and stack. |
| Panel wipe | A full-frame outlined colour panel slides across as the transition. |
| Type jump | Giant word cuts between sizes/colours on beats. |

## 4. Build process

1. **Pick palette, outline weight, shadow offset, radius:** fix them for the whole piece.
2. **Hero frames:** design 3–5 poster-like frames with clear hierarchy (one giant headline per frame).
3. **Build components once:** card, button, sticker, badge, marquee, cursor as reusable precomps/elements.
4. **Animate:** slams and stickers on beats, presses with cursor clicks, tickers during holds, panel wipes between scenes.
5. **Check:** contrast, consistent outline/shadow everywhere, nothing floaty.

## 5. Critique checklist

- Same outline weight and shadow offset/direction everywhere?
- Any blur, gradient, transparency or soft shadow? Remove.
- One giant focal headline per frame; body text plain and readable?
- Text contrast ≥ 4.5:1 on every fill?
- Is the motion snappy (snap or spring), never slow fades?
- Do presses move into the shadow (offset and shadow change together)?
- Are stickers and doodles accents, not clutter?
