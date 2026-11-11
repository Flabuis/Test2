# Visual design in reels

Use this file when deciding how a reel looks: the style family, how many colours, where the light comes from, what the background is made of, how to lay out 9:16, 1:1 and 16:9, what stays fixed on screen, and how to critique a still frame. It comes from a frame-by-frame study of 30 short-form motion-design reels from one social platform in one season. Limits: the files were 720 px wide rips, so fine grain and small type were hard to judge; lens, light and colour values are estimates from the picture; hex codes are approximations quoted from the study notes; figures marked (measured) were taken from one frame per reel. Pacing, camera, transitions, type and sound have their own reference files, so this one covers the still picture. Numbers in "Build" lines are starting points to tune, not measurements.

## 1. Style families

Rule: pick one family per reel and hold it. Mix looks only when each has a job and a constant binds them (section 6): an illustrated intro for attention, a speaker for trust and screen recordings for proof [DeZ3P_8NeHT, a tutorial reel]; white scrapbook for the pitch, black stage for the problem, blue sky for the how-to [Dd6Uc27ssjp, a plugin promo]; range shown on purpose [DcOIGDdss_L, a showreel].

| Family | What defines it | Reels | Closest skill |
|---|---|---|---|
| Dark-mode glass UI | Black stage, dark glass cards with a thin light edge, soft coloured radial glow behind each object, blue default and green on success, cursor-led states | DeY58dONeuY (file-manager UI), DXzurbATRQT (UI-motion promo), DclkKscsRbs and DeZOFtEMkuA (1:1 pitches), Db28edFqHTP and DdY8V8XKJD6 (glass cards on mesh gradient) | glassmorphism-motion |
| Swiss and Bauhaus geometry | Flat colour fields, grid with crop marks and mono labels, wide or heavy grotesque, primaries, one dominant colour per shot | Dcs-MiOpO2V (botanical title sequence), DeF8z3XoLdh (primaries teaser, isometric cube field), DdwCXaQIHNU (HUD teaser, heavy grotesque on flat fields) | swiss-style-motion, bauhaus-motion, isometric-motion; neo-brutalism-motion for DdwCXaQIHNU |
| Paper collage and duotone | Cream or grey paper, B&W or duotone cutouts, halftone, soft contact shadows, torn bits, hand-drawn marks | DZCY6bjOsUQ (statue promo), DcL6By1z4QE (duotone explainer), DeMrHF6qi0z (lyric collage), Dd6Uc27ssjp, Dd_t1ZhNAoR (chat-story explainer) | vox-collage-design, risograph-motion, pop-art-motion |
| Neon kinetic type | Near-black ground, one neon hue, glow plus a thin white outline echo, faint reflective floor | DcYXIWbxzAN (greeting type), DeSvnCQIgs3 (logo reveal on reflective floor) | y2k-chrome-motion, synthwave-motion |
| Pastel 3D and macro | Soft studio light, glossy plastic or latex, very shallow focus, 20-24 mm rooms and 85-100 mm macro (estimates) | Dc0izivoZNw (3D course trailer), DeXDu86snYE (balloon macro, dark stage), DeXtJrAtOcr (keynote-style launch parody, off-white) | clay-3d-motion, cinematography-for-ai |
| Retro-OS 1-bit line art | Black void, white window line art with double border and drop shadow, one warm accent | DePvWkxNAun (retro-OS monologue) | pixel-art-motion, line-art-motion |
| Flat icon and glossy sticker | Pale ground, flat icons with one saturated accent each; or sky gradient with rounded white type | Dbmcud4IexE (icon morph chain), DdCH-tFy7Wp | flat-2d-motion |
| Particle-dust lyric video | Dark ground, gold on dark, one dot-grid texture on the sampled scenes, particle dissolves | DeRpl8Yhrb2 (lyric video) | particle-motion, pixel-art-motion |

