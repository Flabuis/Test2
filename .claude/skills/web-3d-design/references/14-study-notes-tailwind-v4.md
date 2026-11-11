# 14 — Study Notes: "Tailwind CSS v4 Full Course 2026 | Master Tailwind in One Hour"

Source: JavaScript Mastery, YouTube `6biMWgD6_JY`, 54:20. (Part 1 = concepts. The landing-page build is behind their paid platform.)
Files: `Training Data/Principles study/jsm-tailwind-v4-course/` (transcript.txt, transcript-paragraphs.txt, video.en.vtt, video.description; video.mp4 + frames once downloaded).
Why it matters to us: every build in 13 is styled with Tailwind, and it's the default styling layer for R3F/Next/Vite projects.

## 1. What Tailwind is
- **Utility-first:** instead of naming classes (`.container-heading {…}`), you compose tiny single-purpose classes in the markup: `flex justify-center items-center text-lg text-cyan-400`.
- UI kits (Bootstrap, MUI) are "fast-food menus", so every site looks the same. Tailwind is "a stocked kitchen": ingredients, not meals. Component layers built on it: **shadcn/ui**, Headless UI, Tailwind UI.
- **Not inline styles:** inline styles can't do pseudo-classes (`hover:`), media queries or dark mode, and they can't be reused. Utilities can do all of that and are shared rules.
- Used in production by OpenAI, Shopify, GitHub, Microsoft, NASA, and others.
- Sandbox: **play.tailwindcss.com**. Its "Generated CSS" tab shows what each class compiles to (theme vars → base → components → utilities).

## 2. Core utility grammar
| Pattern | Meaning |
|---|---|
| `m-4` / `p-4` | margin / padding all sides. **Margin = outside spacing** (pushes others away). **Padding = inside spacing** |
| `mt-` `mr-` `mb-` `ml-` / `mx-` `my-` | one side / horizontal / vertical |
| `w-full` `h-10` | width 100% / height 2.5rem (40px). Spacing scale is based on CSS variables (`--spacing`) |
| `text-lg` | font-size **plus a matching line-height** |
| `text-center` `font-mono` `font-extrabold` | align / family / weight |
| `bg-violet-200` `text-cyan-400` `border-violet-600` | colour family + shade (50–950) |
| `border-2` `rounded-md` `rounded-full` `shadow-xl` `ring-1` | border width / radius / shadow / ring outline |
| Hover any class in the editor (official Tailwind extension) | shows the exact CSS and rem/px value |

## 3. JIT compiler (the superpower)
- Generates CSS **only for classes you actually use**, so the bundle is tiny, builds are fast, and dev matches prod.
- **Arbitrary values** in square brackets: `text-[13px]`, `bg-[#101728]`, `p-[16px]`, `min-[320px]:...`. Fine for one-offs. If you repeat one, make it a theme token instead (section 6).

## 4. Layout
- **Position:** `relative` (offset from its normal spot), `absolute` (relative to nearest positioned parent), `fixed` (pinned to the viewport), `sticky` (normal until scrolled to a threshold); plus `top-0 inset-0 z-10`.
- **Display:** `block`, `inline`, `hidden`, **`flex`**, **`grid`**. "In CSS everything is a rectangle."
- **Flex:** `flex justify-between|center|end|around|evenly items-center gap-6` (or `space-x-6`). `flex-col` switches the axis (then `items-*` controls the cross axis).
- **Grid:** `grid grid-cols-3 gap-2`. Children fill the width automatically. `col-span-2`, `grid-rows-*`, `grid-flow-*`.
- Practice games: **Flexbox Froggy**, **Grid Garden**.

