"""Звук для PS1-версии серии 5 «Ловушка»: синтез SFX, эмбиента и фоновой музыки (без внешних сэмплов).
Тайминги совпадают с index.html. Выход: sfx5.wav (44.1 кГц, стерео).
Запуск: python3 sfx5.py
"""
import numpy as np
from scipy.signal import butter, lfilter
import wave, os

SR = 44100
T = 60.0
N = int(SR * T)
rng = np.random.default_rng(7)
L = np.zeros(N); R = np.zeros(N)


def lp(x, f, o=2):
    b, a = butter(o, min(f, SR / 2 - 100) / (SR / 2)); return lfilter(b, a, x)


def hp(x, f, o=2):
    b, a = butter(o, f / (SR / 2), 'high'); return lfilter(b, a, x)


def bp(x, lo, hi, o=2):
    b, a = butter(o, [lo / (SR / 2), hi / (SR / 2)], 'band'); return lfilter(b, a, x)


def env(n, a=0.005, d=0.2, curve=4):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-curve * np.maximum(0, t - a) / max(d, 1e-4))
    return e


def add(sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N or i + len(sig) <= 0: return
    s = sig[:max(0, N - i)]
    gl, gr = gain * np.sqrt((1 - pan) / 2), gain * np.sqrt((1 + pan) / 2)
    L[i:i + len(s)] += s * gl; R[i:i + len(s)] += s * gr


def tone(f, dur, kind='sq', vib=0.0):
    t = np.arange(int(dur * SR)) / SR
    ph = 2 * np.pi * f * t + (vib * np.sin(2 * np.pi * 6 * t) if vib else 0)
    if kind == 'sq': return np.sign(np.sin(ph)) * 0.5
    if kind == 'tri': return 2 / np.pi * np.arcsin(np.sin(ph))
    return np.sin(ph)


def noise(dur): return rng.uniform(-1, 1, int(dur * SR))


def crush(x, bits=8, down=2):  # «приставочная» зернистость
    y = np.repeat(x[::down], down)[:len(x)]
    q = 2 ** (bits - 1); return np.round(y * q) / q


# ---------- элементы ----------
def blip(f=1300, d=0.022): return tone(f, d, 'sq') * env(int(d * SR), 0.001, d * 0.6, 3)
def wood_thud(f=140, d=0.25, bright=1800):
    n = int(d * SR); x = lp(noise(d), bright) * env(n, 0.001, d * .25, 5) * 0.8
    x += np.sin(2 * np.pi * f * np.arange(n) / SR * (1 - 0.3 * np.arange(n) / n)) * env(n, 0.001, d * .35, 5)
    return x
def chop():
    n = int(.35 * SR); x = bp(noise(.35), 600, 4000) * env(n, .001, .05, 6) * 1.2 + wood_thud(110, .35, 1200) * .8
    return x
def clank(f=900):
    d = .6; n = int(d * SR); t = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * f * k * t) * a for k, a in [(1, 1), (2.76, .6), (5.4, .35), (8.9, .2)]) * env(n, .001, .25, 5)
    return x * .5 + bp(noise(d), 2000, 8000) * env(n, .001, .02, 6) * .6
def whoosh(d=.55, f0=400, f1=3000, rise=True):
    n = int(d * SR); x = noise(d); out = np.zeros(n); seg = 512
    for s in range(0, n, seg):
        k = s / n; f = f0 + (f1 - f0) * (k if rise else 1 - k)
        out[s:s + seg] = bp(x[s:s + seg + 0], max(80, f * .7), min(18000, f * 1.3), 1)[:len(out[s:s + seg])]
    w = np.sin(np.pi * np.arange(n) / n) ** 2
    return out * w * 1.5
def crack():
    d = .5; n = int(d * SR); x = hp(noise(d), 1500) * env(n, .0005, .03, 6)
    for k in range(6):
        i = int(rng.uniform(0, .25) * SR); s = hp(noise(.02), 2500) * env(int(.02 * SR), .0005, .005, 5); x[i:i + len(s)] += s * rng.uniform(.4, 1)
    return x + wood_thud(90, .5, 900) * .6
