# Synthwave: Blender recipes

Use the `blender` MCP (`get_scene_info`, `run_python`, `render_preview`). Save .blend files to `C:\Users\basha\Motion Design\Cluads Work Folder\synthwave\`. Blender 4.2+ (EEVEE Next).

## Grid terrain

1. Plane, size 40 × 80, subdivided (e.g. 40 × 80 cuts) so cells are 1 unit.
2. **Mountains at the sides, flat road in the middle:** Displace modifier (Noise/Clouds texture, strength 2–6) masked by a vertex group or a Gradient texture that is 0 in the centre and 1 at the edges (Geometry Nodes: Set Position offset Z = noise × smoothstep(|x|)).
3. **Wireframe:** Wireframe modifier (thickness 0.02–0.05) with an Emission material (magenta, strength 5–15); keep a dark solid copy below for occlusion (solid black faces + glowing edges).
4. **Endless loop:** animate the terrain's Y location by exactly one or more whole cells over the loop length (linear interpolation, cycles modifier), or animate the camera forward and reset. Use the Geometry Nodes noise in object space so the terrain shape repeats with the move (or keep the noise static and move only one cell).

Free reference: RetroShaper's "Into the Synthwave" Geometry Nodes landscape (itch.io, Blender 3.5+).

## Sun

- Circle/disc mesh facing the camera at the horizon, far away.
- Emission shader with colour from a Gradient Texture (vertical: yellow → orange → pink), strength 5–20.
- Slits: Wave Texture (Bands, direction Z) or a Math chain: `fract(z * freq + time) < threshold(z)` where the threshold grows toward the bottom; feed into Mix Shader with Transparent BSDF (Alpha). Drive the offset with `frame/96` for the scroll.

## Sky, fog, stars

- World: Gradient (Sky Texture off) from dark navy at the zenith to magenta/orange at the horizon via a Gradient Texture on the World's vector (Generated, Z).
- Fog: World Volume Scatter (density 0.01–0.03) in EEVEE or a Mist pass composited in AE, so the grid fades into the horizon.
- Stars: an icosphere scattered on a far dome via Geometry Nodes (Distribute Points + Instance), tiny Emission spheres.

## Car, palms, objects

Silhouette palms as low-poly black meshes with a rim light (Area light behind, magenta). Neon trims on a car with Emission strips.

## Bloom and render

- **EEVEE Next:** there is no bloom checkbox any more; use the **Compositor Glare node** (Fog Glow, Threshold 0.8–1.0, Size 8–9; mix with Streaks for star glints). The realtime viewport compositor shows it.
- **Cycles:** same Glare node; heavier but cleaner fog.
- Colour management: AgX, Look Punchy (or Standard view transform for maximum neon saturation).
- Render 1080×1920 or 1920×1080 at 30/60 fps; PNG sequence with a separate title pass; VHS finish in AE.
