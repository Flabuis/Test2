---
name: glassmorphism-motion
description: Glassmorphism in motion - frosted translucent panels with backdrop blur, light edge strokes, soft shadows and vivid backgrounds; Apple-style Liquid Glass with refraction, edge lensing, specular highlights and gooey merging; and 3D glass objects with transmission, dispersion and iridescence. Covers legibility and contrast rules, and motion rules (living backgrounds, parallax between layers, light sweeps, blur focus pulls, liquid morphs). Includes After Effects, HyperFrames/CSS/GSAP and Blender recipes. Use when the user asks for glassmorphism, frosted glass, glass UI, Liquid Glass, iOS 26 style, translucent panels, glass 3D icons, refraction effects, or premium tech/product UI motion.
---

# Glassmorphism motion

Glassmorphism puts translucent "glass" layers over a colourful background: the backdrop shows through, blurred, so the layers feel physical and stacked in depth. It needs three things working together: **a vivid background, a believable glass material, and hierarchy that stays readable**.

Three variants:
- **Frosted glass UI (default):** semi-transparent panels, strong backdrop blur, a thin light edge, soft shadow (the 2020–21 trend; still the base of most glass UI).
- **Liquid Glass (Apple, 2025):** less blur, real refraction and lensing at the edges, specular highlights that react to movement, elements that merge and split like liquid.
- **3D glass objects:** rendered glass icons and shapes with transmission, dispersion and iridescence over gradients.

Pair with: `design-principles` (contrast, hierarchy), `typography`, `layout-composition`, `motion-reel` (product reels). Design hero frames as stills first ([[motion-is-graphic-design]]).

References:
- `references/after-effects.md`: backdrop blur panels, edge lensing, specular sweeps, gooey merges, living backgrounds.
- `references/css-gsap.md`: `backdrop-filter`, SVG lensing, gooey filter, GSAP moves for HyperFrames.
- `references/blender.md`: 3D glass materials, lighting and render settings.
- `references/history.md`: background, Apple guidance, sources.

## 1. Visual language (every hold frame must pass)

| Element | Rule |
|---|---|
| Background | Glass needs something to show. Vivid gradient orbs, mesh gradients, photos or video, with enough colour and some shape. Not busy detail; not flat and dull. |
| Panel fill | White at 10–25% (light) or near-black at 20–40% (dark). Slight tint from the brand colour is fine. |
| Backdrop blur | Frosted: 20–40 px at 1080 wide (16–24 px in UI points). More blur = more legible, less "see-through". Liquid Glass: light blur (4–10 px) plus refraction. |
| Edge | 1–2 px inner stroke, white gradient 60% → 10% from the light side. Without it panels bleed into the background. |
| Light | One light direction for the whole piece (usually top-left): brighter top-left edge, specular highlight there. |
| Shadow | Large, soft, low opacity (blur 40–80 px, 10–20%), offset down. Never hard. |
| Corners | Generous, consistent radii (24–48 px at 1080); Liquid Glass uses capsules and concentric radii. |
| Grain | 2–4% noise on the glass to sell frost and stop gradient banding. |
| Layers | 2–3 glass levels at most. Don't stack glass on glass on glass; hierarchy muddies. |
| Type | Clean sans (SF Pro, Inter, Manrope, Satoshi). White or near-black chosen for contrast; semibold or bold on glass. |
| Contrast | Body text ≥ 4.5:1, large text ≥ 3:1 against the *worst* part of the blurred background behind it. Add a darker/lighter tint behind text if needed. |

**Starter palettes (backgrounds)**
- Aurora: `#7B5CFF` violet, `#FF6FD8` pink, `#3BC9FF` cyan, `#0B0F2A` night.
- Sunset: `#FF8A3D` orange, `#FF4D8D` rose, `#FFD166` gold, `#2A1B3D` plum.
- Fresh: `#3DDC97` mint, `#2F80ED` blue, `#A0F0FF` ice, `#F4F7FB` mist.

## 2. Motion principles

1. **Living background.** Background orbs drift slowly (8–20 s loops), so the glass constantly shows change through it. This is what makes glass read as glass.
2. **Parallax depth.** Glass layers move faster and further than the background; closer layers more. Even small moves sell the depth.
3. **Smooth, physical easing.** Springy but controlled (ease-out with a light settle). Nothing snaps; glass has mass.
4. **Light reacts.** A specular sheen sweeps across a panel when it arrives or tilts; highlights shift with angle.
5. **Blur as focus.** Elements can enter blurred and sharpen (a focus pull). Raising the backdrop blur pushes the background back when a panel takes focus.
6. **Refraction on movement (Liquid).** As glass passes over content, the content bends at the edges (lensing). Movement makes this visible; static frames hide it.
7. **Liquid merge and split.** Liquid Glass elements stretch, merge into neighbours and split off like droplets (gooey motion) with a jelly settle.
8. **Restraint.** One or two glass elements move at a time. Avoid long cross-fades between glass layers (double blur looks muddy).
9. **Smooth frame rate.** 30–60 fps, motion blur on for fast moves. Never posterize.

## 3. Signature moves

| Move | How |
|---|---|
| Panel rise | Glass card slides up 60–120 px with ease-out and fades in its fill; the backdrop blur ramps from 0 to full. |
| Light sweep | A soft diagonal sheen crosses the panel once on arrival. |
| Stack reveal | Cards fan out in Z with parallax, each with a slightly different blur and shadow. |
| Focus pull | The background blur increases as a panel comes forward; it drops when the panel leaves. |
| Tilt | A card rotates in 3D a few degrees with the specular highlight following the tilt. |
| Liquid morph | A capsule button stretches and splits into a menu, or droplets merge into a bar. |
| Lens pass | A glass circle or capsule moves over text or an image, magnifying and bending it at the edges. |
| Glass type | Big headline cut out of glass (blurred backdrop inside the letterforms, light edge). |
| 3D glass hero | A rendered glass icon turns slowly, refracting the gradient behind, with dispersion fringes. |

**Transitions:** blur-through (the scene blurs out into the next scene's background), glass panel wipe (a large frosted panel slides across, revealing the next scene behind it), liquid merge into the next element.

## 4. Build process

1. **Background first:** design the gradient orb field or footage and its slow motion loop.
2. **Hero frames:** design 2–4 still frames with glass panels; check contrast on the worst background moment.
3. **Glass system:** fix blur, fill opacity, edge stroke, shadow, radius and light direction for all panels.
4. **Animate:** background loop → panel entrances → parallax → light sweeps → details.
5. **Check:** scrub the full background loop under every text panel for contrast; watch for banding (add grain) and muddy double-blur moments.

## 5. Critique checklist

- Is the background vivid enough to show through, but not so busy it fights the text?
- Is text contrast safe at every moment of the background loop?
- Does every panel have an edge stroke and a consistent light direction?
- Are shadows soft and low opacity?
- Are there more than 3 glass layers stacked anywhere?
- Is the background moving, and do the layers parallax?
- Any banding in gradients or blur? Add grain.
- Liquid: does the refraction/lensing read during motion, and do merges settle with a soft jelly?
