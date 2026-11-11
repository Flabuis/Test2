# 13 — Study Notes: JavaScript Mastery "Three.js Developer Course" (playlist, 6 builds, ~19 h)

Source: JavaScript Mastery (Adrian Hajdin), playlist `PL6QREj8te1P7d4j3k8Snfa187o-IjXuJx`.
Files: `Training Data/Principles study/jsm-threejs-course/NN-<id>/` with `transcript.txt` (timestamped lines), `transcript-paragraphs.txt` (one paragraph per minute, easier to read), `video.en.vtt`, `video.description` (chapters + GitHub links), plus `video.mp4` and `frames/` once the background download finishes.

| # | Video | Length | What it builds | Key new techniques |
|---|---|---|---|---|
| 01 | Master Creative Frontend in 2 Hours (React, Three.js, GSAP) | 2:22 | Apple **MacBook Pro** landing page clone | gltfjsx CLI, Lightformer studio lighting, PresentationControls + snap, GSAP model switcher, Zustand store, scroll-pinned video mask, scroll-scrubbed image "explosion", **video texture that changes per scroll step** |
| 02 | Build & Deploy an Amazing 3D Portfolio (Beginner Three.js) | 4:29 | Dev portfolio: hacker-room hero, bento grid, project monitor, avatar | **1 h theory section**, vanilla → Vite → R3F progression, Leva for positioning, responsive `calculateSizes`, cursor-follow camera (maath `easing.dampE`), floating props (drei `Float` + GSAP yoyo), video-on-monitor, Ready Player Me + Mixamo avatar with hover-triggered animations |
| 03 | Apple iPhone 15 Pro site (Three.js & GSAP) | 3:52 | iPhone 15 Pro clone | **GSAP crash course** (to/from/fromTo/timeline/stagger/ScrollTrigger), video carousel with progress bars (`gsap.ticker`), **drei `View` = multiple 3D views on one canvas**, two-model rotate-and-swap timeline, reusable `animateWithGsap` helper, Sentry performance monitoring |
| 04 | 3D Developer Portfolio (floating island + fox) | 2:54 | Explorable **floating island** world | Drag/keyboard-rotate world with momentum (damping), **rotation "stages" that open popups**, sky sphere rotating with input, bird flying a **sine-wave path**, plane propeller via `useAnimations`, **fox whose animation follows form state** (idle/walk/hit), background music toggle, react-router pages |
| 05 | AI-Powered 3D Website (T-shirt customizer) | 2:20 | **3D product configurator** + DALL·E | **Valtio** proxy store, Framer Motion page transitions (`AnimatePresence`), `CameraRig` (pointer tilt + intro/customizer camera targets), **drei `Decal`** for logo + full texture, `easing.dampC` colour lerp, **`AccumulativeShadows` + `RandomizedLight`** backdrop, Express + OpenAI backend |
| 06 | 3D Web Developer Portfolio (2023) | 2:53 | Classic dev portfolio | `frameloop="demand"`, PC model with OrbitControls limits, framer-motion `SectionWrapper` HOC (stagger on view), react-tilt cards, vertical timeline, **tech "balls" = icosahedron + Decal + Float**, rotating Earth GLTF, **star field with `maath/random.inSphere` + `Points`** |

---

## 1. Core mental model (from video 02's theory section)
- **Dimensions:** 0D point, 1D line, 2D plane, 3D volume, **4D = time** (= animation).
- **History:** OpenGL → WebGL (2010s, hundreds of lines for a cube) → **Three.js** (Mr.doob) as the friendly layer. Analogy: Three.js is to WebGL what Tailwind is to CSS.
- **Pipeline:** scene → camera → objects → lights → animation updates → render (repeat every frame).
- **Scene vs. environment:** the scene is the container (the planet), the environment is the atmosphere/backdrop (the sky). One scene can swap environments (day/night). You can have separate scenes per page section.
- **Object types:** `Mesh` (geometry + material), `Points` (stars/particles), `Line`, `Group` (like a div, transform together), `Sprite` (always faces the camera). All inherit from **`Object3D`** → position / rotation / scale.
  - Rotation intuition: **X = nod**, **Y = shake head "no"**, **Z = steering wheel**.
- **Geometry:** vertices (corner dots) → edges (lines) → faces. **Everything is triangles.** More segments = smoother, but heavier.
- **Materials:** Basic (unlit), Lambert/Phong (cheap shiny), **Standard (PBR: roughness/metalness, the default)**, Physical (clearcoat, sheen, transmission), Toon (bands), Matcap, Normal, Depth. Textures: diffuse, normal, specular, bump, displacement maps.
- **Lights:** ambient (cloudy day, no shadows), point (bulb), directional (sun, parallel rays, sharp shadows), spot (cone, stage light), hemisphere (sky colour + ground colour gradient).
- **Cameras:** Perspective (realistic), Orthographic (no perspective: iso, blueprints), Stereo (VR). Properties: **FOV**, position/POV, aspect ratio, near/far clipping planes.
- **Controls:** Orbit (Apple product spin), Trackball (free), Fly, PointerLock (FPS), FirstPerson (real estate walkthroughs).

