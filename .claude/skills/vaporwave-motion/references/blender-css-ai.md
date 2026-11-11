# Vaporwave: Blender, CSS/GSAP (HyperFrames) and Higgsfield

## Blender (via the `blender` MCP)

Save to `C:\Users\basha\Motion Design\Cluads Work Folder\vaporwave\`.
- **Statue:** import a public-domain statue scan (e.g. Scan the World / museum open-access scans; check the licence). Decimate (ratio 0.05–0.2) for a low-poly look, Shade Flat. Material: Principled, Base Color white/marble or a pastel tint, Roughness 0.4; or Emission-free toon look with a ColorRamp on a Diffuse → Shader to RGB setup.
- **Scene:** checkerboard floor (Checker Texture, Scale 20, pink/cyan or black/white), pastel gradient World, floating primitives (UV sphere chrome: Metallic 1 Roughness 0.05; pyramids; torus), palm cut-outs as image planes.
- **Animation:** statue Z rotation 360° over the loop (linear, Cycles modifier), primitives bobbing with Noise modifiers on location (phase-locked to the loop length) or sine drivers `sin(frame/48*2*pi)*0.1`.
- **PS1 / early-3D look:** render at 25–33% resolution, then upscale in AE with nearest-neighbour (Draft quality) or in the compositor with Scale node (Filter: Nearest); no anti-aliasing (Film > Filter Size 0.01 px); posterize colours.
- Render PNG sequence with transparency for compositing.

## CSS / GSAP (HyperFrames)

Win95 chrome: the open-source **98.css** library recreates Windows 98 UI (windows, buttons, title bars); or hand-roll:
```css
.win { background:#C0C0C0; box-shadow: inset -1px -1px #0a0a0a, inset 1px 1px #fff, inset -2px -2px #808080, inset 2px 2px #dfdfdf; }
.title { background: linear-gradient(90deg,#000080,#1084D0); color:#fff; font: bold 16px "W95FA", "MS Sans Serif", sans-serif; }
.checker { background: conic-gradient(#FF71CE 25%, #01CDFE 0 50%, #FF71CE 0 75%, #01CDFE 0) 0 0 / 120px 120px; transform: perspective(600px) rotateX(70deg); }
.sky { background: linear-gradient(#FBC2EB, #A6C1EE); }
.pixel { image-rendering: pixelated; }
```
Fullwidth text helper:
```js
const fw = s => [...s].map(c => c === " " ? "\u3000" : (c >= "!" && c <= "~") ? String.fromCharCode(c.charCodeAt(0) + 0xFEE0) : c).join("");
// fw("vaporwave") -> "ｖａｐｏｒｗａｖｅ"
```
GSAP:
```js
const L = 8;  // loop seconds
tl.to(".statue", { rotationY: 360, duration: L, ease: "none" }, 0);
tl.to(".float", { y: -14, duration: L / 4, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0);
// error cascade (stepped)
gsap.utils.toArray(".err").forEach((e, i) => tl.fromTo(e, { opacity: 0, scale: .9 }, { opacity: 1, scale: 1, duration: 0.05, ease: "steps(1)" }, 1 + i * 0.1));
tl.set(".err", { opacity: 0 }, 2.6);
// checker scroll
tl.fromTo(".checker", { backgroundPosition: "0 0" }, { backgroundPosition: "0 240px", duration: L, ease: "none" }, 0);
```

## Higgsfield prompts

- "vaporwave aesthetic collage, white marble Greek bust of Helios on a pink and cyan checkerboard floor, pastel gradient sky, palm trees, floating chrome sphere, Windows 95 error window, Japanese katakana text, VHS grain, dreamy, 1990s"
- "empty 1990s shopping mall atrium with fountain and palm trees, pastel neon lighting, hazy, VHS footage look, mallsoft"
- "Windows 95 desktop in pastel colours with overlapping error dialogs and a pixel cursor, retro computer, lo-fi"
- Video: "slow rotation of a marble statue floating in a pastel void, checkerboard floor, dreamy slow motion, VHS texture, seamless loop"
Avoid real brand logos and recognisable copyrighted characters.