## 5. Responsive (mobile-first). The #1 thing to get right
- Breakpoints `sm` 640 / `md` 768 / `lg` 1024 / `xl` 1280 / `2xl` 1536 are **min-width**. `md:block` means "at 768px **and up**".
- **Unprefixed = mobile (all sizes).** Never use `sm:` to target phones. Write the phone layout first, then layer `sm:` → `md:` → `lg:` changes.
- Larger breakpoints override smaller ones when both match.
- `max-sm:` / `max-md:` flip it to "below this width". Combine them for ranges (`md:max-lg:`).
- Example: `hidden md:block` = hidden on phones, shown from tablet up.
- Custom breakpoints can be added in the theme (`--breakpoint-xs`, `--breakpoint-3xl`), or used inline with arbitrary values `min-[320px]:`.

## 6. Dark mode
- Prefix with `dark:`: `bg-white text-black dark:bg-black dark:text-white`. By default it follows the **OS/browser `prefers-color-scheme`**.
- **Manual toggle (v4):** add to your CSS
  ```css
  @custom-variant dark (&:where(.dark, .dark *));
  ```
  then toggle `document.documentElement.classList.toggle('dark')` from JS/React (or use a `data-theme` attribute variant).

## 7. Customisation & reuse (big v4 change: config lives in CSS, not `tailwind.config.js`)
```css
@import "tailwindcss";

@theme {
  --color-chestnut: #973f29;      /* → text-chestnut, bg-chestnut, border-chestnut */
  --font-display: "Satoshi", sans-serif;  /* → font-display */
  --breakpoint-3xl: 1920px;       /* → 3xl: */
}

@layer base {                      /* global element defaults */
  h3 { @apply text-lg font-semibold text-slate-900 dark:text-white; }
  p  { @apply text-slate-500 dark:text-slate-400; }
}

@layer components {                /* named reusable components */
  .card { @apply m-10 rounded-lg bg-white p-6 shadow-xl ring-1 ring-slate-900/5 dark:bg-slate-800; }
}

@utility flex-center {             /* custom single-purpose utility */
  @apply flex justify-center items-center;
}
```
- Order of preference for reuse:
  1. **Components** in React (a `<Button/>` that holds the long class list).
  2. `@layer components` classes.
  3. `@utility` for small repeated combos.
  4. Arbitrary values only for true one-offs.
- Theme namespaces cover colours, fonts, text sizes, breakpoints, containers, blur, animations, and more.
- **shadcn/ui**: copy-in components with variants, still styleable with plain utilities (`className="text-red-500"`).

## 8. Tips & tricks
| Trick | Class |
|---|---|
| Recolour native checkboxes/radios | `accent-pink-500` |
| **Fluid type** (smooth, no breakpoint jumps) | `text-[min(10vw,70px)]` (or `clamp()` in an arbitrary value) |
| Style file-input button | `file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2` |
| Text selection colour | `selection:bg-green-400 selection:text-black` |
| Caret colour | `caret-pink-500` |
| JS-free accordion | native `<details>`/`<summary>` + `open:` variant (`open:bg-white`) |
| Others to know | `before:`/`after:`, `active:`, `focus-visible:`, `landscape:`/`portrait:`, `aria-*:`, `print:`, gradients (`bg-linear-to-r from-… to-…`), `animate-spin/ping/pulse/bounce`, `motion-safe:`/`motion-reduce:` |
- Don't memorise classes: **⌘/Ctrl-K on tailwindcss.com** plus the official editor extension (autocomplete and hover CSS). Muscle memory comes with use.

## 9. How it plugs into our 3D web work
- The HTML layer over a `<Canvas>`: `absolute inset-0` canvas behind, `relative z-10` content in front, `pointer-events-none` on overlays that shouldn't block dragging the 3D.
- Section rhythm from 01/10 maps to utilities: `py-24 md:py-40` sections, `max-w-7xl mx-auto px-4` container, `grid md:grid-cols-12` editorial grid.
- Brand tokens go in `@theme` (colours, display font) so a re-skin is one edit, the same principle as 13's `constants/index.js`.
- Use `motion-reduce:` to drop heavy animation classes for reduced-motion users (see 04/05).
