# Sound design for reels

Use this file when you plan, score, mix or export the audio of a short-form motion reel: delivery targets, balance and layers, which sounds go on which visual events, music and voice treatment, and how tightly to lock picture to sound. It distils a study of 30 Instagram motion reels; each rule names the reels that show it. The audio was measured and read from spectrograms, never listened to, so effect and instrument names are inferred. Synthesis and mix scripts (`music.py`, `sfx.mjs`, `mix.py`, `review.py`) are in the motion-reel skill, `reference/AUDIO.md`.

## 1. Delivery targets

Rule: master to -14 LUFS integrated, true peak -1 dBTP or lower, loudness range 2-4 LU unless the arc is deliberate.

| Measure | Seen in the 30 reels | Aim for |
|---|---|---|
| Integrated | median -14.2 LUFS; 28 of 30 within -14.5 to -14.0; outliers -14.8 [DdjM8xRNzk_] and -15.1 [DeY58dONeuY], both sparse | -14 LUFS |
| True peak | median -0.35 dBTP; 12 above 0 (+3.1 [DdwCXaQIHNU], +1.8 [Dbmcud4IexE], +1.6 [DeY58dONeuY]); only 5 at -3 or lower (-6.4 [DeMrHF6qi0z], -5.1 [Db28edFqHTP]) | -1 dBTP; -2 to -3 for sharp synthetic transients [DcYXIWbxzAN, DZUZITfz0Qu] |
| Loudness range | median 3.2 LU; 14 at or under 3, 21 at or under 4; 8 above 5, all gated, sparse or long [DdjM8xRNzk_ 14.0, DeY58dONeuY 11.1, DcOIGDdss_L 10.5] | 2-4; wider only by design |
| Crest | median 19.8 dB, inflated by silent gaps [DeY58dONeuY 61.5] | not a punch measure; export 48 kHz AAC |

The -14 cluster probably reflects platform normalisation; readings over 0 dBTP can be codec overshoot, not clipping [Dcs-MiOpO2V, Dbmcud4IexE]. Local test: AAC re-encodes at 128k and 192k moved true peak by -1.7 to +0.9 dB against the source [DZUZITfz0Qu, DcYXIWbxzAN, DeF8z3XoLdh]. So limit at -1 dBTP and measure the final encode. Lower the loudest stem (usually SFX) before the limiter. Premiere: Hard Limiter last on the master. After Effects: markers and Audio Levels only. HyperFrames and Remotion: mix offline (`mix.py`, hyperframes-audio) and mux.

## 2. Spectrum and stereo

Rule: weight at 60-250 Hz, soft top, bass and hits mono, width only in pads, intros, tails and gaps.

Median band levels (dB, study scale): sub -10.1, bass +0.7, lowmid -4.3, mid -4.0, himid -11.6, air -19.5. Bass is the loudest band in 18 of 30 reels and above mid in 22; air sits 12 dB or more under bass in 26. Median side fraction 0.116, correlation 0.77. Effectively mono: [DeF8z3XoLdh 0.001], [DdCH-tFy7Wp 0.014]. Mono bass under wider mids [DdY8V8XKJD6, DeaJ4yUg95f]; pad correlation about 0.1 against hits about 0.7 [DXzurbATRQT]; width in gaps [Dcs-MiOpO2V 0.30-0.58 against 0.03-0.16 in blocks]; narrower at the drop [Db28edFqHTP 0.28 to 0.09]; wider as an ending lift [DeaJ4yUg95f].

Build: bass and kick mono below about 120-150 Hz (recipe value) [DdwCXaQIHNU, DcOIGDdss_L]; scoop 250-500 Hz under a sub [Dc0izivoZNw, DcYXIWbxzAN]; decorrelated pad low-passed near 2.5 kHz so ticks are the only bright thing [DXzurbATRQT]. Out-of-phase moments were logged at [DeZOFtEMkuA 5.5 s, a widening rise] and [DclkKscsRbs 2.0 s]: mono-check any widened passage.

## 3. Layer model

Rule: choose the lead layer first (bed, voice or effects), keep the others in support, and treat silence as a layer.

