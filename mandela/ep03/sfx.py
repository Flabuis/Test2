"""Том 3: звук серии + интро (вариант «без руки») + аутро. Выход: sfx.wav."""
import os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
from sfxlib import *

D = 118.0; T = INTRO + D + OUTRO; m = Mix(T); E = INTRO; CUT = 8.05
intro(m); outro(m, E + D)
# вариант интро: на склейке рука пропадает — глушим звуки руки после склейки, даём срыв и низкий удар
cut = int(CUT * SR)
for ch in (m.L, m.R): ch[cut:int(10.35 * SR)] *= .25
m.add(fade(static(.15), .002, .02), CUT, .6); m.add(sting(3.0), CUT + .05, .55); m.add(fade(drone(5.9, 31, 700), .05, .4), CUT, .5)
m.add(motor(2.4, 55), CUT + .1, .2)                                           # кассета ползёт сама

def ring(d=1.4):   # звонок дискового телефона
    t = tt(d); s = (np.sin(2 * np.pi * 1000 * t) + np.sin(2 * np.pi * 1250 * t)) * (np.sin(2 * np.pi * 20 * t) > 0)
    return fade(s * .35, .01, .05)
def breath(d):
    t = tt(d); return bp(noise(d), 300, 2000) * (np.sin(2 * np.pi * .45 * t) ** 2) * 1.3
def am_beep(): return beep(1400, .35)
def reels(d): return fade(motor(d, 45) * .6 + lp(noise(d), 1500) * .1, .05, .1)
def tel(x): return bp(x, 320, 3300)

m.add(fade(hum(D, 60) * .4 + lp(noise(D), 3000) * .04, .3, .3), E, .3); m.add(beep(1000, .3), E + .05, .1)
for k in range(len('ОКРУГ МАНДЕЛА, ВИСКОНСИН')): m.add(click(), E + 1.0 + k / 28, .2)
for k in range(len('АРХИВНАЯ ЗАПИСЬ №3')): m.add(click(), E + 2.4 + k / 28, .15)
# кухня: холодильник, часы
m.add(fade(lp(noise(46), 120) * 1.5 + sine(50, 46) * .1, 1, .5), E + 6, .3)
for k in range(46): m.add(click() * .5, E + 6 + k, .15)                        # часы на стене
# сообщения
for t0, d in ((20.0, 5.6), (30.8, 5.6), (36.6, 5.6), (42.4, 9.4)):
    m.add(clack(900), E + t0, .4); m.add(am_beep(), E + t0 + .2, .25); m.add(reels(d), E + t0, .3); m.add(fade(tel(noise(d)) * .06, .05, .1), E + t0 + .4, 1)
m.add(fade(drone(6, 46, 300), 1, .5), E + 25.6, .35)
m.add(fade(tel(breath(4.4)), .3, .3), E + 43.0, .7)
m.add(fade(drone(9, 38, 500), 2, .1), E + 42.4, .5)
# камера наблюдения: только гул, ветер и склейки
m.add(fade(hum(26, 50) * .6 + lp(noise(26), 600) * .5, .2, .2), E + 52, .25)
for t0 in (56, 60, 64, 68, 72): m.add(click(), E + t0, .7); m.add(fade(static(.12), .002, .02), E + t0, .3)
m.add(fade(drone(8, 33, 600), 4, .1), E + 64, .5)
m.add(sting(3.0), E + 72.0, .7); m.add(fade(static(3), 1.5, .05), E + 75, .3)
# инструкция + подмешанные кадры
m.add(fade(hum(18, 60), .2, .2), E + 78, .25); m.add(fade(drone(18, 46, 250), 1, 1), E + 78, .3)
for t0 in (78.8, 83.4, 88.0): m.add(clack(1200), E + t0, .2)
for t0 in (85.9, 90.3): m.add(fade(static(.14), .002, .02), E + t0, .6)
m.add(thud(50, .6, 500), E + 92.8, .6)
# телефон звонит «вам»
m.add(fade(lp(noise(16), 120) * 1.5, .2, .2), E + 96, .3)
for t0 in (96.6, 99.1, 101.6): m.add(ring(), E + t0, .55)
m.add(clack(800), E + 104.0, .5); m.add(am_beep(), E + 104.4, .25); m.add(reels(7.4), E + 104.4, .3)
m.add(fade(tel(breath(3)), .5, .5), E + 108.8, .5)
# финал: двор, датчик двери
m.add(fade(hum(6, 50) * .6 + lp(noise(6), 600) * .5, .1, .5), E + 112, .25)
for k in range(12): m.add(beep(2000, .12), E + 112.5 + k * .5, .06)

mix = np.stack([m.L, m.R]); mix += np.stack([reverb(m.L), reverb(m.R)]) * .3
peak = np.max(np.abs(mix)); mix = mix / peak * .85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, round(float(peak), 3), 'сек', T)
