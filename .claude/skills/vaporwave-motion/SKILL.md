---
name: vaporwave-motion
description: Vaporwave in motion - pastel pink/cyan/lavender palettes, Greek and Roman statues, Windows 95 / early-Mac UI and error pop-ups, Japanese and fullwidth text, checkerboard floors and pastel grids, palm trees, dolphins, malls and corporate stock imagery, early 3D primitives, low-res dithering and VHS - with motion rules (slowed dreamy drift, seamless loops, slow statue rotations, window cascades, echo trails, ghosting dissolves, sudden glitches, low frame rates). Covers classic vaporwave, mallsoft, early-web/Win95, seapunk and future funk, with After Effects, Blender, CSS/GSAP and Higgsfield recipes. Use when the user asks for vaporwave, ａｅｓｔｈｅｔｉｃ, Windows 95 aesthetic, statue aesthetic, mallsoft, seapunk, future funk, retro internet, or ironic 90s consumer nostalgia.
---

# Vaporwave motion

Vaporwave (early 2010s internet music and art; the name riffs on "vaporware") samples the leftovers of late-80s/90s consumer culture (elevator music, infomercials, corporate stock, Windows 95, malls, Japanese electronics) and slows them into a dreamy, hazy, slightly uncanny nostalgia for a future that never arrived. Its tone is **ambiguous irony**: is it celebrating consumerism or mocking it? Visually it's collage: classical statues + old computers + pastel neon + Japanese text + glitch.

**Not synthwave.** Synthwave is a sincere, glossy celebration of the 80s (sunset drive, chrome, energy). Vaporwave is slower, pastel, ironic, lo-fi, and collage-based. Don't mix them by accident (see `synthwave-motion`).

Pair with: `typography` (when breaking rules on purpose), `layout-composition` (collage balance), `pop-art-motion` (consumer imagery), `y2k-chrome-motion` (the next era; also not to be mixed in by accident), `higgsfield-generate`. Design hero frames as collages first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: Win95 windows and pop-up cascades, statues, checker floors, echo trails, slowed footage, dithering, VHS.
- `references/blender-css-ai.md`: rotating statues and early-3D scenes in Blender, CSS (98.css-style windows, fullwidth text), GSAP loops, Higgsfield prompts.
- `references/history.md`: origins, sub-genres, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Palette | Pastel neon: pink `#FF71CE`, cyan `#01CDFE`, mint `#05FFA1`, lavender `#B967FF`, pale yellow `#FFFB96`; skies `#FBC2EB` → `#A6C1EE`. Plus Win95 grey `#C0C0C0`, navy `#000080`, desktop teal `#008080`. |
| Classical | Greek/Roman busts and statues (Helios, Apollo, David), columns, often cut out over gradients or grids. |
| Retro tech | Windows 95 / Mac OS 9 windows, error dialogs, cursors, loading bars, CD-ROMs, CRT TVs, Walkmans, early web GIFs, MS Paint and WordArt. |
| Japanese text | Katakana/kanji and **fullwidth** Latin (ａｅｓｔｈｅｔｉｃ), often vertical. |
| Spaces | Checkerboard and tiled floors, pastel perspective grids, empty malls, fountains, offices with plants, pools, sunsets, palm trees. |
| Early 3D | Floating primitives (spheres, pyramids, chrome balls), low-poly models, flat-shaded renders. |
| Texture | Low-res, dithering, JPEG artefacts, VHS noise, chromatic aberration, scanlines, glitch. |
| Composition | Collage: floating objects, centred statue as hero, layered windows, generous gradient space; deliberately a bit "too much" but with one focal point. |
| Type | Win95 system fonts (MS Sans Serif lookalikes: W95FA, Pixelated MS Sans Serif), Times New Roman italic, Arial, WordArt-style gradient/extruded type, Japanese fonts, fullwidth spacing. Irony welcome; legibility still required. |

