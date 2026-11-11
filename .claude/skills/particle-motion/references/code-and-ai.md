# Particles: HyperFrames / Canvas / Three.js and Higgsfield

## HyperFrames rules (deterministic, seek-safe)

- For small DOM bursts (≤ ~40 particles: confetti, dot bursts, glyph dissolves) use the installed rule `hyperframes-animation/rules/particle-burst.md`: a fixed seeded pool, one driver tween with `ease: "none"`, and position as a pure function of time (ballistic formula). Particles start and end at opacity 0; fire on a cause.
- Seeded random everywhere: `prand(n) = fract(sin(n*127.1+311.7)*43758.5453)`. Never `Math.random()` at render time.
- Never accumulate state per frame (`pos += vel`) at render time: a seek breaks it.

## Canvas 2D (hundreds to a few thousand particles)

Draw every frame from a pure function of `t`:
```js
const N = 1500, P = [...Array(N)].map((_, i) => ({
  x0: prand(i*3)*W, y0: prand(i*5)*H, s: 0.5 + prand(i*7)*2.5, ph: prand(i*11)*6.283,
  life: 2 + prand(i*13)*3, born: prand(i*17)*8 }));
function draw(t) {                       // called from the timeline's onUpdate with tl.time()
  ctx.clearRect(0,0,W,H); ctx.globalCompositeOperation = "lighter";
  for (const p of P) {
    const a = ((t - p.born) % p.life + p.life) % p.life / p.life;          // 0..1 age, loops
    const x = p.x0 + Math.sin(p.ph + t*0.6) * 40 + a * 120;               // analytic drift
    const y = p.y0 - a * 200 + Math.cos(p.ph*1.7 + t*0.4) * 30;
    ctx.globalAlpha = Math.sin(Math.PI * a);                                // fade in and out
    ctx.beginPath(); ctx.arc(x, y, p.s, 0, 6.283); ctx.fill();
  }
}
```
For true flow-field integration (not analytic), **pre-bake**: simulate all frames once at setup into a Float32Array (frames × N × 2), then draw frame `Math.round(t*fps)` from the bake. That stays seek-safe.

## Three.js points (thousands to millions)

`THREE.Points` with a custom ShaderMaterial; compute position in the vertex shader from attributes (seed, start, target) and a `uTime` uniform set from the timeline. Morphs: `mix(start, target, smoothstep(0., 1., uProgress - delay))`. Curl noise in GLSL (analytic, deterministic). Additive blending, `depthWrite: false`, size attenuation for depth. Use the HyperFrames Three.js adapter (see `hyperframes-animation`).

## Higgsfield prompts

- "glowing particles forming the [logo/word] in mid-air, thousands of tiny light particles converging from swirling streams, dark background, blue and white glow, shallow depth of field bokeh, cinematic"
- "subject disintegrating into fine dust particles drifting away on the wind, from left to right, dramatic lighting, dark background"
- "abstract flow field of luminous particles streaming in curling currents, long exposure feel, magenta and cyan, black background"
- "golden sparks bursting from an impact, motion streaks, embers drifting, dark background"
Use AI clips for backgrounds and atmosphere; build logo formations in AE/Blender for exact, legible results.
