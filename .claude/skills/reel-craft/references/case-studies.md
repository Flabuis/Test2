# Case study index

Use this file to pick one to three of the 30 studied reels as precedent for a brief, then pull their evidence. The study covered 30 short motion reels, frame by frame and for sound. Reels appear only as an id plus a descriptor. The source headings carry creator and brand names and the reels carry captions and lyrics: keep all of those out of briefs and outputs. Take techniques, not content. A bracket with one id means the technique was seen in one reel only.

## How to use it

1. Classify the brief by format and mean shot length (next section), then pick 1 to 3 ids from "Find a reference by need" or the index.
2. Read each id's section in `DETAIL-batch-01.md` and section 8 of `audio/parts/<id>.md`; look at `sheets/<id>.jpg`.
3. Build a timing sheet: list the reference's events in seconds and convert to frames at your delivery fps. Source fps: 25 of 30 reels are 30; Dc0izivoZNw, Dd6Uc27ssjp and DeO1Rh7x5Qm are 24, DcGaekAMU90 is 25, Dd_t1ZhNAoR is 20. Keep order and spacing; change content, colour, look.
4. Pair the mechanism with the closest style skill, plus `visual-design.md`, `formats-and-recipes.md`, `pacing-and-timing.md` and `sound-design.md` in this folder. Stills: design-principles, layout-composition, typography. Camera and lens: cinematography-for-ai. Paper-collage documentary: vox-collage-design, vox-after-effects-recipes. Coded, beat-synced build: motion-reel.
5. Convert time in code, not by hand: GSAP `stagger` of 2-4 frames at 30 fps is 0.067-0.133 s; Remotion `delay = i * 2..4` frames; an AE frame counter is `Math.max(1, 211 - Math.floor(time * 30))` in a source-text expression, one step per frame [DeXDu86snYE].

## Shape of the set (computed from meta.md, all 30)

18 reels are 9:16, 9 are 16:9, 3 are 1:1. Median duration 24.0 s. Median hard cuts 2; 8 reels have none and 17 have 3 or fewer. Mean shot length (duration / (cuts + 1)) has a median of 6.8 s: 10 reels average under 2.5 s (shortest Dcs-MiOpO2V at 0.4 s; DcOIGDdss_L 1.3 s) and 13 average 8 s or more. Dissolves and whips hide cuts in DeRpl8Yhrb2 (72 shots in EVENTS.txt) and Dc0izivoZNw (8 shots), so their means are upper bounds. Pacing guide: the type stings, teasers and showreel average under 2.5 s per shot [Dcs-MiOpO2V, DcYXIWbxzAN, DdwCXaQIHNU, DeF8z3XoLdh, DcOIGDdss_L]; the six phone-shot screen takes have 0 or 1 cut [Db28edFqHTP, DdY8V8XKJD6, DdjM8xRNzk_, DeSvnCQIgs3, DeXtJrAtOcr, DeaJ4yUg95f].

## Index of the 30 reels

Cuts are hard cuts from meta.md (scene change above 0.3). Flashes inflate the count and fades hide cuts, so DZUZITfz0Qu is given as 11 shots. "Reel" means showreel, trailer or teaser. The style column is a navigation aid from STUDY-batch-01.md plus judgment; "none close" means no style skill fits.

