# Camera and lens

How to place and move the camera in a reel, in two senses: the virtual camera inside a motion-graphics scene, and the real or simulated camera (phone shot of a screen, macro, talking head, wide low angle, depth of field, blur on cut frames). Each section gives the rule, the evidence from 30 reels, then a build. Shot sizes and move meanings live in cinematography-for-ai; null rigs and fly-through easing live in vox-after-effects-recipes (references/camera-and-finishing.md), so neither is repeated here.

**Limits, read first.** Every lens value (mm), angle, drift amount and screen-fill percentage is an estimate from the picture, never metadata; the two study passes disagreed on one lens (talking head, 50 vs 85 mm). Handheld amounts are by eye, in pixels of the 720 px wide files. Push rates are computed from the frame notes, not from the detector's zoom flags, which come from a coarse five-step grid (0.94 to 1.06 per frame). Sound pairings are inferred from spectrograms. Sample: 30 reels, one platform, one season. Conversions use 30 fps unless a reel's own fps is stated.

## 1. Virtual camera

**Rule 1: choose the strategy before animating.** Flat, no camera, shape morphs and type do everything: [DXzurbATRQT, Dbmcud4IexE, DcYXIWbxzAN]. One move per piece: a card tunnel is the only camera move [DZCY6bjOsUQ]. Constant motion: dolly, roll or orbit in every shot, a whip or white flash at each cut [Dc0izivoZNw]. UI pieces tilt the objects, not the camera [DeY58dONeuY, DXzurbATRQT].

| Move | Intent | Amount and timing seen | Reels, in figure order |
|---|---|---|---|
| Slow push on a held frame | keeps a hold alive without a new beat | 2 to 12 percent over 0.5 to 2.1 s; median 4 percent per second, range 2.1 to 15 (computed) | [DZCY6bjOsUQ, DZUZITfz0Qu, Dcs-MiOpO2V, Dd6Uc27ssjp, DclkKscsRbs, DeO1Rh7x5Qm, DdjM8xRNzk_, DdY8V8XKJD6] |
| Hero push | tension toward a payoff | object width 60 to 100 percent in 48 frames (42 percent per second), then about 8 percent per second | seen in one reel [DeXDu86snYE] |
| Crash zoom into a letter or ball | leave a scene so the next grows from the landing field | about 3x in 3 to 7 frames, heavy blur, lands on a flat field; frame change peaks at f57, flat by f60 | [DeF8z3XoLdh, Dcs-MiOpO2V, Dc0izivoZNw, DcGaekAMU90] |
| Whip | hide a cut inside blur | 4 to 6 frames of travel (0.17 to 0.2 s), 10 in one reel; whip frame blurred, tilted about 20 degrees | [Dc0izivoZNw, DZUZITfz0Qu, DclkKscsRbs, Dd6Uc27ssjp] |
| Orbit | show a form from several sides | 19 degrees per second (8 per 10 frames at 24 fps); 7 per second over 42 frames while tilting | [Dc0izivoZNw, DeF8z3XoLdh] |
| Roll | energy, dutch tilt | about 15 degrees clockwise over 40 frames at 24 fps (9 per second); 2 to 3 degrees over 2 s on a flat-lay push | [Dc0izivoZNw, DcOIGDdss_L] |
| Dive through a stack | speed or an "everywhere" idea | 6 to 8 percent per second plus slow roll over 3.8 s; 15 percent per second; rings pass the lens every 0.2 to 0.4 s; a 100-frame dive from a 3D word onto a city then a globe | [DZCY6bjOsUQ, DcOIGDdss_L, DeF8z3XoLdh, DeRpl8Yhrb2] |
| Top-down locked plane | keeps cut-outs on one floor | 51.7 s without a cut: objects bob 3 to 5 px, tilt 2 to 4 degrees, one shadow direction (lower right), one 2 to 3 percent frame bump with a ring pulse | [DcL6By1z4QE]; straight-down desk plates [Dd_t1ZhNAoR, Dc0izivoZNw] |
| UI dolly | point at the element discussed | 21 frames at 20 fps into a document; 40 frames at 25 fps until type blurs, then refocus | [Dd_t1ZhNAoR, DcGaekAMU90, DeZOFtEMkuA] |
| Card tilt | gives each state change a small 3D move | 5 to 10 degrees, settles flat; about 8 on exit; 2 idle float; windows tumble away in 10 frames | [DeY58dONeuY, DXzurbATRQT, Dd6Uc27ssjp, DePvWkxNAun] |
| Isometric | geometric, orthographic look | cube heights driven by distance from centre, rig orbits about 10 degrees | seen in one reel [DeF8z3XoLdh] |

