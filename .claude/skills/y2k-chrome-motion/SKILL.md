---
name: y2k-chrome-motion
description: Y2K chrome / Y2K Futurism in motion - liquid metal and mirror-chrome type, iridescent and holographic gradients, inflated bubble forms, translucent candy plastic, sparkles, lens flares, wireframe globes, cyber-sigil shapes and early-2000s UI - with motion rules (sheen sweeps, moving reflections, liquid melts and morphs, chrome spins, sparkle twinkles, flare passes, glitch cuts, bouncy pops, glow). Includes After Effects, Blender, CSS/GSAP and Higgsfield recipes. Use when the user asks for Y2K, Y2K chrome, liquid metal, chrome text, metallic type, holographic, iridescent, cybersigilism, Frutiger Aero, early-2000s or millennium futurism, or fashion/music/tech hype reels.
---

# Y2K chrome motion

Y2K Futurism (late 1990s – early 2000s, revived since the late 2010s) is the look of millennium tech optimism: **liquid chrome, iridescent gradients, bubbly inflated forms, glossy plastic and lens flares**. Chrome is the hero material. Today the strongest work uses only a few of these signals, aimed at the hero element, not everywhere.

Fit: fashion, music, streetwear, beauty, creator brands, tech launches, events. Poor fit where trust is the main job (finance, health) unless used very lightly.

Pair with: `typography` (display type quality), `design-principles`, `layout-composition`, `glassmorphism-motion` (translucent layers), `clay-3d-motion` (inflated forms), `higgsfield-generate`. Design hero frames as stills first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: 2D and 3D chrome type, sheen, liquid melt, sparkles, glow, flares, glitch.
- `references/blender.md`: chrome, liquid metal and iridescent materials, lighting, bloom.
- `references/css-gsap-ai.md`: CSS chrome type and sheen, holographic gradients, GSAP moves, Higgsfield prompts.
- `references/history.md`: origins, sub-styles and sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Chrome | Mirror metal with high-contrast banding: bright white highlights next to near-black reflections, cool steel midtones. The contrast is what reads as chrome. |
| Liquid | Molten, blobby, dripping silhouettes; rounded, melted edges. |
| Iridescence | Holographic gradients (pink, lilac, ice blue, mint) on chrome edges, backgrounds or plastic. |
| Forms | Inflated bubble shapes, orbs, rings, wireframe globes, 4-point sparkles, cyber-sigil (sharp tribal chrome) shapes, butterflies, early-2000s UI windows. |
| Plastic | Translucent candy colours (iMac G3 style): see-through tinted shells with glossy highlights. |
| Light | Glints, star sparkles, lens flares, bloom/glow on highlights. Use 1–3 flares per frame, not dozens. |
| Background | Either deep black/navy (chrome pops), a soft baby-blue/lilac sky gradient, or an iridescent gradient. Keep it simpler than the hero. |
| Type | Wide, extended or techno faces (Audiowide, Orbitron, Michroma, Syncopate, Eurostile/Microgramma Extended, Monument Extended) for chrome headlines; bubble faces (Rubik Bubbles, inflated custom type) for playful variants; thin wide-tracked sans for small text. |
| Restraint | One chrome hero per frame; the supporting text stays flat (cool steel or white). |

**Palettes**
- Liquid chrome: white `#F6FBFF`, silver `#C9D1DA`, steel `#8FA0B2`, gunmetal `#2E3742`, near-black `#05060A`, accent ice `#9FE7FF`.
- Holo pop: pink `#FF9DE2`, lilac `#C8A8FF`, ice `#9FE7FF`, mint `#B5FFD9`, chrome white `#F6FBFF`, sky `#BFE3FF`.
- Cyber: acid lime `#C6FF3D`, hot magenta `#FF2BD6`, chrome, black `#000000`.

Chrome gradient (works for 2D type and as a reference for the reflection banding):
`linear-gradient(105deg,#3a4350 0%,#f6fbff 20%,#8fa0b2 38%,#ffffff 50%,#2e3742 64%,#eef6fd 82%,#6b7888 100%)`

