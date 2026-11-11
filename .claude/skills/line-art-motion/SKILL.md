---
name: line-art-motion
description: Line art in motion - monoline and variable-weight line illustration, continuous one-line drawings, minimal editorial/botanical/fashion lines, technical and blueprint lines, hand-drawn boiling lines, outline + offset spot-colour fills, single-line handwriting - with motion rules (draw-on in drawing order, a pen tip leading the line, continuous lines that travel and turn into the next drawing, tapered strokes, line boil, morphing paths, erase-offs, offset fills popping after lines). Includes After Effects (Trim Paths, taper, wiggle paths, pointOnPath pen tip), Illustrator prep (single-line fonts, image trace, width tool), SVG/GSAP DrawSVG and Higgsfield recipes. Use when the user asks for line art, line drawing animation, one-line or continuous line, outline illustration, minimal line, draw-on / write-on, signature animation, blueprint lines, or hand-drawn line style.
---

# Line art motion

Line art says everything with lines: no fills (or only flat accents), no shading except line weight. In motion, its superpower is the **draw-on**: the viewer watches the drawing happen. The craft is a confident line (clean curves, intentional weight) and drawing it in a believable order.

Variants:
- **Monoline (default):** one consistent weight, rounded caps; clean, modern, icon-friendly.
- **Variable weight:** 2–4 clearly different weights (thick outer contours, thin details) or tapered pen strokes; editorial, fashion, botanical.
- **Continuous line:** one unbroken line drawing the whole subject; poetic, elegant.
- **Hand-drawn / boiling:** wobbly line that boils on 2s/3s; friendly, explainer, sketchbook (see also `vox-collage-design` ink marks).
- **Technical / blueprint:** precise thin lines, construction lines, dimensions; white/cyan on deep blue or black on paper.
- **Outline + offset fill:** lines with flat colour shapes slightly misaligned underneath (trendy editorial look).

Pair with: `typography` (handwriting and labels), `layout-composition`, `flat-2d-motion` (when fills join), `swiss-style-motion` (rule draws), `risograph-motion` (offset fill cousin). Design the finished drawing first, then plan the draw order ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: Trim Paths draw-ons, drawing order, taper, pen tip, continuous lines, boil, morph, offset fills, handwriting.
- `references/illustrator-svg-ai.md`: Illustrator prep (paths, width profiles, single-line fonts, image trace), SVG/GSAP DrawSVG, Higgsfield prompts.
- `references/history.md`: background and sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Line weight | Monoline: one weight (4–8 px at 1080). Variable: ≤ 4 clearly different weights (e.g. 8 / 4 / 2 px); never weights that are almost the same. |
| Caps and joins | Round caps and joins for friendly lines; butt/miter for technical. |
| Curves | Smooth, few anchor points, confident arcs; no wobbly accidents (unless the hand-drawn variant). |
| Economy | Reduce the subject to the fewest expressive lines; negative space does the rest. |
| Closure | Leave gaps and open lines where the eye fills in; not everything needs closing. |
| Colour | One line colour (ink on paper, white on dark, cyan on navy) + at most 1–2 flat accent colours for fills. |
| Fills | None, or flat accent shapes offset 6–20 px from the line for the editorial look. |
| Type | Clean sans or a single-line/handwriting script; labels in the same line colour. |
| Grid | Technical variant on a visible grid; others free but balanced. |

**Palettes:** ink `#1B1B1B` on paper `#F5F1E8`; white `#FFFFFF` on night `#0E1116`; blueprint `#E6F4FF` on `#0B3D91`; accent fills: coral `#FF6B5B`, mustard `#F2C14E`, sage `#9BC1A3`, sky `#8EC5FF`.

## 2. Motion principles

1. **Draw in a believable order.** Big structural lines first, then secondary contours, then details and texture lines; follow the natural stroke direction (top to bottom, left to right for most hands).
2. **Constant pen speed.** A pen travels at a roughly even speed: longer lines take longer. Set durations proportional to path length; ease only at the start and end of a stroke.
3. **Overlap strokes.** The next stroke starts slightly before the last ends ([[overlapping-motion]]); stagger 2–4 frames.
4. **A pen tip leads.** Optional dot, pen or glowing tip riding the end of the drawing line.
5. **Continuous line travels.** In one-line work, the line never lifts: it draws a subject, keeps going, and becomes the next subject.
6. **Taper and pressure.** Strokes taper in and out like a real pen (thin start, full middle, thin end).
7. **Line boil for hand-drawn.** 2–3 slightly different line versions cycling at 8–12 fps keep holds alive.
8. **Morph lines.** One drawing's paths morph into another's (matching path counts), or lines un-draw and re-draw.
9. **Fills follow lines.** Offset fills pop or wipe in after the line completes, never before.
10. **Erase with intent.** Un-draw from the start (Trim Start) to pass the baton to the next drawing.

## 3. Signature moves

| Move | How |
|---|---|
| Draw-on | The illustration draws itself in a natural order. |
| Pen-led line | A pen tip leads a single line across the frame. |
| One-line story | A continuous line draws subject A, travels, and becomes subject B. |
| Write-on | Handwritten word or signature writes itself. |
| Draw + fill | Lines draw, then offset colour fills pop in. |
| Blueprint build | Construction lines, then object lines, then dimensions draw on. |
| Line morph | A drawing reshapes into another. |
| Boil hold | Hand-drawn lines boil gently during holds. |
| Flow lines | Dashed lines and arrows travel along routes. |
| Un-draw transition | Lines retract from their start, revealing the next scene. |

## 4. Build process

1. **Draw the finished art** (Illustrator or AE shapes) with clean paths: few points, correct stroke direction, separate paths per stroke.
2. **Plan the drawing order** and number the paths.
3. **Animate draw-ons** with Trim Paths (or DrawSVG), durations proportional to length, overlapping.
4. **Add life:** pen tip, taper, boil, fills, morphs, transitions.
5. **Check:** the order feels like a hand drawing, the line never jumps, and the final frame is a clean illustration.

## 5. Critique checklist

- Consistent weights (monoline) or clearly distinct weights (≤ 4)?
- Clean curves with few points; round caps/joins where friendly?
- Draw order natural (structure → details)? Stroke directions consistent?
- Speed proportional to length; strokes overlap?
- Fills appear after lines and are offset deliberately?
- Final frame is a balanced illustration with good negative space?