Key (median per-frame luma, whole frame, computed from frames_data): 9 sit below 70 [DXzurbATRQT, DcYXIWbxzAN, DdjM8xRNzk_, DdwCXaQIHNU, DePvWkxNAun, DeRpl8Yhrb2, DeSvnCQIgs3, DeXDu86snYE, DeY58dONeuY], 7 sit above 170 [DZCY6bjOsUQ, Dbmcud4IexE, DcGaekAMU90, DcL6By1z4QE, DclkKscsRbs, DdCH-tFy7Wp, DeZOFtEMkuA], 14 sit between (phone-shot reels land mid because a bright screen sits in a dark room). Choose dark or light key first; lighting follows from it.

Build: set the key first (comp background and the master colour theme), load the closest style skill from the table before designing frames, and build the key frame stills before animating.

## 2. Palette discipline

1. One accent hue on a neutral ground (black, white or cream). 12 reels read this way (my reading of the notes) [DZCY6bjOsUQ red, DcYXIWbxzAN mint, DdjM8xRNzk_ orange, DePvWkxNAun red-orange, DeXDu86snYE orange, DeO1Rh7x5Qm green, Dd_t1ZhNAoR magenta, Dcs-MiOpO2V red, DdY8V8XKJD6 blue, DcL6By1z4QE indigo duotone, DeRpl8Yhrb2 gold, DeY58dONeuY blue].
2. Spend the accent on the punch word or beat only: one key word per line in red or yellow [DeRpl8Yhrb2]; accent on key words, underlines and buttons [Dd_t1ZhNAoR]; key phrase in orange [DeXDu86snYE]; red-orange saved for check badges, the glow and the closing question [DePvWkxNAun]; red serif punch words on cream [DZCY6bjOsUQ].
3. Multiple hues work only by assignment: one dominant colour field per shot, hard cut [DeF8z3XoLdh, DdwCXaQIHNU gives every word its own ground]; a fixed brand set owned by the subject [DeSvnCQIgs3]; one brand hue present in every segment while chapters take their own colours [DcGaekAMU90]; a looping room hue [DeaJ4yUg95f]; one accent per icon on a pale ground [Dbmcud4IexE].
4. Mixed sources get one tint: duotone [DcL6By1z4QE, DeMrHF6qi0z] or B&W [DZCY6bjOsUQ]. DcL6By1z4QE also shares one shadow direction.
5. Background mood marks chapters: black, light blue, white [DclkKscsRbs, DeZOFtEMkuA]; white, green mat, black, pink grid, red wall [Dd_t1ZhNAoR]; a dark-to-light theme flip on a single glow burst [DXzurbATRQT, 14.4-14.8 s].

Colour as meaning:

| Colour | Means | Reels |
|---|---|---|
| Green | success, sent, OK | DeY58dONeuY (card edge, pill and check turn green), Dd_t1ZhNAoR (sent bubbles) |
| Red, red-orange | loss, rising tension, the emotional beat | Dd_t1ZhNAoR (money lost), DeXDu86snYE (countdown turns white to red near impact), DePvWkxNAun |
| Blue | neutral action, default UI | DeY58dONeuY |
| Magenta, violet | emphasis | Dd_t1ZhNAoR, DcGaekAMU90, DeZ3P_8NeHT (keyword in the call to action) |
| Warm vs cool light | menace vs tenderness; green and gold for turning points | DeRpl8Yhrb2 |

Hex approximations from the notes (read from the picture): cream #F3EDE0 [DZCY6bjOsUQ]; brand violet #7A00FF [DcGaekAMU90]; magenta-violet #B000FF [Dd_t1ZhNAoR]; mint neon #3CF0A8 [DcYXIWbxzAN]; red #C8102E [Dcs-MiOpO2V]; burnt orange #F04E23, acid lime #C8F73A, indigo #6C63FF [DdwCXaQIHNU]; radial centre #D9DBFF to deep indigo corners [DcL6By1z4QE]. Sample other values from a reference frame.

Build: define the palette as 1 neutral ground, 1 accent, optional semantic colours, as a theme object (GSAP/Remotion) or labelled colour controls on a master null (After Effects). For duotone use Tint (Map Black To dark indigo, Map White To pale lavender) on every cutout, then one shared drop shadow.

## 3. Lighting

