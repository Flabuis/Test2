# Transitions catalogue

Use this file to choose, time and build the transition between two beats of a reel. It catalogues 16 transition families seen in 30 reels from one social platform in one season, with duration in frames at 30 fps, reel ids with timestamps, a build recipe (After Effects, GSAP/HyperFrames, Remotion) and when to leave it out, then a decision table and rules on density, motivation and consistency. Limits: timings come from frame sheets read at about 5 fps plus every frame around big changes, converted to 30 fps from reels made at 20, 24 and 25 fps, so very fast transitions are inferred; build values (blur size, expressions) are starting points, not measurements; "Avoid" lines are inference. Descriptors are in the key at the end. Related: `*-motion` skills, `cinematography-for-ai`, `sound-design.md`.

## Density first (computed from meta.md and EVENTS.txt)

- 8 of 30 reels have no hard cut and 16 (including those 8) have two or fewer. The 8: Db28edFqHTP, DcL6By1z4QE, DdCH-tFy7Wp, DdY8V8XKJD6, DePvWkxNAun, DeSvnCQIgs3, DeXtJrAtOcr, DeaJ4yUg95f.
- 6 reels average 0.6 to 1.5 s per shot: Dcs-MiOpO2V, DcOIGDdss_L, DdwCXaQIHNU, DeMrHF6qi0z, DZUZITfz0Qu, Dd6Uc27ssjp. They use hard cuts plus a bridge of 1 to 7 frames.
- All 30: median 0.09 hard cuts per second, median per-reel mean shot 3.2 s. The detector counts flashes as cuts (DZUZITfz0Qu has 11 shots, not 26).

## Catalogue

### 1. Blur ramp (blur-in on the cut frame, cross-blur)
- **Frames:** the first frame after a cut, or an arriving word or card, starts blurred and sharpens in 3 to 6 frames [DZUZITfz0Qu 2.94, 4.77 s; DZCY6bjOsUQ 5.4 s; DeZOFtEMkuA 1.0 s]; 12 for a whole card [Db28edFqHTP 6.6 s]. Cross-blur overlaps blur-out and blur-in [Db28edFqHTP 2.4 s].
- **Build:** AE Gaussian Blur (Repeat Edge Pixels), `ease(time-inPoint,0,5*thisComp.frameDuration,40,0)`. GSAP `blur(24px)` to `blur(0px)`, `5/30`, `power2.out`. Remotion `interpolate(frame,[0,5],[24,0],{extrapolateRight:"clamp"})`.

### 2. Flash, white-out and strobe
- **Frames:** a hit flash is 1 to 3 [DdwCXaQIHNU 8.0, 10.0, 13.0 s; DcYXIWbxzAN 0.03 s; Dcs-MiOpO2V 1.53 s]; 6 to 12 when it carries a flip [DdjM8xRNzk_ 4.8 s orange fill; DXzurbATRQT 14.4 to 14.8 s dark to light; Dc0izivoZNw 8.3 s]. Strobe: invert on alternate frames for 9 [DZUZITfz0Qu 1.17 s]; three recolours in 5 [DZUZITfz0Qu 6.94 s]; 2-frame colour blink between chapter cards [DcGaekAMU90 15.7 s].
- **Build:** AE white solid, opacity 0-100-0 over 2 frames, or Exposure ramp plus Glow over 6 to 12; strobe is Invert with opacity `Math.floor(time/thisComp.frameDuration)%2*100`; CSS `filter:"invert(1)"` on `frame%2`.
- **Avoid:** one on every cut; calm reels spend one to three [DXzurbATRQT 6.6, 14.4 s]; strobe is the main language only in [DZUZITfz0Qu].

### 3. Glitch strip displacement
- **Frames:** 4 to 8 horizontal bands carry the next shot, inverted and colour-shifted, repositioned every 1 to 2 frames (12 to 15 fps stutter) for 2.5 s up to the cut, the next shot rising from below for the last 4 frames; later bursts last 5 to 6 [DZUZITfz0Qu 0.4 to 2.9, 5.6, 6.9 s]. Accents of 1 to 10 frames: pixel-sort smear [DeMrHF6qi0z 4.6 s; DcOIGDdss_L 26.0 s], letter scramble into a logo [DeO1Rh7x5Qm 18.1 s].
- **Build:** AE 4 to 8 strips (rectangular masks, feather 0) of the next shot, Invert, x `posterizeTime(15); random(-300,300)`; or Displacement Map from stripe noise. GSAP stacked `clip-path: inset()` copies moved on 2-frame steps.
- **Avoid:** UI, SaaS and explainer reels.

