# Pixel art: Aseprite workflow and cleanup

Save pixel files to `C:\Users\basha\Motion Design\Cluads Work Folder\pixel\` (Aseprite `.aseprite`, PNG sequences, sprite sheets).

## Editors

Aseprite (paid, standard), LibreSprite (free fork), Pixelorama (free), Photoshop with Pencil tool + Nearest Neighbor interpolation (`photoshop` MCP: set Image Interpolation to Nearest Neighbor, Pencil tool, grid = 1 px).

## Aseprite workflow

1. New sprite at native size (e.g. 64×64 character, or the full scene canvas 320×180), Color Mode Indexed, load a palette (Lospec .hex/.gpl).
2. Layers: line, colour, shading, effects. Linked cels for static parts.
3. Animation: frames with per-frame **duration** (ms) for timing by holds; **tags** per animation (idle, walk, attack) with loop direction; onion skin for in-betweens.
4. Block poses first (contact, passing for walks; anticipation, action, recovery for attacks), then in-betweens, then clean-up pass for orphan pixels.
5. Typical durations: idle 150–250 ms per frame, walk 100–120 ms, attack anticipation 150–200 ms, impact 50–80 ms, recovery 100 ms.

CLI export (batch, no UI):
```bash
aseprite -b hero.aseprite --tag walk --scale 6 --save-as walk_{frame}.png
aseprite -b hero.aseprite --sheet hero_sheet.png --data hero_sheet.json --format json-array --sheet-type horizontal
```
(`--scale` uses nearest-neighbour. Prefer scaling at the very end of the pipeline.)

## Sub-pixel animation

To move an edge by "half a pixel": on the in-between frame, set the edge pixel to a mid-tone between the shape colour and the background (or add a pixel in the mid-tone ahead and recolour the trailing pixel). Use it for idles, breathing, cloth, hair, glints; best on larger sprites and low-detail areas.

## Python cleanup (AI-generated or wrongly scaled "pixel art")

AI and resized images often have uneven pixel sizes and hundreds of colours. Snap them back to a grid and palette:
```python
# python -I pixel_clean.py in.png out.png --px 8 --palette pico8
from PIL import Image
import sys
src, dst, px = sys.argv[1], sys.argv[2], 8          # px = apparent size of one "pixel" in the source
PICO8 = ["000000","1D2B53","7E2553","008751","AB5236","5F574F","C2C3C7","FFF1E8",
         "FF004D","FFA300","FFEC27","00E436","29ADFF","83769C","FF77A8","FFCCAA"]
im = Image.open(src).convert("RGB")
small = im.resize((im.width // px, im.height // px), Image.NEAREST)     # one sample per cell (or BOX for averaging)
pal = Image.new("P", (1, 1)); flat = sum([[int(h[i:i+2], 16) for i in (0, 2, 4)] for h in PICO8], [])
pal.putpalette(flat + [0] * (768 - len(flat)))
q = small.quantize(palette=pal, dither=Image.Dither.NONE)
q.convert("RGB").save(dst.replace(".png", "_1x.png"))                  # native-res master
q.resize((q.width * 6, q.height * 6), Image.NEAREST).convert("RGB").save(dst)
```
Then fix lines and orphans by hand; automated cleanup never matches hand-placed pixels.
