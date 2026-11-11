---
name: clay-3d-motion
description: Clay 3D style in motion - soft rounded plasticine forms, matte subsurface clay materials, pastel or playful palettes, fingerprints and handmade imperfection, soft miniature-set lighting and depth of field - plus motion rules for both smooth "claymorphism" (squash and stretch, jiggle, inflate pops, blob morphs) and stop-motion claymation (animating on twos, boiling surfaces, holds, micro-jitter). Includes Blender (via the blender MCP), After Effects compositing and Higgsfield prompt recipes. Use when the user asks for clay 3D, claymation, claymorphism, plasticine, play-doh look, soft 3D, cute 3D characters, Aardman-style, stop-motion 3D, or tactile handmade 3D motion.
---

# Clay 3D motion

Clay 3D makes digital work feel **touchable**: soft rounded forms, matte material with a little light passing through, and small handmade imperfections, shot like a tabletop miniature. There are two motion flavours:

- **Smooth clay (claymorphism):** 24–30 fps, bouncy, soft-body squash and stretch. Brand and UI reels.
- **Claymation (stop-motion):** on twos (12 fps), held poses, the surface "boils" between frames. Handmade, charming, Aardman/Laika feel.

Pick one per piece. Don't mix them.

Pair with: `cinematography-for-ai` (lenses, miniature camera), `design-principles` (colour, hierarchy), `layout-composition`, `higgsfield-generate` (style frames, image-to-video). Design hero frames as finished stills first ([[motion-is-graphic-design]]).

References:
- `references/blender.md`: modelling, clay shader, lighting, camera, stop-motion setup, render; Python for the `blender` MCP.
- `references/after-effects-and-ai.md`: compositing passes, posterize, grain, and Higgsfield prompts.
- `references/history.md`: claymation history, studios and sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Form | Chunky, rounded, inflated. Big bevels, no sharp edges. Simple primitives (spheres, capsules, rounded boxes, noodles). |
| Proportion | Cute and toy-like: big heads, short limbs, thick parts. Thin parts break the clay illusion. |
| Material | Matte clay: high roughness (0.55–0.75), low specular, a little subsurface scattering. Never glossy plastic. |
| Surface | Subtle imperfection: soft lumps, faint fingerprints, tiny noise bump. Smooth claymorphism keeps it nearly invisible; claymation shows it. |
| Colour | Pastels (claymorphism) or saturated playful colours (claymation). 4–6 hues + a cream/off-white. Avoid pure black and pure white; use deep navy and cream. |
| Colour variation | Slight hue/value variation across a surface, as real clay is never perfectly uniform. |
| Light | Soft, large light sources, gentle contact shadows, ambient occlusion in creases. A cool fill against a warm key. |
| Set | Tabletop miniature: seamless curved backdrop (cyc), a floor the objects sit on, props at the same handmade scale. |
| Camera | 50–85 mm, slight high angle (20–35°), shallow depth of field for the miniature feel. |
| Type | Rounded, chunky faces (Fredoka, Baloo, Nunito Black, Cooper Black, Recoleta) built as 3D clay letters or flat type on the comp. |

**Starter palettes**
- Pastel clay: cream `#F6EEE3`, peach `#FFB8A1`, butter `#FFE29A`, mint `#A8E6CF`, sky `#9BD1F9`, lilac `#C9B6F2`, navy `#2B2F4C`.
- Playful claymation: tomato `#E8503A`, sunflower `#F6C744`, grass `#5BB55B`, ocean `#2F7FD8`, plum `#7A4E9C`, cream `#F4E9D8`.

## 2. Motion principles

**Both flavours**
1. **Weight.** Everything has mass: it eases in and out, lands with a squash, and settles.
2. **Squash and stretch, volume preserved.** Stretch along the motion, squash on impact. When Y scales by s, X and Z scale by 1/√s.
3. **Soft contacts.** Objects press into surfaces and each other, then recover. Nothing clicks rigidly together.
4. **Overlap and jiggle.** Soft parts (ears, bellies, blobs, toppings) lag and wobble 2–6 frames after the main body stops.
5. **Arcs and anticipation.** Wind up before jumps and throws; travel on arcs.
6. **Tabletop camera.** Slow, steady moves, like a motion-control rig on a miniature set. No impossible flying cameras.

**Smooth clay (claymorphism)**
7. **Bouncy timing.** Inflate pops (0 → 115 → 92 → 100% with squash), elastic settles, playful but readable.
8. **Blob morphs.** Shapes melt and merge into new shapes (metaballs, remesh, shape keys).
9. **Smooth 24–30 fps** with motion blur.

**Claymation (stop-motion)**
10. **On twos.** 12 poses per second (hold every pose 2 frames at 24 fps). Fast actions can go on ones; slow holds on threes.
11. **Boil.** The surface detail (fingerprints, noise, colour variation) changes on every pose, so the clay looks re-handled.
12. **Micro-jitter.** Tiny random position/rotation offsets (0.2–0.5 mm scale) per pose on objects and camera; tiny exposure flicker (1–2%).
13. **No motion blur**, and holds stay mostly still apart from the boil.

## 3. Signature moves

| Move | How |
|---|---|
| Inflate pop | Object grows from flat to full with overshoot and squash. |
| Squish land | Drop, squash on contact, rebound, jiggle settle. |
| Press and stamp | A shape presses into a clay slab, leaving an imprint (logo reveal). |
| Noodle draw | A clay noodle (round curve) extrudes along a path to write a word or line. |
| Blob merge | Two blobs merge into one, then reshape into the next object. |
| Roll in | Ball rolls in on an arc, squashes, unrolls into a character or logo. |
| Replacement face | Claymation: mouth and eye shapes swap per pose. |
| Tabletop push | Slow dolly or slider move across the miniature set with shallow focus. |
| Hand-made wipe | A clay slab or rolling pin flattens across the frame into the next scene. |

## 4. Build process

1. **Look frame:** generate or build 1–2 hero stills to lock palette, form language and lighting (Higgsfield prompt in references).
2. **Model:** primitives with big bevels and subdivision; inflate 2D logos and type; noodles from curves. Save .blend files in `Cluads Work Folder\clay\`.
3. **Shade:** one master clay material with per-object colour (and a small colour variation); add fingerprints and lumps to taste.
4. **Light and set:** cyc backdrop, soft key/fill/rim, AO, shallow DOF.
5. **Animate:** blocking poses → splines with squash, stretch and overlap. For claymation, switch keys to stepped/twos and enable the boil.
6. **Render and finish:** Cycles (or EEVEE for speed), then composite in AE: grade, grain, posterize for claymation.
7. **Check:** pause on any frame. It should look like a photo of a real handmade miniature.

## 5. Critique checklist

- Does it read as clay, not plastic? (Too shiny → raise roughness, lower specular.)
- Are there any sharp edges or thin parts? Round and thicken them.
- Is the surface too perfect? Add slight lumps and colour variation.
- Is it too dirty? Fingerprints should be subtle unless it's deliberate claymation.
- Do impacts squash, and do soft parts jiggle after stops?
- Is the volume preserved during squash and stretch?
- Claymation: is it really on twos, with the boil changing per pose and no motion blur?
- Is the camera behaving like a real tabletop rig, with believable depth of field?