### 4. Mask wipe in the shape of the next scene
- **Frames:** a shape opens a window on the next scene or morphs into another: circle held about 24 frames, then circle to X in 12 [DZUZITfz0Qu 3.4 to 4.6 s]; shard mask 6 [DeMrHF6qi0z 3.0 s]; pixel staircase 5 and rectangle 2 [Dcs-MiOpO2V 1.87, 0.8 s]; circle wipe 10 [DeZ3P_8NeHT 20.0 s]; a letter's hole opens into the next scene [DdwCXaQIHNU 3.6 s]; silhouette mattes over live footage [DeMrHF6qi0z 6.6 to 8.8 s].
- **Build:** AE next scene under a shape layer used as Alpha Matte, Scale 0 to 150% ease-out in 6 to 12 frames; shape to shape with Path keys, equal vertex counts, Set First Vertex. Remotion `clipPath` with `interpolatePath`; GSAP MorphSVGPlugin.
- **Avoid:** shapes the design lacks; the examples borrow the shape from the content.

### 5. Bar, barcode and slice wipes; colour wash and gradient wipe
- **Frames, bars:** vertical bars slide up for 7 frames then resolve with 4 to 6 px jitter, 22 in all [DZUZITfz0Qu 8.0 s]; block, bar, diagonal slash, pill in 18 [DdY8V8XKJD6 13.6 s]; band 6 [DdjM8xRNzk_ 18.6 s]. **Wash:** gradient floods and drains in 12 [DXzurbATRQT 1.6 s]; 12 per swap [DcGaekAMU90 38.7 s]; 6-frame wipe to white [DeZOFtEMkuA 2.2 s]; standing in for cuts [DdY8V8XKJD6 6.2, 7.8 s].
- **Use:** in no-cut shots the wash is the cut. **Build:** AE Venetian Blinds, or Linear Wipe (feather 150 to 300 px) on a colour ramp, 0 to 100 in 12 frames ease in-out; GSAP `clip-path: inset()` on a gradient div.
- **Avoid:** off-palette colour (all use the accent hue).

### 6. Shape morph and match cut by shape
- **Frames:** one property at a time, 9 to 15 frames, ease-out with a settle, then about 1 s hold, no hard cut in 104 s [Dbmcud4IexE]; circle to square to star in 12 [DXzurbATRQT 4.2 s]; letter to ribbon in 6 [DeSvnCQIgs3 1.6 s]; letter O to portal to dot field [DdwCXaQIHNU 3.2 to 4.6 s]; one ball reused as letter, tunnel, blob, sun [DeF8z3XoLdh]. Links are geometric echoes; rotation bridges a change in object count [Dbmcud4IexE 18.3 to 22.0 s].
- **Build:** AE Path keys with equal vertex counts, Merge Paths, Trim Paths; colour as a separate 4-frame key; overshoot expression. GSAP MorphSVGPlugin; Remotion `interpolatePath` with `spring`. See `flat-2d-motion`.
- **Avoid:** objects with no shared geometry; keep the ground muted so one accent reads [Dbmcud4IexE].

### 7. UI state morph (button to menu to dialog)
- **Frames:** each state grows from the last one's shape in 12 to 18 frames: capsule to button (18), press squash, tilt into a menu card, then square, dialog, progress card, pill, check; six states, 1.2 s success hold [DeY58dONeuY 2.4 to 12.4 s]. The cursor arrives 9 to 15 frames before its trigger [DeY58dONeuY, DeZOFtEMkuA, DclkKscsRbs].
- **Build:** AE one rounded rectangle, animate Size and Roundness, X/Y tilt 5 to 10 degrees settling to 0, content blurs in 6 frames after the container. Remotion `spring`, `interpolateColors`.