| Rule | Evidence | Build |
|---|---|---|
| The screen is the key light in phone-shot reels; when screen mood changes, the room changes | Screen spills a pink cast on wall and tablet [Db28edFqHTP]; orange or white screen floods keyboard and desk, maroon turns the desk warm brown [DdjM8xRNzk_]; blue-lavender display [DdY8V8XKJD6] | Duplicate the screen precomp, scale up, large Fast Box Blur, Add or Screen over the room layer, opacity linked to screen brightness |
| Practicals are few: one hard white LED bar, one coloured strip or glow at the base | Light bar plus red curtain glow at the bottom [Db28edFqHTP]; bar, purple LED strip [DdY8V8XKJD6]; amber backlight, red fan-LED glow, white bar [DdjM8xRNzk_] | Two thin glow layers, not more |
| Room hue can be the metronome | Hue moves about every 1.5-2 s through blue, violet, magenta, red, warm grey, teal, cyan on a 9-10 s loop, no cuts [DeaJ4yUg95f] | Colour solid in Overlay or Color mode, Hue/Saturation Master Hue expression `(time/9.5)*360` or a keyframed palette |
| A moving vignette is a light | Dark corners travel lower left, top left, top right between shots; inverts to black with a lighter central beam at 7.7-9.1 s; a diagonal light wedge opens the reel [DZCY6bjOsUQ]; vignette grows from corners as green deepens [DeO1Rh7x5Qm]; heavy vignette on radial gradient [DcL6By1z4QE] | Black solid, elliptical mask, large Mask Feather, keyframe mask position per shot (CSS radial-gradient with GSAP in HyperFrames) |
| Glossy objects get a rim and a hot specular streak on a near-black stage | Soft rim at the top edge, tiny white specular; rim ring turns white at maximum stretch [DeXDu86snYE]; chrome blobs reflect orange and blue studio lights [DdwCXaQIHNU]; glossy red blob with highlight [DeF8z3XoLdh]; glossy lavender key under soft studio light [Dc0izivoZNw] | Blender: black world, large area light behind and above as rim, one small strip light for the streak |
| In 2D, glow stands in for light | Glow is a blurred copy of the stroke, with a white outline echo 1-2 frames behind [DcYXIWbxzAN]; radial glow behind each UI object, green on success [DeY58dONeuY]; warm halo behind one character floods the floor [DePvWkxNAun]; orange glow at the bottom edge [DclkKscsRbs]; blue floor glow [DeZOFtEMkuA] | After Effects Glow, or duplicate, Gaussian Blur, Add; echo copy time-offset 2 frames. CSS: stacked `drop-shadow`, blurred duplicate with `mix-blend-mode: screen` |
| People and locations: one side key with soft practicals, or a graded look | Key from camera-left, lamp and window soft behind, about 85 mm f/2 look [DeZ3P_8NeHT]; warm window light, 50 mm look [DeO1Rh7x5Qm]; red backlight with green-teal fill [DeMrHF6qi0z]; warm highlights, teal shadows, lifted blacks [DZUZITfz0Qu] | Lens and focal-length figures are estimates; see cinematography-for-ai |
| One shadow direction, soft contact shadows | Top-down plane, every cutout shadow to the lower right, objects land on soft contact shadows [DcL6By1z4QE]; soft drop shadows on cutouts [DZCY6bjOsUQ]; big soft shadows on paper cards [DeO1Rh7x5Qm] | One shared drop shadow preset, same angle on every layer |

Light follows emotion: torch-orange for menace, aurora green and sunrise gold for turning points, cool navy for tenderness, monochrome for grief [DeRpl8Yhrb2]. Flash and colour-flood frames were scored with a sub hit, swell or noise wash in these three reels [DcYXIWbxzAN, DdjM8xRNzk_, Dbmcud4IexE]; see the sound reference.

## 4. Backgrounds, texture, grain, gradient, floor

