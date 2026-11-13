"""Том 2: звук серии + общее интро/аутро. Выход: sfx.wav. Тайминги серии — от её начала (+INTRO в ролике)."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from sfxlib import *

D = 118.0; T = INTRO + D + OUTRO; m = Mix(T); E = INTRO
intro(m); outro(m, E + D)
# крючок аутро: в темноте проступает он
m.add(sting(2.0), E + D + 4.3, .45); m.add(fade(drone(1.4, 33, 600), .05, .4), E + D + 4.3, .6)

def steps(t0, n, gap=.5, g=.3):
    for k in range(n): m.add(thud(70 + k % 2 * 10, .15, 700), t0 + k * gap, g, (-.2, .2)[k % 2])

# фон записи
m.add(fade(hum(36, 60) * .5 + lp(noise(36), 3000) * .05, .3, .3), E, .3); m.add(fade(hum(40, 60) * .5, .3, .3), E + 78, .3)
m.add(beep(1000, .3), E + .05, .1)
for k in range(len('ОКРУГ МАНДЕЛА, ВИСКОНСИН')): m.add(click(), E + 1.0 + k / 28, .2)
for k in range(len('АРХИВНАЯ ЗАПИСЬ №2')): m.add(click(), E + 2.4 + k / 28, .15)
# улица, мигалки
m.add(fade(lp(noise(16), 500) * 1.2, 1, 1), E + 6, .25); m.add(fade(drone(16, 55, 300), 2, 1), E + 6, .35)
m.add(fade(lp(noise(16), 900) * .4 + bp(noise(16), 1500, 3000) * .2, 2, 1), E + 6, .08)  # рация где-то вдали
for k in range(5): m.add(fade(bp(noise(.6), 800, 2500), .02, .1), E + 9 + k * 2.6, .08, -.5)
# досье
for k, t0 in enumerate((22.8, 24.6, 27.8, 32.4, 34.4)):
    for c in range(18): m.add(click(), E + t0 + c / 28, .12)
m.add(thud(90, .3, 1200), E + 33.4, .5)
# видеокамера: тишина дома, гул ТВ-шума, шаги, дыхание
m.add(fade(static(34), .5, .5), E + 36, .05); m.add(fade(lp(noise(42), 250), .5, .1), E + 36, .25)
m.add(click(), E + 36.0, .4); m.add(click(), E + 50.2, .4)                # кнопка лампы на камере
steps(E + 53.0, 14, .5, .28)
m.add(fade(drone(10, 43, 350), 3, .2), E + 56, .45)
m.add(sting(2.5), E + 60.4, .6)
m.add(fade(drone(4, 30, 800) * 1.4, .5, .1), E + 63, .6); m.add(fade(static(3.5), 1.5, .1), E + 63, .2)
m.add(thud(60, .5, 800) * 1.4, E + 67.4, .8); m.add(clack(500), E + 67.45, .6)   # камера упала
steps(E + 67.7, 7, .26, .4)
m.add(fade(static(8), .1, .1), E + 70, .1); m.add(fade(drone(8, 36, 500), .5, .1), E + 70, .45)
m.add(whoosh(.5, 400, 2500), E + 74.0, .3); m.add(whoosh(.5, 2500, 400), E + 74.8, .3)
m.add(sting(3), E + 75.2, .7); m.add(fade(static(1.8), .05, .05), E + 76.2, .4)
m.add(beep(1000, .4), E + 77.6, .15)
# оповещение
for k in range(3): m.add(fade(sine(853, .5) + sine(960, .5), .01, .02) * .4, E + 78.0 + k * .6, .4)
m.add(fade(drone(19, 46, 250), 1, 1), E + 79, .3)
for t0 in (83.0, 85.6, 88.6, 93.4): m.add(clack(1200), E + t0, .2)
# фото из дела
m.add(fade(drone(14, 41, 300), 1, .5), E + 98, .4); m.add(clack(800), E + 98.0, .3)
m.add(fade(hum(14, 60), 1, .5), E + 98, .2); m.add(sting(3), E + 108, .5)
# финал
for k in range(len('ЕСЛИ ВЫ СМОТРИТЕ ЭТУ ЗАПИСЬ')): m.add(click(), E + 112.2 + k / 28, .15)
m.add(fade(drone(6, 33, 500), .3, .5), E + 112, .5); m.add(sting(2), E + 115.6, .6)

mix = np.stack([m.L, m.R]); mix += np.stack([reverb(m.L), reverb(m.R)]) * .3
peak = np.max(np.abs(mix)); mix = mix / peak * .85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, round(float(peak), 3), 'сек', T)