### 8. Text to waveform; letters to object
- **Frames:** type blurs, spreads, compresses into a waveform [DeaJ4yUg95f 1.8 to 3.2 s]; letters become a hand in 22, explode for 24, reassemble in 12 [DcYXIWbxzAN 1.2 to 4.6 s]; a streak unrolls into a wordmark in 12 [DeSvnCQIgs3 8.2 s]; letters fall in from -30/+40 degrees in 12 [DdwCXaQIHNU 13.2 s]; text to particles to a globe, 60 [DeRpl8Yhrb2 62 s].
- **Build:** AE Create Shapes from Text then Path morph; Wave Warp; per-letter Animator. GSAP SplitText plus stagger; Remotion per-letter `spring`. See `typography`.
- **Avoid:** text unrelated to the subject.

### 9. Mosaic, particle and shatter dissolve
- **Frames:** pixelate-in 3 to 4 frames per object [DcL6By1z4QE 0.67, 6.7, 16.3 s]; cloud to pixel mass in 30, wall to squares in 21 [DePvWkxNAun 5.7, 51.0 s]; every change is dots, dust or sparks, 20 to 60 [DeRpl8Yhrb2 62, 304 s]; shatter into fragments in 19, the pitch-to-product hinge [Dd6Uc27ssjp 14.2 s]; collapse to a dot in 12 [DdY8V8XKJD6 19.2 s].
- **Build:** AE Mosaic blocks 8 to 200 for an arrival, or Block Dissolve; Particular or CC Particle World; Shatter. See `particle-motion`, `pixel-art-motion`.

### 10. Whip pan, blur slide and crash zoom
- **Whip:** 5 frames, tilted 20 degrees [Dc0izivoZNw 3.0 s]; 6 [DclkKscsRbs 4.2 s]; 7 [DZUZITfz0Qu 7.8 s]; into macro, tunnel, eye [DcOIGDdss_L 14.3, 34.3, 42.3 s]; blur slides, 19 [DcGaekAMU90 79.4 s]. **Crash zoom:** 3 frames [Dcs-MiOpO2V 0.83 s]; 6, landing inside a ball [DeF8z3XoLdh 1.8 s]; 6 on type [Dc0izivoZNw 22.7 s]; 29 into a glyph [DcGaekAMU90 19.5 s]; 12-frame dive [DeXtJrAtOcr 8.4 s].
- **Build:** AE Motion Tile (Mirror Edges), Position ease in-out, Directional Blur peaking mid-move, cut at the peak; crash zoom: Scale 100 to 400%, Continuously Rasterize, Radial Blur (Zoom).
- **Avoid:** reels with no camera use neither [DXzurbATRQT, Dbmcud4IexE].

### 11. Card through depth and 3D tilt
- **Frames:** panels tilt 5 to 10 degrees and settle [DeY58dONeuY]; a tunnel of tilted cards, camera push 6 to 8% per second plus roll for 3.8 s, text swapped in place by 12-frame cross-fade [DZCY6bjOsUQ 14.0 s]; card slides off with a 3D tilt [DXzurbATRQT 9.0 s]; cards fan out in 12 [DdY8V8XKJD6 15.6 s]; mock-up rushes the lens in 24 [DeXDu86snYE 16.2 s].
- **Build:** AE 3D layers, one camera (Z ramp for tunnels), Camera Lens Blur; tilt 8 degrees to 0 in 12 frames. CSS `perspective(1200px) rotateY(8deg)`.

### 12. Push, slide, replacement and tile cascade
- **Replacement:** the old object leaves as the new arrives, no cut for 52 s [DcL6By1z4QE]; pill out left, new in right with 8 degrees of rotation [DXzurbATRQT 19.0 s]; object exits up as another rises [DZCY6bjOsUQ 10.8 s]; slide 15 px per frame, ease-out [Db28edFqHTP 9.2 s]; windows tumble in 10 [DePvWkxNAun 15.3 s]. **Cascade:** items 2 to 4 frames apart [DcGaekAMU90 80.6 s; DcOIGDdss_L 2.3 s; DdwCXaQIHNU 10.2 s; DeO1Rh7x5Qm 11.5 s]; ripple by distance from the centre [DeF8z3XoLdh 4.2 s]; one tile set as grid, sphere, ring [Dd6Uc27ssjp 22.5 s].
- **Build:** AE start the new move 3 to 6 frames before the old ends; `index*2*thisComp.frameDuration` or Card Wipe. GSAP `stagger:{each:2/30,from:"center"}`; Remotion `<Sequence from={i*2}>`.
- **Avoid:** dead frames (the next move starts before the last ends); unify unrelated cutouts with one tint and shadow direction [DcL6By1z4QE].