## 2. Stack progression (best practice)
1. **Vanilla + CDN**: fastest to try (that's what `WebBuilding/lesson-01` does).
2. **Vite + `npm i three`**: real project, autocomplete, modules.
3. **React Three Fiber (R3F) + drei**: declarative JSX instead of imperative code. It scales better because scenes become components and state drives the 3D.
   - Every Three.js class becomes a camelCase JSX tag (`new THREE.Mesh` → `<mesh>`). Constructor args go into `args={[...]}`, and properties become props.
   - **Only 3D objects live inside `<Canvas>`.** HTML needs drei `<Html>`, and GUI panels (Leva) go outside the canvas. Error *"X is not part of the THREE namespace"* means a div ended up inside the Canvas.
   - Use the R3F docs for R3F-specific things, but the **Three.js docs are still the reference** for which geometries, materials and props exist.

## 3. Model workflow (used in every build)
1. **Find:** Sketchfab (free, download **glTF/GLB**), R3F examples/CodePen, poly.pizza, Ready Player Me (avatars). Choose **1K textures for secondary models**, 4K only for the hero.
2. **Optimise in Blender:** a friend cut the hacker-room model about 10× smaller with the same texture quality, removed shadow casters and extra meshes from the island, and added a separate screen mesh to the computer so a video could be mapped onto it. **Blender skills directly improve web 3D.**
3. **Convert:** `npx gltfjsx model.glb -T` (CLI; `-T` = transform/compress → `*-transformed.glb`) or the gltf.pmnd.rs web tool. Output is a React component with every mesh exposed.
4. **Fix the generated component:** rename it, export it as default, fix the GLB path in `useGLTF()` **and** `useGLTF.preload()`, put the file in `public/models`.
5. **Wrap it** in `<Suspense fallback={<CanvasLoader/>}>`. The loader uses drei `useProgress()` and shows `progress.toFixed(2)%`.
6. **Position it:** scale, position and rotation (radians: `Math.PI` = 180°, `-Math.PI/2` = 90° clockwise). Use **Leva** sliders (`useControls`) to dial values live, then hard-code them.

## 4. Lighting recipes
- **Apple studio look (01):** drei `<Environment resolution={256}>` containing two **`<Lightformer form="rect" intensity={10} scale={10}>`** soft boxes left and right (rotated `Math.PI/2`), plus 3 `<spotLight angle={0.15} decay={0}>` from top, bottom and sides. "It's not only the model, it's the lights." Without them the MacBook looked dull.
- **Product backdrop (05):** `<AccumulativeShadows temporal frames={60} alphaTest={0.85} scale={10}>` containing two `<RandomizedLight amount={4} radius={9} intensity={0.55} ambient={0.25} position={[5,5,-10]}>` gives soft studio contact shadows. Add `<Environment preset="city">` for reflections.
- **Outdoor island (04):** directional "sun" (intensity 2) + ambient 0.5 + **hemisphere** (sky `#b1e1ff`, ground black). The hemisphere light was the biggest jump in quality.
- **Hero PC (06):** hemisphere 0.15 + point light (screen glare) + spotlight (angle 0.12, penumbra 1, castShadow).
- **Fix washed-out textures:** `texture.colorSpace = SRGBColorSpace; texture.needsUpdate = true` (CodeRabbit caught this in 01).

## 5. Interaction & motion patterns
| Pattern | How (code idea) | Video |
|---|---|---|
| **Cursor-follow tilt** | in `useFrame((state, delta) => easing.dampE(group.rotation, [-state.pointer.y/3, state.pointer.x/5, 0], 0.25, delta))` (maath). Invert the Y sign to choose whether the model "opens up" on scroll down. Disable on mobile | 02, 05 |
| **Camera ease to target** | `easing.damp3(state.camera.position, [0,0,20], 0.25, delta)`, with different targets per breakpoint and per UI state (intro vs. customizer) | 02, 05 |
| **Floating props** | drei `<Float floatIntensity={1}>`, or GSAP `gsap.to(ref.position, {y:'+=0.5', duration:1.5, repeat:-1, yoyo:true})` | 02, 06 |
| **Product spin that snaps back** | drei `<PresentationControls snap polar={[-π, π]} azimuth={[-Infinity, Infinity]} config={{mass:1, tension:0, friction:26}}>` | 01 |
| **Orbit limits** | `<OrbitControls enableZoom={false} maxPolarAngle={Math.PI/2} minPolarAngle={Math.PI/2}>`; `autoRotate` for globes | 02, 06 |
| **Model A ↔ B switch** | GSAP: slide the outgoing group `x: ±5` + traverse its meshes setting `material.transparent=true` and tween `opacity` to 0, while the incoming group slides to 0 and fades to 1 | 01 |
| **Re-colour a model** | `scene.traverse(child => child.isMesh && !NO_CHANGE.includes(child.name) && child.material.color.set(color))`. Keep a list of mesh names that must not change (screen, keys). Smooth version: `easing.dampC(material.color, target, 0.25, delta)` | 01, 05 |
| **Video on a screen** | drei `useVideoTexture('/textures/project1.mp4')` → `<meshBasicMaterial map={txt} toneMapped={false}/>` on the screen mesh. Set `flipY=false` if it's upside down. Swap the source per selection | 02, 01 |
| **Image on a screen** | `useTexture('/screen.png')` → `meshBasicMaterial` / `meshMatcapMaterial` on the screen mesh | 01, 02 |
| **Logo/print on a surface** | drei `<Decal position rotation scale map={logoTex} depthTest={false}/>` inside the mesh. Set `map.anisotropy=16` for sharpness | 05, 06 |
| **Spin-on-change flourish** | `useGSAP(() => gsap.from(group.rotation, {y: Math.PI/2, duration:1, ease:'power3.out'}), [texture])` | 02 |
| **Drag-to-rotate world** | pointer down/move/up on `gl.domElement`: `delta = (clientX-lastX)/viewport.width`, `rotation.y += delta*0.01*π`, store speed. In `useFrame`, when not dragging: `speed *= 0.95` (damping) until < 0.001. Arrow keys do the same. Normalise rotation to 0–2π and map ranges to **stages** that trigger UI popups | 04 |
| **Sky follows input** | `if (isRotating) sky.rotation.y += 0.15*delta` | 04 |
| **Ambient flyer path** | `pos.y = Math.sin(clock.elapsedTime)*0.2+2`. Move along X, flip `rotation.y = π` when passing `camera.x ± 10` | 04 |
| **Baked GLB animations** | `const {actions} = useAnimations(animations, ref)`, then `actions['Take 001'].play()`. Switch clips: stop all → `actions[name].reset().fadeIn(0.5).play()`, cleanup `fadeOut(0.5)` | 02, 04 |
| **Character reacts to UI** | form focus → `walk`, blur → `idle`, submit → `hit`/run, then idle after 3 s. Hovering work-experience cards plays `salute`/`clapping`/`victory` (Mixamo FBX via `useFBX`) | 04, 02 |
| **Star field** | `random.inSphere(new Float32Array(5000), {radius:1.2})` → `<Points positions stride={3} frustumCulled>` + `<PointMaterial size={0.002} sizeAttenuation depthWrite={false} transparent/>`; rotate the group a little each frame. Absolute, `z-index:-1` behind content | 06 |
| **Tech icon balls** | `<Float><mesh scale={2.75}><icosahedronGeometry args={[1,1]}/><meshStandardMaterial flatShading color="#fff8eb"/><Decal map={iconTex}/></mesh></Float>` | 06 |
| **Many views, one canvas** | drei `<View track={ref}>` per DOM box + one `<Canvas eventSource={root}>` with `<View.Port/>` (avoids the browser's WebGL context limit) | 03 |

## 6. GSAP + scroll (videos 01 & 03)
- **Register once** in `App`: `gsap.registerPlugin(ScrollTrigger)`. Use the `useGSAP(() => {...}, {scope: ref, dependencies:[...]})` hook from `@gsap/react` (it cleans up automatically).
- **Methods:** `to` (current → target), `from` (target → current, good for entrances), `fromTo`, **`timeline`** (sequence; position param `'<'` = start together, `'-=0.6'` = overlap), **`stagger`** (`{each:0.5, from:'center', grid, axis, ease}`).
- **ScrollTrigger options:** `trigger`, `start:'top top'` (element edge, then viewport edge), `end:'bottom top'` or `'+=150%'`, **`scrub:true|1`** (1:1 with scroll, or smoothed), **`pin:true`** (hold the section), `toggleActions:'restart reverse restart reverse'` (enter / leave / enterBack / leaveBack), `invalidateOnRefresh:true` (recalculate on resize).
- **Recipes built:**
  - **Hero video:** autoplay muted playsInline. `videoRef.playbackRate = 2`, because micro-animations should be quick and not make the site feel slow.
  - **Pinned video → mask reveal (01):** pin the section, scrub a timeline that scales the logo-mask SVG and fades in the content (`opacity:1, y:0`). Desktop only.
  - **Exploding screenshots (01):** `scrub:1`, timeline tweens each image from the centre to its `left/right/bottom/transform` stored in constants. The centre MacBook (`p5`) is skipped. End at `center center` so it finishes as the section centres, then the text reveals.
  - **Spin + content sync (01):** pinned timeline rotates the MacBook `y: 2π`. A second timeline uses `.call(() => setTexture('/videos/feature-2.mp4'))` + `.to('.box2', {opacity:1, y:0})` per feature. **Preload videos** with an off-DOM `document.createElement('video')`, `preload='auto'`. Images avoid the texture-swap flash completely.
  - **Masonry/bento cards:** `gsap.to(['.left-column', '.right-column'], {opacity:1, y:0, stagger:0.5, scrollTrigger:{trigger:'#highlights', start: isMobile ? 'bottom bottom' : 'top top'}})`.
  - **Video carousel (03):** per-slide videos, progress dots driven by `gsap.ticker.add(updateProgress)` reading `video.currentTime / duration`, ScrollTrigger `toggleActions:'restart none none none'` to start when in view, slide with `xPercent`.
  - **Reusable helper (03):** `animateWithGsap(target, animationProps, scrollProps)` wraps `gsap.to` + a standard ScrollTrigger. Use it for the many "fade-up on enter" moments.
- **Framer Motion alternative (05, 06):** `motion.div` with variants (`fadeIn(direction, type, delay, duration)`, `textVariant`, `slideIn`), a **SectionWrapper HOC** (`initial="hidden" whileInView="show" viewport={{once:true, amount:0.25}}` + staggerContainer), and `AnimatePresence` for page swaps.

## 7. Responsive & performance
- **Breakpoint hooks:** `react-responsive` `useMediaQuery({maxWidth:1024})`, or `window.matchMedia` + a listener. Feed a **`calculateSizes(isSmall, isMobile, isTablet)`** function that returns per-device scale/position for every model (tuned with Leva).
- Smaller models and **no cursor-tilt on mobile** (it fights scrolling). Only pin and scrub on desktop.
- **`<Canvas frameloop="demand">`** for static scenes (renders only when something changes), `dpr={[1,2]}`, `gl={{preserveDrawingBuffer:true}}` (needed for screenshot/download), drei `<Preload all/>`.
- Use compressed `-transformed.glb` from gltfjsx and 1K textures for secondary models.
- Avoid **float equality** on scale (`scale === 0.08`); use named constants (CodeRabbit).
- Add the scene to `useEffect` dependency arrays when traversing it. Clone materials only when you need them separate.
- ESLint: add `@react-three/eslint-plugin` and set `react/no-unknown-property: off` to silence R3F prop warnings.
- **Measure (03):** Sentry performance and web vitals (LCP ≈ 300 ms achieved), errors grouped by browser and device. It's a strong talking point on a portfolio: "built it **and** monitored it".

## 8. Project/portfolio structure they reuse
- `constants/index.js` holds all content (nav links, projects, experiences, tech icons, model sizes, animation targets). **Separate content from logic** so the site is re-skinnable.
- `components/` for UI, `components/models/` or `canvas/` for 3D (anything rendered inside `<Canvas>`), `store/` for global state (Zustand / Valtio), `utils/` for motion variants and animation helpers, `public/models|textures|videos` for assets.
- Hosting: `npm run build` → upload `dist/` (Hostinger in the videos; Vercel/Netlify/Cloudflare work the same). Git from day one, and review PRs with an AI reviewer.

## 9. Lessons for our own work (motion-designer angle)
1. **These are After Effects ideas in code:** pinned + scrubbed timelines = precomps on a scroll-driven time remap; `easing.damp` = expression-driven easing toward a target; `stagger` = sequence layers with offsets; video textures = footage mapped onto a 3D layer.
2. **Blender is the secret weapon:** clean, low-poly, baked models with separate named meshes (screen, body, details) make every technique above possible (recolour lists, video screens, decals).
3. **The Apple formula:** studio-lit hero product, then a pinned cinematic video, then scroll-revealed specs, then a spin with feature captions synced to on-screen video, then a calm bento grid. It's temporal flow (see 10) built in code: punch → linger → pulse → release.
4. **Signature build candidates for the Lessons roadmap:**
   - Lesson 3: Blender → GLB → gltfjsx.
   - Lesson 4: GSAP timeline.
   - Lesson 5: pinned scroll spin with synced captions.
   - Lesson 6: star field and decals.
   - Lesson 7: Lightformer studio lighting.
   - Lesson 8: R3F portfolio with a cursor-tilt hero and an avatar.