def buzzer(d=.45):
    return lp(tone(110, d, 'sq') + tone(116, d, 'sq'), 3000) * env(int(d * SR), .005, d * .7, 2) * .7
def jingle(notes, step=.09, kind='sq', d=.18):
    out = np.zeros(int((len(notes) * step + d + .3) * SR))
    for i, n in enumerate(notes):
        s = tone(440 * 2 ** ((n - 69) / 12), d, kind) * env(int(d * SR), .002, d * .5, 3); j = int(i * step * SR); out[j:j + len(s)] += s
    return out
def saw_stroke(d=.22, f=900):
    n = int(d * SR); x = noise(d); t = np.arange(n) / SR
    teeth = (np.sin(2 * np.pi * 70 * t) > .3).astype(float)  # «зубья»
    return bp(x, f * .6, f * 2.5) * teeth * np.sin(np.pi * t / d) * 1.2
def twang():
    d = 1.1; n = int(d * SR); t = np.arange(n) / SR
    f = 520 * (1 + .25 * np.exp(-t * 5) * np.sin(2 * np.pi * 9 * t))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .001, .5, 3) * .6
def boing():
    d = .35; n = int(d * SR); t = np.arange(n) / SR; f = 220 + 500 * t / d
    return np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .3 * env(n, .002, .15, 3)
def crickets(d):
    n = int(d * SR); t = np.arange(n) / SR; out = np.zeros(n)
    for f0, rate, ph in [(4300, 2.3, 0), (4700, 1.7, .5), (3900, 2.9, 1.1)]:
        chirp = (np.sin(2 * np.pi * rate * t + ph) > .6).astype(float) * (np.sin(2 * np.pi * 30 * t) > 0)
        out += np.sin(2 * np.pi * f0 * t) * lp(chirp, 200) * .25
    return out
def fire(d):
    n = int(d * SR); x = lp(noise(d), 900) * .35
    for _ in range(int(d * 14)):
        i = rng.integers(0, n - 2000); s = hp(noise(.008), 2000) * env(int(.008 * SR), .0003, .002, 4) * rng.uniform(.3, 1); x[i:i + len(s)] += s
    return x
def wind(d, cut=500):
    n = int(d * SR); x = lp(noise(d), cut, 2); m = 0.6 + 0.4 * np.sin(2 * np.pi * np.arange(n) / SR * .13)
    return x * m * 2.0



def pad(notes, d, cut=1400):
    n = int(d * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for m in notes:
        f = 440 * 2 ** ((m - 69) / 12)
        for det in (-0.004, 0.004):
            x += 2 / np.pi * np.arcsin(np.sin(2 * np.pi * f * (1 + det) * t))
    a = np.minimum(1, t / 1.2) * np.minimum(1, (d - t) / 1.2)
    return lp(x, cut) * a / len(notes)
def bell(m, d=1.6):
    f = 440 * 2 ** ((m - 69) / 12); n = int(d * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) + .3 * np.sin(2 * np.pi * f * 3.01 * t)) * np.exp(-t * 3)
def roar(d, cut=700):
    n = int(d * SR); x = lp(noise(d), cut, 2); m = .7 + .3 * lp(noise(d), 4)
    return x * m * 2.5
def brick(f=None):
    d = .12; n = int(d * SR); x = bp(noise(d), 1500, 5000) * env(n, .0005, .02, 6)
    return x + np.sin(2 * np.pi * (f or rng.uniform(600, 900)) * np.arange(n) / SR) * env(n, .001, .03, 6) * .5
def chatter(d):
    out = np.zeros(int(d * SR)); t0 = 0
    while t0 < d - .05:
        s = hp(noise(.012), 2500) * env(int(.012 * SR), .0003, .003, 4); i = int(t0 * SR); out[i:i + len(s)] += s; t0 += rng.uniform(.045, .07)
    return out