**Rule 2: layer type by depth.** Type sits behind a 3D hero, not in front [Dc0izivoZNw]. During a dive, copy stays on a flat layer and changes in place with a 0.4 s cross-fade [DZCY6bjOsUQ]. Type may shrink while the camera pushes in (6 percent) [DdjM8xRNzk_].

**Build, After Effects** (after-effects MCP, run_extendscript):
- Rig: 3D null, camera parented, key only the null. Zoom in px = mm x comp width / 36 at the default film size: on 720 px, 26 mm = 520, 85 mm = 1700, 100 mm = 2000. `cam=comp.layers.addCamera("CAM",[comp.width/2,comp.height/2]); cam.property("ADBE Camera Options Group").property("ADBE Camera Zoom").setValue(85*comp.width/36);`
- Crash zoom on a precomp, anchor on the glyph: `u=linear(time,t0,t0+6*thisComp.frameDuration,0,1); s=100*Math.pow(3,u); [s,s]` (equal ratio per frame reads as a real zoom). Raise the comp shutter angle or key CC Radial Fast Blur over the same frames; end on a flat field.
- Whip: Position slide plus Directional Blur on an adjustment layer, 0 to peak to 0 over 4 to 6 frames, up to 20 degrees of roll at the peak.
- Orbit: camera parented to a null at the subject, key its Y rotation. Dive: cards on a Z ladder, key the rig's Z.
- Focus: Depth of Field on; Focus Distance `length(toWorld([0,0,0]),thisComp.layer("FOCUS").toWorld([0,0,0]))`, key FOCUS to rack. Camera Lens Blur for 2D layers.

**Build, HyperFrames/GSAP:** one `#world` wrapper inside a `#stage` with CSS perspective; tween only the wrapper (scale or z push, rotationZ roll, rotationY orbit). Crash zoom: scale 1 to 3 in 0.2 s, `power3.in`, plus a blur ramp. Whip: x with `expo.out` and an SVG feGaussianBlur `stdDeviation="x 0"`. Tilts: rotationX/Y 8 to 0, back-out settle. Keep it all on the one paused timeline the renderer seeks.

**Build, Remotion:** `interpolate(frame,[f0,f0+6],[1,3],{easing:Easing.in(Easing.exp),extrapolateLeft:"clamp",extrapolateRight:"clamp"})`; `spring()` for tilt settles; `@remotion/three` ThreeCanvas with `orthographic` for isometric (true elevation 35.264 degrees; see isometric-motion); `@remotion/motion-blur` CameraMotionBlur on whips and crash zooms.

## 2. Real or simulated camera

