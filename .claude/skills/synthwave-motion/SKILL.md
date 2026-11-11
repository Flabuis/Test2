---
name: synthwave-motion
description: Synthwave / Outrun / retrowave in motion - neon perspective grids racing to the horizon, segmented sunsets, wireframe mountains, palm silhouettes, starfields, 80s horizon-chrome and neon-tube type, lasers, VHS and CRT texture - with motion rules (endless forward drive, beat-pulsing neon, neon flicker-on, chrome title slams with star glints, slow sun sets, parallax, VHS glitch transitions). Covers Outrun, Darksynth, Dreamwave, Laser/Tron and Arcade sub-styles, with After Effects, Blender, CSS/GSAP and Higgsfield recipes. Use when the user asks for synthwave, outrun, retrowave, 80s retro, neon grid, retro sunset, Miami Vice / Kavinsky / Stranger Things style titles, darksynth, or VHS 80s.
---

# Synthwave motion

Synthwave takes 1980s excess (arcade games like Out Run, action movies, sports cars, neon, VHS) and modernises it until it's only just recognisable. The scene is almost always the same **dream drive at dusk: a neon grid racing to the horizon under a giant segmented sun**. It's music-led, so motion is beat-driven.

Pair with: `typography` (title lettering), `cinematography-for-ai` (drive shots), `y2k-chrome-motion` (different era: don't mix Y2K liquid chrome into 80s horizon chrome), `higgsfield-generate`, `motion-reel` (beat grids). Design hero frames as stills first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: grid floor, sun, mountains, starfield, horizon-chrome and neon type, lasers, VHS/CRT finish.
- `references/blender.md`: 3D grid terrain, sun shader, fog, bloom, looping drives.
- `references/css-gsap-ai.md`: CSS grid/sun/neon, GSAP moves, Higgsfield prompts.
- `references/history.md`: origins, sub-styles, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Grid | Neon perspective grid on the floor, lines converging to a central vanishing point, fading into haze at the horizon. Magenta or cyan. |
| Sun | Big circle on the horizon, gradient yellow → orange → pink top to bottom, cut by horizontal slits that get thicker toward the bottom. |
| Landscape | Silhouette or wireframe mountains, palm trees, a road, sometimes a sports car or city skyline. Background dark, midground wireframe, foreground grid. |
| Sky | Gradient from near-black/navy at the top to violet, magenta and orange at the horizon. Starfield in the dark top. |
| Composition | Strong central symmetry: horizon at about the middle or lower third, sun centred, vanishing point centred. |
| Glow | Everything bright glows: neon lines, sun, type. Bloom is the main texture. |
| Type | Horizon chrome (sky-blue to white top half, hard dark horizon line, warm orange/brown bottom half, star glint) for titles; neon script or tube type (Mr Dafoe, Streamster, Monoton) for subtitles; extended sans (Eurostile Extended, Michroma) or arcade pixel (Press Start 2P) for small text. |
| Texture | Optional VHS/CRT: scanlines, slight chromatic aberration, tracking noise, grain, soft bloom. Keep subtle on holds. |

**Palettes**
- Outrun: night `#0B0221`, deep purple `#2A0B4A`, magenta `#FF2BD6`, cyan `#00F0FF`, violet `#8C2BFF`, sunset orange `#FF8A00`, sun yellow `#FFD319`.
- Darksynth: black `#050505`, blood red `#FF1E3C`, crimson `#8B0015`, steel `#A8B3C7`.
- Dreamwave: dusk lilac `#B39DDB`, pink `#FF9ECD`, peach `#FFC3A0`, teal `#5EE6D0`, navy `#1B1F4B`.

## 2. Motion principles

1. **Endless drive.** The grid scrolls toward the camera at constant (linear) speed, looped seamlessly. The world never stops moving.
2. **Beat-locked neon.** Synthwave sits around 80–118 BPM. Grid brightness, sun glow and neon accents pulse on the kick or snare; cuts and title hits land on bars.
3. **Slow epic layers.** The sun sets or rises very slowly; its slits scroll down. Mountains parallax slowly, stars barely move. Big, calm background against a fast floor.
4. **Neon ignition.** Neon type flickers on like a real tube (an irregular on/off sequence over 0.3–0.8 s), then holds with a faint hum flicker.
5. **Chrome title slam.** Horizon-chrome titles zoom or slam in from depth, settle, then a star glint and lens flare cross on the beat.
6. **Laser sweeps.** Thin laser beams and light streaks sweep across on transitions.
7. **Drive camera.** Gentle sway, slight roll on curves, and slow push-ins. Never handheld chaos.
8. **VHS on transitions.** Tracking glitches, RGB split and noise bursts on cuts (2–8 frames); holds stay clean apart from light scanlines.
9. **Smooth playback.** 30–60 fps (or 24 with motion blur) for the drive; the VHS overlay supplies the retro grit.

## 3. Signature moves

| Move | How |
|---|---|
| Grid drive | Floor grid scrolls endlessly toward the camera, fading at the horizon. |
| Sunset | The segmented sun slowly sinks; its slits scroll; glow pulses on the beat. |
| Title slam | Chrome title flies in from the vanishing point, settles, star glint + flare. |
| Neon ignite | Script subtitle flickers on, then hums. |
| Grid pulse | Grid lines flash brighter on each kick. |
| Laser sweep | Beams sweep across the sky or floor on a transition. |
| Wireframe reveal | Mountains or a car draw on as glowing wireframes. |
| Rewind | VHS rewind (fast backwards with tracking lines) as a transition or callback. |
| Arcade pop | Pixel text and score counters pop in on beats. |

**Transitions:** VHS glitch cut, laser wipe, white flash + flare, push through the sun, cut on the bar.

## 4. Sub-styles

- **Outrun (default):** sunset drive, palms, car, magenta/cyan/orange, optimistic nostalgia.
- **Darksynth:** black and red, aggressive, cyberpunk, horror-movie edge; harder cuts, more glitch.
- **Dreamwave / chillwave:** soft pastel dusk, slower, hazier, softer glow.
- **Laser / Tron grid:** pure wireframe and laser lines on black, very clean, cyan/magenta.
- **Arcade:** pixel type, score counters, 8-bit sprites, CRT curvature.
- Vaporwave (statues, Windows 95, pastel irony) is a different aesthetic; don't mix it in unless asked.

## 5. Build process

1. **Music first:** get the track and BPM; mark bars and kicks.
2. **Hero frame:** design the master scene still (grid, sun, sky, mountains, title) in the chosen palette.
3. **Build the world:** grid + sun + sky + mountains + stars in AE (2.5D) or Blender (3D), as a seamless loop.
4. **Titles:** horizon-chrome title, neon subtitle.
5. **Animate to the beat:** drive loop, pulses on kicks, title hits on bars, transitions on phrases.
6. **Finish:** bloom/glow, light VHS/CRT pass, grade.
7. **Check:** pause on a frame: symmetrical, glowing, readable title, clear horizon.

## 6. Critique checklist

- Is the composition centred, with a clear horizon and vanishing point?
- Does the grid fade into the horizon (no hard cutoff)?
- Is the sun segmented, with slits thicker toward the bottom?
- Does the palette stay within the sub-style?
- Is the glow bright but the title still legible?
- Does the motion lock to the beat (pulses, cuts, hits)?
- Is the VHS texture subtle on holds and stronger only on transitions?
- Does the chrome read as 80s horizon chrome, not Y2K liquid chrome?
