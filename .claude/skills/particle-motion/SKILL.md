---
name: particle-motion
description: Particle motion design - abstract tech particles, dust and bokeh, sparks, confetti, plexus networks, flow fields and curl-noise swirls, galaxy vortices, point clouds, logo and text formation from particles, disintegration and dissolves - with design rules (hierarchy, density and negative space, size tiers, lifecycle, colour and glow, depth) and motion rules (force-driven motion, emitters, turbulence, attractors, cause-and-effect bursts, chaos to order). Includes After Effects (CC Particle World, Particular, Form, Plexus), Blender Geometry Nodes simulation zones, HyperFrames/Canvas/Three.js and Higgsfield recipes. Use when the user asks for particles, particle effects, dust, sparks, confetti, plexus, flow field, disintegration/dissolve, Thanos snap effect, particle logo reveal, galaxy/swirl, magic dust, or abstract tech backgrounds.
---

# Particle motion

Particles are many small elements whose motion comes from **rules and forces**, not individual keyframes: an emitter births them, forces (velocity, gravity, drag, turbulence, attractors) move them, and they age and die. The craft is making thousands of things read as **one designed shape with a clear focal point**, not noise.

Pair with: `design-principles` (hierarchy, contrast), `layout-composition` (negative space), `cinematography-for-ai` (depth of field, camera), `y2k-chrome-motion` / `synthwave-motion` (sparkle and glow styles), `higgsfield-generate`. Design the key frames (the swarm's shapes) first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: CC Particle World, Particular, Form, Plexus, dissolves, logo formation, finishing.
- `references/blender.md`: Geometry Nodes simulation zone particles, curl noise, attractors, logo formation, rendering.
- `references/code-and-ai.md`: HyperFrames rules (deterministic, seek-safe), Canvas 2D and Three.js points, Higgsfield prompts.
- `references/history.md`: concepts and sources.

## 1. Design rules (every frame must pass)

| Element | Rule |
|---|---|
| Purpose | Particles do one job: build a form, guide the eye, punctuate a beat, or set atmosphere. Decide which before building. |
| Hierarchy | One hero particle mass (or the form it builds) + quieter ambient particles. Never uniform noise across the frame. |
| Density | Dense where attention should go, sparse elsewhere; keep real negative space. Density gradients show direction. |
| Size tiers | Three tiers: few large (soft, out of focus, foreground), some medium, many small. Sizes vary per particle. |
| Shape | One shape language per piece: dots, soft glows, streaks, squares/pixels, glyphs, shards or confetti chips. |
| Colour | 1–3 colours, often varying over lifetime (birth colour → death colour). Glow cores near white. |
| Blending | Additive/Screen for light particles on dark; Normal/Multiply for physical ones (confetti, dust on light). |
| Depth | Depth of field and parallax: near particles big and blurry, far ones small and sharp-ish; atmosphere fades the distance. |
| Lifecycle | Particles fade/scale in at birth and fade/shrink out at death. Nothing pops into existence or freezes mid-air. |
| Legibility | Type or logos formed by particles must resolve fully (or nearly) for a readable hold. |

**Palettes**
- Tech blue: `#0A0F1E` bg, `#2F7BFF`, `#6FE3FF`, `#FFFFFF` cores.
- Warm sparks: `#0B0606` bg, `#FF7A1A`, `#FFC24B`, `#FFF3D6`.
- Magic dust: `#140B26` bg, `#B26BFF`, `#FF6BD5`, `#FFE9FF`.
- Confetti: brand colours on light background, Normal blend.

## 2. Motion principles

1. **Forces, not keyframes.** Animate emitters and forces (birth rate, velocity, turbulence strength, attractor position); let the simulation move the particles.
2. **Natural variation.** Randomise speed, size, life and direction per particle (10–50% variation). Uniform particles look fake.
3. **Turbulence that flows.** Use curl noise / flow fields for organic swirling: particles stream and curl without bunching. Keep noise scale large relative to the frame for readable currents.
4. **Cause and effect.** Bursts fire on a cause (impact, beat, click, word landing). Particles react to objects passing (wake, displacement).
5. **Chaos to order (and back).** The most satisfying move: scattered particles converge into a logo/word, hold, then release back into chaos (or the reverse).
6. **Ease the system, not the particles.** Ramp birth rate and force strength smoothly; let individual motion stay physical (gravity arcs, drag).
7. **Lead with a hero.** A bright lead particle, spark or trail guides the eye before the mass arrives.
8. **Motion blur or streaks** on fast particles; slow ambient dust stays crisp or softly blurred by depth of field.
9. **Restraint and budget.** Enough particles to read as a mass, no more. Less density at text; kill particles before the next beat.
10. **Determinism.** Seeded randomness so renders and re-renders match (essential in HyperFrames and for client revisions).

## 3. Signature moves

| Move | How |
|---|---|
| Logo/text formation | Particles fly in from scatter (or a stream) and settle into the logo shape; the solid logo fades in under them; particles fade. |
| Disintegrate | The subject erodes from one side into particles that drift away on turbulence ("Thanos snap"). |
| Burst | Sparks/confetti/dots fire from an impact point with gravity and drag, then die. |
| Trail | Particles stream behind a moving lead object or along a path. |
| Flow field | Thousands of particles stream along curl-noise currents; slow, hypnotic background. |
| Plexus | Points connected by lines when close; network/tech/data look. |
| Vortex / galaxy | Particles orbit a centre, spiral in or out. |
| Swarm / flock | Boid-like groups move together, split, regroup. |
| Shape morph | A point cloud shifts from one shape to another (sphere → logo → text). |
| Bokeh ambience | Large soft out-of-focus dots drifting slowly behind the content. |
| Audio-reactive | Birth rate, size or turbulence pulse with the music. |

**Transitions:** dissolve to particles and re-form as the next scene, burst flash, particle wipe (a stream sweeps across and the next scene forms behind it).

## 4. Build process

1. **Define the job and the shapes:** what form the particles take at each key moment (scatter, stream, logo, burst).
2. **Pick the tool:** AE built-ins for simple dust/bursts, Particular/Form/Plexus if installed, Blender Geometry Nodes for big 3D systems and point-cloud morphs, Canvas/Three.js for HyperFrames.
3. **Block forces:** emitter, birth rate, life, velocity, gravity/drag, turbulence, attractors.
4. **Design the look:** shape, size tiers, colour over life, blending, glow, depth of field.
5. **Time it:** births and bursts on causes/beats, formation holds long enough to read, deaths before the next beat.
6. **Finish:** glow, motion blur, grade; check density and negative space on paused frames.

## 5. Critique checklist

- Is there a clear focal mass and real negative space?
- Do sizes, speeds and lifetimes vary?
- Do particles fade in and out (no pops or frozen particles)?
- Does turbulence flow smoothly (no jittery noise, no clumping)?
- Does the formed logo/text read clearly during its hold?
- Is every burst caused by something?
- Is the colour limited and glow controlled (no blown-out mush)?
- Is it deterministic (same result on re-render)?
