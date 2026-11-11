---
name: reel-craft
description: Craft rules for Instagram reels and short-form motion, learned from a frame-by-frame and audio study of 30 reference reels - visual design and palette, pacing and cut rate, the hook, camera and lens, transitions, kinetic typography and captions, sound design and loudness, plus twelve format recipes (UI promo, phone-shot screen, type sting, glitch edit, tutorial, showreel, lyric video, macro ad, icon morph, comment-bait, collage, stat count-up). Use when the user asks to design, plan, animate, critique or sound-design a reel, Instagram reel, short-form motion, promo, product ad, explainer, kinetic type piece, UI animation, showreel or lyric video, or asks for motion design reference, a hook, pacing, transitions, or sound design for video.
---

# Reel craft

A rulebook for short-form motion, built from 30 public reels from one platform and one season. Every frame was measured (luma, change, shift, zoom), contact sheets were read at about 5 fps plus every frame around big changes, and the audio was measured (loudness, bands, onsets, tempo) and read from spectrograms. Honest limits: 30 reels is a sample, so ranges describe tendencies, not norms; the files were 720 px rips; lens, light, tempo and key are estimates; nobody listened to the audio, so effect names are inferred; the sample is nearly all Latin script, promo and showcase work.

Pair with: `explainer-documentary` (plan the story, hook and scenes), the style skills (`swiss-style-motion`, `glassmorphism-motion`, `flat-2d-motion`, `clay-3d-motion`, `y2k-chrome-motion` and the rest) plus `design-principles`, `layout-composition` and `typography` (the look), `cinematography-for-ai` (shot size, lens, AI video prompts), `after-effects` MCP, `motion-reel` and HyperFrames (the build), and `references/sound-design.md` for sound. Design key frames as stills first, then animate between them. Each move starts before the last ends.

References (open only what the step needs):
- `references/visual-design.md`: style family, key (dark or light), palette, lighting, backgrounds, layout per aspect ratio, constants, still-frame critique.
- `references/pacing-and-timing.md`: cut rate by class, hook timing, beat length, caption cadence, holds, stagger, long-form, endings.
- `references/camera-and-lens.md`: virtual camera moves with amounts, phone-shot-of-a-screen, macro and HUD, talking head, blur on cut frames.
- `references/transitions.md`: 16 transition families with frames and builds, decision table, density rules.
- `references/kinetic-type-and-captions.md`: type classes, word cadence, build styles, emphasis, counters, caption placement, five reusable recipes.
- `references/formats-and-recipes.md`: beat sheets for 12 formats, pick-a-format table, pre-flight checklist.
- `references/sound-design.md`: loudness targets, layers, effect vocabulary, music, voice, sync, mix commands.
- `references/case-studies.md`: index of the 30 reels by need, with how to open the raw evidence.
- `references/analysis-method.md`: scripts and method to repeat the study on new reels.

## The ten laws of a reel

1. **Pick the format class first, because cut rate follows class:** cut-driven reels run a median 1.03 s per shot (0.38 s in word-per-shot edits [DdwCXaQIHNU, Dcs-MiOpO2V]), while phone-shot screen takes have 0 to 1 cuts and a beat every 0.7 to 1.5 s [Db28edFqHTP, DdY8V8XKJD6].
2. **Start something by 0.4 s, finish the hook line by about 2 s, and land the first hit, cut or reveal at about 2.0 s** [DclkKscsRbs 0.8 s, DZCY6bjOsUQ 1.8 s; first big audio arrival at 2.0 s in eight reels, e.g. DdwCXaQIHNU, DeSvnCQIgs3].
3. **One new idea per beat, held at least 0.3 s, with the next move starting before the last ends and text entering only after the previous element has left** [Db28edFqHTP, DcL6By1z4QE].
4. **Words build at 0.2 to 0.35 s each (6 to 10 frames at 30 fps), each larger than the last, with one emphasis device on one word per beat** [DZCY6bjOsUQ 0.2 s, median 0.27 s over nine reels].
5. **Use one accent hue on a neutral ground and spend it on the punch word only** (12 of 30 reels read this way [DZCY6bjOsUQ, DcYXIWbxzAN]); use more hues only by assignment, such as one colour field per shot [DdwCXaQIHNU, DeF8z3XoLdh].
6. **Fix one to three constants that never move (caption, HUD, frame, ground), and keep 9:16 caption text out of the lowest 30% of the frame as a precaution (no platform safe zone was measured)** [12 reels carry furniture, e.g. DeMrHF6qi0z, DdwCXaQIHNU; fixed phone-shot caption tops sit at 11 to 23% of height, mid-frame captions at 49 to 57%, one bottom caption at 66 to 70%].
7. **Choose one camera strategy and keep it:** flat pieces get no camera [DXzurbATRQT, Dbmcud4IexE], phone shots get 12 to 15 px of slow drift and no cuts [Db28edFqHTP], a crash zoom is about 3x in 3 to 7 frames with heavy blur [DeF8z3XoLdh], and type sits behind a 3D hero, never in front [Dc0izivoZNw].
8. **Use one bridge per cut (1 to 7 frames in cutting formats, 12 to 18 frames in no-cut formats), echo the content in it, and save the biggest transition for the hinge at 40 to 77% of runtime** [DZUZITfz0Qu; DXzurbATRQT 44%, DeXDu86snYE 77%].
9. **Score only the biggest 3 to 9 events in 25 to 35 s, make contrast by subtraction (a 0.2 to 0.5 s dropout or a 4-beat low-cut before the hit), and land impacts 0 to 60 ms before the cut** [Dc0izivoZNw, Db28edFqHTP 37 ms, DZUZITfz0Qu].
10. **Hold the final lockup 1.0 to 2.7 s (median 1.5 s), and export at -14 LUFS with true peak at or under -1 dBTP,** because 12 of 30 originals peaked above 0 dBTP [DdwCXaQIHNU +3.1].

