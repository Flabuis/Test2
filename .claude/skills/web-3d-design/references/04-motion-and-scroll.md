# 04 — Motion & Scroll on the Web

## Principles (from motion design, applied to UI)
- **Motion has a job**: guide attention, show cause and effect, show hierarchy, or carry the brand. Decoration-only motion is noise.
- **Overlap**: each move starts before the last one ends (stagger 0.03–0.1s). No dead frames.
- **Strong first second**: the hero should animate within about 300ms of load. Never hold the page behind a long loader.
- Durations: micro (hover, button) 150–250ms; UI transitions 300–500ms; hero and story moments 0.8–1.6s.
- Easing: entrances `power3.out` / `expo.out`; exits `power2.in`; movement between two states `power2.inOut`. Avoid linear except for loops and scroll scrubbing.

## CSS first
- Animate only `transform` and `opacity` (GPU-friendly). Never animate `width`, `top` or `margin` in a loop.
- `transition` for hovers, `@keyframes` for loops, `view-transition` API for page transitions.
- Native scroll-driven animations: `animation-timeline: view()` / `scroll()`. No JS needed for simple reveals.

## GSAP (the industry standard)
```js
gsap.from('.hero h1 .word', { yPercent: 110, duration: 1, ease: 'expo.out', stagger: 0.06 });
const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
tl.from('.a', { y: 40, opacity: 0 }).from('.b', { y: 40, opacity: 0 }, '-=0.6'); // overlap
```
- `timeline` = an AE composition; position parameter (`'-=0.6'`, `'<'`) = sliding layers on the timeline.
- **SplitText**: split headlines into lines/words/chars for the masked "rise-in" reveal (wrap each in an `overflow:hidden` mask).
- GSAP can tween any number: Three.js `mesh.position`, uniforms, camera FOV.

## ScrollTrigger (scroll storytelling)
```js
gsap.to(camera.position, { z: 2, scrollTrigger: { trigger: '#s2', start: 'top top', end: '+=150%', scrub: 1, pin: true } });
```
- `scrub`: animation progress is tied to the scrollbar, so scroll acts as a timeline scrubber.
- `pin`: hold a section in place while its animation plays.
- Patterns: pinned 3D product that rotates as you scroll; a camera flying through a scene in chapters; horizontal scroll galleries; text that fills in as you scroll.
- Plan it like a reel: a **shotlist of scroll chapters**, each with a start state (key frame) and end state.

## Smooth scroll
**Lenis** gives inertia scrolling (the award-site feel). Connect it to ScrollTrigger: `lenis.on('scroll', ScrollTrigger.update)` and drive it from `gsap.ticker`. Don't hijack scroll direction or speed in ways that fight the user.

## Signature interactions
- Magnetic buttons (the element moves slightly toward the cursor).
- Custom cursor that grows or changes on hover targets (desktop only).
- Image hover distortion (WebGL shader) or a clip-path reveal.
- Page transitions: an overlay wipe, or a shared-element morph (a thumbnail expanding into the hero).
- Marquees for logos and taglines.
- Number counters and line draws for stats.

## Accessibility for motion
Always respect `prefers-reduced-motion`: turn off scrubbing, parallax and auto-play, keep simple fades.
```css
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }
```
