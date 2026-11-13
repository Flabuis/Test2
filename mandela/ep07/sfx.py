"""Том 7 (финал): звук особого интро, истории 7:00 и особого аутро. Выход: sfx.wav."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from sfxlib import *

I7, D, O7 = 18.0, 420.0, 10.0; T = I7 + D + O7; m = Mix(T); E = I7; O = E + D
def duck(a, b, k=.0):
    i, j = int(a * SR), int(b * SR)
    for ch in (m.L, m.R): ch[i:j] *= k
def siren(d, f0=700, f1=500):
    t = tt(d); f = f0 + (f1 - f0) * (np.sin(2 * np.pi * 1.5 * t) > 0); return fade(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .3, .02, .1)
def creak(d=1.2, f0=180):
    t = tt(d); f = f0 * (1 + .3 * np.sin(2 * np.pi * .8 * t)); return bp(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (np.sin(2 * np.pi * 30 * t) > 0), 300, 2500) * np.sin(np.pi * t / d) * .5

# ---------- особое интро ----------
m.add(fade(lp(noise(18), 150) * .3, 1, .5), 0, .5)
m.add(fade(static(4.0), 1.2, .3), 4.0, .22); m.add(fade(static(8.2), .3, .05), 8.0, .1)          # шум тише в паузе
m.add(fade(hum(14), 1.5, .2), 4.0, .25); m.add(click(), 4.8, .6); m.add(thud(60, .4, 600), 4.8, .5)
m.add(dark_amb(14, 31), 4.0, .5)
m.add(fade(bp(noise(3.0), 200, 1200) * .5, 1, .3), 12.0, .25); m.add(creak(2.6, 120), 12.2, .25)     # чужая рука ползёт из темноты
m.add(clack(800), 15.0, .5); m.add(motor(.8, 70), 15.1, .35); m.add(thud(110, .25, 1500), 15.6, .5)
m.add(impact(2.0) * .8, 15.4, .6); m.add(click(), 16.2, .5); m.add(whoosh(1.6, 200, 3000), 16.4, .25)

# ---------- акт 1: студия ----------
m.add(beep(1000, .4), E + .1, .12)
for k, s in enumerate(('ОКРУГ МАНДЕЛА.', 'ПОСЛЕДНИЙ ВЫПУСК.', 'ФЕВРАЛЬ 1992')):
    for c in range(len(s)): m.add(click(), E + (.6, 1.8, 3.0)[k] + c / 28, .15)
m.add(fade(hum(68, 60) * .4 + lp(noise(68), 2500) * .04, .5, .5), E + 7, .3); m.add(dark_amb(68, 41), E + 7, .35)
for t0 in (29.0, 35.0, 40.4, 46.0): m.add(motor(.3, 160), E + t0 - .3, .25); m.add(sting(2.6), E + t0, .35)
duck(E + 25.6, E + 28.0, .08)                                                                         # «Вернулись все» — тишина
# ---------- акт 2: архив ----------
m.add(fade(lp(noise(71), 200) * 1.2, .5, .5), E + 75, .3); m.add(fade(drone(71, 46, 300), 2, .5), E + 75, .3)
for k in range(30): m.add(motor(1.4, 55 + k % 4 * 7) * .5, E + 110 + k * 1.2, .12, (-.3, .3)[k % 2])  # копировальные магнитофоны
m.add(braam(4.2, 41.2), E + 123.2, .7); m.add(fade(static(4.2), .05, .2), E + 123.2, .25)
m.add(siren(13.4) * np.linspace(.6, 1, int(13.4 * SR)), E + 130, .18)
m.add(sting(3), E + 139, .5)
for c in range(30): m.add(click(), E + 146.2 + c / 28, .15)
m.add(beep(1000, .5), E + 151.4, .12)
# ---------- акт 3: запись пастора ----------
m.add(fade(lp(noise(104.8), 2500) * .06 + lp(noise(104.8), 150) * 1.0, .5, .2), E + 152, .3)
m.add(fade(choir(104.8, (50, 57, 62), .4) * np.linspace(.2, 1.2, int(104.8 * SR)), 4, .2), E + 152, .3)
m.add(dark_amb(104.8, 36), E + 152, .45)
for k in range(1, 14):
    t0 = 152 + k * 8
    if t0 < 256: m.add(click(), E + t0, .5); m.add(fade(static(.14), .002, .01), E + t0, .4)
m.add(impact(2.5), E + 237.6, .8); m.add(braam(4.0, 36.7), E + 237.6, .6)
m.add(riser(6.8, 50, 1800), E + 250.0, .5)
m.add(fade(sine(3000, 2.2) * .3 + hp(noise(2.2), 4000) * .3, .05, .05), E + 256.8, .5)               # засветка
m.add(impact(3.0), E + 259.0, 1.0); m.add(fade(choir(3, (62, 65, 69, 74), 1), .05, 1), E + 259.0, .7)
m.add(fade(static(5.1), .1, .1), E + 259.5, .35); m.add(fade(static(5.4), .1, 1.4), E + 264.6, .25)
# ---------- акт 4: диктор от себя ----------
m.add(fade(hum(90, 60) * .4, .5, .5), E + 270, .3); m.add(dark_amb(90, 38), E + 270, .4)
m.add(creak(2.2, 90), E + 271.2, .35)
m.add(fade(drone(67, 33, 400) * np.linspace(0, 1.2, int(67 * SR)), 5, .3), E + 278, .45)                # фигура за спиной
duck(E + 310.6, E + 314.0, .15)
m.add(fade(static(9.4), .3, .05), E + 336, .1); m.add(riser(4.4, 60, 1600), E + 341, .5)
m.add(fade(static(.4), .01, .01), E + 345.4, .7); m.add(impact(2.5), E + 345.4, .9); m.add(braam(4.2, 34.6), E + 345.8, .6)
m.add(fade(static(2.4), .5, .05), E + 357.6, .4)
# ---------- акт 5: из телевизора ----------
m.add(fade(lp(hum(53, 60) + whine(53), 900), .5, .5), E + 360, .35); m.add(dark_amb(60, 33), E + 360, .4)
m.add(creak(3.4, 100), E + 395, .3); m.add(clack(700), E + 398.6, .35)
m.add(creak(3.0, 70), E + 404.2, .25)
duck(E + 407.0, E + 410.0, 0.0)                                                                       # «Открой дверь» — полная тишина
duck(E + 410.0, E + 420.0, .18)                                                                       # дальше — почти тихо, под шёпот
m.add(fade(drone(10, 31, 300), 2, 3), E + 410, .08)
# ---------- особое аутро ----------
m.add(fade(static(5), .05, 2.0) * np.concatenate([np.linspace(.2, 1, int(3 * SR)), np.linspace(1, 0, int(2 * SR))]), O, .45)
m.add(click(), O + 6.0, .3); m.add(fade(lp(noise(2.2), 150), .4, .6), O + 6.0, .3)

mix = np.stack([m.L, m.R]); mix += np.stack([reverb(m.L), reverb(m.R)]) * .3
peak = np.max(np.abs(mix)); mix = mix / peak * .85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, round(float(peak), 3), 'сек', T)