def wind_howl(d):
    n = int(d * SR); t = np.arange(n) / SR; x = noise(d); out = np.zeros(n); seg = 2048
    for s in range(0, n, seg):
        f = 500 + 250 * np.sin(2 * np.pi * .23 * s / SR) + 120 * np.sin(2 * np.pi * .61 * s / SR)
        out[s:s + seg] = bp(x[s:s + seg], f * .85, f * 1.15, 1)
    return out * (.6 + .4 * np.sin(2 * np.pi * .17 * t)) * 3
def footstep(): return wood_thud(rng.uniform(70, 100), .12, 900)
def sting():  # «дун-дун-дуун»
    out = np.zeros(int(2.6 * SR))
    for k, (st, m, d) in enumerate([(0, 43, .35), (.45, 42, .35), (.9, 38, 1.6)]):
        f = 440 * 2 ** ((m - 69) / 12); n = int(d * SR); tt = np.arange(n) / SR
        s = sum(np.sign(np.sin(2 * np.pi * f * h * tt)) / h for h in (1, 2, 3)) * env(n, .01, d * .8, 2)
        s = lp(s, 1800); i = int(st * SR); out[i:i + n] += s
    return out * .5
def tape_rewind(d):
    n = int(d * SR); t = np.arange(n) / SR; f = 700 + 2200 * (t / d) + 300 * np.sin(2 * np.pi * 7 * t)
    s = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .25 + bp(noise(d), 2000, 9000) * .5
    return lp(s, 7000) * np.minimum(1, t / .1) * np.minimum(1, (d - t) / .1)
def pour(d):
    n = int(d * SR); x = lp(noise(d), 350); g = (np.sin(2 * np.pi * 5 * np.arange(n) / SR) > .2) * 1.0
    return x * (.5 + .5 * lp(g, 20)) * 3 * np.minimum(1, np.arange(n) / SR / .2)


def glass_ping(f=2400, d=.5):
    n = int(d * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 2.7 * t) + .25 * np.sin(2 * np.pi * f * 4.1 * t)) * np.exp(-t * 9) * .5
def shatter():
    d = 1.4; n = int(d * SR); x = hp(noise(d), 3000) * env(n, .0005, .08, 5) * 1.2
    for k in range(22):
        tt = rng.uniform(0, .9) ** 1.6; s = glass_ping(rng.uniform(1800, 5200), .35) * rng.uniform(.3, 1); i = int(tt * SR); x[i:i + len(s)] += s[:n - i]
    return x
def breath(d=.3):
    n = int(d * SR); return bp(noise(d), 500, 2500) * np.sin(np.pi * np.arange(n) / n) ** 2 * 1.5
def bellows(d=.45):
    n = int(d * SR); t = np.arange(n) / SR
    return (lp(noise(d), 700) * 2.5 + bp(noise(d), 200, 500) * 1.5) * np.sin(np.pi * t / d) ** 1.5
def trombone():
    out = np.zeros(int(2.4 * SR))
    for k, (st, m, d) in enumerate([(0, 58, .4), (.45, 57, .4), (.9, 56, .4), (1.35, 55, 1.0)]):
        f = 440 * 2 ** ((m - 69) / 12); n = int(d * SR); tt = np.arange(n) / SR
        ff = f * (1 - (.06 * tt / d if k == 3 else 0)) * (1 + .012 * np.sin(2 * np.pi * 6 * tt))
        s = lp(np.sign(np.sin(2 * np.pi * np.cumsum(ff) / SR)) * .5 + np.sin(2 * np.pi * np.cumsum(ff) / SR), 1400) * env(n, .03, d * .9, 1.5)
        i = int(st * SR); out[i:i + n] += s
    return out * .5
def sand_pour(d):
    n = int(d * SR); return hp(noise(d), 3500) * np.sin(np.pi * np.arange(n) / n) ** .7 * .8
