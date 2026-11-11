# Pacing and timing

This file is the clock of a reel: how often the picture changes, how long beats and holds last, how text and counters are timed, how rhythm survives without cuts, and how pieces from 6 seconds to 6 minutes are paced. Numbers are measured from the 30-reel study or read from its frame-numbered notes. Frame counts assume 30 fps (the set also has three 24 fps reels, one 25 fps, one 20 fps), so keep staggers in frames if you change fps. Limits are in section 12.

## 1. Pick the cut rate from the format class

**Rule.** Choose the class first. Cut rate follows class, not aspect ratio: the fastest reel is 16:9 [Dcs-MiOpO2V], the second fastest 9:16 [DZUZITfz0Qu].

**Evidence.** Hard cuts per second from meta.md; mean shot = duration / (cuts + 1); median frame change from EVENTS.txt headers. Classes are my grouping; the descriptors apply wherever an id appears later.

| Class | Reels (hard cuts per s) | Duration s, median | Mean shot s | Median frame change |
|---|---|---|---|---|
| Single-take phone shot of a screen (6) | Db28edFqHTP SaaS promo 0, DdY8V8XKJD6 SaaS promo 0, DeSvnCQIgs3 logo morph 0, DeXtJrAtOcr launch parody 0, DeaJ4yUg95f room-light UI 0, DdjM8xRNzk_ brand promo 0.04 | 10.3-26.5, 19.3 | whole take | 0.64-2.89, 0.84 |
| Screen-native UI or app promo (7) | DXzurbATRQT shape morphs 0.12, DeY58dONeuY upload UI 0.06, DclkKscsRbs pitch 0.08, DeZOFtEMkuA pitch 0.08, DdCH-tFy7Wp comment-bait promo 0, DeO1Rh7x5Qm app typography 0.09, Dc0izivoZNw 3D trailer 0.08 | 8.1-32.9, 16.1 | 6.0-8.5 | 0.37-2.68, 0.75 |
| Voice-driven explainer or tutorial (8) | DZCY6bjOsUQ cutout promo 0.38, Dd6Uc27ssjp plugin promo 0.60, DcGaekAMU90 chapter tutorial 0.45, Dd_t1ZhNAoR chat story 0.30, DeZ3P_8NeHT talking head 0.19, DeXDu86snYE macro balloon ad 0.10, DcL6By1z4QE object swap 0, DePvWkxNAun monologue 0 | 26.2-95.5, 57.4 | 1.6-7.4 (six with cuts) | 0.55-4.93, 1.18 |
| Hype, kinetic type, sting (6) | Dcs-MiOpO2V title sequence 2.34, DZUZITfz0Qu glitch edit 1.76, DdwCXaQIHNU word teaser 1.06, DeMrHF6qi0z lyric collage 0.50, DeF8z3XoLdh Bauhaus teaser 0.46, DcYXIWbxzAN neon sting 0.32 | 6.3-15.2, 13.3 | 0.40-2.10 | 2.16-13.41, 5.35 |
| Showreel or morph chain (2) | DcOIGDdss_L showreel 0.74, Dbmcud4IexE icon morphs 0.02 | 84.1, 103.8 | 1.3; none | 2.64; 0.35 |
| Long lyric video (1) | DeRpl8Yhrb2 0.045 | 377.9 | 21 by hard cuts | 3.88 |

- In the 11 cut-driven reels (at least 0.19 cuts per s, leaving out the flash-intro sting [DcYXIWbxzAN]), 297 EVENTS segments have median 1.03 s, quartiles 0.5 and 1.9 s, 90th percentile 3.3 s; 49% last 1 s or less, 96% 5 s or less. Per-reel medians: 0.38-0.39 s [DdwCXaQIHNU, Dcs-MiOpO2V] to 1.78 s [Dd_t1ZhNAoR].
- Whole set: median 0.09 cuts per s; 18 of 30 at 0.125 or less; 8 with none. By aspect: 9:16 (18 reels) 0-1.76, median 0.09; 16:9 (9) 0.02-2.34, median 0.32; 1:1 (3) 0-0.08. Duration median 24 s; 18 of 30 are 26.5 s or less; 8 exceed 50 s.
- Grid: about six reels snap cuts to a measured beat grid [DdwCXaQIHNU 0.25 s multiples, DeF8z3XoLdh 0.5 s, Dcs-MiOpO2V, DdCH-tFy7Wp, DcYXIWbxzAN, DcOIGDdss_L 38-56 s]. Nine of 15 readable tempos sit at 107-122 BPM, three at exactly 120: a beat is 15 frames, an eighth 7.5, a sixteenth 3.75. Voice reels cut on a phrase's first syllable instead [DZCY6bjOsUQ: 9 of 11 cuts within 80 ms].

