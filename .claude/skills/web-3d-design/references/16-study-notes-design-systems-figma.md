# 16 — Study Notes: UI Collective, "Learn Design Systems: Figma Variables, Components, AI, and More"

Source: UI Collective, YouTube `lsgVRCJ4fko`, 4:00:41.
Files: `Training Data/Principles study/uic-design-systems-figma/` (transcript.txt, transcript-paragraphs.txt, video.en.vtt, video.description with ~60 chapters; video.mp4 + frames/ every 30 s once downloaded).
Why it matters: every serious site (and every brand film, menu or social kit) needs one source of truth for colours, type and spacing. This is the method for building it. It's the same idea as `@theme` tokens (14) and `constants/index.js` (13).

## 1. Design tokens
- **Token = a raw value + a role that's reused.** `#000000` alone isn't a token. `text-action = #000` is. `8px` alone isn't a token. `radius-medium = 8` is.
- Common token types: **colour, typography, shadow, spacing, border, radius** (plus grid and motion in very mature systems).
- **Figma variables = Figma's implementation of design tokens.** Change one parent variable and every component using it updates.
- **Designs come first.** Build a few real screens you like, then extract the tokens from them. Only experts can go straight to a token library with no designs.

## 2. Where AI fits (and doesn't)
- **AI can't define your tokens.** It doesn't know your brand, products or components. You'll spend longer reverse-engineering its "canvas vs. surface vs. accent-soft" tokens than building your own.
- **AI is inconsistent at building components:** missing variants, unnecessary divider components, properties set up wrong.
- **AI is good for:** generating a type scale from exact rules, pushing values into Figma via the MCP, Figma Agents building text styles from your variables, and writing **skills** that teach AI your system (section 9).
- "Design-system sync" features in AI tools (including Claude Design's) only pick up roughly 28% of a real system in his experience. Don't trust them blindly.

## 3. Collection architecture
Two common structures. They do the same job:
| Three-tier (recommended, scales better) | Two-tier |
|---|---|
| **Brand**: raw colour scales (purple-50…950, red, green, gray, orange, blue + foundation black/white) | **Primitive**: raw scales **and** role scales together |
| **Alias**: scales given roles: `primary`, `error`, `success`, `warning`, `information`, `neutral`, `foundation`. **Multi-brand modes live here** (Brand A / Brand B), plus font family/weight strings, border-width and radius | n/a |
| **Mapped**: what components actually use: `surface/*`, `border/*`, `text/*`, `icon/*`. **Light/Dark modes live here** | **Semantic**: same as mapped |
| **Responsive** (4th collection): type sizes, line heights, layout spacing. **Desktop/Mobile modes** | same |
- **Rule: mapped → alias → brand. Never connect mapped straight to brand.** Only mapped tokens are applied to designs.
- **No component-specific tokens** (`button-purple`, `menu-purple`…). With 50+ components you'd have to update each one. Use shared semantic tokens that every component pulls from.
- **Scope variables** (Edit variable → scope): border-width only offers Stroke, radius only offers Corner radius, and brand colours are hidden so designers can only pick mapped tokens.

## 4. Colour scales (the #1 place teams go wrong)
- Build them **by hand so you know the maths**. Base colour = **500**. Lighter steps: overlay it at 80/60/40/20/10% on white and **colour-pick the solid result** (no opacity in variables, because opacity looks different on every background). Darker steps: the same over black.
- **Name by the maths, not by counting:** 20% jumps = 100 steps, a 10% jump = 50. Result: 50, 100, 200…900, 950. Need an in-between later? A 50% step between 200 and 300 = **250**. The scale grows logically.
- Start with only: **primary** (+ maybe secondary/tertiary), **red = error, green = success, orange = warning, blue = information, gray = neutral/text**, plus black and white. You rarely need 18 hues.

## 5. Mapped tokens: the starter set
| Group | Tokens |
|---|---|
| **surface** | `page` (white), `default` (cards, modals, widgets), `action`, `action-hover`, `success`, `error`, `warning`, `information`, `disabled` |
| **border** | same as surface minus page (keep the counts aligned for easier maintenance), plus `focus` |
| **text** | `heading` (neutral-900), `body` (700), `caption` (500), `placeholder`, **`on-action`** (text sitting on an action surface, e.g. white on a purple button), `on-action-hover`, `action` / `action-hover` (links), `success/error/warning/information`, `disabled` |
| **icon** | mirrors text: `default`, `placeholder`, `on-action`, `action`, status colours, `disabled`. **Paired icon and text should use the same value** |
- **Dark mode:** finish light mode first, build components, test accessibility, **then** add a Dark column by **inverting the scale** (50↔950, 100↔900…). **Keep the brand 500 unchanged** so the brand stays recognisable. Then test and tweak.

## 6. Type & spacing
- **Type scale:** use a ratio (typescale.com; **Major Third 1.25** is a solid default). **Base paragraph = 16px** (the accessibility-safe size). **Round every size to a multiple of 4.** **Line height = 1.2 × size**, also rounded to a multiple of 4. Paragraph spacing ≈ half the size.
- Prompt pattern for AI: "Create a type scale … H1–H6, paragraph L/M/S, caption, Major Third 1.25, line-height 1.2× font size, round to nearest multiple of 4", then push it into the Responsive collection via the Figma MCP.
- Font family and weight are string variables in **alias**, so they can differ per brand.
- **One master number scale** (0, 1, 2, 4, 8, 12, 16, 20, 24, 32…) that every number variable references, the same 4-pt logic as the type scale. Advanced, but ideal.
- **Border widths:** none 0 / sm 1 / md 2 / lg 4. **Radius:** none / sm / md / lg / xl. More than about 4–5 of each is rarely needed.
- **Layout ("jumper") variables:** t-shirt spacing tokens in Responsive whose value **jumps** between modes (e.g. `large` = 24 desktop → `small` = 16 mobile). Name them by size, not use case (`page-margin` is wrong because card gaps may need the same jump). Only create the combinations your real designs need.

## 7. Component-building rules (from building ~25 components)
- **Auto layout always** (Shift+A). Padding and gap in multiples of 4. **Hug** contents, never fixed widths that let text overflow. **Fill** where a child must stretch (field icons pinned to the edge).
- **Icons are components** with a consistent bounding box (24×24 or 20×20). Check that hiding icons doesn't change the component height. **QA as you go.**
- **Properties:** text property for labels; boolean (layer) property + **instance swap** for each optional icon (`icon left` / `icon right`); **expose nested instances** so the properties of atoms show on the parent.
- **Variants:** `status` = default / hover / focus / disabled; `type` = default / outline / transparent (buttons), unselected / selected (checkbox, radio, switch, menu item, tab), default / filled / error (fields). Lowercase names.
- **Focus state:** a 2px `border/focus` rectangle **outside** the component, set to **ignore auto layout** (absolute), constraints left-right/top-bottom so it stretches. Name the layer `focus`. It's essential for keyboard and screen-reader users.
- **Strokes on the outside** (inside strokes or removing a border changes the height).
- **Borders instead of divider components** (e.g. bottom stroke on menu items). Fewer layers, cleaner instances.
- **Atomic design:** build atoms (label, field, checkbox item) and compose them (input = label + field + hint; checkbox-label = checkbox + text). This stops designers manually pairing text with different styles and gaps.
- Sensible maxima: menu ≤ 6–8 items, breadcrumb ≤ 6, tab bar ≤ 8, avatar group ≤ 5.
- **Reuse setups:** a tab-bar item started as a copy of the button with its properties trimmed.
- **Mobile:** no separate mobile design system. Add a `type: desktop / mobile` **variant only where the layout genuinely changes** (e.g. navigation collapsing into a menu).
- **What's a component?** Used more than once means a component. But it only goes into the shared design-system file if it's used across pages, teams or products. One-flow components stay local.
- **Publish:** Assets → Publish library (paid workspace). Hide internal atoms (e.g. `.checkbox item`) and publish the composed ones.

## 8. Handoff & frameworks
- **Dev Mode** gives developers specs. Even paying for 1–2 months while building the system is worth it. **Ask your developers what else they need documented.** There's no universal handoff.
- **Using a code framework** (Radix, shadcn, etc.): Figma **variant and property names, defaults and sizes must match the framework 1:1**, or technical debt builds up. A kit built for devs usually has a poor or stale Figma file, and vice versa.
- **Don't copy IBM Carbon, Shopify Polaris, etc.** Use them as reference only. You'd inherit their legacy decisions and debt without knowing why.

## 9. Making AI follow your design system (≈85% accuracy, then polish)
Create separate **skills** (one focused prompt each, with a link to the Figma frame):
1. **One skill per component group** (form elements, navigation, data display): which components exist, their variants, properties and how they relate. "Only include components in this group. Do not invent."
2. **Variables skill:** a table of mapped tokens with light/dark values **and a usage description** (when to use, when not). Mapped only, no brand or alias.
3. **Type styles skill:** family, weight, size, line height and letter spacing per style. No strict usage rules (leave the AI some freedom, then adjust).
4. **Rules + technical-debt skill:** e.g. "4+ options → checkboxes, fewer → radios", "max 5 avatars", plus known flaws you can't fix yet (e.g. outline button contrast, 12px radio label) so the AI doesn't "fix" them inconsistently.

## How this connects
- **Tokens in code:** brand/alias/mapped maps directly to Tailwind v4 `@theme` (14): `--color-purple-500` (brand) → `--color-primary-500` (alias) → `--color-surface-action` (mapped), with dark values via the `dark:` variant or a `.dark` override block.
- **For our brand films and reels:** the same token sheet (palette scale, type scale, radius, motion durations) keeps After Effects, web and social assets consistent. A "brand kit" is a design system for motion.
- See 17 (Claude Design) for generating a system from a visual reference, and why to still audit it with these rules.
