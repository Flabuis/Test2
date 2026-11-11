# Synthwave: After Effects recipes

Build through the `after-effects` MCP. Save projects to `C:\Users\basha\Motion Design\After Effects Projects\`, renders to `...\Cluads Work Folder\`. Add comp markers on beats first.

## Grid floor (no plugins; based on PremiumBeat's retrowave loop)

1. Square solid (e.g. 4000×4000), Effect > Generate > **Grid**: Size From Width Slider, Width 100–160, Border 3–5, colour white.
2. Make it 3D, X Rotation 90°, position it as the floor below the camera (or use a 3D camera looking toward the horizon).
3. **Scroll:** Effect > Distort > **Offset**, Shift Center To animated on Y. Seamless loop: move exactly one grid cell per loop period, linear. Expression:
```js
var cell = 140, period = 60 / 100;          // one cell per beat at 100 BPM
[value[0], value[1] + (time / period) * cell];
```
4. **Colour:** a solid with Gradient Ramp (magenta near the camera → violet → fading to dark at the horizon) above the grid with Track Matte = Luma (grid as the matte).
5. **Glow:** Glow (Threshold 50%, Radius 10, Intensity 1.5) + second Glow (Radius 60–100, Intensity 0.8).
6. **Horizon fade:** a black-to-transparent gradient (or feathered mask) over the far part of the grid, plus a thin bright horizon line with heavy glow.
7. **Beat pulse:** on Glow Intensity or grid colour solid Exposure, a spike on each beat marker:
```js
var m = thisComp.marker, t = 99;
if (m.numKeys) { var k = m.nearestKey(time); if (k.time > time && k.index > 1) k = m.key(k.index - 1); t = time - k.time; }
value + (t >= 0 ? 1.2 * Math.exp(-t * 8) : 0);
```

## Segmented sun

1. Ellipse shape (600–900 px), Gradient Fill (linear, top yellow `#FFD319` → orange `#FF8A00` → pink `#FF2BD6` at the bottom).
2. **Slits:** a shape layer of horizontal rectangles (Repeater: Copies 10, Position (0, 40), Scale 112% so each copy gets taller) placed over the lower half, used as **Alpha Inverted Matte** for the sun (or a Merge Paths: Subtract inside one shape layer).
3. Scroll the slits down slowly (linear), looping one slit spacing.
4. Glow: Glow Radius 80–150, Intensity 0.6, plus a soft radial gradient halo behind.
5. Set/rise: move the sun down behind the horizon over the whole piece (slow, ease in-out).

## Sky, stars, mountains

- **Sky:** Gradient Ramp or 4-Color Gradient: `#0B0221` top → `#2A0B4A` → `#FF2BD6` → `#FF8A00` at the horizon.
- **Stars:** Fractal Noise (Contrast 400–600, Brightness −80, Scale 30) → Levels so only dots remain; Screen blend; slow Offset scroll; random twinkle via a second Fractal Noise with evolving Evolution as an opacity matte.
- **Mountains:** a zig-zag shape path: solid dark fill + 2–3 px neon stroke on the ridge + Glow; a second farther layer lighter and smaller. For wireframe mountains, add triangulation lines or render them in Blender.
- **Palms:** silhouette vectors in near-black with a thin rim-light stroke on one side.

## 80s horizon chrome title

1. Text: extended or script-italic bold, white.
2. Layer Styles > **Gradient Overlay**, angle 90°, hard-stop gradient: `#0A1F6E` (top) → `#56B4FF` → `#FFFFFF` (45%) | hard stop | `#2B1300` (50%) → `#B85C00` → `#FFD9A0` (bottom). The hard stop in the middle is the horizon reflection.
3. **Bevel and Emboss:** Inner Bevel, Size 6–10, Soften 0, Gloss contour ring for extra banding.
4. **Stroke:** 3–6 px, gradient light pink/white or dark navy for the outline; optional second outer stroke via a duplicate.
5. **Star glint:** a 4-point star (Star tool: Points 4, Inner Radius 10%) + Glow on an edge; twinkle it (scale and rotate 45°) on the hit.
6. **Lens flare:** Lens Flare effect (105 mm) on a black solid, Add mode, swept across.

## Neon tube type

1. Script or monoline font. Stroke-only (fill off), stroke 6–10 px, round joins, colour pink or cyan with a whiter core (duplicate with a 2–3 px white stroke on top).
2. Glow stack: Glow Radius 10 / 40 / 120 (three instances, intensity 1.0 / 0.8 / 0.5), or Deep Glow.
3. **Ignite flicker** (seek-safe sequence) on Opacity:
```js
var on = inPoint, seq = [1,0,1,1,0,0,1,0,1,1,1,0,1];
var i = Math.floor((time - on) / thisComp.frameDuration / 2);
var base = (i < 0) ? 0 : (i < seq.length ? seq[i] * 100 : 100);
base - (i >= seq.length && Math.sin(time * 97) > 0.97 ? 35 : 0);   // rare hum dips
```

## Lasers

Thin lines (2–4 px) with Trim Paths sweeps or position sweeps, white core + coloured Glow, Add mode. Fan of beams: one line + Repeater rotation.

## VHS / CRT finish (adjustment layers, top of the comp)

- **Scanlines:** Venetian Blinds (Direction 0°, Width 2–3 px, Completion 30–45%), opacity 20–40%.
- **Chromatic aberration:** duplicate the comp, Shift Channels to R only and B only, offsets ±2–4 px (more on transitions), Add/Screen.
- **Tracking band:** a horizontal gradient band moving down used as a Displacement Map (Max Horizontal 20–60) + Noise inside it; only on transitions.
- **Jitter:** Transform Position `posterizeTime(30); wiggle(15, 1.5)`.
- **CRT:** Optics Compensation (FOV 20–40, Reverse Lens Distortion off) for slight bulge; vignette; Noise 3–6%; slight blur 0.5.
- **Grade:** Curves: lift blacks into purple, push magentas.

## Finish

- Glow before VHS; VHS last.
- Render ProRes master; H.264 at high bitrate (neon on dark bands badly).
