---
name: web-3d-design
description: Plan, design, build and critique websites, especially 3D and motion-led sites - web design principles (hierarchy over the F-pattern, grids, 60-30-10 colour, H1/H2/P type roles, conversion = clarity + scannability + motivation), UX structure (sitemap, wireframes, hero, CTA, case studies), the LIFT layout check and temporal flow, design systems and tokens (brand/alias/mapped, surface/border/text/icon, dark mode, component states), Tailwind v4, Three.js and React Three Fiber (scenes, GLB/gltfjsx workflow, lighting recipes, video and decal textures, cursor tilt, star fields), GSAP ScrollTrigger scroll storytelling (pin, scrub, Apple-style product pages), performance, accessibility, client process and Claude Design workflows. Use when the user asks to build or design a website, landing page or portfolio, a 3D website, Three.js / R3F / WebGL scene, scroll animation, Apple-style product page, design system or design tokens, Tailwind styling, or wants a website critiqued or improved.
---

# Web & 3D web design

A website is **graphic design that moves and responds**. Design the key screens (mobile and desktop) as finished frames first, then build the motion and interaction between them, the same way you block key frames before animating ([[motion-is-graphic-design]]).

Pair with: `design-principles`, `layout-composition` (LIFT), `typography`, the style skills (`glassmorphism-motion`, `synthwave-motion`, `particle-motion`, `isometric-motion`, `low-poly-motion`…) for the look, `higgsfield-generate` for imagery, `motion-reel` for launch videos of the site.

On the user's PC: web projects go in `C:\Users\basha\Motion Design\WebBuilding\`, the reference notes are mirrored in `C:\Users\basha\Motion Design\Training Data\Web Design Principles\`, and the source videos (transcripts + frames) are in `...\Training Data\Principles study\`.

## References (read the one you need before working)
| File | Use for |
|---|---|
| `references/01-web-design-fundamentals.md` | Grid, spacing, type, colour, hierarchy, responsive |
| `references/02-ux-structure-and-content.md` | Process, sitemap, home page anatomy, case studies, copy, handoff |
| `references/03-3d-web-threejs.md` | Three.js mental model (AE/Blender → Three), materials, lights, shaders, post, style ↔ technique map |
| `references/04-motion-and-scroll.md` | Motion principles, GSAP, ScrollTrigger, Lenis, signature interactions, reduced motion |
| `references/05-performance-accessibility-shipping.md` | Budgets, 3D perf rules, a11y, SEO, hosting |
| `references/06-critique-checklist.md` | Scored review of any site |
| `references/07…12-study-notes-*.md` | The Futur reviews, Self-Made Web Designer (7-min principles, client process), Satori layout/LIFT/grids, Flux Academy basics |
| `references/13-study-notes-jsm-threejs-course.md` | **3D playbook**: model workflow, lighting recipes, ~20 interaction patterns, scroll recipes, responsive/perf (6 real builds) |
| `references/14-study-notes-tailwind-v4.md` | Tailwind v4 utilities, breakpoints, dark mode, `@theme` / `@layer` / `@utility` |
| `references/15-study-notes-fireship-threejs-portfolio.md` | Minimal vanilla Three.js scroll-camera portfolio and modern upgrades |
| `references/16-study-notes-design-systems-figma.md` | Design tokens, collections, colour-scale maths, component rules, AI skills, handoff |
| `references/17-study-notes-claude-design-workflow.md` | Claude Design process: spec → reference → generated system → code |
| `assets/starter-scene.html` | Working single-file Three.js scene (CDN import map, lights, OrbitControls, loop, resize) |

## 1. Workflow
1. **Brief:** site type and goal (shop = buy, media = read/watch, marketing = enquire, app = task), audience, the one action, brand keywords (e.g. "refined rustic").
2. **Sitemap**, then **content-only wireframe** (section purposes, no visual decisions) or box wireframe if layout is the question.
3. **Key screens:** hero + 1–2 sections, mobile and desktop. Use a real visual reference, not adjectives.
4. **Tokens / design system** extracted from those screens (section 4).
5. **Beat-map the page** like a reel shotlist: each section = punch / linger / pulse / release (temporal flow). Decide where 3D and scroll moments go.
6. **Build:** pick the stack (section 5) → layout → 3D → motion.
7. **Ship:** perf + a11y pass → critique (`06`) → deploy.
8. **Present with reasons** (a Loom or call explaining *why*), not just a URL.

## 2. Design rules that decide most outcomes
- **One leverage point per screen** (scale, contrast, position, isolation). Squint test. **Hierarchy, not the F-pattern**: people scan in many patterns.
- **Hero:** the headline matters more than the image, and it must hook above the fold. No rotating carousels.
- **CTA:** solid fill, the accent (10% of 60-30-10), the highest contrast in its section. **Never a ghost button for the primary action.** Repeat it at the end.
- **Type roles:** one H1 per page, an H2 per section, plain readable P (16px+, 45–75ch, line-height 1.5–1.7). Two typefaces max.
- **Grid:** 12 → 8 → 4 columns. Spacing on a 4/8-pt scale. White space doesn't have to be white (sky, blur, empty cells). Break the grid with one element only.
- **Conversion test for every section:** **clear** (who, what next, why care), **scannable**, **motivating**. Design for the visitors, not the designer or client.
- **Depth, not flatness:** a light source, shadows, layering, selective focus, vignette. Art-direct imagery (bespoke > stock; high-res, sharp, lit, cropped, graded).
- **LIFT:** Leverage point, Internal rhythm (consistent spacing + one planned disruption), Friction with flow kept, Transferability (thumbnail, dark/light, mobile).