## 2. Motion principles

1. **Slowed and dreamy.** Like slowed + reverb: footage at 50–75% speed with frame blending, slow drifts and rotations. Nothing urgent.
2. **Seamless loops.** Pieces feel like a GIF or screensaver: 4–12 s loops that repeat perfectly.
3. **Slow statue rotation.** A bust turns slowly (360° over 8–20 s) or floats with a gentle bob.
4. **Window cascades.** Win95 windows and error dialogs pop open in stepped cascades (offset 20–30 px each), with cursor movement and clicks.
5. **Echo and ghosting.** Trails (echo effect), double exposures and slow dissolves are on-style here (unlike most other styles).
6. **Sudden glitch.** Calm is interrupted by short glitches: RGB split, datamosh smears, tracking lines, then back to calm.
7. **Low frame rates.** Optional 12–15 fps steps for GIF/early-web feel; or smooth slow motion. Pick per piece.
8. **Floating world.** Objects hover and bob in space (screensaver logic): sine floats, slow spins, objects bouncing off frame edges (DVD logo).
9. **Lo-fi finish.** Pixelation, dithering, VHS noise, slight blur, crushed or lifted pastel grade.

## 3. Signature moves

| Move | How |
|---|---|
| Statue spin | Bust slowly rotates in a pastel void or on a checker floor. |
| Error cascade | A stack of error dialogs pops open diagonally; the cursor clicks OK. |
| Desktop zoom | Push into a CRT monitor or a Win95 desktop that becomes the next scene. |
| Checker floor drift | Camera glides over an infinite checkerboard toward a sunset or a statue. |
| Screensaver | 3D pipes, starfield, flying toasters style; objects bouncing off edges. |
| Echo trail | Objects leave fading ghost copies as they drift. |
| Fullwidth title | ｖａｐｏｒ　ｔｉｔｌｅ types on with a blinking cursor, Japanese subtitle below. |
| Mall walk | Slowed footage of a mall/fountain/palm atrium with VHS texture. |
| Datamosh glitch | Pixel smear transition into the next scene. |
| Loading bar | A Win95 progress bar fills as the transition. |

**Transitions:** slow crossfade/ghosting, window opening into a new scene, CRT turn-off/on, datamosh smear, VHS tracking glitch, progress bar.

## 4. Sub-styles

- **Classic vaporwave (default):** statues, Win95, pastel neon, Japanese text, checker floors.
- **Mallsoft:** empty malls, fountains, food courts, corporate muzak; softer, more photographic, slowed.
- **Early web / Win95:** desktops, windows, pixel icons, GIFs, under-construction banners.
- **Seapunk (adjacent):** aqua and seafoam, dolphins, water, holographic textures.
- **Future funk:** brighter, faster, anime clips (use only licensed/original art), disco energy.
- **Hardvapour:** darker, harsher, glitchier (rare).

## 5. Build process

1. **Pick sub-style and loop length** (seamless loop if possible).
2. **Collage hero frames:** statue or object hero + background (gradient, grid, checker) + UI layers + text.
3. **Assets:** statue scans/renders, Win95 UI components, Japanese/fullwidth text, textures. Use public-domain statue scans and original UI recreations (no real brand logos).
4. **Animate slow:** drifts, spins, floats; cascades and cursor clicks on beats; glitch accents.
5. **Finish:** echo, VHS, dithering/pixelation, pastel grade; check the loop point.
6. **Check:** dreamy and ironic but still composed, with one focal point and readable text.

## 6. Critique checklist

- Pastel neon palette + Win95 grey, not synthwave sunset-chrome?
- Is there a clear hero (statue/object) in the collage?
- Is the motion slow and dreamy, with glitches only as accents?
- Does the loop seam disappear?
- Is the lo-fi texture present but not destroying legibility?
- Fullwidth/Japanese text correct (no garbled characters)?
- No real brand logos or copyrighted footage used without rights?
