"""Том 6: звук серии + обычное интро/аутро. Новые синтезированные хоррор-звуки: braam, impact, riser, choir, dark_amb. Выход: sfx.wav."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from sfxlib import *

D = 118.0; T = INTRO + D + OUTRO; m = Mix(T); E = INTRO
intro(m); outro(m, E + D)
def duck(a, b, k=.12):       # «провал в тишину» перед ударом
    i, j = int(a * SR), int(b * SR)
    for ch in (m.L, m.R): ch[i:j] *= k

m.add(fade(hum(D, 60) * .35 + lp(noise(D), 3000) * .04, .3, .3), E, .25); m.add(beep(1000, .3), E + .05, .1)
for k in range(len('ОКРУГ МАНДЕЛА, ВИСКОНСИН')): m.add(click(), E + 1.0 + k / 28, .2)
for k in range(len('АРХИВНАЯ ЗАПИСЬ №6')): m.add(click(), E + 2.4 + k / 28, .15)
# поле: эмбиент, ветер, тонкий звон света
m.add(dark_amb(18, 38), E + 6, .55); m.add(fade(lp(noise(18), 600) * 1.1, 2, 1), E + 6, .25)
m.add(fade(sine(1760, 18) * .04 + sine(1763, 18) * .04, 3, 2), E + 6, .4)
# пастор: церковь, свечи, свет за окнами нарастает
m.add(fade(lp(noise(16.6), 150) * 1.2, .3, .3), E + 24, .3); m.add(fade(choir(16.6, (50, 57, 62), .4), 4, .3), E + 24, .35)
m.add(riser(9.9, 50, 700), E + 30, .5); m.add(impact(2.5), E + 39.9, .9); m.add(fade(static(.7), .01, .1), E + 39.95, .6)
# нагнетание: идём к свету
m.add(dark_amb(16, 33), E + 40.6, .6); m.add(fade(sine(55, 16) * .3, 3, .2), E + 40.6, .5)
for k in range(6): m.add(thud(48, .4, 300), E + 44 + k * 1.9 - k * k * .06, .25 + k * .05)   # «сердце», ускоряется
m.add(riser(8.0, 40, 1200), E + 47.6, .55); m.add(reverse_swell(impact(1.5)), E + 54.0, .6)
duck(E + 55.5, E + 56.0, .05)
m.add(impact(3.0), E + 56.0, 1.0); m.add(braam(4.5, 36.7), E + 56.0, .8); m.add(fade(choir(8, (62, 65, 69, 74), 1.0), .1, 1.5), E + 56.0, .7)
m.add(riser(4.2, 80, 2000), E + 59.6, .45); m.add(fade(static(4.4), 1.5, .02), E + 59.6, .35)
duck(E + 64.0, E + 64.6, .02)
# оповещение
m.add(fade(drone(20, 46, 250), .5, 1), E + 64, .3)
for t0 in (64.8, 69.8, 71.6, 74.0): m.add(clack(1200), E + t0, .2)
m.add(braam(3.0, 41.2), E + 78.8, .55)
# церковь утром, прихожане оборачиваются
m.add(dark_amb(20, 40), E + 84, .45); m.add(fade(lp(noise(20), 150) * 1.2, .3, .3), E + 84, .25)
m.add(riser(5.2, 45, 900), E + 96.4, .5); m.add(braam(4.0, 34.6), E + 101.6, .75); m.add(fade(static(2.4), .5, .05), E + 101.6, .4)
duck(E + 103.8, E + 104.1, .05)
# финал: свет, глаза открываются
m.add(dark_amb(14, 33), E + 104, .55); m.add(riser(5.0, 50, 1500), E + 106.4, .4)
m.add(impact(3.0), E + 111.4, 1.0); m.add(fade(choir(6.6, (61, 64, 68, 73), 1.0), .05, .5), E + 111.4, .6); m.add(fade(static(6.6), 2, .05), E + 111.4, .3)

mix = np.stack([m.L, m.R]); mix += np.stack([reverb(m.L), reverb(m.R)]) * .35
peak = np.max(np.abs(mix)); mix = mix / peak * .85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, round(float(peak), 3), 'сек', T)
