"""Том 4: звук серии + интро + аутро (кассета выброшена, на экране улыбка). Выход: sfx.wav."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from sfxlib import *

D = 118.0; T = INTRO + D + OUTRO; m = Mix(T); E = INTRO; O = E + D
intro(m); outro(m, O)
m.add(fade(lp(noise(3), 300), .05, .5) * .6, 8.2, .25)                       # мокрые пальцы по кассете
# аутро: вместо тишины — гул экрана и низкий смех-вой, когда появляется улыбка
m.add(fade(hum(4.0, 60) + whine(4.0), .1, .3), O + 2.9, .35); m.add(sting(3.5), O + 3.0, .55)
t = tt(3.8); m.add(fade(lp(np.sin(2 * np.pi * (70 + 8 * np.sin(2 * np.pi * 3.2 * t)) * t) * (np.sin(2 * np.pi * 4 * t) > 0), 600), .3, .5), O + 3.0, .25)

def musicbox(notes, t0, step=.32, g=.12):
    for i, n in enumerate(notes):
        f = 440 * 2 ** ((n - 69) / 12); d = 1.2; x = (np.sin(2 * np.pi * f * tt(d)) + .3 * np.sin(2 * np.pi * f * 3 * tt(d))) * np.exp(-tt(d) * 4)
        m.add(x, t0 + i * step, g)
def siren(d, f0=700, f1=500, drop=0.0):
    t = tt(d); f = f0 + (f1 - f0) * (np.sin(2 * np.pi * 1.5 * t) > 0); f = f * (1 - drop * t / d)
    return fade(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .3, .02, .1)

m.add(fade(hum(48, 60) * .4 + lp(noise(48), 3000) * .04, .3, .3), E, .3); m.add(beep(1000, .3), E + .05, .1)
for k in range(len('ОКРУГ МАНДЕЛА, ВИСКОНСИН')): m.add(click(), E + 1.0 + k / 28, .2)
for k in range(len('АРХИВНАЯ ЗАПИСЬ №4')): m.add(click(), E + 2.4 + k / 28, .15)
m.add(fade(static(.4), .01, .05), E + 4.4, .4)
# подвал
m.add(fade(lp(noise(16.6), 200) * 1.4, 1, .3), E + 6, .3); m.add(fade(drone(16.6, 49, 300), 2, .3), E + 6, .3)
for k in range(8): m.add(bp(noise(.3), 2000, 4000) * env(int(.3 * SR), .01, .1, 3), E + 7 + k * 2, .04)   # капель
# день рождения: музыкальная шкатулка (своя мелодия), детский смех — шум, потом пауза
mel = [72, 72, 74, 72, 77, 76, 72, 72, 74, 72, 79, 77]
musicbox(mel, E + 22.8); musicbox(mel[:6], E + 26.8)
m.add(fade(bp(noise(11.4), 300, 3000) * .2, .5, .3), E + 22.6, .3)              # гомон за столом
m.add(clack(900), E + 34.0, .4); m.add(fade(static(10.4), .05, .05), E + 34.0, .04)
for k in range(4): m.add(beep(1600, .08), E + 34.6 + k * .5, .15)
m.add(beep(900, .2), E + 37.4, .2); m.add(fade(drone(10, 41, 400), 2, .2), E + 37.4, .45)
m.add(clack(900), E + 44.4, .4); m.add(sting(3), E + 44.6, .6)
# предупреждение: сирена замедляется и проседает
m.add(siren(3.4), E + 48.0, .45); m.add(siren(6.4, 700, 500, .7) * np.linspace(1, .6, int(6.4 * SR)), E + 51.6, .45)
m.add(fade(drone(10, 36, 500), .1, .3), E + 48, .4)
m.add(fade(static(.6), .02, .02), E + 58.0, .5); m.add(motor(.6, 160), E + 58.0, .3); m.add(click(), E + 58.6, .5)  # перемотка и снова PLAY
# подвал, телевизоры включаются сами
m.add(fade(lp(noise(25.4), 200) * 1.4, .3, .3), E + 58.6, .3); m.add(fade(drone(25.4, 46, 300), 1, .3), E + 58.6, .35)
for i in range(3): m.add(thud(90, .3, 1500), E + 66.2 + i * .6, .5); m.add(fade(whine(13 - i * .6) + static(13 - i * .6) * .3, .05, .3), E + 66.2 + i * .6, .3)
m.add(sting(3), E + 79.6, .5)
# инструкция + подмена
m.add(fade(hum(20, 60), .2, .2), E + 84, .25)
for t0 in (84.8, 89.4, 93.8): m.add(clack(1200), E + t0, .2)
m.add(fade(static(2.4), .02, .05), E + 98.2, .35); m.add(fade(drone(6, 33, 600), .05, .5), E + 98.2, .55)
# финал
m.add(fade(drone(14, 36, 400), .5, .1), E + 104, .45)
for k in range(len('ЕСЛИ ВЫ ВСЁ ЕЩЁ СМОТРИТЕ')): m.add(click(), E + 105 + k / 28, .15)
m.add(sting(3), E + 110, .6)

mix = np.stack([m.L, m.R]); mix += np.stack([reverb(m.L), reverb(m.R)]) * .3
peak = np.max(np.abs(mix)); mix = mix / peak * .85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, round(float(peak), 3), 'сек', T)