### 2.1 Phone shot of a screen
**Rule: one continuous handheld take of a bright screen in a dim room; the screen's animation is the edit.** Six reels: [Db28edFqHTP, DdY8V8XKJD6, DdjM8xRNzk_, DeSvnCQIgs3, DeXtJrAtOcr, DeaJ4yUg95f]. All 720x1280, 30 fps, 10.3 to 26.5 s (median 19.3 s), zero hard cuts in five and one in [DdjM8xRNzk_]; screen changes inflate the detector's shot count (9 shots there).
- **Frame** (estimated from contact sheets, five reels; [DeSvnCQIgs3] sits higher, monitor at 16 to 58 percent, black below with a second caption): screen at about full frame width and 35 to 41 percent of height (a 16:9 screen at 720 px wide is 405 px, 32 percent of 1280; bezel and perspective add the rest), top edge 26 to 39 percent down. Above: room or ceiling plus the caption. Below, the bottom 28 to 36 percent: a foreground device, tablet [Db28edFqHTP, DdY8V8XKJD6] or keyboard [DdjM8xRNzk_, DeXtJrAtOcr, DeaJ4yUg95f].
- **Lens and angle:** phone main lens, about 26 mm equivalent [Db28edFqHTP, DdjM8xRNzk_], desk height. Keystone from an off-axis seat in one reel [DdjM8xRNzk_].
- **Drift, slow not shaky:** 12 px up over the last second [Db28edFqHTP]; 10 px sideways over 1.2 s, later 6 px down [DdY8V8XKJD6]; about 15 px up over 3.8 s [DdjM8xRNzk_]. That is 0.5 to 1.7 percent of frame width per second (computed). The shift detector flagged none of the six, but its median cannot see zero-mean jitter.
- **Focus:** a refocus onto the foreground device for about 0.3 s (9 frames) at 8.0 to 8.7 s [Db28edFqHTP], another after a state change [DdY8V8XKJD6]. Pull or autofocus hunt cannot be told apart.
- **Room:** dim, not black: mean frame luma 47 to 101 of 255 (median 86; all-30 median 99). White LED bar above the screen, coloured glow at base or edge [Db28edFqHTP, DdY8V8XKJD6, DdjM8xRNzk_]. The screen is the key light and spills onto wall, keys and tablet [Db28edFqHTP, DdjM8xRNzk_], or an RGB wash steps blue, violet, magenta, red, warm grey, teal, cyan every 9 to 10 s [DeaJ4yUg95f].
- **Reality cues:** a hand leaves frame within 0.4 to 1.0 s [DdjM8xRNzk_, DeXtJrAtOcr, DeaJ4yUg95f]; host-app panels stay around the comp [DeSvnCQIgs3]; a caption fixed on every frame in five of six [Db28edFqHTP, DdY8V8XKJD6, DeSvnCQIgs3, DeXtJrAtOcr, DeaJ4yUg95f].
- **Build:** real: phone, handheld, screen bright, room lights low, one bar light, one coloured strip. Simulated: a room still (photo or Higgsfield image), Corner Pin the UI precomp onto the screen, a blurred UI copy in Add mode on the wall for spill, a 12 to 15 px keyframed drift (not wiggle), a 9-frame Camera Lens Blur rack to the foreground device, caption on top. The files cannot prove these were real shoots.

### 2.2 Macro and HUD
**Rule: for a payoff, push into a surface until it fills the frame, hold one razor focus plane on the tip, and announce the lens change in a camera HUD.** Every macro look here appears to be CG depth of field, none optical. A balloon-pop ad [DeXDu86snYE]: record dot with timecode top left, lens label top right switching from 85 mm to a 100 mm macro label at f54, corner brackets, a countdown in frames at bottom centre, then a 12-frame scan-line wipe to wireframe and back. A 3D course trailer [Dc0izivoZNw]: estimated 85 to 100 mm, a key filling the frame, about 2 percent per frame push across the press (f160 to f176). Dive close-ups: a doughnut as a blurred ring, 0.5 s to hero [DdjM8xRNzk_]; a 6-frame dive onto an earbud surface [DeXtJrAtOcr].
- **Correction to the notes:** the countdown is not a 5 Hz clock. It is 211 minus the frame index, stepping every frame (175 at f36, 174 at f37, 168 at f43; timecodes 01:07, 03:21, 06:05 show 174, 100, 026), reaching 1 near 7.0 s [DeXDu86snYE]. Build: Source Text `Math.max(1, 211 - timeToFrames(time))`, timecode from the same frame.
- **Build:** AE camera 85 to 100 mm (zoom 1700 to 2000 on 720 px), DOF on, high aperture, FOCUS null on the tip. Fade the HUD at 7.2 to 7.6 s over a held max-stretch frame, then the payoff [DeXDu86snYE].

### 2.3 Talking head and the proof shot
**Rule: locked camera, medium close-up, one side key, soft practicals behind, captions on the chest, a new picture every 1.5 to 3 s.** Seen in one reel [DeZ3P_8NeHT]: lavalier, key from camera left, lamp and window out of focus behind, laptop lit at lower right, estimated 50 to 85 mm at an f/2 look. Captions sit mid-chest. Emphasis is the speaker leaning toward the lens, never a camera zoom. For demos, screen recording on top and speaker below keeps the face present. Proof shot, also one reel: a 1.3 s real desk shot (laptop centred, 50 mm look, warm window light, shallow focus, 3 percent push over 20 frames at 24 fps) inside a typographic ad [DeO1Rh7x5Qm].

### 2.4 Wide low angle and letterbox
**Rule: for hype, go low and wide, centre the subject, lock the camera, add all movement in post.** [DZUZITfz0Qu]: about 24 to 35 mm look, subject dead centre, distortion when close, 4 to 6 px jump-cut shake on alternate frames (f258 to f261). [DcGaekAMU90]: low-angle portraits, about 16 mm look, hard cuts about every 0.3 s (7 to 8 frames at 25 fps). [Dc0izivoZNw]: 20 to 24 mm rooms against 85 to 100 mm macro, swaps hidden by a whip or flare. Aspect as lens: a 2.8:1 band on a pull-back [Dc0izivoZNw], a 4:1 strip for one creature [DcOIGDdss_L], 16:9 windows inside a 9:16 canvas [Dc0izivoZNw, DeMrHF6qi0z].