Conflict resolved: the source notes and five files said the frame countdown in the macro ad updates every 6 frames; re-reading the every-frame contact sheet (f50 to f58 read 161 down to 153) and the frame-numbered notes shows it steps one unit per frame, 211 minus the frame index, red near the end [DeXDu86snYE]. Use `Math.max(1, 211 - frame)`, not a 5 Hz clock.

## Workflow

1. **Brief and format.** Audience, goal, assets, aspect (18 of 30 are 9:16), length. Pick a format in `formats-and-recipes.md` (pick-a-format table), then 1 to 3 precedent ids in `case-studies.md`.
2. **Hook and beat sheet.** Write beats, not cuts: one idea each, a count of beats per second from the class rate. Plan the first 2 s and the hinge. Use `pacing-and-timing.md`; for story, `explainer-documentary`.
3. **Design key frames.** Choose family, key (dark or light), palette, constants, layout per aspect, then stills for 3 to 6 beats. Load the closest style skill. Critique each still with the checklist in `visual-design.md` section 7.
4. **Choose transitions and camera.** One strategy, one to three transition families, one bridge per cut, a trigger in frame for each change. `transitions.md`, `camera-and-lens.md`.
5. **Kinetic type.** Two or three type classes, word cadence, one emphasis device, caption placement for the aspect. `kinetic-type-and-captions.md`.
6. **Sound plan.** Lead layer, tempo, sync mode (grid, hit, structure, voice), the 3 to 9 scored events, the dropout, the ending. `sound-design.md`. Compute grid frames with `Math.round(beat*60/bpm*fps)`.
7. **Build.** After Effects via MCP, `motion-reel` or HyperFrames for coded, beat-synced work. Put constants on the top layer, outside time remaps.
8. **Critique.** Run the pre-flight checklist (`formats-and-recipes.md`), the still checklist, and the sound mix checklist. Fix dead frames, second accents and unheld states first.
9. **Export and check.** Measure loudness on the final encode, limit at -1 dBTP, run a mono-sum and phone-speaker check, confirm the end hold.

## Quick lookups

| Request | Recipe (formats file) | Study ids |
|---|---|---|
| Make a product promo | 1 (UI promo), or 2 if it is shot off a screen | Db28edFqHTP, DdY8V8XKJD6, DXzurbATRQT |
| Phone-shot screen reel | 2 (single take, no cuts) | Db28edFqHTP, DdjM8xRNzk_, DeaJ4yUg95f |
| Kinetic logo sting | 3 (type or logo sting), plus 9 for morphs | DeF8z3XoLdh, DdwCXaQIHNU, DcYXIWbxzAN, DeSvnCQIgs3 |
| Tutorial with voice over | 5 (talking head plus screen) | DeZ3P_8NeHT, DcGaekAMU90, Dd6Uc27ssjp |
| Showreel | 6 | DcOIGDdss_L |
| Lyric video | 7 | DeRpl8Yhrb2, DeMrHF6qi0z |
| Hype or glitch edit | 4 | DZUZITfz0Qu, Dcs-MiOpO2V |
| One-object ad | 8 (macro ad) | DeXDu86snYE, Dc0izivoZNw |
| Comment-bait or booking CTA | 10 (1:1) | DdCH-tFy7Wp, DclkKscsRbs, DeZOFtEMkuA |
| Collage or cutout explainer | 11 | DcL6By1z4QE, DZCY6bjOsUQ, Dd_t1ZhNAoR |
| Stats and results beat | 12 (inside another reel) | DdwCXaQIHNU, DdY8V8XKJD6 |

## Using the study data

The source data lives in `C:/Users/basha/Motion Design/Training Data/Instagram Refs/`: `DETAIL-batch-01.md` (frame-by-frame notes, one `## <id>` heading per reel), `STUDY-batch-01.md`, `meta.md`, `frames_data/` (EVENTS.txt and a per-frame CSV per reel), `sheets/<id>.jpg`, `dense/` contact sheets, `audio/` (spectrograms and `audio/parts/<id>.md`), and the mp4s.

To open a case study: pick ids from `references/case-studies.md`, Grep `## <id>` in the detail file and Read that section with offset and limit, view `sheets/<id>.jpg` then 3 to 4 dense sheets, read sections 8 and 9 of the audio part, then build a timing sheet in seconds and convert to frames at your fps. Take techniques, not content: keep creator names, brands, captions and lyrics out of briefs and outputs.

The analysis scripts and method are in `references/analysis-method.md` (and `scripts/`), so the study can be repeated on new reels. New batches go in the same folder as `DETAIL-batch-02.md` and `audio/SOUND-STUDY-batch-02.md`.
