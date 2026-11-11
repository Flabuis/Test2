# Glassmorphism: background and sources

Translucent blurred "glass" appeared in Windows Vista's Aero (2007) and Apple's iOS 7 (2013) and macOS Big Sur (2020) interfaces. The name "glassmorphism" spread around 2020–21 as a successor to neumorphism: semi-transparent panels, background blur, a subtle border and soft shadow, over vivid backgrounds. In June 2025 Apple introduced **Liquid Glass** across iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26 and tvOS 26: a translucent material that refracts the content behind it, reflects surrounding content, and reacts to movement with real-time specular highlights.

Apple guidance (as reported; read the Human Interface Guidelines > Materials for exact wording):
- Liquid Glass aims to keep the content beneath more visible than heavy blur did; legibility comes from refraction, some blur and edge highlighting.
- Don't overuse it in the content layer; don't layer Liquid Glass on Liquid Glass (confuses hierarchy).
- Its colour adapts to surrounding content and between light and dark.

Accessibility concerns: transparency can reduce text contrast; heavy blur can be uncomfortable; stacked depth can confuse hierarchy; heavy blur is expensive on mobile GPUs. Check WCAG contrast (4.5:1 body, 3:1 large text) over the actual background and offer reduced-transparency fallbacks in live UI.

## Sources (gathered 2026-10-10)

- [IxDF: Glassmorphism](https://ixdf.org/literature/topics/glassmorphism)
- [Axess Lab: Glassmorphism meets accessibility](https://axesslab.com/?p=5111)
- [CMARIX: Glassmorphism, the new UI design trend](https://www.cmarix.com/blog/glassmorphism-the-new-trendsetter-in-2021-for-ui-design/)
- [Figr: Glassmorphism](https://figr.design/blog/glassmorphism-0e8b1)
- [UXMagic: What is glassmorphism](https://uxmagic.ai/blog/what-is-glassmorphism)
- [LogRocket blog: glassmorphism](https://blog.logrocket.com/?p=185521)
- [Design+Code: CSS glassmorphism animation](https://designcode.io/css-handbook-glassmorphism-animation)
- [Creative Market: Text Glassmorphism Motion Effect AEP](https://creativemarket.com/JosepMotion/284951073-Text-Glassmorphism-Motion-Effect-AEP)
- [cultvfx: Frosted glass effect](https://cultvfx.gumroad.com/l/frostedglass)
- [Wikipedia: Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass)
- [Pixel Envy: Apple updated its HIG for Liquid Glass](https://pxlnv.com/linklog/hig-liquid-glass/)
- [Design Milk: Apple returns to a layered design with Liquid Glass](https://design-milk.com/apple-returns-to-a-layered-software-design-with-liquid-glass-interface/)
- [Yanko Design: Liquid Glass hands-on](https://www.yankodesign.com/2025/06/12/apples-liquid-glass-hands-on-why-every-interface-element-now-behaves-like-physical-material/amp/)
- [STRV: Liquid Glass and the future of design](https://strv.com/blog/liquid-glass-and-the-future-of-design)
- [The Plus Addons: Liquid Glass UI](https://theplusaddons.com/blog/liquid-glass-ui/)

Numeric starting points (blur 12–20 px, fill 12–25%, 1 px gradient border) come from design-blog guidance; video values in the skill are scaled for 1080-wide frames.