def squeak(d=.25, f0=900, f1=1500):
    n = int(d * SR); t = np.arange(n) / SR; f = f0 + (f1 - f0) * t / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / d) * .3

def mouse_squeak(f=3200, d=.12, down=False):
    n = int(d * SR); t = np.arange(n) / SR; ff = f * (1 + (-.3 if down else .25) * t / d)
    return np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.sin(np.pi * t / d) * .5
def rustle(d):
    n = int(d * SR); x = bp(noise(d), 1500, 7000); m = lp(np.abs(noise(d)), 15) * 3
    return x * m * np.minimum(1, np.arange(n) / SR / .05) * np.minimum(1, (d - np.arange(n) / SR) / .1)
def hammer_hit(): return wood_thud(220, .18, 2500) * .9 + clank(1400)[:int(.18 * SR)] * .25
def shiver_teeth(d):
    out = np.zeros(int(d * SR)); t0 = 0
    while t0 < d - .03:
        s = hp(noise(.008), 3000) * env(int(.008 * SR), .0002, .002, 4); i = int(t0 * SR); out[i:i + len(s)] += s; t0 += rng.uniform(.035, .055)
    return out
def snore(d=1.6):
    n = int(d * SR); t = np.arange(n) / SR
    return lp(noise(d), 250) * (np.sin(np.pi * t / d) ** 2) * (1 + .6 * np.sin(2 * np.pi * 28 * t)) * 1.5
def stitch(): return hp(noise(.05), 3000) * env(int(.05 * SR), .002, .02, 4) * .6

def gurgle(d=1.6, f0=70):
    n = int(d * SR); t = np.arange(n) / SR
    f = f0 * (1 + .5 * np.sin(2 * np.pi * 3.1 * t) + .3 * np.sin(2 * np.pi * 7.3 * t))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) + .4 * lp(noise(d), 300) * 3
    bub = np.zeros(n)
    for k in range(int(d * 9)):
        i = rng.integers(0, max(1, n - 3000)); m = int(.05 * SR); tt = np.arange(m) / SR
        bub[i:i + m] += np.sin(2 * np.pi * (150 + 300 * tt / .05) * tt) * env(m, .002, .02, 4)
    return lp(x * .6 + bub * .5, 900) * np.sin(np.pi * t / d) ** .6
def crunch(): return lp(noise(.18), 2500) * env(int(.18 * SR), .005, .08, 4) + wood_thud(70, .18, 600) * .3
def boil(d):
    out = np.zeros(int(d * SR))
    for k in range(int(d * 18)):
        i = rng.integers(0, len(out) - 2000); m = int(.03 * SR); tt = np.arange(m) / SR
        out[i:i + m] += np.sin(2 * np.pi * rng.uniform(300, 900) * tt * (1 + tt * 20)) * env(m, .001, .01, 4)
    return out + lp(noise(d), 600) * .3
def door_creak(d=.6):
    n = int(d * SR); t = np.arange(n) / SR; f = 300 + 200 * np.sin(2 * np.pi * 1.5 * t)
    return bp(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (np.sin(2 * np.pi * 40 * t) > 0), 400, 2500) * np.sin(np.pi * t / d) * .5
def birds(d):
    out = np.zeros(int(d * SR)); t0 = .3
    while t0 < d - .4:
        m = int(.09 * SR); tt = np.arange(m) / SR; s = np.sin(2 * np.pi * (3200 + 1200 * np.sin(2 * np.pi * 18 * tt)) * tt) * np.sin(np.pi * tt / .09)
        i = int(t0 * SR); out[i:i + m] += s; t0 += rng.uniform(.15, .9)
    return out * .3
def spoon(): return glass_ping(1800, .12) * .5 + wood_thud(300, .12, 3000) * .2