By the study's flags: music-led 16 (e.g. [DXzurbATRQT, DcYXIWbxzAN]), finished song 2 [DeMrHF6qi0z, DeRpl8Yhrb2], voice only 5 [DZCY6bjOsUQ, DePvWkxNAun], voice plus bed or effects 4 [DcGaekAMU90, Dd6Uc27ssjp, Dd_t1ZhNAoR, DeXDu86snYE], effects-led 3 [DeY58dONeuY, DdjM8xRNzk_, DclkKscsRbs]. Layers per reel, from the study's flags: 10 use one, 16 two (counting the voice-like layer in DclkKscsRbs), 4 three, none four. No reel has an ambience bed: gaps are digital silence [DeY58dONeuY, DeRpl8Yhrb2] or bed residue [Dcs-MiOpO2V]. The only room-tone cues are a 1.0 s pre-roll at -45 dB [DeXtJrAtOcr] and a probable reverb return heard between words [DePvWkxNAun]. Do not add room tone to a rendered piece.

## 4. Sound-effect vocabulary

Rule: sound-design the biggest changes and leave the rest silent. The strongest reels place 3-9 hits in 25-35 s [Dc0izivoZNw; DXzurbATRQT has four sub events]. Typed text, count-ups, checkmarks, wipes and particle dissolves are often unscored [DeO1Rh7x5Qm, Db28edFqHTP, DdY8V8XKJD6, DeRpl8Yhrb2]. Filter falls, dropouts and silence often replace whooshes [Dc0izivoZNw 15.6-17.5].