### 2.5 Depth of field and blur on cut frames
**Rule: soften the first frames after a cut; recovery speed sets the mood.** Measured as gradient energy at 360x640, a content-dependent proxy. Hype edit [DZUZITfz0Qu]: first frame at 65, 47, 45 percent of settled sharpness (cuts f88, f143, f262), 90 percent after 11, 8, 8 frames. Calm promo [DZCY6bjOsUQ] f162: 34 percent, 20 frames; the notes said 3 frames by eye. 2D focus pulls on type and cards take 3 to 4 frames [DclkKscsRbs, DeZOFtEMkuA, DeO1Rh7x5Qm]. Build: adjustment-layer Gaussian Blur or Camera Lens Blur keyed to 0 over 8 frames from the cut frame (hype) or 20 (calm); in the DOM, tween `filter: blur()`.

## 3. Sound for camera moves
1. Whip or camera cut: the swell starts about 0.1 s before the cut and the sub hit follows [Dc0izivoZNw]; a falling filter sweep (2.25 to 2.9 s) builds into a hard cut at 2.94 s [DZUZITfz0Qu].
2. Crash zoom: riser and suck-out dip over the 0.7 s before, hit on the landing frame [DeF8z3XoLdh].
3. Macro to a press: level collapse of about 0.7 s (12 to 13 dB), then a broadband hit on the press [Dc0izivoZNw]. Held tension: mono sub drone with a riser 4.5 to 7.0 s, music cut dead 7.0 to 7.4 s on the frozen frame, sub impact saved for the pop, 0.2 s gap before the brand reveal [DeXDu86snYE].
4. Many moves get no sound: a crash zoom and two whips had no onset or whoosh [Dcs-MiOpO2V]; filter dips replace whooshes [Dc0izivoZNw]. Score only the biggest.
5. Phone shots have no cuts, so structure points are the edits: a 2.07 s low-end hole (6.46 to 8.53 s) overlaps the refocus and returns 37 ms before the picture change [Db28edFqHTP]. Four of six use a produced track, not room audio [Db28edFqHTP, DdY8V8XKJD6, DeSvnCQIgs3, DeaJ4yUg95f].

## 4. Shot recipes
| Shot | Frame and lens (est.) | Camera | Light and focus | Length | Reels |
|---|---|---|---|---|---|
| Phone shot of a screen | screen full width, 35 to 41 percent tall, about 26 mm | drift 12 to 15 px, one 0.3 s refocus | dim room, LED bar, coloured base glow | 10 to 27 s, no cuts | [Db28edFqHTP, DdjM8xRNzk_, DeXtJrAtOcr] |
| Macro tension push | surface fills frame, 85 then 100 mm | 67 percent in 48 frames, then 8 per second | dark stage, rim light, HUD | 7 s build | [DeXDu86snYE] |
| Macro press | key fills frame, 85 to 100 mm | 2 percent per frame, 16 frames | razor focus on the tip | under 1 s | [Dc0izivoZNw] |
| Talking head | medium close-up, 50 to 85 mm | locked, lean-in | side key, soft practicals | holds 1 to 3 s | [DeZ3P_8NeHT] |
| Wide low hero | subject centred, 24 to 35 mm | locked, blur snap-in | warm highlights, teal shadows | 0.3 to 3 s | [DZUZITfz0Qu, DcGaekAMU90] |

## 5. Mistakes to avoid
1. A camera on a flat icon-morph or kinetic-type piece; move the objects instead [DXzurbATRQT, Dbmcud4IexE, DcYXIWbxzAN].
2. Heavy wiggle or cuts in a phone shot; the six reels show slow drift, one refocus, and five have no cuts.
3. A crash zoom over 7 frames, unblurred, or landing on a busy frame [DeF8z3XoLdh].
4. Type in front of the 3D hero, or scaled by a dive [Dc0izivoZNw, DZCY6bjOsUQ].
5. Treating mm values or detector zoom flags as exact, or a HUD counter as a slow clock [DeXDu86snYE].