## 3. Motion rules
- Motion must have a job. **Overlap** moves (stagger 0.03–0.1 s), no dead frames, **strong first second** (hero animates within ~300 ms).
- Durations: micro 150–250 ms · UI 300–500 ms · hero/story 0.8–1.6 s. Easing: enter `power3/expo.out`, exit `power2.in`, A→B `power2.inOut`. Linear only for loops and scrub.
- Animate only `transform`/`opacity`. Respect `prefers-reduced-motion` (no scrub, parallax or autoplay; simple fades).
- **Scroll storytelling (GSAP):** `registerPlugin(ScrollTrigger)` once; `useGSAP` with scope. Recipes: pinned section + `scrub` timeline; pinned video → logo-mask reveal; screenshots exploding outward on scrub; product spin with `.call()` swapping the screen video per caption (preload the videos); staggered bento reveal. Details in `13` §6 and `04`.

## 4. Design system essentials (`16`)
- Tokens = value + role. **Brand** (raw scales) → **Alias** (primary, error, success, warning, information, neutral; brand modes) → **Mapped** (`surface/*`, `border/*`, `text/*`, `icon/*`; light/dark modes) + **Responsive** (type sizes, layout "jumper" spacing; desktop/mobile). Mapped never links straight to brand. No component-specific tokens.
- Colour scale by hand: base = 500, overlay at 80/60/40/20/10% on white/black and pick the solid colour; name by the maths (50, 100…900, 950; insert 250 later).
- Type: Major Third 1.25, base 16, round to multiples of 4, line-height 1.2×. Dark mode = invert the scale but keep brand-500.
- Components: auto layout, hug, icons as components, variants `status` (default/hover/**focus**/disabled) × `type`, focus ring outside, borders not dividers, atomic composition.
- In code: tokens become Tailwind v4 `@theme` variables (`14`). Claude Design can generate a system from a reference image (`17`). Audit it against these rules before using it for a lasting brand.

## 5. Stack decision
| Need | Use |
|---|---|
| Learning, one-off scene, embed | Single HTML + Three.js via import map (`assets/starter-scene.html`) |
| Real vanilla site | Vite + `three` + GSAP (+ Lenis) |
| Component site, state-driven 3D, portfolio, configurator | Vite/Next + **React Three Fiber + drei** + Tailwind v4 + GSAP or Framer Motion; Zustand/Valtio for 3D state |
| Quick visual 3D prototype | Spline (less control) |
| Styling | Tailwind v4 (mobile-first: unprefixed = phone, `md:` = 768+) |

## 6. 3D build essentials (`03`, `13`, `15`)
- **Pipeline:** scene → camera (fov 35–50 cinematic) → objects (geometry + material) → lights → loop → render. **1 unit = 1 m**, radians (`Math.PI` = 180°). Always: resize handler, `setPixelRatio(Math.min(dpr, 2))`.
- **Models:** Sketchfab / own Blender → GLB (1K textures for secondary models; clean, separate named meshes such as screen and body) → `npx gltfjsx model.glb -T` → fix paths in `useGLTF` + `preload` → `<Suspense fallback={loader}>` with `useProgress` → position with Leva sliders, then hard-code. Bake lighting/AO in Blender.
- **Lighting:** product = `<Environment>` + 2 `<Lightformer>` soft boxes + spotlights; configurator = `AccumulativeShadows` + 2 `RandomizedLight`; outdoor = directional sun + ambient + **hemisphere**. Set `texture.colorSpace = SRGBColorSpace`.
- **Interaction patterns:** cursor tilt (`easing.dampE(rot, [-py/3, px/5, 0], .25, dt)`; off on mobile), camera ease to target per breakpoint and state, `<Float>`, `PresentationControls snap`, OrbitControls with polar limits, model A↔B GSAP fade/slide, recolour via traverse + no-change list, **video on a screen** (`useVideoTexture` → `meshBasicMaterial`), **Decal** logos, drag-to-rotate world with damping and "stages", star field (`maath/random.inSphere` + `Points`), multiple views on one canvas (drei `View`).
- **HTML over canvas:** canvas `fixed inset-0 -z-10` (or absolute behind), content scrolls on top in a 12-col grid aligned beside the 3D; `pointer-events-none` on overlays that shouldn't block dragging.

## 7. Ship checklist (`05`)
LCP < 2.5 s, INP < 200 ms, CLS < 0.1 · `frameloop="demand"` for static scenes, instancing over many meshes, Draco/KTX2, pause offscreen/hidden, dispose · semantic HTML, keyboard + visible focus, alt text, real text not baked into canvas, AA contrast · static fallback for no-WebGL · test on a real phone and Safari · then run `06-critique-checklist.md`.

## 8. Client process (`09`)
Onboarding (discovery call with the client as the star → contract + first payment → kickoff with deadlines for both sides; reply within 48 h) → design/dev (sitemap and content wireframe → homepage → inner pages; **1 revision round per stage, 24 h feedback window**) → launch (low-traffic day, test every form, purchase and email yourself) → offboarding (support window, FAQ + Loom docs, ongoing check-ins = repeat work).
