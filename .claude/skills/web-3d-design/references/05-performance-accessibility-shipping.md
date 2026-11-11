# 05 — Performance, Accessibility & Shipping

## Performance budget (targets)
- **LCP < 2.5s**, **INP < 200ms**, **CLS < 0.1** (Core Web Vitals).
- First load JS under about 300KB gzipped. 3D model under about 2–5MB (Draco + KTX2). Hero image under about 200KB (AVIF/WebP).
- 60fps on a mid-range phone. Test on a real phone, not only the dev machine.

## 3D performance rules
- Cap pixel ratio at 2 (or 1.5 on mobile).
- Draw calls matter more than polygons: merge geometry, use `InstancedMesh` for repeats, share materials.
- Bake lighting, AO and shadows into textures. Use few real-time lights.
- Compress models (Draco/Meshopt) and textures (KTX2). Use power-of-two texture sizes, 2K max on mobile.
- Pause rendering when the canvas is offscreen (`IntersectionObserver`) or the tab is hidden.
- `dispose()` geometries, materials and textures when removing them.
- Show a lightweight poster image or loader progress (`LoadingManager`) while assets stream.
- Have a fallback for no WebGL or low-power devices: a static image or video.
- Check with `stats.js` / `r3f-perf` and `renderer.info` (calls, triangles).

## Images & fonts
- `<img loading="lazy" decoding="async" width height>`. Always set dimensions to avoid layout shift.
- `srcset`/`sizes` or `<picture>` for responsive images. Use AVIF → WebP → JPG.
- Preload the hero image and main font. Self-host fonts with `font-display: swap`.
- Background video: muted, `playsinline`, short loop, H.264/WebM, poster frame, under about 3MB.

## Accessibility (non-negotiable)
- Semantic HTML: `header`, `nav`, `main`, `section`, `h1`→`h6` in order, `button` for actions, `a` for navigation.
- Everything works by keyboard with a visible focus state (`:focus-visible`).
- Alt text on meaningful images, `alt=""` on decorative ones. The canvas gets `aria-label` or a text alternative.
- Colour contrast meets WCAG AA. Don't use colour alone to carry meaning.
- Support `prefers-reduced-motion`. Never auto-play sound.
- Real text in HTML, not baked into images or the canvas (helps SEO, translation and screen readers).

## SEO basics
`<title>`, meta description, Open Graph image, one `h1` per page, meaningful URLs, sitemap.xml. Server-render or pre-render content if the site is JS-heavy.

## Tooling & hosting
- **Vite**: dev server and bundler (`npm create vite@latest`). Use it once a project outgrows a single HTML file.
- Frameworks: plain Vite + Three.js for experiments; **Next.js/Astro + R3F** for full sites.
- Hosting: Vercel, Netlify, Cloudflare Pages (free tiers, deploy from Git). Higgsfield websites is also available via the higgsfield-websites skill.
- Check before launch: Lighthouse, PageSpeed Insights, a real phone, Safari (WebGL quirks), keyboard-only run-through.
