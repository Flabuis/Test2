# Particles: Blender recipes

Use the `blender` MCP (`get_scene_info`, `run_python`, `viewport_screenshot`, `render_preview`). Save .blend files to `C:\Users\basha\Motion Design\Cluads Work Folder\particles\`. Blender 4.x.

## Geometry Nodes simulation zone particle system

Node tree on an emitter mesh (or a plane/curve):
1. **Birth:** Distribute Points on Faces (Density, Seed) → Store Named Attribute `vel` (random vector or along normal × speed), `age` = 0, `life` = Random Value (1.5–4 s), `id` = Index.
2. **Simulation Zone** (input: Delta Time):
   - Join the new points (birth per frame: Distribute with a density driven by a "rate" value) with the simulated geometry.
   - Forces: `vel += (gravity + curl_noise(pos) * strength - vel * drag) * dt`.
     Curl-like flow: Noise Texture (4D, W = scene time × speed) as a vector field; for true divergence-free flow take the cross-derivative of noise or use a Vector Rotate trick; summing 2–3 noise scales gives richer currents.
   - Attractor: `vel += normalize(target - pos) * pull * dt` (Object Info of an empty).
   - `pos += vel * dt`, `age += dt`.
   - Delete Geometry where `age > life`.
3. **Output:** Instance on Points (Ico Sphere radius 0.005–0.02, or a custom shape) with scale from `1 - age/life` (shrink at death) × Random Value (size variation) → Set Material.
4. **Material:** Emission with colour from an Attribute node (`age/life` → ColorRamp birth → death colour), strength 5–20; or Principled for physical particles.

Bake the simulation (Physics > Simulation Nodes > Bake) for reliable renders and scrubbing.

Free learning references: ChrisP's "Simulation Nodes for Beginners" series (age, max age, gravity, collisions), Digital Production's custom particle system article.

## Logo / text formation (point cloud morph)

1. Convert text/logo to mesh; Distribute Points on Faces (high density) = target positions.
2. Create the same number of points scattered randomly in a box (Points node + Random Value) = start positions (match by index).
3. `pos = mix(start, target, smoothstep(0, 1, t - delay_i))` where `t` is driven by an animated value and `delay_i` is a per-point random 0–0.4 so points arrive staggered. Add noise that fades out as they arrive: `+ noise(pos) * (1 - progress)`.
4. Reverse the factor for dispersal. Same method morphs shape A → shape B.

## Legacy particle system (quick)

Emitter object > Particle System: Number, Frame Start/End, Lifetime + Random, Velocity Normal/Random; Render As Object (small sphere); Physics: Brownian, Drag; Force Fields (Turbulence, Vortex, Wind) for motion. Fast to set up; less control than Geometry Nodes.

## Rendering

- **EEVEE:** fast; turn on motion blur (Render Properties > Motion Blur); Bloom via compositor Glare (Fog Glow) in 4.2+.
- **Cycles:** best for depth of field bokeh and many emissive particles; higher samples for small bright points (or render particles as a separate pass).
- Depth of field: camera f-stop 1.4–2.8 focused on the hero formation; foreground particles become bokeh.
- Render with transparent film and composite over backgrounds in AE.
