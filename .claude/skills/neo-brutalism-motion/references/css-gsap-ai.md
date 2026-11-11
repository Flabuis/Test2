# Neo-brutalism: CSS / GSAP (HyperFrames) and Higgsfield

## CSS components

```css
:root { --ink:#000; --bg:#FFF6E5; --y:#FFE14D; --p:#FF6FB5; --b:#5B8CFF; --g:#B8FF5C;
        --bw: 8px; --sh: 12px; --r: 10px; }        /* video scale; UI: bw 3px, sh 4-6px */
.nb { background: var(--y); border: var(--bw) solid var(--ink); border-radius: var(--r);
      box-shadow: var(--sh) var(--sh) 0 var(--ink); }
.nb.pressed { transform: translate(var(--sh), var(--sh)); box-shadow: 0 0 0 var(--ink); }
h1 { font: 400 180px/0.9 "Archivo Black", sans-serif; letter-spacing: -0.02em; color: var(--ink); }
.label { font: 700 28px "Space Mono", monospace; text-transform: uppercase; }
.sticker { transform: rotate(-8deg); border-radius: 999px; }
.marquee { background: var(--ink); color: #fff; white-space: nowrap; overflow: hidden; transform: rotate(-3deg); }
.mark { background: linear-gradient(var(--g), var(--g)) no-repeat left / 0% 100%; }   /* highlight swipe */
```
Animate `transform` only; keep border width fixed (changing borders causes reflow). Live UI: `:focus-visible { outline: 4px solid #000; outline-offset: 4px; }`.

## GSAP moves

```js
const beat = 0.5, at = n => n * beat;
// slam card with overshoot and shake
tl.from(".card", { y: -900, rotation: -6, duration: 0.28, ease: "back.out(2.2)", stagger: 0.12 }, at(1))
  .to(".scene", { x: 6, y: -4, duration: 0.033, yoyo: true, repeat: 1, ease: "none" }, at(1) + 0.28);
// press into shadow (snap)
tl.to(".btn", { x: 12, y: 12, boxShadow: "0px 0px 0 #000", duration: 0.07, ease: "steps(2)" }, at(3))
  .to(".btn", { x: 0, y: 0, boxShadow: "12px 12px 0 #000", duration: 0.18, ease: "back.out(3)" }, at(3) + 0.12);
// sticker slap
tl.from(".sticker", { scale: 0, rotation: 25, duration: 0.25, ease: "back.out(3)" }, at(4));
// highlight swipe
tl.to(".mark", { backgroundSize: "100% 100%", duration: 0.15, ease: "power4.out" }, at(5));
// marquee (linear, seek-safe)
tl.fromTo(".marquee .track", { xPercent: 0 }, { xPercent: -50, duration: 6, ease: "none", repeat: 3 }, 0);
// cursor click
tl.to(".cursor", { x: 420, y: 260, duration: 0.35, ease: "power3.out" }, at(6))
  .to(".cursor", { scale: 0.88, duration: 0.06, yoyo: true, repeat: 1 }, at(6) + 0.35);
```

## Higgsfield prompts

- "neo-brutalist poster design, thick black outlines, hard offset black shadows with no blur, flat saturated yellow, pink and blue blocks, oversized bold black display type, stickers and rotated badges, cream background, playful, clean flat vector"
- "neubrutalism UI mockup for [product], outlined cards with hard shadows, flat bright colours, big bold headline, mono labels, cursor arrow, flat 2D"
Use generations as style frames; rebuild typography and components natively for exact type and motion.
