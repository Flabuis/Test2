# 17 — Study Notes: Sergei Chyrkov, "NO MORE AI SLOP | Claude Design Full Tutorial"

Source: Sergei Chyrkov, YouTube `T96O8dTzi2Q`, 14:47.
Files: `Training Data/Principles study/claude-design-tutorial/` (transcript.txt, transcript-paragraphs.txt, video.en.vtt, video.description; video.mp4 + frames once downloaded).
Thesis: **the difference between generic AI output and a polished site isn't a better prompt, it's a design process**, built around a reusable design system.

## The workflow (pizza-builder landing page example)
1. **Spec first, with AI help:** describe the project in a few words to Claude chat and ask it to write a **detailed prompt / spec as a Markdown file**. Download the `.md`.
2. **Baseline:** in Claude Design (desktop app → Design), "Implement" + attach the `.md`, no template, no design system, Opus. Result: works (size picker, toppings, preview) but looks **generic** (SVG-style illustrations, template feel). Expect this.
3. **Find a visual reference:** Pinterest / Mobbin ("fun website design"). Pick 1–2 images whose **typography and mood** you like. Inspiration, not copying.
4. **Create a design system from the reference:** Design System dropdown → Create → sources can be **GitHub repo, local codebase, Figma file, or visual assets**. Drop the image in and name it. Output is a large system: fonts, numbers/type scale, colours, blobs and shapes, wordmark, elevations, radii, animations, example landing-page style. "Would take days in Figma."
5. **Apply the system to the project:** + → pick the design system, then a targeted prompt: *"Update the website design layout using the design system. Hero full viewport. Add parallax on-scroll animations with pizzas and ingredients."* Result: full-screen hero, custom cursor, parallax (adjustable in **Tweaks**), horizontal-scroll section on a tomato background, text animations, full-screen footer.
6. **Real imagery:** generate a few photos (people, real pizza) and ask it to place them, replacing illustrations with photography. A big quality jump.
7. **Hand off to code:** Share → **Send to Claude Code** (local agent or web session), or download a zip for Cursor. Build in Claude Code with a **cheaper model** (Sonnet), because the design decisions are already made. Saves tokens.
8. **Reuse the same system for brand assets:** a menu (Document template, answering its questions: single page, pizzas/drinks/salads, 20 items, no photos) and Instagram posts from an attached photo. **Website, menu and social all stay consistent** because they share one system.

## Principles
- **Process > prompt.** Spec → baseline → reference → system → apply → refine → code.
- **The design system is the leverage point.** Create it once, apply it everywhere (web, print, social).
- **Visual references beat adjectives.** One good reference image gives the AI typography, palette and shape language that words can't.
- **Replace AI illustration with real photography** to escape the "AI look".
- **Token economy:** Claude Design is expensive (he hit usage limits). Design in Design, build in Code with a cheaper model.
- He still calls the results "would work on it more" for designers. **Human polish is still needed.**

## Cross-check with 16 (UI Collective)
- UI Collective warns that AI design-system **sync with existing Figma systems** only captures part of a real system, and that AI-invented token sets are hard to reason about. Claude Design's *generated-from-a-reference* system is great for **speed and exploration**, but for a long-lived brand, **audit it with the 16 rules**: tokens in tiers, mapped names by role (surface/border/text/icon), no component-specific tokens, 4-pt scales, focus states, light/dark tested.
- Best of both: generate with Claude Design → audit and rename tokens → export to code tokens (`@theme`, 14) → teach AI agents with skills (16 §9).

## How we can use this ourselves
- **We have the same capability:** the Artifact tool's quickstart lists Design / Design System types. A user's design system can be created from a codebase or reference and then used for slides, designs and pages. For client brand films: build a design system from the brand's references once, then generate the site, social posts, end cards and decks from it.
- For motion reels: the same system defines **motion tokens** (durations, easing, overlap) alongside colour and type, so reel graphics and the website feel like one brand.