1. The ground is one constant surface, not a fill. A pink-orange-lavender mesh gradient is the single constant under every beat [Db28edFqHTP]; a radial gradient from light centre to deep indigo corners [DcL6By1z4QE]; mint-to-forest gradient with bokeh blobs and drifting gradient clouds [DeO1Rh7x5Qm]; cyan sky gradient with soft halftone dots and cloud sprites [DdCH-tFy7Wp]; blurred gradient blobs [DXzurbATRQT]. Build: animate the gradient slowly (stops or blob positions) so the ground lives; Remotion or CSS: layered radial-gradients with moving positions.
2. Paper and desk surfaces say "handmade": cream or warm grey paper [DZCY6bjOsUQ, DeMrHF6qi0z, Dd6Uc27ssjp, DeZ3P_8NeHT] with handwriting or hand-drawn marks on top [Dd6Uc27ssjp, DeMrHF6qi0z]; green cutting mat shot top-down [Dd_t1ZhNAoR, DcGaekAMU90]; pink grid sheet for diagrams [Dd_t1ZhNAoR]; pale grid with guide lines and small red registration dots [Dcs-MiOpO2V].
3. One binding texture across all assets. A single dot-grid on portraits, silhouettes and type keeps anime stills, 3D type and photo elements in one style (seen in the sampled sheets, 7 of 26) [DeRpl8Yhrb2]; halftone [Dcs-MiOpO2V, DeMrHF6qi0z]. Fine film grain was explicit in one reel only [DcL6By1z4QE]; whether others carry grain is unknown at this resolution. Build: Color Halftone or a dot-grid overlay at low opacity; Add Grain over the final comp.
4. Floors give 2D depth. A faint reflective floor line at the lower third [DcYXIWbxzAN]; wordmark on a reflective floor, reflection drifting 4 px sideways [DeSvnCQIgs3]; windows mirrored on a floor with dust at the base and a particle horizon line [DePvWkxNAun]. Build: duplicate, flip vertically, gradient-matte fade, slight blur, offset below the baseline.
5. Skies and stages are sets: blue sky with clouds as the how-to set [Dd6Uc27ssjp], hook set [DdCH-tFy7Wp]; black stage [DeXDu86snYE] with a per-object glow [DeY58dONeuY].

## 5. Layout by format

Sample: 18 reels are 9:16 (720x1280), 9 are 16:9 (about 1280x720), 3 are 1:1 (720x720). Build at 1080x1920, 1920x1080 and 1080x1080 and place by percentage of height so the figures below scale. No platform safe-zone figures were recorded in the sources; the observed text positions below show what these reels did.

| Format | Rules and evidence |
|---|---|
| 9:16 phone shot of a screen | Three bands (measured): dark wall about 0-33% carrying the fixed caption and a light bar, display about 35-74%, tablet and desk about 74-100% [Db28edFqHTP, DdY8V8XKJD6 similar, display about 30-73%]. Top of the fixed caption at about 11%, 18%, 20% and 23% of height (measured) [DeSvnCQIgs3, DeaJ4yUg95f, DdY8V8XKJD6, Db28edFqHTP]. A bottom caption sits at about 66-70% (measured) [DeXtJrAtOcr], leaving the lowest 30% free of caption text. Handheld about 26 mm look [Db28edFqHTP, DdjM8xRNzk_], slight keystone [DdjM8xRNzk_]. Keep UI type large and enter text only after the previous element leaves [Db28edFqHTP]. Real application panels around the comp read as work in progress [DeSvnCQIgs3]. |
| 9:16 picture window | Fixed black header, centred window, caption pill below. Measured: window 720x540 (4:3, not 16:9 as the study notes say), y 370-910, equal 370 px black above and below, header label at about 25-27%, pill at about 73-78% [DeMrHF6qi0z]. |
| 9:16 stacked panels | Two 16:9 panels, each about 720x403, 4 px gap, y 212-1021 (17%-80%), black above and below, small pill label top-left of each (measured) [Dc0izivoZNw]. Speaker plus screen split: screen recording on the upper two thirds, speaker in the bottom third so the face is never lost [DeZ3P_8NeHT]. |
| 9:16 caption systems | Same-size lowercase captions mid-frame, one or two words [Dd6Uc27ssjp]; mono pixel caps near mid-frame, about 49-57% of height in two measured frames, although the study note says about 70% [DeZ3P_8NeHT]. |
| 16:9 | HUD furniture: corner brackets, tiny mono readout, crosshair circles [DdwCXaQIHNU]; bottom-right progress bar and section label [DeF8z3XoLdh]; type cropped by the frame edge on purpose [Dcs-MiOpO2V, DcGaekAMU90]. |
| 1:1 | Centre-stacked scenes: one headline, one pill or card, one cursor; backgrounds as chapters (black, light blue, white) [DclkKscsRbs, DeZOFtEMkuA, DdCH-tFy7Wp]. |

