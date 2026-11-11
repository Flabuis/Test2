---
name: vox-after-effects-recipes
description: Exact After Effects recipes for Vox-style and documentary motion graphics - choppy posterized motion, paper boil, 3D camera fly-throughs with nulls, Z-space parallax, map reveals, bar/pie/line charts, timelines, newspaper pages, archival pop-outs, torn-paper and ink transitions, flicker and grain finishing - with expressions and settings, built through the user's after-effects MCP connector. Use when animating Vox, Aevy TV, collage, paper, archival, map or infographic scenes in After Effects.
---

# Vox After Effects recipes

Exact settings from 13 tutorials (mostly createdaley). Use the `after-effects` MCP connector:
`run_extendscript` for multi-layer builds, `preview_frame` to check, `render_comp` for test MP4s.
Save test projects in a dedicated tests folder on a drive with plenty of free space.

Read the reference file for the scene you're building:
- `references/scenes.md`: maps, charts, timelines, newspaper, archival, collage, infographics.
- `references/camera-and-finishing.md`: camera rigs, transitions, the finishing stack.

## The five layers of every scene
| Layer | Motion |
|---|---|
| Text | minimal pop: scale/opacity, tracking-in, typewriter cursor, highlight wipe |
| Main object | pop up from below, paper unfold, slide with overshoot, hold-keyframe "hit" |
| Background | static paper with a subtle boil |
| Secondary | small jitter, wobble, 1-2 frame boil |
| Camera | one move per shot: slow push, or fly/pan to the next design |

## Core expressions
- Choppy jitter (handheld, cards, textures): `posterizeTime(6); wiggle(1,4)` on Transform position.
  Stronger photo jitter: `posterizeTime(6); wiggle(10,30)`. Grid jitter: `posterizeTime(6); wiggle(1,10)`.
- Paper boil: `posterizeTime(6); wiggle(2,4)` on a 4K paper texture's position (scaled to fit).
- Flicker: Curves (or Exposure) on an adjustment layer with `posterizeTime(6); wiggle(2,100)` on opacity.
- Crawling dashes: Stroke > Dashes (Dash 13) and Offset `time*-10`.
- Texture evolution: `posterizeTime(12); time*120` on Fractal Noise evolution.

## Core motion rules
- Posterize Time adjustment layer on top: 12 fps (8-15). This is the Vox feel. Re-check timing after
  posterizing so hits still land on the beat.
- Easing: F9 easy ease, then in the Graph Editor pull handles to make moves start fast and settle
  (handle pulled toward the start) or snap (both handles to the middle: slow-spike-settle).
- Stagger repeated elements (bars, lines, letters) by 0.1-0.2 s.
- Strokes before fills: draw shapes on as outlines (Trim Paths), then switch to the fill.
- Hold keyframes for stop-motion "hit" poses.
- B&W duplicate animates first, colour version follows a few frames later.
- Motion blur on everything, last (it slows renders).

## Known gotchas
- On some systems/locales, text numbers come out as Arabic-Indic digits unless you set `textDocument.digitSet = DigitSet.DEFAULT_DIGITS`.
- Text layers: `layer.property("Source Text")`; skip non-text layers when looping by name.
- Use real paper/wall scans for texture; Fractal Noise overlay at high opacity looks like sand.
- Bahnschrift (Bold/Condensed, a Windows system font) works for condensed labels; Times New Roman for serif.
