"""Том 1: звук серии + общее интро/аутро. Выход: sfx.wav. Тайминги серии — от её начала (+INTRO в ролике)."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from sfxlib import *

D = 96.0; T = INTRO + D + OUTRO; m = Mix(T); E = INTRO
intro(m); outro(m, E + D)

# под всей серией — гул плёнки и тихий шум
m.add(fade(hum(D, 60) * .5 + lp(noise(D), 3000) * .05, .3, .3), E, .3)
m.add(beep(1000, .3), E + .05, .1)
# А. титр
for k in range(len('ОКРУГ МАНДЕЛА, ВИСКОНСИН')): m.add(click(), E + 1.0 + k / 28, .2)
for k in range(len('АРХИВНАЯ ЗАПИСЬ №1')): m.add(click(), E + 2.4 + k / 28, .15)
# Б. улица
m.add(fade(lp(noise(14), 500) * 1.2, 1, 1), E + 6, .25)                         # ветер
m.add(fade(drone(14, 55, 300), 2, 1), E + 6, .35)
for k in range(6): m.add(bp(noise(.08), 3500, 5000) * np.sin(np.pi * np.arange(int(.08 * SR)) / int(.08 * SR)), E + 7 + k * 1.9, .05)   # сверчки
m.add(sting(3), E + 17.6, .5)
# В. настроечная таблица и оповещение
m.add(beep(1000, 1.3), E + 20.0, .35)
for k in range(3): m.add(fade(sine(853, .5) + sine(960, .5), .01, .02) * .4, E + 21.4 + k * .6, .4)   # тревожный двухтональный сигнал
m.add(fade(drone(12, 46, 250), 1, 1), E + 22, .3)
# Г. двор
m.add(fade(lp(noise(12.4), 400), 1, .5), E + 34, .2); m.add(fade(drone(12.4, 52, 300), 1.5, .2), E + 34, .35)
for k in range(4): m.add(click(), E + 39.8 + k * 1.5, .25)
m.add(sting(3), E + 46.4, .6); m.add(fade(drone(6, 41, 500), .2, .5), E + 46.4, .5)
m.add(whoosh(1.5, 3000, 200), E + 50.4, .3)
# Д. инструкция
m.add(beep(1000, .25), E + 52.4, .2)
for t0 in (53.6, 56.4, 58.2, 61.0, 65.2): m.add(clack(1200), E + t0, .2)
m.add(fade(static(2.8), .05, .05), E + 69.2, .25); m.add(sting(1.5), E + 70.6, .5)
# Е. гостиная
m.add(fade(hum(16, 60), .5, .5), E + 72, .3); m.add(fade(static(16), .5, .5), E + 72, .06)
m.add(fade(drone(16, 49, 350), 2, .5), E + 72, .4); m.add(sting(3), E + 84, .5)
# Ж. лицо
m.add(fade(drone(6, 36, 600), .1, .3) * 1.5, E + 88, .55); m.add(fade(static(6), .1, .3), E + 88, .12)
m.add(fade(static(2), .05, .2), E + 94, .3); m.add(beep(1000, 1.6), E + 94.3, .12)

mix = np.stack([m.L, m.R]); mix += np.stack([reverb(m.L), reverb(m.R)]) * .3
peak = np.max(np.abs(mix)); mix = mix / peak * .85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, round(float(peak), 3), 'сек', T)