**Build.** Plan beats first, then derive cuts. A zero-cut class still needs a visible change every 1-4 s (sections 3, 8).

## 2. The first second and the hook

**Rule.** Start something by 0.4 s, finish the hook line by about 2 s, land the first hit, cut or reveal at about 2 s.

**Evidence.**
- First deliberate element at 0.0-0.4 s: [DZCY6bjOsUQ, DZUZITfz0Qu, DcYXIWbxzAN, DXzurbATRQT, DclkKscsRbs, DdCH-tFy7Wp, DdjM8xRNzk_, DeF8z3XoLdh, DdwCXaQIHNU, DeZOFtEMkuA, DeSvnCQIgs3, Dd_t1ZhNAoR].
- A 4-7 word hook line completes in 0.8-2.5 s [DclkKscsRbs 0.8, DeZOFtEMkuA 1.2, DdjM8xRNzk_ 1.6, DZCY6bjOsUQ 1.8, Dd_t1ZhNAoR 2.5].
- Slow starts come with a physical setup: screen lit at 1.4 s [DeXtJrAtOcr]; first text at 1.2 s after 0.94 s of digital silence [DeaJ4yUg95f]; near-still desk until 0.83 s [Dc0izivoZNw]. Phone-shot takes carry a fixed caption from frame 0 [Db28edFqHTP, DdY8V8XKJD6, DeSvnCQIgs3, DeXtJrAtOcr, DeaJ4yUg95f].
- First scene change at 2.0-4.4 s in 12 reels [DXzurbATRQT, DcOIGDdss_L, DZCY6bjOsUQ, DdwCXaQIHNU, DZUZITfz0Qu, DeMrHF6qi0z, Dc0izivoZNw, Dd6Uc27ssjp, Dd_t1ZhNAoR, DeO1Rh7x5Qm, DeF8z3XoLdh, DclkKscsRbs]. Exceptions: under 1 s [DcGaekAMU90, Dcs-MiOpO2V]; 12 s or later after an intro world [DeZ3P_8NeHT 12.4, DeXDu86snYE 16.0]. The sound study puts the first big arrival within 0.1 s of 2.0 s in eight reels [DdwCXaQIHNU, DeF8z3XoLdh, DeSvnCQIgs3, DeaJ4yUg95f, DeXtJrAtOcr, DcOIGDdss_L, DdjM8xRNzk_, DeZOFtEMkuA].
- Hook shapes: word-per-beat build [DZCY6bjOsUQ, DdjM8xRNzk_, Dd_t1ZhNAoR]; ball drop at 0.4 s [DeF8z3XoLdh]; four flash frames [DcYXIWbxzAN].

**Build.** Precompose a 60-frame hook: first keyframe by frame 12, words 6 frames apart, the scored hit or scene change on frame 60. For voice, start each word on the speaker's first syllable.

## 3. One idea per beat

**Rule.** One new idea per beat. Plan by beats, not cuts. Text enters only after the previous element has left [Db28edFqHTP].

| Beat length | Where seen |
|---|---|
| 0.2-0.6 s | one word per shot [DdwCXaQIHNU, DeF8z3XoLdh] |
| 0.6-1.5 s | screen beats [Db28edFqHTP 0.7-1.0, DdY8V8XKJD6 1.0-1.5], cutout promo [DZCY6bjOsUQ 1.0-1.5], slides [DeXtJrAtOcr 1.5], chapter cards [DcGaekAMU90 0.9-1.1] |
| 1-3 s | UI states [DeY58dONeuY about 1.8, DXzurbATRQT 1.5-2], app lines [DeO1Rh7x5Qm 1-2.5], showreel pieces [DcOIGDdss_L 1-3] |
| 2-4 s | one sentence per picture [Dd_t1ZhNAoR 2-4, DcL6By1z4QE 3-4, DePvWkxNAun 2-3] |

Beats outnumber cuts: about 20 beats in 11 shots [DZCY6bjOsUQ]; a new beat every 0.7-1.0 s with no cut for 16 s [Db28edFqHTP]. **Build.** A beat arrives over 0.3-0.5 s, holds at least 0.3 s [Db28edFqHTP], and leaves while the next arrives [DcL6By1z4QE, Dbmcud4IexE, DeY58dONeuY].