## 2. Motion principles

1. **Reflections move.** Chrome is only alive when its reflections travel: animate the environment, the sheen or the object rotation, never leave chrome static.
2. **Sheen sweep.** One bright sheen crosses the hero during each hold (about 0.6–1 s). Not on loop every second.
3. **Liquid behaviour.** Chrome melts, drips, ripples and re-forms; morphs flow like mercury with a soft wobble settle.
4. **Hero spins.** Logos and objects turn in 3D (turntables, flips) to show off reflections; ease in and out.
5. **Sparkle punctuation.** 4-point sparkles twinkle (scale up with a quick rotation, then fade) on accents and beats.
6. **Playful energy.** Bouncy elastic pops, zoom bursts, quick UI window pop-ups, cursor clicks. Faster cutting than glass or clay, but still smooth 30–60 fps.
7. **Glow and flare on hits.** A flare or bloom flash on major beats; a flare passes as the camera or object moves.
8. **Digital texture in transitions.** Short glitch, RGB split, scanlines or pixelation on cuts (2–6 frames), not on holds.
9. **Restraint.** Keep 1–2 effects per moment. Chrome + sheen + one sparkle reads premium; chrome + glitch + flare + holo + sparkles reads cheap.

## 3. Signature moves

| Move | How |
|---|---|
| Chrome title | Extended chrome headline lands with a light settle; a sheen sweeps; a sparkle pops on a corner. |
| Mercury morph | A liquid chrome blob flows and reshapes into the logo or word. |
| Melt / drip | Chrome type drips or melts down, then re-forms. |
| Turntable | Chrome logo spins 180–360° in 3D, reflections streaking across. |
| Flare pass | A lens flare streaks across as the camera pushes; bloom flashes on the hit. |
| Holo shift | Iridescent gradient hue cycles across a surface. |
| Bubble pop | Inflated bubble type or orbs pop in with elastic overshoot. |
| UI pop-ups | Early-2000s window dialogs, loading bars and cursors pop in and stack. |
| Wireframe globe | Spinning wireframe globe or orbit rings behind the hero. |
| Glitch cut | 2–6 frame RGB split + scanline flash into the next scene. |

**Transitions:** white flash + flare, chrome wipe (a reflective bar sweeps across), liquid morph, glitch cut, zoom through a tunnel or ring.

## 4. Sub-styles

- **Liquid chrome (default):** silver mercury forms, extended type, black or sky backgrounds.
- **Cyber-sigil chrome:** sharp tribal/thorny chrome shapes and gothic or blackletter chrome type; darker, edgier (2020s revival).
- **Holographic pop:** iridescent pastel gradients, bubble type, sparkles; playful.
- **Frutiger Aero (adjacent):** glossy aqua, bubbles, nature + tech, sky blues and greens; lighter and optimistic (mid-2000s).
- **Retro 80s chrome (cousin):** horizon-reflection chrome (sky blue to dark horizon line to warm ground), neon grids and sunsets. Not strictly Y2K; don't mix it in by accident.

## 5. Build process

1. **Pick a sub-style and 2–3 signals** (e.g. chrome type + sheen + sparkles).
2. **Hero frames:** design 2–4 stills; check the chrome banding reads at phone size.
3. **Build chrome:** 3D (Blender or AE Advanced 3D) for spins and liquid; 2D gradient/bevel methods for flat type.
4. **Animate:** hero entrances → reflections and sheen → sparkles and flares on beats → transitions.
5. **Check:** chrome reads as chrome (strong highlight/dark contrast), effects are restrained, type stays legible.

## 6. Critique checklist

- Does the chrome have strong banding (bright highlights *and* dark reflections)? Grey gradients read as plastic.
- Do the reflections move?
- Is there one hero, with supporting elements kept flat?
- Count the effects per moment: more than 2 at once? Cut.
- Are flares and glows tasteful (not covering type)?
- Is the extended/techno type legible at phone size?
- Is the palette within the chosen sub-style?
