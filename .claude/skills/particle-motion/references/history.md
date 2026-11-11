# Particles: concepts and sources

A particle system (term from William Reeves, *Star Trek II* Genesis effect, 1983) models fuzzy phenomena (fire, smoke, sparks, dust) as many small particles with birth, life and death, moved by forces. Core parts: emitter (shape, rate), per-particle attributes (lifetime, velocity, size, colour, all with randomness), forces (gravity, drag/air resistance, turbulence, attractors, vortices), collisions, and rendering (sprites, streaks, blending). Budget: particle count ≈ emission rate × lifetime.

- **Turbulence / curl noise:** curl noise (Bridson et al., 2007) takes the curl of a smooth noise potential to make a divergence-free velocity field: swirling motion with no sinks or sources, so particles don't clump. Summing about three octaves of noise looks good.
- **Flocking (boids):** Craig Reynolds (1987) treated birds as particles each following three local rules: separation (collision avoidance), alignment (velocity matching), cohesion (flock centering). Tuning the weights is the hard part.
- **Motion graphics tools:** After Effects CC Particle World and CC Particle Systems II (built in), Trapcode Particular/Form (Maxon Red Giant), Plexus (Rowbyte); Blender particle systems and Geometry Nodes Simulation Zones (Blender 3.6+); Cinema 4D X-Particles; Houdini POPs.

## Sources (gathered 2026-10-10)

- [tutvid: particle text/logo reveal in After Effects, no plugins](https://tutvid.com/after-effects/particle-text-logo-reveal-effect-after-effects-no-plugins/)
- [Pluralsight: animating a logo with particles in After Effects](https://pluralsight.com/courses/animating-logo-particles-after-effects-1179)
- [Envato Tuts+: inspiring Particular video styles](https://photography.tutsplus.com/tutorials/15-inspiring-adobe-after-effects-particular-video-styles--cms-30867)
- [Motion Array: particles logo reveal template](https://motionarray.com/after-effects-templates/particles-logo-reveal-262158)
- [BlenderNation: Simulation Nodes for Beginners series](https://www.blendernation.com/2022/12/08/simulation-nodes-for-beginners-tutorial-series/)
- [Digital Production: your own particle system with simulation nodes](https://digitalproduction.com/2023/08/10/your-own-particle-system-with-simulation-nodes/)
- [Lester Banks: spirograph with simulation zone](https://lesterbanks.com/?p=68819)
- [Ryan King: abstract particle animation loop (Geometry Nodes)](https://ryanking.artstation.com/store/ddD3q/abstract-particle-animation-loop-geometry-nodes)
- [Unity: particle system modules](https://docs.unity3d.com/Manual/ParticleSystemModules.html)
- [Vizrt: particle system](https://documentation.vizrt.com/viz-artist-guide/5.4/Particle_System.html)
- [Beutl: particle emitter](https://docs.beutl.beditor.net/reference/library/drawables/particles/particle-emitter)
- [SIGGRAPH HyperGraph: Reynolds, Flocks, Herds and Schools](https://education.siggraph.org/static/HyperGraph/animation/art_life/flocks.htm)
- [Reynolds 1987 paper (PDF)](https://cedric.cnam.fr/~cubaud/PROCEDURAL/reynoldsSIGGRAPH87.pdf)
- [Autodesk Softimage ICE: Curl Noise framework](https://download.autodesk.com/global/docs/softimage2014/en_us/files/iceref_CurlNoise_Framework.htm)
- [Bridson et al. curl noise (DNEG-hosted PDF)](https://www.dneg.com/wp-content/uploads/2022/11/2007.pdf)
- [The Little Grasshopper: noise-based particles](https://prideout.net/blog/old/blog/index.html@p=63.html)
- Local: HyperFrames `hyperframes-animation/rules/particle-burst.md` (deterministic DOM particle bursts)

Design rules (hierarchy, density, size tiers) are motion-design practice synthesised for this skill.
