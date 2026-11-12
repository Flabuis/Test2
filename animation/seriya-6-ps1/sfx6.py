"""Звук для PS1-версии серии 6 «Нужник»: синтез SFX, эмбиента и фоновой музыки (без внешних сэмплов).
Тайминги совпадают с index.html. Выход: sfx6.wav (44.1 кГц, стерео).
Запуск: python3 sfx6.py
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

def plop():
    d = .5; n = int(d * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(180 + 500 * np.exp(-t * 18)) / SR) * env(n, .002, .12, 4) + lp(noise(d), 800) * env(n, .001, .05, 5) * .4
def drip():
    d = .35; n = int(d * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(900 + 1400 * np.exp(-t * 25)) / SR) * env(n, .001, .08, 5) * .7
def dig(): return lp(noise(.25), 1200) * env(int(.25 * SR), .005, .1, 4) + wood_thud(90, .25, 700) * .4
def menu_move(): return blip(1500, .03)
def menu_ok(): return jingle([84, 91], .05, 'sq', .07)

# ---------- музыка ----------
for i, t0 in enumerate(np.arange(0, 7, 2.4)): add(pad([[57, 60, 64], [56, 59, 64], [57, 60, 63]][i % 3], 2.8, 900), t0, .11)
for i, t0 in enumerate(np.arange(7, 15, 2.7)): add(pad([[60, 64, 67], [62, 65, 69], [64, 67, 71]][i % 3], 3.1, 1300), t0, .12)
for i, t0 in enumerate(np.arange(15, 36.4, 3.0)):
    add(pad([[45, 52, 57, 60], [41, 48, 53, 57], [43, 50, 55, 59], [40, 47, 52, 56]][i % 4], min(3.5, 36.5 - t0), 1100), t0, .14)
    add(bell([81, 84, 88, 83][i % 4]), t0 + 1.0, .04, .4)
for i, t0 in enumerate(np.arange(38.8, 44.4, 1.4)): add(tone(440 * 2 ** (([72, 76, 79, 76][i % 4]) - 69) / 12) if False else pad([[60, 64, 67], [65, 69, 72], [67, 71, 74], [60, 64, 67]][i % 4], 1.6, 2000), t0, .12)
for i, t0 in enumerate(np.arange(44.4, 51.4, 3.4)): add(pad([[60, 64, 67, 72], [65, 69, 72], [67, 71, 74]][i % 3], 3.8, 1500), t0, .13)
for i, t0 in enumerate(np.arange(51.4, 60, 2.9)): add(pad([[60, 64, 67], [65, 69, 72], [57, 60, 64], [56, 60, 63]][i % 4], min(3.4, 60.2 - t0), 1300 - i * 150), t0, .14 - i * .02)

# ---------- 1. изба ----------
add(fire(7.0), 0, .4, .1); add(gurgle(1.8, 50), .8, 1.0); add(gurgle(1.2, 60), 3.0, .7)
for k in range(8): add(footstep(), 4.1 + k * .3, .35)
add(door_creak(.5), 6.5, .4)
# ---------- 2. место ----------
add(lp(wind_howl(44), 500), 7.0, .12, -.4); add(birds(29), 7.0, .1, .5)
for k in range(30): add(crunch(), 7.6 + k * 3.4 / 30, .2, (-.2, .2)[k % 2]); add(blip(700 + k * 15, .02), 7.6 + k * 3.4 / 30, .03)
add(jingle([79, 84], .06, 'sq', .1), 10.4, .12)
add(whoosh(1.5, 300, 1200), 11.8, .25, .5); add(whoosh(1.5, 300, 1200), 13.2, .2, -.5)
# ---------- 3. копаем ----------
add(dig(), 15.2, .5); add(dig(), 15.9, .4)
add(clank(1100), 16.3, .7); add(twang(), 16.35, .35); add(boing(), 16.5, .2)
add(fire(2.6), 19.0, .6); add(whoosh(.6, 400, 2000), 19.0, .3)
for k in range(14): add(dig(), 21.7 + k * .36, .45)
add(jingle([79, 84, 88], .07, 'tri', .25), 26.4, .14)
# ---------- 4. стройка ----------
for i in range(11): add(hammer_hit(), 27.45 + i * .42, .45, .2)
add(jingle([72, 76, 79, 84, 88], .07, 'tri', .25), 31.4, .18)
# ---------- 5. заходит ----------
for k in range(4): add(crunch(), 36.5 + k * .25, .3)
add(door_creak(.4), 37.3, .4); add(wood_thud(140, .25, 1500), 38.2, .5)
# ---------- инвентарь ----------
add(menu_ok(), 38.9, .2)
for tt in (39.5, 40.1): add(menu_move(), tt, .12)
add(menu_ok(), 40.25, .15); add(menu_move(), 40.9, .12); add(menu_ok(), 41.65, .2)
add(whoosh(.8, 2000, 300, False), 41.7, .3)
add(jingle([72, 76, 79, 84], .06, 'sq', .1), 42.6, .16)
# ---------- 6. снаружи ----------
add(plop(), 44.5, .9); add(wood_thud(70, .3, 600), 44.5, .3)
add(door_creak(.4), 45.6, .4); add(jingle([72, 79, 84], .12, 'tri', .3), 46.0, .1)
add(sand_pour(.8) * .6, 47.0, .35); add(door_creak(.4), 48.6, .3)
for k in range(8): add(crunch(), 48.8 + k * .32, .3)
add(door_creak(.5), 50.8, .35)
# ---------- 7. дома ----------
add(fire(8.6), 51.4, .45, .1)
for k in range(5): add(footstep(), 51.5 + k * .28, .3)
add(drip(), 55.05, .9)
add(drip(), 58.4, .5)

# ---------- интерфейс ----------
CAPS = [('Всё съеденное однажды просится наружу.', .8), ('Срочно...', 3.8), ('Место — подальше от избы и от воды. Шагов тридцать, не меньше.', 7.4),
        ('И с подветренной стороны, чтобы запах не несло домой.', 11.6), ('Зимой земля мёрзлая. Лопата отскакивает.', 15.4),
        ('Сначала костёр — отогреть землю. Потом копать. Яма — в полтора метра.', 19.0), ('Над ямой — настил с дыркой. Стены, крыша, дверь.', 27.2),
        ('Сердечко в двери — для света и проветривания.', 31.2), ('Дальше — дело техники.', 36.6), ('Сверху — присыпать золой. Меньше запаха.', 46.0),
        ('Дом. Камин. Туалет. Цивилизация.', 51.6)]
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
fade = np.ones(N); fs = int(55.8 * SR); fade[fs:] = np.linspace(1, 0, N - fs) ** 1.3
mix *= fade
peak = np.max(np.abs(mix)); mix = mix / peak * 0.85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx6.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, 'peak', round(float(peak), 3))
