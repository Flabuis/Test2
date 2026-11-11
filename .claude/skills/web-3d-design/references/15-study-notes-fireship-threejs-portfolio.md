# 15 — Study Notes: Fireship, "Build a Mindblowing 3D Portfolio Website // Three.js Beginner's Tutorial"

Source: Fireship (Jeff Delaney), YouTube `Q7AOvWpIVHU`, 15:38. The video has **no YouTube captions**, so the transcript was made locally with Whisper (`_tools/whisper2txt.py`, small.en). Expect minor word errors.
Files: `Training Data/Principles study/fireship-threejs-portfolio/` (video.mp4, transcript.txt, transcript-paragraphs.txt, video.description, frames/sheet_01–12.jpg).
Inspiration sites shown: **mav.farm** (no scrollbar, scroll animates a whole 3D world), **atlia.net** (CSS Grid + Three.js), zenly, L'Atelier "The Virtual Economy" (wireframe terrain + text).

**Why it's valuable:** the smallest complete version of the "3D background + scrolling HTML" site. It's **vanilla Three.js, no React**, so it's the natural next step after `WebBuilding/lesson-01`.

## The build (vanilla JS + Vite)
1. **Project:** `npm create vite@latest` → vanilla, `npm i three`, `npm run dev`. (The video's `npm init @vitejs/app` and port 3000 are outdated; today it's `create vite` on port 5173.)
2. **HTML:** `<canvas id="bg">` placed **before** the main script. CSS: `canvas { position: fixed; top: 0; left: 0; }` makes it a background, and the HTML content scrolls on top. Content root `main { position: absolute; }`.
3. **The three essentials:** `Scene`, `PerspectiveCamera(75, innerWidth/innerHeight, 0.1, 1000)`, `WebGLRenderer({ canvas: document.querySelector('#bg') })` with `setPixelRatio(devicePixelRatio)` and `setSize(innerWidth, innerHeight)`. Move the camera back on Z.
4. **Object = geometry + material → mesh:** `TorusGeometry(10, 3, 16, 100)` + `MeshBasicMaterial({ color, wireframe: true })` (the wireframe shows the triangles), then `scene.add(torus)`.
5. **Animation loop:** `function animate(){ requestAnimationFrame(animate); torus.rotation.x += 0.01; … renderer.render(scene, camera); }`. It's a "game loop": change properties every frame.
6. **Lighting:** switch to `MeshStandardMaterial` (black until lit), then add a `PointLight(0xffffff)` at (5,5,5) (a light bulb; at 20 it lights a larger area) and an `AmbientLight` (floodlight, lights everything evenly). `0x…` is a hex literal.
7. **Helpers while building:** `PointLightHelper(light)` shows where the light is, `GridHelper(200, 50)` draws a floor grid, `OrbitControls(camera, renderer.domElement)` with `controls.update()` in the loop lets you look around. Remove them for production.
8. **Procedural stars:** `addStar()` = `SphereGeometry(0.25)` + standard material, position `Array(3).fill().map(() => THREE.MathUtils.randFloatSpread(100))` (random −50…50), then `Array(200).fill().forEach(addStar)`.
9. **Textures:**
   - `scene.background = new TextureLoader().load('space.jpg')` for a space backdrop. The loader takes an onLoad callback, which is useful for loading bars.
   - **Texture-mapped cube avatar:** `BoxGeometry(3,3,3)` + `MeshBasicMaterial({ map: jeffTexture })` puts the photo on all 6 faces.
   - **Moon:** `SphereGeometry(3,32,32)` + `MeshStandardMaterial({ map: moonTexture, normalMap: normalTexture })`. The purple **normal map** fakes craters and bumps that catch light. A big realism gain for almost no cost.
10. **Scroll-driven camera (the key trick):**
    ```js
    function moveCamera() {
      const t = document.body.getBoundingClientRect().top; // always ≤ 0
      moon.rotation.x += 0.05; moon.rotation.y += 0.075; moon.rotation.z += 0.05;
      jeff.rotation.y += 0.01; jeff.rotation.z += 0.01;
      camera.position.z = t * -0.01;
      camera.position.x = t * -0.0002;
      camera.rotation.y = t * -0.0002;
    }
    document.body.onscroll = moveCamera;
    moveCamera(); // set the initial position
    ```
    Place objects **further down the Z axis** (`moon.position.z = 30; moon.position.setX(-10)`) so the camera "travels" to them as you scroll. Tune the multipliers by eye. `position.z = 30` and `position.setZ(30)` are equivalent.
11. **Layout = CSS Grid aligned to the 3D:** `main { display: grid; grid-template-columns: repeat(12, 1fr); }`. Sections use `grid-column: 2 / 8` (left), others `grid-column: 6 / span 5` / right-aligned, so text blocks sit beside the 3D objects instead of on top of them. Long content gives scroll room.

## Concepts reinforced
- Every 3D scene = **geometries** + **textures/materials** + **lights** + **camera**, and animation changes their properties in a loop or from a trigger like scroll.
- Three.js is **not a modelling tool**. Model in Blender and import (see 13 for GLB → gltfjsx).
- Basic materials need no light; Standard/PBR materials need light. A **normal map** adds surface detail without geometry.
- Use helpers (light/grid/orbit) as scaffolding, the same way you'd use guides and a camera-view layer in After Effects.

## Upgrades we'd make today (from 03/04/13)
| Fireship version | Better practice |
|---|---|
| `onscroll` sets values directly (jumpy) | Lerp toward a target each frame (`camera.position.z += (target - camera.position.z) * 0.08`), or GSAP ScrollTrigger `scrub` + Lenis smooth scroll |
| 200 separate star meshes (200 draw calls) | One `Points`/`InstancedMesh` (see the 13 star field) |
| No resize handler | Update `camera.aspect`, `updateProjectionMatrix()`, `setSize` on resize (lesson-01 has it) |
| `setPixelRatio(devicePixelRatio)` | Cap at `Math.min(devicePixelRatio, 2)` |
| Always rendering | Pause when the tab is hidden. Respect `prefers-reduced-motion` (no scroll camera, keep static) |
| Rotations accumulate per scroll event | Derive from scroll progress (`rotation = progress * Math.PI*2`) so scrolling back reverses exactly |

## Use in our lessons
This is a good **Lesson 1.5**: extend `WebBuilding/lesson-01` with a fixed background canvas, star field, textured objects placed along Z, and a scroll-driven camera with lerp smoothing over a 12-column grid of real content. It prepares for the GSAP ScrollTrigger lesson.