| id | format, length, aspect, cuts: descriptor | picture | sound | style skill |
|---|---|---|---|---|
| DXzurbATRQT | UI motion, 32.9 s, 9:16, 4 cuts: UI showcase, neon blobs, black-white-black | dot-and-wire motif; shape-morph chain; theme flip on a glow flash (14.4 s) | sub boom 0.17 s before the first cut; thud-plus-click on the flip | line-art-motion |
| DZCY6bjOsUQ | collage, 26.2 s, 9:16, 10 cuts: voice-led promo, red serif on cream, marble cutouts | travelling vignette as light; words build 0.2 s each, escalating size; 3D card tunnel | voice only; 9 of 11 cuts within 80 ms of an onset (53% by chance) | vox-collage-design |
| DZUZITfz0Qu | glitch edit, 14.7 s, 9:16, 11 shots: live-action motorbike edit | strip glitch, 1-frame inversion flashes, circle-to-X mask wipe, blur-snap after cuts | 0.33 s mute, then a hit 60 ms before the cut | none close; pop-art-motion |
| Db28edFqHTP | screen take, 16.1 s, 9:16, 0 cuts: SaaS promo shot off a wall display | pill-to-card beat every 0.7-1.0 s; glass cards at varied Z; one rack focus | low end out for 4 beats (6.46-8.53 s) | glassmorphism-motion |
| Dbmcud4IexE | morph chain, 103.8 s, 16:9, 2 cuts: icon-to-icon chain, lavender-grey | one property per morph, 0.3-0.5 s ease-out settle; geometric-echo links | click trains under mechanical icons; 3 s air wash on the white-out; +1.8 dBTP (avoid) | flat-2d-motion |
| Dc0izivoZNw | reel, 25.6 s, 9:16 canvas at 24 fps, 2 cuts (8 shots): 3D course trailer, render over viewport panel | camera never stops; whip or white flash at each cut; thin focus plane | 0.5 s vacuum, then +13.8 dB on the cursor press | clay-3d-motion |
| DcGaekAMU90 | VO tutorial, 90.7 s, 9:16 at 25 fps, 41 cuts: brand-kit course promo, design-tool UI as set | cursor and UI chrome motivate changes; fixed chapter-card template (2-frame colour blink, held 0.9-1.1 s), build it by changing only number and background colour; one heavy word per 0.3 s | bass swells +7 to +15 dB at section turns | neo-brutalism-motion |
| DcL6By1z4QE | VO explainer, 51.7 s, 9:16, 0 cuts (11 swap segments): duotone cutouts, top-down | old object leaves as the next enters; shared tint and shadow | voice only, LRA 2.2 LU, bass-forward | vox-collage-design |
| DcOIGDdss_L | reel, 84.1 s, 16:9, 62 cuts: game-themed motion-designer showreel | 1-3 s pieces, one full motion each; hard cuts on matching colour or direction | LRA 10.5 LU: 1.4 s dropout; 3.4 s silence under the badge | none single |
| DcYXIWbxzAN | type sting, 6.3 s, 16:9, 2 cuts: neon mint greeting, letters become a hand | glyph strokes reused as fingers; glow = blurred copy plus outline echo | stinger: thud 0.03 s, click 0.14 s on the cut | y2k-chrome-motion |
| DclkKscsRbs | UI motion, 12.0 s, 1:1, 1 cut: square freelance-editor pitch | cursor directs timing; 4-frame blur-in and blur-out on every transition | 0.27 s true silence before the biggest boom | glassmorphism-motion |
| Dcs-MiOpO2V | type sting, 6.8 s, 16:9, 16 cuts: botanical title sequence, Swiss-poster grid | one layout skeleton, cut every 0.4 s; crop marks, mono labels, stepped pixel masks | bed exactly 12 beats (6.72 s at 107.1 BPM) | swiss-style-motion |
| Dd6Uc27ssjp | VO tutorial, 35.1 s, 9:16 at 24 fps, 21 cuts: motion-plugin promo, stock tile grids | one tile set re-arranged per concept; 1-2 caption words per 5-8 frames | paired 0.6 s rise-and-fall sweeps (inferred) | vox-collage-design |
| DdCH-tFy7Wp | UI motion, 8.1 s, 1:1, 0 cuts: square comment-bait, cyan sky, cursor click | big-number hook; cursor-click CTA on white UI | 8-beat 3.04 s loop, scene change on the loop boundary | flat-2d-motion |
| DdY8V8XKJD6 | screen take, 22.5 s, 9:16, 0 cuts: SaaS promo shot off a monitor, stat tiles | gradient wipes as cuts; number roll with vertical blur | sub -33 dB for 0.85 s, then +33 dB at 14.05 s | glassmorphism-motion |
| Dd_t1ZhNAoR | VO explainer, 95.5 s, 9:16 at 20 fps, 29 cuts: freelance chat story | sentence per shot, 2-4 s; colour carries meaning; 3-step counters | 1-1.7 s mute then bass hit (8.6-10.33 s) | flat-2d-motion |
| DdjM8xRNzk_ | screen take, 25.4 s, 9:16, 1 cut: food-brand promo shot off a monitor | screen colour is the room light rig; flash-fill reveal | drone swells (bass +12, +9 dB) under flash fills; LRA 14.0 LU | none close; flat-2d-motion |
| DdwCXaQIHNU | reel, 15.1 s, 16:9, 16 cuts: motion-reel teaser, HUD furniture | one word per shot, 0.2-0.4 s, own colour each; a letter as portal | cuts on 0.25 s grid at 120 BPM; +3.1 dBTP (avoid) | swiss-style-motion |
| DeF8z3XoLdh | reel, 15.2 s, 16:9, 7 cuts: motion-reel teaser, Bauhaus primaries | recurring ball object; verb words animated as themselves | cuts on 0.5 s grid, hits 10-20 ms after | bauhaus-motion |
| DeMrHF6qi0z | lyric, 12.0 s, 9:16 with 16:9 window, 6 cuts: song-lyric collage, live-band footage | fixed header and footer; white silhouette mattes; tiles slide in with rotation and bounce | starts on a strong hit, no fade | pop-art-motion |
| DeO1Rh7x5Qm | UI motion, 21.2 s, 16:9 at 24 fps, 2 cuts: app teaser, type on green gradient | line per 1-2.5 s typed word by word; cards blur-to-sharp on 2-frame stagger | whole-mix dips (4.5, 8.5, 10.0 s), bass back +8 dB | glassmorphism-motion |
| DePvWkxNAun | VO explainer, 68.6 s, 9:16, 0 cuts: retro 1-bit window monologue | one visual alphabet; mosaic dissolves, not fades | voice is the clock; about 3 s room tail | pixel-art-motion |
| DeRpl8Yhrb2 | lyric, 377.9 s, 16:9, 17 cuts (72 shots): 6-minute lyric video, dot-grid type | particle dissolve as transition; one highlighted word per line | bass in = chorus picture; 3.47 s silence, then 14 cuts in 3.9 s | pixel-art-motion |
| DeSvnCQIgs3 | screen take, 10.3 s, 9:16, 0 cuts: logo reveal, phone shot of software window | shape-morph loop on a reflective floor | pull-back to -31 dB, then +23 dB at 1.97 s | y2k-chrome-motion |
| DeXDu86snYE | CG ad, 29.7 s, 9:16, 3 cuts: macro balloon-pop ad, HUD countdown | countdown over slow macro push; 0.4 s scan-line wipe to wireframe | music cut dead as narration starts (7.0-7.4 s) | none close; cinematography-for-ai |
| DeXtJrAtOcr | screen take, 12.6 s, 9:16, 0 cuts: launch-event parody, phone shot of laptop | slide rhythm about 1.5 s with macro dive | -45 dB pre-roll, then about +16 dB over 1.0-2.0 s | none close; cinematography-for-ai |
| DeY58dONeuY | UI motion, 16.1 s, 16:9, 1 cut: file-upload task in six UI states | each state morphs from the last shape; cursor leads each trigger by 0.3-0.5 s | sound on every state, trails picture by 0.15-0.7 s (avoid) | glassmorphism-motion |
| DeZ3P_8NeHT | VO tutorial, 63.1 s, 9:16, 12 cuts: talking head, painted intro, screen demos | three-world edit; screen top two thirds, speaker bottom third | voice only; cuts follow phrases | none close; explainer-documentary |
| DeZOFtEMkuA | UI motion, 12.4 s, 1:1, 1 cut: square editor pitch (sibling of DclkKscsRbs) | each scene wipes or morphs from the last object; blur-in words | sub dip at 3.5 s while highs stay; mono risk at 5.5 s | glassmorphism-motion |
| DeaJ4yUg95f | screen take, 26.5 s, 9:16, 0 cuts: music-app promo, colour-cycling room light | room light steps a fixed palette about every 1.5-2 s | excerpt trimmed to a hit: +42 dB at 2.0 s | none close; synthwave-motion |