# ---------- музыка ----------
for i, t0 in enumerate(np.arange(0, 8.8, 2.9)): add(pad([[60, 64, 67], [65, 69, 72], [62, 65, 69]][i % 3], 3.4, 1400), t0, .13)
for i, t0 in enumerate(np.arange(8.8, 22.6, 3.4)): add(pad([[57, 64, 69], [55, 62, 67], [53, 60, 65], [55, 62, 67]][i % 4], min(3.9, 22.7 - t0), 1100), t0, .13)
for i, t0 in enumerate(np.arange(22.6, 36, 3.3)):
    add(pad([[45, 52, 57, 60], [41, 48, 53, 57], [43, 50, 55, 59], [40, 47, 52, 56]][i % 4], min(3.8, 36.1 - t0), 1100), t0, .15)
    add(bell([81, 84, 88, 83][i % 4]), t0 + 1.0, .05, .4)
add(pad([45, 48, 52], 2.0, 700), 36.0, .14)
for i, t0 in enumerate(np.arange(37.8, 48.8, 3.0)): add(pad([[60, 64, 67], [62, 65, 69], [57, 60, 64], [65, 69, 72]][i % 4], 3.4, 1300), t0, .12)
for i, t0 in enumerate(np.arange(48.8, 60, 3.2)): add(pad([[60, 64, 67, 72], [65, 69, 72], [57, 60, 64], [53, 57, 60]][i % 4], min(3.8, 60.2 - t0), 1300 - i * 150), t0, .15 - i * .02)

# ---------- 1. утро ----------
add(fire(8.8), 0, .4, .1); add(birds(8.6), 0, .15, -.6)
add(jingle([72, 79, 84], .12, 'tri', .3), .7, .1)
add(gurgle(1.3, 60), 3.2, .9)
add(footstep(), 5.7, .3); add(footstep(), 6.0, .3)
add(wood_thud(240, .15, 2500), 6.2, .2); add(buzzer(.3), 7.2, .2)
# ---------- 2. улица ----------
add(door_creak(.6), 8.85, .5)
add(lp(wind_howl(13.8), 500), 8.8, .12, -.4); add(birds(13.8), 8.8, .12, .5)
add(crunch(), 9.55, .7); add(crunch(), 9.75, .5); add(boing(), 9.7, .15)
add(whoosh(.35, 2000, 400, False), 10.7, .3); add(wood_thud(60, .5, 400) * 1.3, 11.05, .7); add(lp(noise(.4), 1200) * env(int(.4 * SR), .002, .15, 4), 11.05, .6)
add(rustle(.6), 11.9, .35)
for k in range(7): add(crunch(), 12.5 + k * .34, .4, (-.2, .2)[k % 2])
# ---------- 3. ящик ----------
add(lp(wind_howl(7.8), 500), 14.8, .1, -.3)
for k in range(5): add(blip(400 + k * 20, .05), 16.4 + k * .5, .05)
for k in range(8): add(mouse_squeak(5000, .02), 18.0 + k * .11, .06, -.4)
for k in range(3): add(mouse_squeak(3800, .05), 18.95 + k * .12, .2)
add(squeak(.1, 900, 600), 19.15, .2); add(wood_thud(130, .3, 1600), 19.35, .7)
add(mouse_squeak(3500, .1), 20.35, .4); for_ = [add(mouse_squeak(5000, .02), 20.4 + k * .11, .06, -.5) for k in range(10)]
add(trombone(), 20.7, .25)
# ---------- 4. справка ----------
add(jingle([84, 88], .05, 'sq', .06), 22.7, .1)
for k in range(13): add(lp(noise(.06), 1500) * env(int(.06 * SR), .002, .02, 4), 22.8 + k * 2.8 / 13, .25, -.5 + k / 13)
add(jingle([79, 84, 88], .06, 'sq', .1), 27.0, .14); add(glass_ping(2400, .2), 27.1, .12)
for k in range(4): add(blip(1600, .03), 28.6 + k * .25, .05)
add(jingle([76, 83], .06, 'tri', .2), 31.25, .14)
for t0 in (31.4, 32.0, 33.2): add(buzzer(.18), t0 + .1, .12)
add(jingle([72, 76, 79, 84], .07, 'tri', .25), 34.4, .2)
# ---------- 5. ночь и добыча ----------
add(tape_rewind(1.2), 36.0, .2); add(crickets(1.2) * .5, 36.2, .2)
for k in range(4): add(crunch(), 37.5 + k * .3, .35)
add(jingle([72, 76, 79, 84, 88], .07, 'tri', .25), 38.6, .2)
# ---------- 6. кухня ----------
add(fire(8.9), 39.95, .5, .1)
for k in range(10): add(lp(noise(.08), 2000) * env(int(.08 * SR), .002, .03, 4), 40.3 + k * .36, .25)
add(buzzer(.25), 40.3, .12)
add(sand_pour(.9) * .6, 44.6, .4); add(lp(noise(.5), 500) * env(int(.5 * SR), .02, .3, 3), 45.0, .3)
for k in range(5): add(lp(noise(.12), 500) * env(int(.12 * SR), .003, .05, 4) + wood_thud(200, .12, 900) * .2, 45.85 + k * .12, .35)
add(boil(2.8), 46.0, .35)
for k in range(20): add(blip(900 + k * 30, .025), 46.2 + k * .105, .04)
add(jingle([79, 84, 88], .08, 'tri', .25), 48.3, .14)
# ---------- 7. еда, урчание ----------
add(fire(11.2), 48.8, .45, .1); add(boil(3.0) * .3, 48.8, .2)
for k in range(9): add(spoon(), 49.0 + k * .63, .25)
for k in range(10): add(blip(600 + k * 60, .03), 49.4 + k * .22, .05)
add(jingle([72, 76, 79, 84], .1, 'tri', .3), 51.6, .12)
add(gurgle(1.4, 55), 54.9, 1.0); add(gurgle(2.2, 48), 56.8, .8)

