"""Том 5: звук серии + глючное интро + аутро («всё это зря»). Выход: sfx.wav."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from sfxlib import *

D = 118.0; T = INTRO + D + OUTRO; m = Mix(T); E = INTRO; O = E + D
intro(m); outro(m, O)
# глюки интро: щелчки, рваный шум, провалы
r = np.random.default_rng(5)
for t0 in r.uniform(4.8, 13.6, 18): m.add(fade(static(r.uniform(.05, .2)), .002, .01), t0, .35)
for t0 in r.uniform(5, 13, 6): m.add(click(), t0, .6)
m.add(beep(700, .9), 11.15, .2); m.add(beep(700, .9), 12.2, .2)            # предупреждение вместо PLAY
# аутро: после шума — «всё это зря», под ним низкий гул
m.add(fade(drone(3.5, 30, 700), .05, .5), O + 2.85, .55); m.add(fade(static(.3), .01, .05), O + 2.85, .4)

m.add(fade(hum(D, 60) * .4 + lp(noise(D), 3000) * .05, .3, .3), E, .3)
m.add(beep(700, 1.0), E + .05, .25)
for k in range(len('ОКРУГ МАНДЕЛА, ВИСКОНСИН')): m.add(click(), E + 1.6 + k / 28, .2)
# сбои по всей кассете
for t0 in (9.8, 18.9, 27.6, 36.6, 44.1, 58.2, 66.8, 79.9, 84.7, 91.3): m.add(fade(static(.2), .002, .02), E + t0, .45); m.add(click(), E + t0, .5)
# оповещение
for k in range(3): m.add(fade(sine(853, .5) + sine(960, .5), .01, .02) * .4, E + 6.2 + k * .6, .35)
m.add(fade(drone(24, 46, 250), 1, 1), E + 6, .3)
for t0 in (11.4, 16.0, 17.8): m.add(clack(1200), E + t0, .2)
m.add(sting(2.5), E + 19.0, .45); m.add(sting(2.5), E + 25.0, .5)
# улица: окна, все поворачивают головы
m.add(fade(lp(noise(25), 500) * 1.2, 1, .5), E + 30, .25); m.add(fade(drone(25, 52, 300), 2, .3), E + 30, .35)
m.add(fade(drone(6.4, 40, 600), .3, .3), E + 40, .45); m.add(sting(3), E + 51, .6)
# телевизор
m.add(fade(hum(20, 60) + whine(20), .3, .3), E + 55, .25)
m.add(fade(drone(5.4, 36, 600) * np.linspace(.5, 1.6, int(5.4 * SR)), .3, .05), E + 64.6, .5); m.add(fade(static(2), .02, .05), E + 70, .6); m.add(sting(2), E + 70, .7)
# зеркало
m.add(fade(lp(noise(20), 150) * 1.4, .5, .5), E + 75, .3); m.add(fade(drone(20, 44, 300), 1, .5), E + 75, .35)
for i in range(3): m.add(clack(1000), E + 80.4 + i * .6, .2)
m.add(sting(3), E + 88.4, .6)
# «умрите»
m.add(fade(drone(7, 28, 900) * 1.6, .05, .2), E + 95, .6); m.add(fade(static(7), .05, .2), E + 95, .3)
for k in range(12): m.add(thud(45, .25, 400), E + 95.2 + k * .5, .35)
# извинения — внезапно тихо и нормально
m.add(beep(1000, .3), E + 102.0, .15); m.add(fade(hum(8.6, 60), .05, .2), E + 102, .2)
# конец записи
m.add(beep(1000, 7.0), E + 110.6, .12); m.add(fade(static(.12), .002, .01), E + 115.2, .7)

mix = np.stack([m.L, m.R]); mix += np.stack([reverb(m.L), reverb(m.R)]) * .3
peak = np.max(np.abs(mix)); mix = mix / peak * .85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, round(float(peak), 3), 'сек', T)