## 4. Word and caption cadence

**Rule.** Voice-led captions run 0.2-0.35 s per word; slower monologue 0.3-0.7 s.

**Evidence.** 0.2 s, 4-5 words per s [DZCY6bjOsUQ]; 0.3 s [DcGaekAMU90]; 0.2-0.35 s [Dd6Uc27ssjp, 5-8 frames at 24 fps]; 0.2-0.3 s [DdjM8xRNzk_]; 0.25 s [DeXDu86snYE]; 0.2 s [DeMrHF6qi0z]; 0.35 s [Dd_t1ZhNAoR]; 0.3, 0.5 or 0.7 s by line [DePvWkxNAun]. Typed letters take 3-4 frames, words 6-10 frames [DcL6By1z4QE]. Mixed-size lines build every 0.5-0.7 s: 5 lines in 60 frames, 7 in 120, 10 in 7 s [DcL6By1z4QE]. Soft product lines: words 0.2 s apart, swaps as 6-frame cross-fades at 24 fps [DeO1Rh7x5Qm].

**Build.** Each word fades or blurs in over 3-4 frames [DZCY6bjOsUQ, DeZOFtEMkuA]; stagger 6 frames or place on voice onsets (GSAP `stagger: 0.2, duration: 0.12`). Big nouns large, glue words small [DcL6By1z4QE].

## 5. Build, hold, release

**Rule.** Hold after every build; release with a flash, cut or morph.

**Holds seen.** 0.3 s minimum on a UI beat [Db28edFqHTP]; 0.5 s on a built headline before a hard cut [DZCY6bjOsUQ]; 0.8 s on a single-word question card [DcL6By1z4QE]; 0.7-1.3 s per icon [Dbmcud4IexE]; 1.2 s on a success state [DeY58dONeuY]; 2.5 s calm window [DePvWkxNAun]; 2.8 s tension pause on a white frame [Dd_t1ZhNAoR]; only 2 frames of clean picture between glitch bursts [DZUZITfz0Qu].

**Shapes.**
1. Countdown to payoff [DeXDu86snYE]: a frame counter that steps one unit per frame (211 minus the frame index) runs 211 to 001 in about 7.0 s and turns red near the end; the dented surface holds at full stretch 0.4 s; the pop lands at 23.0 s of 29.7 s (about 77%); an end card follows.
2. Dark build, then flash: dark for 4.8 s, flash fill [DdjM8xRNzk_]; halo grows 0.4 s, white flash flips the theme [DXzurbATRQT]; glow brightens every 0.35 s for 2.2 s, flash, hard cut [Dd_t1ZhNAoR].
3. Audio absence before the hit: 0.33 s gap [DZUZITfz0Qu]; 4-beat bass hole before the biggest change [Db28edFqHTP].

## 6. Escalation by repetition

**Rule.** Repeat one device three times with rising intensity.

**Evidence.** Counters: four steps, last held 1.0 s [DZCY6bjOsUQ]; a badge counting every 0.35 s and a price in three steps [Dd_t1ZhNAoR]; a stat counter whose jumps shrink (about 61, 13, 3, 1) and a ring gauge that slows into its end (84, 98, 99) [DdwCXaQIHNU]. Intensity: glow brighter every 0.35 s, an icon brighter every 0.3 s [Dd_t1ZhNAoR]; each word larger than the last [DZCY6bjOsUQ]. Stacking: windows pile up, captions double and triple, modals drop 2 frames apart, badges stamp every 0.2 s [DePvWkxNAun]; 5 then 10 objects [DcL6By1z4QE]; a connector word three times with widening spacing [DcGaekAMU90]; seven 5-frame segments in a row [DcOIGDdss_L].

**Build.** Interval 9-10 frames to read a count, 2-6 to stack. Ease counters out: `v = Math.round(target * (1 - Math.pow(1 - p, 3)))`.

## 7. Stagger, easing, overshoot

| Device | Stagger |
|---|---|
| Sibling cards, chips, lines | 1-3 frames, usually 2 [DeO1Rh7x5Qm 2 at 24 fps with 3-frame blur-to-sharp; Dc0izivoZNw; DcOIGDdss_L; DdwCXaQIHNU; DcGaekAMU90 2.5-3; Dcs-MiOpO2V and DeZOFtEMkuA 1] |
| Discrete reveals (words, nodes, pills, tiles) | 6-12 frames [Db28edFqHTP 6, DZCY6bjOsUQ 6, DePvWkxNAun 6, DeZ3P_8NeHT 10, DeMrHF6qi0z 12, DeZOFtEMkuA 6-8] |
| Tower or stack | 2 frames [DePvWkxNAun] |
| Entrance blur | 3-4 frames to sharp [DclkKscsRbs, DeZOFtEMkuA] |