Framing UI inside a physical screen: keep the physical frame (tablet, light bar, LED strip) identical across the take [DdY8V8XKJD6], and leave margin inside the screen for handheld drift, which was about 10 px sideways and 12 px upward in two takes [DdY8V8XKJD6, Db28edFqHTP]. Build: corner-pin the UI over footage, or shoot a real display.

## 6. Constants that hold a reel together

Rule: choose one to three things that never move and let everything else change. 12 reels carry fixed furniture for most or all of the run [DZCY6bjOsUQ, Db28edFqHTP, DdY8V8XKJD6, DeSvnCQIgs3, DeaJ4yUg95f, DeXtJrAtOcr, DeMrHF6qi0z, Dc0izivoZNw, DdwCXaQIHNU, DeF8z3XoLdh, Dcs-MiOpO2V, DXzurbATRQT from 14.8 s]; DeXDu86snYE holds its HUD until about 7.2 s.

| Constant | Evidence |
|---|---|
| Fixed caption or footer | Name footer on every frame [DZCY6bjOsUQ]; top captions in the phone shots (section 5); footer from 14.8 s [DXzurbATRQT] |
| HUD furniture | Brackets, readout, crosshairs [DdwCXaQIHNU]; progress bar [DeF8z3XoLdh]; REC dot, lens label, countdown [DeXDu86snYE]; grid, crop marks, mono labels on every image [Dcs-MiOpO2V] |
| Fixed frame | Header, window and pill [DeMrHF6qi0z]; stacked panels [Dc0izivoZNw] |
| Recurring object | One ball reused as title letter, tunnel portal, grid centre, jelly blob, helix core and sun [DeF8z3XoLdh]; eye-window and glowing pencil [DePvWkxNAun]; wire-and-dot motif [DXzurbATRQT] |
| Template | Chapter cards change only colour and number [DcGaekAMU90]; pill chips in the last third [DcOIGDdss_L]; terminal card at start and end [DeRpl8Yhrb2] |
| Shared treatment | One tint and one shadow direction [DcL6By1z4QE]; one dot-grid [DeRpl8Yhrb2] |

Build: put furniture on the top layer or an untouched precomp, outside time-remapping (After Effects); outside per-scene timelines in GSAP; outside `<Sequence>` in Remotion.

## 7. Critique checklist for a still frame

1. Name the ground in one word. Is it a neutral or a single gradient? (section 4)
2. Count hues beyond the ground. More than one needs an assignment: one field per shot, a brand set, or semantic meaning (section 2).
3. Is the accent on the one punch element only?
4. Point at the light: screen, travelling vignette, rim, or glow. Do all shadows fall one way? (section 3)
5. Is there one binding texture or tint across assets? [DcL6By1z4QE, DeRpl8Yhrb2]
6. Hierarchy: one big word with tiny connector words, sizes escalating? [DZCY6bjOsUQ, DcL6By1z4QE]
7. Is furniture in the same place as the previous frame? Any element that drifts without a reason?
8. Caption text clear of the lowest 30% in 9:16 [DeXtJrAtOcr, DeSvnCQIgs3], and type cropped by an edge only on purpose?
9. Colour meaning intact: green not used for loss, red not used for success?
10. UI state: one state per beat, and is the cursor or trigger visible before the change? [DeY58dONeuY]
11. Depth: does text sit behind a 3D object when it should, with contact shadows under grounded objects? [Dc0izivoZNw, DcL6By1z4QE]

Evidence limits: 30 reels, one platform, one season; cross-reel counts are readings of the study notes, so treat them as tendencies.