| Sound (AUDIO.md type) | Region and length | Visual event | Seen in |
|---|---|---|---|
| Sub boom (thump) | 30-100 Hz, 0.5-0.9 s decay, sub +5 to +11 dB, centred | theme flip, flash, whip, logo slam | [DXzurbATRQT, DclkKscsRbs, DeF8z3XoLdh] |
| First-frame stinger | thud 60-500 Hz plus a 1-3 frame click | white flash, then cut | [DcYXIWbxzAN thud 0.03 s, click 0.14 s] |
| UI click or tick (click, tick) | 2-8 kHz, 20-80 ms, pairs about 90 ms apart, near 0 dBFS over a quiet bed; clusters of 5-8 in 0.5 s for stutter; confirm ping about 262 Hz, 0.3-0.5 s | pop-in, press, card landing, typing (about 100 ms apart), success | [DXzurbATRQT, DdjM8xRNzk_, DeY58dONeuY, Dd6Uc27ssjp] |
| Sweep or wash (whoosh, riser) | 1-8 kHz; sweeps read 0.5-0.6 s (the detector's window, so order of magnitude), builds to 2.5 s, washes 1-3 s | scene change, reveal, white-out | [DeF8z3XoLdh, Dd_t1ZhNAoR, Dbmcud4IexE] |
| Gated tone, hit roll, counter ticks | gate 90-125 ms; 3-6 hits one 16th apart (0.13-0.18 s), rising; 3-5 mid ticks then a low lift | glitch; gather and reassemble; number steps | [DZUZITfz0Qu, DcYXIWbxzAN, Dd_t1ZhNAoR] |
| Dropout | 0.2-0.5 s gap or 0.85-2 s low-cut | the accent itself | section 5 |

At most two sounds on one frame (AUDIO.md). One UI-sound reel trails its picture by 0.12-0.7 s [DeY58dONeuY]; do not copy that, use the section 7 windows.

## 5. Music

Rule: one bass-forward bed on one tempo, pulled back for about 2 s, then a hard entry; make contrast by taking away.

- Tempo: of 15 usable readings, nine sit at 107-122 BPM [DZUZITfz0Qu 110, Db28edFqHTP 116, DdY8V8XKJD6 109, DeSvnCQIgs3 113, Dcs-MiOpO2V 107, DeaJ4yUg95f 122, and 120 in DcOIGDdss_L, DdwCXaQIHNU, DeF8z3XoLdh], four at 73-86 [Dc0izivoZNw, DcYXIWbxzAN, DeO1Rh7x5Qm, DeMrHF6qi0z], two faster [DeRpl8Yhrb2, DdCH-tFy7Wp]. Key is unreliable (F major in 17 of 30, voice-only reels included); use it only to tune sub hits to the bed's root [DcYXIWbxzAN].
- Setup, then entry: bass-free or pulled back for 1.4-2 s, first big arrival near 2.0 s [DdwCXaQIHNU +12 dB; DeF8z3XoLdh -34 dB then +17 dB; DeSvnCQIgs3 -31 dB then +23 dB at 1.97; DeaJ4yUg95f 0.94 s silence then +42 dB]. Or hit frame 1 [DcYXIWbxzAN, DdCH-tFy7Wp]. "2.0" means within a 0.5 s window.
- Cut the bed to the picture: length = beats x 60 / BPM [Dcs-MiOpO2V 12 beats = 6.72 s at 107.1; DdCH-tFy7Wp 8-beat loop of 3.04 s with the scene change on the loop boundary].

| Subtractive gesture | Length | Return | Reel |
|---|---|---|---|
| High-pass about 220 Hz | 4 beats, 62 frames | full band on the picture change, 37 ms later | [Db28edFqHTP] |
| Sub and bass void | 0.85 s (26 frames) | sub +33 dB at the slash, RMS only +3.4 dB | [DdY8V8XKJD6] |
| Bass mute over a scene change | 0.73 s | strongest hit on the downbeat | [DdCH-tFy7Wp] |
| Whole-mix dip | 0.5-1 s in [DeO1Rh7x5Qm], 0.3-0.7 s in [DcGaekAMU90] | bass re-entry (+8 dB in the first), bass hit on the cut (second) | [DeO1Rh7x5Qm, DcGaekAMU90] |
| True silence | 0.27-0.33 s (8-10 frames) | boom, or hit 60 ms before the cut | [DclkKscsRbs, DZUZITfz0Qu] |
| Long silence | 3.47 s | +63 dB re-entry, 14 cuts in 3.9 s | [DeRpl8Yhrb2] |

A gap near a third of a second reads as deliberate. After Effects: High-Low Pass with hold keyframes on the cutoff, or an Audio Levels expression: `t=thisComp.marker.key(1).time; v=linear(time,t-0.4,t-0.35,0,-30); time>=t?[0,0]:[v,v]`.

No reel demonstrated ducking (`mix.py` ducks by sidechain). Instead: remove the bed when narration starts [DeXDu86snYE 7.0-7.4 s]; bring it up only on emphasis [Dd_t1ZhNAoR]; swell bass +8 to +15 dB at section turns [DcGaekAMU90]; keep the vocal flat and move the bass about 50 dB [DeRpl8Yhrb2].

Endings, approximate: about 15 fades of 0.4-1.5 s [DXzurbATRQT, DdwCXaQIHNU]; about 14 hard stops [Dc0izivoZNw, DdCH-tFy7Wp, DeSvnCQIgs3]; silence under a logo hold 0.4-3.4 s [Dc0izivoZNw, DcOIGDdss_L].

## 6. Voice-over

Rule: dry, close, mono, low register, hard-levelled, top rolled off; picture follows phrases; effects fill the gaps.

- Pitch (f0 median, range, Hz): [DZCY6bjOsUQ 112, 86-168], [DeZ3P_8NeHT 108, 83-135], [DePvWkxNAun 132, 100-150], [DcGaekAMU90 141, 100-175]; the highest is [DeXtJrAtOcr 202, 190-250].
- Pace: 2.9-5.8 onsets per second [DeXtJrAtOcr, DcL6By1z4QE]; captions step 0.2-0.7 s per word [DePvWkxNAun, Dd6Uc27ssjp]. Fragments of 1.5-3 s with 0.3-0.5 s gaps at -36 to -49 dB [DePvWkxNAun]; keep breath dips of 6-12 dB every 3.5-5 s [DZCY6bjOsUQ].
- Processing, reconstructed not measured: high-pass 70-80 Hz; low shelf +3-5 dB at 100-250 Hz (bass over mid by 6 dB [DZCY6bjOsUQ], 12 dB [DcL6By1z4QE]); 3-6 dB gain reduction (LRA 1.6-3.1 [DZCY6bjOsUQ, Dd6Uc27ssjp, DeZ3P_8NeHT]); roll off above 6-8 kHz; mono; no reverb, or a 0.8-2.5 s return heard only in gaps [DePvWkxNAun]. Four voice-led reels overshot 0 dBTP [DeXDu86snYE, DcGaekAMU90, Dd_t1ZhNAoR, DZCY6bjOsUQ].
- Picture: cut on the first syllable of the next phrase, not the breath [DZCY6bjOsUQ: 9 of 11 cuts within 80 ms of an onset against 53% chance, modest evidence]. Big moves in pauses is a tendency [DePvWkxNAun].
- Gaps belong to effects, not the bed: typing ticks as speech thins, a 1-1.7 s mute, then a bass hit [Dd_t1ZhNAoR 8.6-10.3 into 10.33; Dd6Uc27ssjp].

## 7. Audio-visual sync policy

Rule: pick one sync mode per piece before editing. Percentages are cuts within 80 ms of an onset, against chance.

| Mode | Reels | Build |
|---|---|---|
| Grid-locked | [DdwCXaQIHNU 80% vs 50%, n=15], [DeF8z3XoLdh 100% vs 64%, n=5], [Dcs-MiOpO2V], [DdCH-tFy7Wp], [DcYXIWbxzAN] | cut on 0.25 or 0.5 s multiples |
| Hit-locked at big beats | [DZUZITfz0Qu 80% vs 68%, n=10], [Dc0izivoZNw 71% vs 54%, n=7], [DXzurbATRQT], [DeXDu86snYE] | hand-place impacts |
| Structure-locked, no cuts | [Db28edFqHTP], [DdY8V8XKJD6], [DeSvnCQIgs3] | drops on picture changes |
| Voice-paced | [DZCY6bjOsUQ 82% vs 53%, n=11], [DcGaekAMU90 75% vs 60%, n=48], [DeZ3P_8NeHT 81% vs 72%], [Dd6Uc27ssjp 52% vs 53%, n=23] | cut to phrases |
| Texture only | [DeMrHF6qi0z 38% vs 67%], [DeO1Rh7x5Qm], [DeaJ4yUg95f], [DeRpl8Yhrb2 about 9 hand matches in 71 cuts]; one sound per state, loosely timed [DeY58dONeuY] | bed under loose picture |

Of 28 reels with cuts, 22 beat chance and 6 fell below; among the 11 with 10 or more cuts the margin was -1 to +30 points, median +15. Onsets run at 3-6 per second, so chance is already 44-72%: judge by structure, not percentages. Median offset 0.0 s, 22 of 28 within 40 ms.

Windows (1 frame = 33 ms at 30 fps): impacts on the cut frame or up to 2 frames early [DZUZITfz0Qu 47-60 ms, Db28edFqHTP 37 ms], sometimes 7-20 ms late [DcYXIWbxzAN, DeF8z3XoLdh]; swells start 4-30 frames early [Dc0izivoZNw, DXzurbATRQT]; small UI sounds within 1 frame of contact.

Grid arithmetic: `f=(beat,bpm,fps=30)=>Math.round(beat*60/bpm*fps)`. At 120 BPM a beat is 15 frames and an eighth 7.5, so alternate 7 and 8; at 107.14 BPM a beat is 16.8 frames, so compute each beat from the formula. Median shot lengths, computed from the shot lists: 0.38-0.39 s in word-per-shot edits [DdwCXaQIHNU, Dcs-MiOpO2V], 1.0-1.8 s in voice-paced reels [DcGaekAMU90, Dd_t1ZhNAoR, DZCY6bjOsUQ].

## 8. Recipes per format

| Format | Build | Timing and ending |
|---|---|---|
| UI or SaaS promo, 15-35 s [Dc0izivoZNw, DXzurbATRQT, DdY8V8XKJD6, DeZOFtEMkuA] | bass bed at 73-120 BPM, or a 250-500 Hz pad with four sub events; hand-placed hits; ticks only at contacts | sub swell about 4 frames before a whip; 15-frame vacuum, then the biggest hit on the cursor press; 2-4 frame bass mutes before key hits [Dc0izivoZNw]; hard stop plus 0.4 s silence, or a 45-frame fade |
| Single take, no cuts [Db28edFqHTP, DdY8V8XKJD6, DeSvnCQIgs3] | one bed on a fixed 8th or 16th grid | pull back about 1 s, big step on the first full state; 4-beat low-cut; 0.5 s sub mutes at animation phases [DeSvnCQIgs3]; stop on black, or let highs fall over 15-30 frames |
| Kinetic type or logo sting, 6-15 s [DcYXIWbxzAN, Dcs-MiOpO2V, DdwCXaQIHNU, DeF8z3XoLdh] | mono sub and bass, 16th ticks, stabs, one rise or fall in the highs, no voice | track = whole beats; 0.125 s stutter under 0.2 s cards [DdwCXaQIHNU]; 0.5 s sub dip before the final slam; black cut on a bass gate-off [Dcs-MiOpO2V]; 1-1.5 s decay or hard stop |
| Glitch or hype edit [DZUZITfz0Qu] | gated 444 Hz tone at 90 ms, falling sweep, kick dropping from 500 Hz to under 50 Hz | hits 0.54, 0.54, 0.73 s; 10-frame mute, then a hit 2 frames before the cut |
| Voice explainer [DcGaekAMU90, Dd_t1ZhNAoR, DePvWkxNAun, DZCY6bjOsUQ] | section 6 voice; bass-only bed or none | bed swells at section turns; 0.3-0.7 s dip then a bass hit on the cut [DcGaekAMU90]; end on a 0.5 s fade, a 1.5 s bass-only tail, or a 3 s room tail [DePvWkxNAun] |
| Showreel, 60-100 s [DcOIGDdss_L, Dbmcud4IexE] | 120 BPM bed with a quiet pad pocket and chopped middle, or one tonal bed with bass hits on the largest jumps | sections 4-6 dB apart unless gating; 1.5 s log fade; 3.4 s silence under the badge |
| Song-led lyric or excerpt [DeRpl8Yhrb2, DeMrHF6qi0z] | a finished song as the only bed | bass in = chorus picture, bass out = verse [DeRpl8Yhrb2]; change on bass entries, not every beat; snippets: hard in-point, no fade [DeMrHF6qi0z] |

## 9. Mix checklist and commands

1. Lead layer chosen, three layers at most, no ambience bed.
2. Bass and hits mono, 250-500 Hz scooped.
3. First 1.4-2 s pulled back or a frame-1 hit; one dropout before the biggest hit.
4. Hits inside the section 7 windows; some big events silent on purpose.
5. Voice flat and dry; bed removed or automated.
6. Ending chosen: hard stop, 1-1.5 s fade, or silence under the hold.
7. Ceiling -1 dBTP; final encode re-measured; mono-sum and phone-speaker checks.

```
# measure
ffmpeg -hide_banner -nostats -i cut.mp4 -vn -af ebur128=peak=true:framelog=quiet -f null - 2>&1 | grep -E "^\s+(I|LRA|Peak):"
# normalise pass 1
ffmpeg -hide_banner -nostats -i cut.mp4 -vn -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null -
# pass 2: paste the pass 1 values
ffmpeg -i cut.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=X:measured_TP=X:measured_LRA=X:measured_thresh=X:offset=X:linear=true" -c:a aac -b:a 192k -ar 48000 final.mp4
# dual-mono sum, compare with the plain measure of final.mp4
ffmpeg -hide_banner -nostats -i final.mp4 -vn -af "pan=stereo|c0=0.5*c0+0.5*c1|c1=0.5*c0+0.5*c1,ebur128=peak=true:framelog=quiet" -f null - 2>&1 | grep -E "^\s+(I|LRA|Peak):"
# phase over time, +1 in phase (run in the output folder; drive colons break filter paths)
ffmpeg -i final.mp4 -vn -af "aphasemeter=video=0,ametadata=print:key=lavfi.aphasemeter.phase:file=phase.txt" -f null -
```

`loudnorm` falls back to dynamic mode when input LRA exceeds the target, so raise `LRA=` for gated pieces. A dual-mono loss over about 1 LU is my working threshold, not from the reels (one at correlation 0.89 lost 0.2 LU). 

## 10. Caveats

Nothing was listened to: layers, instruments, effects, tempo and key are inferred from spectrograms, onset bands, band levels and pitch tracks on a 0.5 s timeline; kick versus bass note and riser versus filter sweep cannot be separated. Detectors misfire (sweeps on speech, key biased by drones, flashes counted as cuts). Sync percentages are weak at 3-6 onsets per second and few cuts; picture times are good to 0.1-0.3 s. The sample is 30 reels from one platform and season, probably platform-encoded, so loudness, peaks and the soft top may reflect delivery. Recipe values are reconstructions, not settings.