**Easing seen.**
1. Ease-out arrivals: 15 px per frame slide [Db28edFqHTP]; one property per morph over 0.3-0.5 s, then a settle [Dbmcud4IexE].
2. Overshoot is tiny or one frame [DXzurbATRQT, Db28edFqHTP, DeSvnCQIgs3, DcL6By1z4QE, DdwCXaQIHNU]. Visible bounces belong to dropped objects: a ball settling in about 0.8 s [DeF8z3XoLdh], tiles [DeMrHF6qi0z], chrome blobs [DdwCXaQIHNU].
3. Rotation settles: 12 degrees to level in 6 frames; letters from -30 and +40 degrees to level in 12 frames [DdwCXaQIHNU]; 3D tilts of 5-10 degrees settling flat [DeY58dONeuY].
4. Loops stay linear: text wall 20 px per frame [DeF8z3XoLdh]; pinwheel 12-14 degrees per 0.33 s [Dbmcud4IexE].
5. Glitch is un-eased: positions change every 1-2 frames, a 12-15 fps stutter built from 3-frame loops [DZUZITfz0Qu].

**Build (starting values, not measured).** AE: `t = time - (index-1)*2*thisComp.frameDuration`, overshoot barely visible. GSAP: `power3.out`, `back.out(1.2)`, `steps(3)` for stutter. Remotion: `spring({frame: frame - i*2, fps, config: {damping: 14}})`.

## 8. Rhythm without cuts

**Rule.** Put the clock in the content: a screen beat about every second, wipes, flashes and morphs standing in for cuts, a room light or screen mood as metronome.

**Evidence.**
- Screen beats about 1 per s [Db28edFqHTP]; gradient wipes at 6.2 and 7.8 s, white flash 11.2 s, bar sweep 13.6-14.2 s [DdY8V8XKJD6].
- Screen mood as light source: dark, orange, white, dark, with a flash fill and a band sweep [DdjM8xRNzk_].
- Room light moves one hue every 1.5-2 s through a 9-10 s loop, in step with the screen [DeaJ4yUg95f].
- Morph chain: hold 0.7-1.3 s, morph 0.3-0.5 s, one change per 1-3 s for 103.8 s [Dbmcud4IexE]. Six UI states in about 11 s, cursor 0.3-0.5 s ahead of each result [DeY58dONeuY].
- Object swaps, no cut: one object per sentence, 3-4 s; one ring pulse and a 2-3% frame bump, 4 frames to expand [DcL6By1z4QE].
- Camera: handheld rise of 12 px in the final second, rack focus at 8.0-8.7 s [Db28edFqHTP]; pushes of 6% over 1.2 s [DdjM8xRNzk_] and 5% over 1.6 s [DdY8V8XKJD6]; 8% per s [DeXDu86snYE].
- Measured calm: median frame change 0.74-1.09 [DeSvnCQIgs3, DeXtJrAtOcr, DeaJ4yUg95f, DePvWkxNAun, DcL6By1z4QE], against 13.4 in the glitch edit [DZUZITfz0Qu].

**Build.** Drive a glow or gradient layer from one looped expression (After Effects: `hue = 360*(time % 9.5)/9.5` into Hue/Saturation), and put screen beats on the same 1-2 s grid.

## 9. Long-form pacing

**Rule.** Lengthen by adding beats, not by lengthening beats. Mark chapters with a repeating card and punctuate with single-word beats.

