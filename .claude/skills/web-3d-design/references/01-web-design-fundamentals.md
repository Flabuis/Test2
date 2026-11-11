# 01 — Web Design Fundamentals

## Grid
- **12-column grid** on desktop (it divides into 2, 3, 4 and 6). Gutters 16–32px. Max content width roughly 1200–1440px; let full-bleed images run edge to edge.
- Reduce the columns as the screen narrows: **12 → 8 (tablet) → 4 (mobile)**. Simpler sites use 4 → 2 → 1.
- Outer margins: about 16–24px on mobile, 4–8vw on desktop.
- In CSS use `display:grid; grid-template-columns: repeat(12, 1fr)` with `gap`. Use flexbox for single rows and columns.
- Break the grid on purpose, at most one or two moments per page (an overlapping image, an oversized headline). Breaking it everywhere reads as messy.

## Spacing
- Use an **8px base scale**: 4, 8, 16, 24, 32, 48, 64, 96, 128, 160.
- Spacing groups things (proximity). Space inside a group must be smaller than the space between groups.
- Section padding is generous: 96–160px on desktop, 64–96px on mobile. Premium sites use a lot of whitespace.

## Typography
- Use **2 typefaces at most**: a display face for personality and a text face for reading. A single variable family is fine.
- Body text 16–20px, line-height 1.5–1.7, line length **45–75 characters** (`max-width: 65ch`).
- Headlines are tight: line-height 0.9–1.15, tracking −1% to −4% at large sizes.
- Use a type scale (ratio 1.25–1.5) and fluid sizes: `font-size: clamp(2.5rem, 6vw, 7rem)`.
- Contrast comes from **size + weight + colour**. Avoid more than about 4 distinct styles per page.
- Web fonts: use `font-display: swap`, subset where possible, preload the hero font.

## Colour
- Use the **60-30-10** split: background / surface / accent. Keep one accent for actions, so CTAs are the most saturated thing on the page.
- Define colours as CSS variables (`--bg`, `--fg`, `--accent`) so dark mode and theming are just a token swap.
- Contrast: **4.5:1** for body text, **3:1** for large text and UI elements (WCAG AA).
- Avoid pure black on pure white for long reading. Use #0e0e12 on #f5f5f2 or similar.

## Hierarchy (what to see 1st, 2nd, 3rd)
1. One dominant element per screen (headline or hero visual).
2. Supporting copy.
3. Action (CTA).
Squint test: blur the screen and check the order still reads correctly.
Don't design around the F-pattern. People scan in many patterns (layer-cake, spotted, marking…), so make hierarchy carry the order (see 08).

## Responsive
- Design **mobile and desktop key frames** together; don't treat mobile as an afterthought.
- Touch targets ≥ 44×44px. Hover doesn't exist on touch, so any info shown on hover needs a tap or always-visible fallback.
- Use `clamp()`, `min()`, `max()`, container queries and `aspect-ratio` instead of many breakpoints.
- Common breakpoints: 480 / 768 / 1024 / 1440.

## Imagery
- One striking hero image beats a carousel. Carousels hide content, and people rarely look past slide 1.
- Keep crop and colour treatment consistent across the site (same grade, same corner radius, same shadow).
- Give images some depth: light, shadow and selective focus (see 07). A flat, evenly blurred image looks fake.
