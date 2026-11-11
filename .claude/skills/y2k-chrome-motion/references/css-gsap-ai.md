# Y2K chrome: CSS / GSAP (HyperFrames) and Higgsfield prompts

## CSS chrome type

```css
.chrome {
  font: 400 160px/0.95 "Audiowide", "Orbitron", sans-serif; text-transform: uppercase; letter-spacing: .02em;
  background: linear-gradient(105deg,#3a4350 0%,#f6fbff 20%,#8fa0b2 38%,#ffffff 50%,#2e3742 64%,#eef6fd 82%,#6b7888 100%);
  background-size: 220% 100%; background-position: 0% 50%;
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 2px 0 #1b2129) drop-shadow(0 18px 30px rgba(0,0,0,.35));
}
.holo { background: linear-gradient(120deg,#FF9DE2,#C8A8FF,#9FE7FF,#B5FFD9,#FF9DE2); background-size: 300% 300%; }
.sparkle { width: 60px; height: 60px; background: #fff;
  clip-path: polygon(50% 0,58% 42%,100% 50%,58% 58%,50% 100%,42% 58%,0 50%,42% 42%);
  filter: drop-shadow(0 0 12px #fff); }
```
(The chrome gradient comes from the HyperFrames `embedded-captions` "chrome" style.)

## GSAP moves

```js
const beat = 0.5, at = n => n * beat;
// chrome title settle + sheen sweep (move the gradient)
tl.fromTo(".chrome", { y: 30, scale: 1.08, opacity: 0 }, { y: 0, scale: 1, opacity: 1, duration: 0.45, ease: "power3.out" }, at(1))
  .fromTo(".chrome", { backgroundPosition: "0% 50%" }, { backgroundPosition: "100% 50%", duration: 0.9, ease: "power2.inOut" }, at(2));
// sparkle twinkle
tl.fromTo(".sparkle", { scale: 0, rotation: 0 }, { scale: 1.2, rotation: 45, duration: 0.2, ease: "back.out(3)", stagger: 0.12 }, at(2.5))
  .to(".sparkle", { scale: 0, opacity: 0, duration: 0.35, ease: "power2.in", stagger: 0.12 }, at(3));
// holo shift
tl.to(".holo", { backgroundPosition: "100% 50%", duration: 4, ease: "none" }, 0);
// bubble pop
tl.from(".bubble", { scale: 0, duration: 0.6, ease: "elastic.out(1, 0.5)", stagger: 0.08 }, at(4));
// 3D spin of a logo
tl.to(".logo", { rotationY: 360, transformPerspective: 900, duration: 1.4, ease: "power2.inOut" }, at(5));
```
Glitch: three copies of the scene with `mix-blend-mode: screen`, tinted R/G/B, offset with `set()` calls for 2–6 frames on the cut. Liquid: SVG `feTurbulence` + `feDisplacementMap` on chrome type, animating `baseFrequency` via the timeline.

## Higgsfield prompts

Use `higgsfield-generate` for hero assets (render chrome objects, then animate in AE).

- **Liquid chrome type:** "the word [WORD] as liquid chrome mercury lettering, mirror-polished metal, dripping melted edges, high contrast white highlights and black reflections, Y2K futurism, studio lighting, black background, sharp detail"
- **Y2K chrome object:** "glossy liquid chrome [object], inflated rounded forms, iridescent pastel reflections, 4-point star sparkles, soft lens flare, baby blue to lilac gradient background, early 2000s futurism, 3D render"
- **Cyber-sigil:** "sharp tribal cybersigilism chrome ornament, thorny mirror metal shapes, black background, Y2K revival, symmetrical"
- **Video:** "slow 3D turntable of the chrome [logo], reflections streaking across, sparkle glints, subtle lens flare, black background" (image-to-video from the still).

Reject results where the chrome is flat grey (no strong highlight/dark contrast).