**Evidence.**
- Mean shot stays 1-3 s: 2.2 s in 90.7 s [DcGaekAMU90], 3.2 s in 95.5 s [Dd_t1ZhNAoR], 1.3 s in 84.1 s [DcOIGDdss_L].
- Fixed chapter card, only number and colour change, 2-frame colour blink; six flip through in 3.5 s and it returns at 28.8, 29.4, 41.9, 75.2 s. White single-word beats at 0.3 s per word break the piece at 9.3, 45.1, 73.6, 88.0 s [DcGaekAMU90].
- Recurring scenes work as chapters: a diagram scene at 40.6 and 61.95 s, a desk scene at 3.5, 17.5, 51.8 s [Dd_t1ZhNAoR].
- Showreel: pieces 1-3 s, neon title cards every 20-30 s, label chips only from 55.3 s, 3.4 s closing badge [DcOIGDdss_L].
- Monologue phases: caption block every 2-3 s, objects accumulate, blank window and held question in the last 9 s [DePvWkxNAun]. A pivot at 52% of runtime on one full-screen card [DcL6By1z4QE].
- Intro world 12.4 s (20% of 63.1 s), then steps changing every 1.5-3 s, call to action last 2 s [DeZ3P_8NeHT].
- Six-minute lyric video [DeRpl8Yhrb2]: 17 hard cuts; 13 segments over 10 s fill 64% of runtime, the longest 40.8 s; most arrangement sections 15-35 s; caption lines every 1.5-2 s; portraits every 0.7-1.0 s near the end; a 3.47 s silence (275.4-278.9 s) releases 14 cuts in 3.9 s, mostly 4-9 frames each; one title card opens (0-2.7 s) and closes (376.0-377.8 s).

**Build.** Storyboard in 15-35 s chapters, hold the class beat rate inside each, use one burst after a silence, bookend with a repeated card.

## 10. Endings

**Rule.** Hold the final lockup 1.0-2.7 s (median 1.5 s across the 12 readings in the first two rows).

| Ending | Hold | Reels |
|---|---|---|
| Logo or lockup | 1.0-2.7 s | [DXzurbATRQT 2.7, DeO1Rh7x5Qm 2.5, Dc0izivoZNw 2.0, DcYXIWbxzAN 1.7, DdY8V8XKJD6 1.3, DeaJ4yUg95f 1.2, DeZOFtEMkuA 1.2, DeF8z3XoLdh 1.0, DeSvnCQIgs3 1.0, DclkKscsRbs 1.0] |
| Black end card or call to action | 1.7-2.0 s | [DeZ3P_8NeHT 2.0, DeXtJrAtOcr 1.7] |
| Quiet long hold or fade | 3.0-5.7 s | [DeXDu86snYE wordmark 4.8, DcOIGDdss_L badge 3.4, DdjM8xRNzk_ hero spin 3.8, DePvWkxNAun held question 3.0, Dbmcud4IexE logo fade 5.7] |
| No hold | 0-0.5 s | [Dd_t1ZhNAoR, Dcs-MiOpO2V, DeMrHF6qi0z 0.3] |

Audio ends in a fade about as often as a hard stop (15 versus 14 reels). The final segment is nearly still in EVENTS (88-99%) [DXzurbATRQT, Dc0izivoZNw, DcOIGDdss_L]. **Build.** Make the lockup the last beat's exit [DXzurbATRQT 0.6 s] and keep it still for the hold.

## 11. Pacing table by format

| Format | Total | Cut rate | Beat or shot | Hold after build | End |
|---|---|---|---|---|---|
| Single-take phone shot | 10-27 s | none | beat 0.7-1.5 s | 0.3 s or more | 1.0-1.3 s, 3.8 s hero |
| UI or app promo | 8-33 s | 0-4 cuts | state 1.5-2.5 s | about 1.2 s on a result | 1.0-2.7 s |
| Voice explainer or tutorial | 26-96 s | 0.1-0.6 per s, or none with swaps | beat 1-4 s, shot 1.6-7.4 s | 0.5-0.8 s on text, 2.5-2.8 s pauses | 0-2.0 s, 3.0 s on a held question |
| Hype, kinetic type | 6-15 s | 0.3-2.3 per s | word 0.2-0.6 s, shot 0.4-2.1 s | 2 frames to 0.3 s, lockup 1 s | 0.3-1.7 s |
| Showreel | about 84 s | 0.74 per s | piece 1-3 s | 0.7-1.3 s | 3.4 s |
| Long lyric | 378 s | 0.045 per s plus bursts | line 1.5-2 s | stretches of 10-41 s | 1.8 s |

See also: motion-reel (beat-grid pipeline), layout-composition (rhythm), typography (size hierarchy), vox-after-effects-recipes (expressions).

## 12. Limits

- 30 reels, one platform, one season; classes hold 1 to 8 reels, so ranges describe, they do not set norms.
- EVENTS segments over-split flashes (91 segments for about 62 true cuts [DcOIGDdss_L]) and in no-cut reels are motion phases, not shots; hard-cut counts miss soft transitions.
- Picture times come from sheets at about 5 fps, good to 0.1-0.3 s; the six-minute reel was seen in 7 of 26 sheets.
- Tempo was inferred from audio nobody listened to; camera and lens figures elsewhere are estimates.