# ---------- интерфейс ----------
CAPS = [('Утро. Тепло. Выспался.', .6), ('Есть охота...', 3.6), ('Только есть в избе нечего.', 5.9), ('За ночь навалило снега.', 9.2), ('Значит, еда — в лесу.', 12.4),
        ('Ящик на палочке. Работает в мультиках.', 15.0), ('В лесу — не очень.', 19.8), ('Снег — подсказка. По следам видно, где ходит заяц.', 22.8),
        ('Петля — на тропе, в узком месте, на высоте кулака от снега.', 26.8), ('Капкан — нужно железо. Яма — мёрзлая земля. Петля — проще всех.', 31.4),
        ('Ставят несколько и проверяют каждое утро.', 36.1), ('Шкуру снять, потроха убрать, мясо промыть.', 40.0),
        ('Вода — из снега. Варить час-полтора: дикое мясо — только проваренное.', 44.3), ('Ммм... Наконец-то.', 49.2), ('Сытно. Тепло. Жизнь налаживается.', 51.8), ('Хм...', 56.4)]
for s, a in CAPS:
    add(jingle([84, 91], .04, 'sq', .05), a, .1)
    for k, ch in enumerate(s):
        if ch.strip(): add(blip(1150 + (k % 3) * 60), a + .2 + k / 30, .03)

# ---------- мастер ----------
mix = np.stack([crush(L, 12, 2), crush(R, 12, 2)])
def verb(x):
    y = np.zeros_like(x)
    for dly, g in [(.031, .5), (.047, .45), (.071, .4), (.113, .3)]:
        dd = int(dly * SR); b = np.zeros(dd + 1); b[0] = 1; a = np.zeros(dd + 1); a[0] = 1; a[dd] = -g
        y += lfilter(b, a, x) * .25
    return lp(y, 5000)
mix = mix + np.stack([verb(mix[0]), verb(mix[1])]) * .35
fade = np.ones(N); fs, fe = int(55.5 * SR), N; fade[fs:fe] = np.linspace(1, 0, fe - fs) ** 1.3   # медленное затухание
mix *= fade
peak = np.max(np.abs(mix)); mix = mix / peak * 0.85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx5.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, 'peak', round(float(peak), 3))
