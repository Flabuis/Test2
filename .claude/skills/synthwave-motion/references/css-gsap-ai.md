# Synthwave: CSS / GSAP (HyperFrames) and Higgsfield prompts

## CSS scene

```css
.sky { background: linear-gradient(#0B0221 0%, #2A0B4A 45%, #FF2BD6 78%, #FF8A00 100%); }
.floor { position: absolute; left: -50%; right: -50%; bottom: 0; height: 60%;
  transform-origin: 50% 0; transform: perspective(500px) rotateX(70deg);
  background-image:
    linear-gradient(#FF2BD6 3px, transparent 3px),
    linear-gradient(90deg, #FF2BD6 3px, transparent 3px);
  background-size: 120px 120px; background-color: #0B0221;
  box-shadow: 0 0 60px #FF2BD6 inset;
  -webkit-mask-image: linear-gradient(transparent 0%, #000 35%); }
.sun { width: 620px; height: 620px; border-radius: 50%;
  background: linear-gradient(#FFD319, #FF8A00 55%, #FF2BD6);
  -webkit-mask-image: repeating-linear-gradient(#000 0 var(--gap-top, 40px), transparent 0 var(--gap, 14px));
  filter: drop-shadow(0 0 60px #FF2BD6); }
.neon { font: 400 120px "Mr Dafoe", cursive; color: #fff;
  text-shadow: 0 0 6px #fff, 0 0 18px #FF2BD6, 0 0 40px #FF2BD6, 0 0 90px #FF2BD6; }
.chrome80 { background: linear-gradient(#0A1F6E 0%, #56B4FF 25%, #fff 49%, #2B1300 50%, #B85C00 75%, #FFD9A0 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; -webkit-text-stroke: 2px #FFE3F6; }
.scanlines { background: repeating-linear-gradient(rgba(0,0,0,.25) 0 2px, transparent 2px 4px); mix-blend-mode: multiply; }
```
For true slits that thicken toward the bottom, use an SVG mask of rectangles with increasing heights instead of `repeating-linear-gradient`.

## GSAP moves

```js
const BPM = 100, beat = 60 / BPM, at = n => n * beat;
// endless grid drive (one cell per beat, linear)
tl.fromTo(".floor", { backgroundPosition: "0 0" }, { backgroundPosition: "0 120px", duration: beat, ease: "none", repeat: 63 }, 0);
// beat pulse
for (let b = 0; b < 64; b++) tl.fromTo(".floor", { filter: "brightness(1.8)" }, { filter: "brightness(1)", duration: beat * 0.8, ease: "expo.out" }, at(b));
// sun set
tl.to(".sun", { yPercent: 35, duration: beat * 64, ease: "sine.inOut" }, 0);
// chrome title slam
tl.fromTo(".chrome80", { scale: 3, opacity: 0, z: 0 }, { scale: 1, opacity: 1, duration: beat, ease: "expo.out" }, at(4));
// neon ignite (seek-safe sequence)
[1,0,1,1,0,0,1,0,1,1].forEach((v, i) => tl.set(".neon", { opacity: v }, at(6) + i / 15));
```

## Higgsfield prompts

- **Master scene:** "synthwave outrun landscape, glowing magenta neon perspective grid floor racing to the horizon, giant segmented retro sun with horizontal slits, yellow to pink gradient, purple wireframe mountains, palm tree silhouettes, starry night sky fading to magenta and orange at the horizon, symmetrical composition, 1980s retro futurism, heavy bloom"
- **Darksynth:** "darksynth scene, black and blood red neon grid, ominous red sun, jagged wireframe mountains, cyberpunk 80s horror mood, heavy glow, VHS grain"
- **Title:** "1980s chrome title lettering '[WORD]', horizon reflection chrome (blue sky top, dark horizon line, orange bottom), bevel, star glint, on a neon grid background"
- **Video:** "camera drives forward over the endless neon grid toward the setting segmented sun, smooth constant speed, stars twinkling, slow parallax mountains" (image-to-video from the master scene still).

Check the result for a centred vanishing point and a properly segmented sun.
