# Particles: After Effects recipes

Build through the `after-effects` MCP. First check which particle plugins are installed: `list_effects` and look for Trapcode Particular, Form, Plexus. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`.

## CC Particle World (built in)

On a black solid (set the layer to Add/Screen later):
- **Birth Rate** 0.5–5 (animate it to start/stop emission), **Longevity** 1–4 s.
- **Producer:** Position (link to a null with an expression for paths), Radius X/Y/Z for the emitter size.
- **Physics:** Animation **Viscouse** or **Fractal Uni** (organic drift), Velocity 0.1–1.0, Inherit Velocity 0–50%, Gravity 0 for floating dust (0.1–0.3 for falling sparks), Resistance 0–5, **Extra** and **Extra Angle** for randomness.
- **Particle:** Type **Faded Sphere** (soft dots), Shaded Sphere, Star, Lens Convex (bokeh), or **Textured QuadPolygon** with a custom layer (glyphs, confetti); Birth/Death Size, Size Variation 50–100%, Max Opacity 50–100%, Birth/Death Colour; Transfer Mode Add for glow.
- **Grid & Guides:** turn off for render.
- Use the comp's 3D camera: CC Particle World responds to it (depth and parallax).
Dust: Birth Rate 0.3, Longevity 4, Velocity 0.05, Gravity 0, Fractal Uni, Faded Sphere 0.02–0.06, add Fast Box Blur 2 + Glow.

## Trapcode Particular (if installed)

- **Emitter:** Point/Box/Sphere/**Layer** (emit from a logo layer's pixels; use Layer RGB → particle colour), Particles/sec, Velocity, Velocity Random 30–60%, Emitter Size.
- **Particle:** Life + Life Random, Sphere / Glow Sphere / Streaklet / **Sprite** (custom layers), Size + Size Random, Size over Life and Opacity over Life curves (ramp in and out), Colour over Life gradient, Blend Mode Add.
- **Physics:** Air: Gravity, Air Resistance, **Turbulence Field** (Affect Position 50–300, Scale 5–15, Evolution Speed, Octaves 2–3) for curl-like flow; Spherical Field to push particles around objects.
- **Aux System:** trails or sparks spawned from main particles.
- **Rendering:** Motion Blur on, Depth of Field from the comp camera.
Reverse-formation trick: emit from the logo layer with outward velocity and turbulence, then **time-reverse** the precomp so particles converge into the logo.

## Trapcode Form / Plexus (if installed)

- **Form:** a grid or layer map of particles that never die; displace with Fractal Field, Disperse & Twist, or audio. Great for text-made-of-dots and shape morphs (Layer Maps from two logos, crossfade).
- **Plexus:** points from layers/OBJ/Particular, Lines (Max Distance 80–200 px), Facets optional; Glow; slow camera orbit. No plugin? Approximate with shape-layer dots and short line shapes using expressions (feasible for < 50 points).

## No-plugin disintegrate (Thanos snap)

1. Precomp the subject.
2. Erosion matte: Gradient Ramp (side to side) + Fractal Noise (Contrast 300, Scale 60) combined (Overlay) → Levels; animate the ramp across. Use as a Luma Inverted matte on the subject so it erodes.
3. Particles: CC Particle World with Producer following the erosion edge (expression from the ramp position), or **CC Pixel Polly** / **Shatter** on a duplicate matted to the erosion edge, with Gravity −0.1 and Turbulent Displace drift.
4. Add drift: Turbulent Displace (Amount 40–80, Size 60, Evolution `time*100`) on the particle layer; fade out.
With Particular: emit from the subject layer (Layer emitter, Layer Sampling Current Time) only where the erosion matte reveals the edge.

## Logo formation without plugins

Card Dance or Shatter reversed, or CC Particle World emitting from a small radius at the logo, time-reversed. Then fade the clean logo in during the last 10–15 frames as particles converge, add a glow pulse when it resolves.

## Bursts and sparks

CC Particle Systems II (2D, fast): Birth Rate high for 2–3 frames then 0, Longevity 0.6–1.2, Velocity 1–3, Gravity 0.5–1, Particle Type Faded Sphere or Line (streaks); Glow. Fire on beat markers.

## Finishing

- Glow stack (Radius 10 and 60), or Deep Glow.
- Motion blur on (shutter 180°, more samples for particles: Comp Settings > Advanced > Samples 16–32).
- Depth of field from a 3D camera for bokeh foreground particles.
- Grade; keep blacks clean so additive particles pop.
- Render ProRes master; particles and gradients band in low-bitrate H.264.
