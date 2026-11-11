# Swiss style: HyperFrames / GSAP

Same rules as `../SKILL.md`. Use one paused GSAP timeline (HyperFrames contract: read `hyperframes-core` first).

## Grid in CSS

```css
:root {
  --m: 80px; --g: 40px; --cols: 4; --rows: 8;
  --ink: #111; --paper: #F2F0EB; --accent: #E30613;
}
.stage { width: 1080px; height: 1920px; background: var(--paper); color: var(--ink);
  display: grid; padding: var(--m); gap: var(--g);
  grid-template-columns: repeat(var(--cols), 1fr); grid-template-rows: repeat(var(--rows), 1fr); }
h1 { font: 700 144px/0.92 "Inter Display", "Helvetica Neue", sans-serif; letter-spacing: -0.035em; }
.line { overflow: hidden; } .line > span { display: block; } /* line-rise mask */
.num { font-variant-numeric: tabular-nums; }
```
Place items with `grid-column` / `grid-row`, never free pixel offsets.

## Eases

| Use | GSAP ease |
|---|---|
| Snap out (default) | `expo.out` or `power4.out` |
| Layout to layout | `power4.inOut` / `expo.inOut` |
| Tickers, scrolls | `none` |
| Never | `back`, `elastic`, `bounce`, `rough`, `wiggle` |

## Time grid

```js
const BPM = 120, beat = 60 / BPM;        // 0.5 s
const at = n => n * beat;                // place tweens on beats
```

## Moves

```js
// line rise
tl.from(".h1 .line > span", { yPercent: 100, duration: beat * 0.75, ease: "expo.out", stagger: 0.1 }, at(1));
// column wipe from the left edge
tl.fromTo(".field", { scaleX: 0, transformOrigin: "0% 50%" }, { scaleX: 1, duration: beat, ease: "expo.inOut" }, at(3));
// rule draw
tl.from(".rule", { scaleX: 0, transformOrigin: "0% 50%", duration: beat * 0.6, ease: "expo.out" }, at(2));
// counter
const o = { v: 0 };
tl.to(o, { v: 2048, duration: beat * 2, ease: "expo.out",
  onUpdate: () => (num.textContent = Math.round(o.v).toLocaleString()) }, at(4));
// cell fill in reading order
tl.from(".cell", { scale: 0, transformOrigin: "0% 0%", duration: beat * 0.5, ease: "power4.out",
  stagger: { each: 0.067, grid: [8, 4], from: "start" } }, at(5));
```

Keep all motion seek-safe (no `Math.random`, no real-time timers).