## Find a reference by need

Frame counts assume 30 fps.

| need | ids | build |
|---|---|---|
| Single-take screen reel | Db28edFqHTP, DdY8V8XKJD6, DdjM8xRNzk_ | Film a display, not a render. Pill-to-card beat every 21-30 frames, held 9 or more [Db28edFqHTP]; gradient wipes as the cuts, a beat per 30-45 frames [DdY8V8XKJD6]; screen colour is the key light [DdjM8xRNzk_]. AE: pill and card as shape layers, animate size and roundness. |
| Light as pacing, no cuts | DeaJ4yUg95f, DdjM8xRNzk_ | Step the room hue through a fixed palette every 45-60 frames [DeaJ4yUg95f]; flood the desk with a full-screen colour flash at a story turn [DdjM8xRNzk_]. Post: a colour layer in Screen mode with hold keyframes. |
| Kinetic type | DdwCXaQIHNU, DcYXIWbxzAN, DeF8z3XoLdh | One word per shot, 6-12 frames, each on its own colour [DdwCXaQIHNU]; verb words play their own verb for 12-18 frames [DeF8z3XoLdh]; rebuild glyph strokes into a new shape, glow as a blurred copy plus an outline copy 1-2 frames behind [DcYXIWbxzAN]. |
| Word-by-word hierarchy | DcL6By1z4QE, DZCY6bjOsUQ | One word per 6 frames, each larger than the last, fading in over 3-4 frames [DZCY6bjOsUQ]; big noun plus tiny connector words [DcL6By1z4QE]. AE: text animator with Opacity and Scale, range selector by word. |
| Macro tension build | DeXDu86snYE, Dc0izivoZNw | Frame countdown stepping every frame over a push that grows the subject from 60% to 100% of frame width in 48 frames (AE Scale 100 to 167%), pop at about 23 s of 29.7 s [DeXDu86snYE]; macro key press with a thin focus plane [Dc0izivoZNw]. |
| UI morph chain | DeY58dONeuY, Dbmcud4IexE, DXzurbATRQT | Each state grows out of the last shape. One property per morph over 9-15 frames, ease-out with a settle, rotation to bridge a change in object count [Dbmcud4IexE]; cursor leads its trigger by 9-15 frames, 5-10 degree tilt then settle flat [DeY58dONeuY]. |
| Collage | DeMrHF6qi0z, DZCY6bjOsUQ, DcGaekAMU90 | Tiles slide in rotated 10-20 degrees and land with a bounce [DeMrHF6qi0z]; grid tiles stagger 2-4 frames [DcGaekAMU90]; a dark vignette travels between shots as the light [DZCY6bjOsUQ]. |
| Glitch edit | DZUZITfz0Qu, Dcs-MiOpO2V | 4-8 thin strips of the next shot, offsets re-randomised every 1-2 frames (a 12-15 fps stutter); 1-frame inverted copy on and off; blur the first frame after a cut and sharpen over 4-5 frames [DZUZITfz0Qu]; stepped pixel mask as a wipe [Dcs-MiOpO2V]. |
| Voice-over tutorial | DeZ3P_8NeHT, Dd6Uc27ssjp, DcGaekAMU90, DZCY6bjOsUQ, DePvWkxNAun | Screen in the top two thirds, speaker in the bottom third [DeZ3P_8NeHT]; 1-2 word captions, 5-8 frames each at 24 fps [Dd6Uc27ssjp]; cursor and UI chrome as the transitions [DcGaekAMU90]; cut on the first syllable of the next phrase [DZCY6bjOsUQ]; put big moves in the 0.3-0.5 s gaps (9-15 frames) [DePvWkxNAun]. |
| Beat-grid cutting | DeF8z3XoLdh, DdwCXaQIHNU, Dcs-MiOpO2V | At 120 BPM cut on 0.5 s (15 frames) [DeF8z3XoLdh] or 0.25 s multiples (7.5 frames, so place by time) [DdwCXaQIHNU]; trim the bed to whole beats: 12 beats = 6.72 s at 107.1 BPM [Dcs-MiOpO2V]. |
| Silence and drop | Db28edFqHTP, DclkKscsRbs, DeRpl8Yhrb2 | Remove the low end for 4 beats, return on the biggest picture change [Db28edFqHTP]; 0.27 s true silence before the biggest boom [DclkKscsRbs]; 3.47 s silence, then a loud re-entry [DeRpl8Yhrb2]. |
| Loudness | Db28edFqHTP, DdY8V8XKJD6, Dcs-MiOpO2V | -14.1 LUFS, peaks -5.1, -4.5, -3.5 dBTP; limiter ceiling -1 dBTP or lower, since 12 of 30 originals exceed 0 [avoid DdwCXaQIHNU, +3.1]. |
| Showreel, logo sting | DcOIGDdss_L, DeSvnCQIgs3 | 1-3 s pieces (30-90 frames), one full motion each, hard cuts on matching colour or direction, 3.4 s hold on the closing badge [DcOIGDdss_L]; shape-morph loop on a reflective floor [DeSvnCQIgs3]. |