### 13. Page curl, paper fold, scan-line wireframe reveal (one reel each)
- **Frames:** corner peel 12 [DcGaekAMU90 34.5, 36.8 s]; sheet folds in 6 [DeO1Rh7x5Qm 0 s]; a scan line sweeps top to bottom in 12 turning the render to wireframe, back in 12 [DeXDu86snYE 11.6, 14.4 s].
- **Build:** AE CC Page Turn (Back Page = next layer); scan: beauty and wireframe renders, Linear Wipe 0 to 100 in 12, glow line at `linear(effect("Linear Wipe")("Transition Completion"),0,100,0,thisComp.height)`. Torn paper: `vox-after-effects-recipes`.

### 14. Countdown and counter steps
- **Frames:** digits 6 frames apart [DdwCXaQIHNU 1.6 s]; frame counter 211 to 001 stepping one unit per frame, red from 043, pop at 23.0 s [DeXDu86snYE]; three price steps, a glow each [Dd_t1ZhNAoR 28.7 s].
- **Build:** AE Source Text `n=Math.max(1,211-Math.floor((time-inPoint)/thisComp.frameDuration)); ("000"+n).slice(-3)`; count-up `Math.round(linear(time,t0,t1,0,248))`.

### 15. Colour-field cut, theme flip, light-colour cycle
- **Frames:** one word per shot on its own colour, 0.2 to 0.4 s [DdwCXaQIHNU 2.4 s]; verbs on single colour fields, 0.4 to 0.6 s [DeF8z3XoLdh 8.0 s]; chapter cards swap only colour and number, held 0.9 to 1.1 s [DcGaekAMU90 15.7 s]; dark to light on a glow burst [DXzurbATRQT 14.4 s] or a whip-cut [DclkKscsRbs 4.2 s]; room light steps a hue every 1.5 to 2 s on a 9 to 10 s loop, no cuts [DeaJ4yUg95f].
- **Build:** AE solid, Fill colour keys on hold; room light as a coloured Screen or Add solid keyed every 45 to 60 frames. Remotion `interpolateColors`.
- **Avoid:** colour changes with no constant: violet [DcGaekAMU90], HUD [DdwCXaQIHNU, DeF8z3XoLdh].

### 16. Plain hard cut (hold, black, phrase start)
- **Frames:** cut after a 0.5 to 1.1 s hold [DZCY6bjOsUQ 2.37, 5.3 s]; pure black with only text [DZCY6bjOsUQ 19.7 s]; matching colour or movement direction [DcOIGDdss_L]; hard cut to black as the last frame [DeSvnCQIgs3 10.0 s] or between sections [DcOIGDdss_L 10.0 s]; cut on a phrase's first syllable, 9 of 11 within 80 ms against 53% by chance [DZCY6bjOsUQ].
- **Build:** freeze the last frame (Time Remap) for the hold, cut on the voice onset; add a blur-in (1) or flash (2) only for a bridge.

## Decision table: what are you changing?

| Changing | Use | Frames | Reels |
|---|---|---|---|
| Scene, cutting format | Hard cut plus one bridge: blur-in, whip, flash | 1 to 7 | DZUZITfz0Qu, DZCY6bjOsUQ, DcOIGDdss_L |
| Scene, continuous format | Replacement with overlap, or mosaic/particle dissolve | 3 to 6; 12 to 60 | DcL6By1z4QE, DePvWkxNAun, DeRpl8Yhrb2 |
| Object | Shape morph, match cut, letters to object | 9 to 15 | Dbmcud4IexE, DXzurbATRQT, DcYXIWbxzAN |
| State | UI state morph, cursor first | 12 to 18 | DeY58dONeuY, DeZOFtEMkuA |
| Mood or theme | Flash flip, colour-field cut, light cycle | 6 to 12; 45 to 60 per hue | DXzurbATRQT, DeaJ4yUg95f, DdjM8xRNzk_ |
| Section | Chapter-card blink, shatter | 2; 19 | DcGaekAMU90, Dd6Uc27ssjp |
| A beat that must hit | Flash, strobe, crash zoom, cut on a phrase start | 1 to 9 | DdwCXaQIHNU, DZUZITfz0Qu |

## Rules: density, motivation, consistency

