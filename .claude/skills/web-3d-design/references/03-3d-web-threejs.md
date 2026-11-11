# 03 — 3D on the Web (Three.js)

## Mental model (After Effects / Blender → Three.js)
| AE / Blender | Three.js |
|---|---|
| Composition / scene | `Scene` |
| 3D camera | `PerspectiveCamera(fov, aspect, near, far)` (fov 35–50 feels cinematic) |
| Render | `WebGLRenderer` → `<canvas>`, every frame |
| Shape layer / object | `Mesh` = `Geometry` + `Material` |
| Null object / parent | `Group` (`group.add(child)`) |
| Keyframes / expressions | The animation loop, `setAnimationLoop(t => …)`, or GSAP tweens |
| Adjustment layers | Post-processing (`EffectComposer`: bloom, DOF, grain) |
| HDRI world | `scene.environment` = RGBE/EXR loaded via `PMREMGenerator` |

Units: think **1 unit = 1 metre** (it matches Blender). Rotations are in **radians** (`Math.PI` = 180°, `THREE.MathUtils.degToRad`).

## Minimal setup checklist
1. Scene, camera, renderer; `setPixelRatio(Math.min(devicePixelRatio, 2))`.
2. Mesh + light (Standard/Physical materials need light or an environment map).
3. Loop: update, then render.
4. Resize handler: `camera.aspect`, `updateProjectionMatrix()`, `renderer.setSize`.
5. Colour: `renderer.outputColorSpace = SRGBColorSpace` (the default) and `toneMapping = ACESFilmicToneMapping`.
See `WebBuilding/lesson-01` for a working version.

## Materials
- `MeshBasicMaterial`: unlit, flat colour. Fast, good for flat/2D styles.
- `MeshStandardMaterial`: PBR, using roughness and metalness. The default choice.
- `MeshPhysicalMaterial`: adds glass (`transmission`, `thickness`, `ior`), clearcoat, sheen, iridescence. Use it for glassmorphism and chrome.
- `MeshToonMaterial`: cel shading. `MeshMatcapMaterial`: baked lighting look, very cheap, great for clay.
- `ShaderMaterial` / `onBeforeCompile`: custom GLSL.

## Lighting recipes
- **Product / hero**: HDRI environment (main reflections) + one directional key + a coloured rim. This is what makes metal and glass look real.
- **Stylised**: ambient + directional, toon/matcap materials.
- Shadows are expensive. Enable only on the key light, keep the shadow camera tight, use `mapSize` 1024–2048, or **bake shadows in Blender** onto a floor texture.

## Models from Blender
- Export as **glTF binary (.glb)**: apply transforms, Y-up, include materials and animations.
- Compress: **Draco** (geometry) and **KTX2/Basis** (textures). `gltf-transform optimize in.glb out.glb` makes files much smaller.
- Load with `GLTFLoader` (+ `DRACOLoader`). Play baked animations with `AnimationMixer`.
- Bake complex lighting and AO into textures in Blender. Real-time lighting can't match Cycles, so bake.

## Interaction
- `Raycaster` + pointer coords → hover and click on 3D objects.
- Mouse parallax: lerp the camera or group rotation toward the pointer (`x += (target - x) * 0.05`). This is the "cursor tilt" seen on most award sites.
- `OrbitControls` for exploring. Usually disable it on marketing sites (it conflicts with page scroll).

## Shaders (GLSL), the signature look
- **Vertex shader** moves points (waves, noise displacement, morphs). **Fragment shader** colours pixels (gradients, grain, distortion).
- Key ingredients: `uTime` uniform, UV coordinates, noise (simplex/perlin), `mix`, `smoothstep`, `fract`.
- Common effects: noise-displaced blob, gradient mesh background, image hover ripple/distortion, particle fields (`Points` + custom shader), dissolve transitions.
- References: The Book of Shaders, Shadertoy.

## Post-processing
`EffectComposer` → `RenderPass` → `UnrealBloomPass`, plus film grain, chromatic aberration, vignette, DOF. Or use the `postprocessing` library (it's faster). Keep it subtle. Bloom on everything looks cheap.

## Worked recipes
See **13** for working code patterns from real builds: gltfjsx workflow, Lightformer/AccumulativeShadows lighting, cursor tilt, PresentationControls, video and decal textures, drag-rotate worlds, star fields, View multi-canvas.

## Ecosystem
- **React Three Fiber (R3F)** + **drei** (helpers: Environment, Float, MeshTransmissionMaterial, ScrollControls, Text) is the modern default for full sites.
- **Spline**: visual 3D editor that exports to the web. Fast for prototypes, less control.
- **Theatre.js**: a timeline/keyframe editor for Three.js scenes. Feels like After Effects.
- **Lenis** (smooth scroll), **GSAP** (animation), **lil-gui** (live tweak panel).

## 3D style ↔ technique map (for the 16 style skills)
| Style | Technique |
|---|---|
| Glass | `MeshPhysicalMaterial` / drei `MeshTransmissionMaterial` + HDRI |
| Y2K chrome | metalness 1, roughness 0.05–0.15, high-contrast HDRI |
| Clay | matcap or Standard with roughness 0.8, soft area light, slight noise |
| Low-poly | `flatShading: true`, low-segment geometry |
| Synthwave | grid plane + fog + bloom + sun gradient shader |
| Particle | `Points`/`InstancedMesh` + GPU shader animation |
| Isometric | `OrthographicCamera`, rotation (35.264°, 45°) |
| Line art | `EdgesGeometry` + `LineSegments`, or an outline post pass |
| Pixel art | render to a low-res target, nearest-neighbour upscale |