## Where to read more

Base: `C:/Users/basha/Motion Design/Training Data/Instagram Refs/`. Open text with Grep `-n`, then Read with offset and limit; open images 3-4 per call.

- `DETAIL-batch-01.md`: `## <id>:` heading per reel, time table, takeaways. `STUDY-batch-01.md`: quick pass and cross-reel patterns.
- `meta.md`, `frames_data/EVENTS.txt`: duration, fps, hard cuts, shot list with change, still %, drift and zoom flags; `frames_data/<id>.csv` per frame.
- `sheets/<id>.jpg`: 12-frame sheet, read first. `dense/<id>_sNN.jpg`: labelled grids; `dense/<id>_TNN.jpg`: every frame around the biggest changes .
- `audio/parts/<id>.md`: nine sections, read 8 then 9. `audio/SOUND-STUDY-batch-01.md`: sections 7 and 8. Also `audio/<id>_summary.json`, `_onsets.csv`, `_cuts.csv`, `audio/spec/<id>_NN.jpg`.
- `<id>.mp4`: sources, extract frames with ffmpeg. `analysis-method.md` covers re-running the pipeline on new reels.

## Limits

The sample is 30 reels from one platform and one season, chosen from links the user sent. Cut counts come from a frame-difference detector. Camera, lens and roll figures in the sources are estimates from the picture. Tempo and key are inferred, and nobody listened to the reels: effect names are guesses from spectrograms. Cut-level sync percentages are weak evidence, since chance baselines run 44-72% at 3-6 onsets per second and many reels have 1 to 5 cuts. DeRpl8Yhrb2 was viewed in 7 of 26 sheets, so its picture notes are a sample. Delivered files were platform-encoded, so the loudness clustering (28 of 30 between -14.5 and -14.0 LUFS) may be delivery, not mixing choice.