1. Pick the density tier first (section above). Fast tiers use 1 to 7 frame bridges; slow tiers use 12 to 18 frame in-frame moves.
2. One bridge per cut (inferred from the cutting reels). The one exception stacks glitch, strobe and mask, a change on nearly every third frame [DZUZITfz0Qu].
3. Hold after every transition: 0.3 s minimum [Db28edFqHTP], about 1 s per icon [Dbmcud4IexE], 0.9 to 1.1 s per chapter card [DcGaekAMU90], 1.2 s on success [DeY58dONeuY].
4. In no-cut formats a new beat every 0.7 to 1.5 s [Db28edFqHTP, DdY8V8XKJD6]; explainers swap objects every 3 to 4 s [DcL6By1z4QE].
5. Save the biggest transition for the hinge: 44% of runtime [DXzurbATRQT 14.4 of 32.9 s], 40% [Dd6Uc27ssjp 14.2 of 35.1 s], 77% [DeXDu86snYE 23.0 of 29.7 s].
6. Give every transition a trigger in frame: cursor [DeY58dONeuY, DcGaekAMU90], a contact flash [DXzurbATRQT 18.4 s], a voice phrase [DZCY6bjOsUQ], a beat grid [DdwCXaQIHNU, DeF8z3XoLdh].
7. Echo the content: pixel steps for halftone [Dcs-MiOpO2V], mosaic for 1-bit windows [DePvWkxNAun], waveform for a sound topic [DeaJ4yUg95f], wireframe for CG [DeXDu86snYE].
8. One to three families per reel: morph only [Dbmcud4IexE], particle only [DeRpl8Yhrb2], replacement plus mosaic [DcL6By1z4QE, DePvWkxNAun].
9. Keep a constant under the changes: footer [DZCY6bjOsUQ], HUD [DdwCXaQIHNU], accent cluster [DeMrHF6qi0z], the physical frame in shot-off-a-screen reels [Db28edFqHTP, DdY8V8XKJD6, DdjM8xRNzk_].

## Sound at the transition (inferred from spectrograms; full policy in `sound-design.md`)

- Hits land on the cut or up to 60 ms before it: median offset 0.0 s, 22 of 28 reels within 40 ms [DZUZITfz0Qu 4.71 s against a cut at 4.77 s]. Swells pre-lap 0.1 to 1 s [Dc0izivoZNw 3.04 s].
- Dropouts beat risers: 0.2 to 0.5 s of silence before the biggest hit [DZUZITfz0Qu 4.37 s; DclkKscsRbs 7.17 s; DeXDu86snYE 24.03 s].
- Many transitions are silent: gradient wipes, counts and checks [DdY8V8XKJD6, Db28edFqHTP]. Score 3 to 9 events in 25 to 35 s, not all.

## Key (id, descriptor)

DXzurbATRQT UI-motion promo; DZCY6bjOsUQ voice-led statue-cutout promo; DZUZITfz0Qu motorbike glitch edit; Db28edFqHTP SaaS promo shot off a wall display; Dbmcud4IexE icon morph chain; Dc0izivoZNw 3D course trailer; DcGaekAMU90 design-tool tutorial promo; DcL6By1z4QE object-swap explainer; DcOIGDdss_L game-themed showreel; DcYXIWbxzAN neon kinetic-type sting; DclkKscsRbs UI pitch 1:1; Dcs-MiOpO2V Swiss-grid title sequence; Dd6Uc27ssjp plugin promo with tile grids; DdCH-tFy7Wp comment-bait promo 1:1; DdY8V8XKJD6 SaaS promo shot off a screen; Dd_t1ZhNAoR chat-story explainer; DdjM8xRNzk_ product promo shot off a monitor; DdwCXaQIHNU kinetic-word teaser; DeF8z3XoLdh Bauhaus kinetic-word teaser; DeMrHF6qi0z lyric collage; DeO1Rh7x5Qm app teaser on gradient; DePvWkxNAun retro-window monologue; DeRpl8Yhrb2 six-minute lyric video; DeSvnCQIgs3 logo reveal shot off a monitor; DeXDu86snYE macro balloon-pop ad; DeXtJrAtOcr keynote-style parody off a laptop; DeY58dONeuY UI file-upload flow; DeZ3P_8NeHT talking-head tutorial; DeZOFtEMkuA UI pitch 1:1; DeaJ4yUg95f laptop UI shot with room-light cycle.
