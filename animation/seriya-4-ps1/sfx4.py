"""Звук для PS1-версии серии 4 «Полати»: синтез SFX, эмбиента и фоновой музыки (без внешних сэмплов).
Тайминги совпадают с index.html. Выход: sfx4.wav (44.1 кГц, стерео).
Запуск: python3 sfx4.py
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

# ---------- музыка ----------
for i, t0 in enumerate(np.arange(0, 10, 3.3)): add(pad([[57, 60, 64], [52, 55, 59], [53, 57, 60]][i % 3], 3.8, 900), t0, .13)
for i, t0 in enumerate(np.arange(10, 17.8, 2.6)): add(pad([[60, 64, 67], [65, 69, 72], [62, 65, 69]][i % 3], 3.0, 1300), t0, .12)
for i, t0 in enumerate(np.arange(18.1, 27.9, 3.2)):
    add(pad([[45, 52, 57, 60], [41, 48, 53, 57], [43, 50, 55, 59]][i % 3], min(3.8, 28.0 - t0), 1100), t0, .15)
    add(bell([81, 84, 88][i % 3]), t0 + 1.0, .05, .4)
for i, t0 in enumerate(np.arange(28, 43, 3.0)): add(pad([[60, 64, 67], [62, 65, 69], [57, 60, 64], [65, 69, 72], [67, 71, 74]][i % 5], 3.4, 1300), t0, .12)
for i, t0 in enumerate(np.arange(43, 49.5, 3.2)): add(pad([[60, 64, 67, 72], [65, 69, 72]][i % 2], min(3.8, 49.5 - t0), 1500), t0, .15)
for i, t0 in enumerate(np.arange(51.2, 60, 3.0)): add(pad([[57, 60, 64], [60, 64, 67], [65, 69, 72]][i % 3], min(3.6, 60.2 - t0), 1300), t0, .14)
add(jingle([72, 76, 79, 84], .5, 'tri', 1.2), 56.6, .07)

# ---------- 1. холодный пол ----------
add(fire(18), 0, .45, .1)
add(lp(wind_howl(18), 400), 0, .12, -.5)
add(shiver_teeth(2.4), 1.2, .18); add(shiver_teeth(1.6), 7.3, .2)
add(wood_thud(80, .3, 700), 4.5, .25); add(rustle(.5), 4.5, .1); add(wood_thud(80, .3, 700), 7.0, .25)
add(jingle([76, 83, 88], .06, 'sq', .1), 9.9, .16); add(boing(), 9.9, .15)
# ---------- 2. солома и мышь ----------
for k in range(6): add(footstep(), 10.1 + k * .32, .35)
add(rustle(.7), 11.5, .4); add(wood_thud(90, .3, 800), 11.75, .35); add(rustle(.6), 11.75, .35)
add(jingle([72, 76, 79], .1, 'tri', .25), 12.2, .1)
add(squeak(.25, 500, 1400), 13.45, .3); add(boing(), 13.5, .25)
add(shiver_teeth(1.4) * 1.5, 13.7, .25); add(rustle(1.3), 13.7, .15)
add(rustle(.3), 15.0, .3); add(mouse_squeak(3400, .14), 15.65, .45, -.3)
add(rustle(.3), 16.4, .25)
d = 1.0; n = int(d * SR); t = np.arange(n) / SR
add(np.sin(2 * np.pi * (180 + 900 * t) * t) * .25 * np.sin(np.pi * t / d), 17.6, .4)
# ---------- 3. схема ----------
add(jingle([84, 88], .05, 'sq', .06), 18.2, .1)
add(whoosh(2.5, 300, 1800), 18.6, .18, .3); add(whoosh(2.5, 1800, 300, False), 23.1, .18, -.3)
for tt in np.arange(18.6, 27.4, .5): add(blip(500 + (tt - 18.6) * 90, .03), tt, .04, .5)
add(wind_howl(3.0), 24.5, .15, -.6)
# ---------- 4. настил ----------
for i in range(8): add(hammer_hit(), 28.58 + i * .32, .45, .3)
add(tape_rewind(.5), 30.95, .25); add(glass_ping(1200, .4), 31.1, .15)
add(jingle([79, 84, 88], .07, 'tri', .25), 32.0, .14)
# ---------- 5. тюфяк ----------
for tt in np.arange(34.4, 36.4, .15): add(stitch(), tt, .3)
for i in range(6): add(whoosh(.35, 600, 2000), 36.6 + i * .27, .12); add(rustle(.25), 36.95 + i * .27, .3)
add(wood_thud(200, .15, 1500), 38.75, .2); add(jingle([76, 81], .06, 'tri', .15), 38.8, .1)
for k in range(5): add(mouse_squeak(4200, .04), 38.95 + k * .13, .15, -.4)
for k in range(4): add(mouse_squeak(3600, .05), 39.7 + k * .17, .2)
add(mouse_squeak(3000, .35, True), 40.45, .4)
add(trombone(), 40.8, .3)
for k in range(10): add(mouse_squeak(5000, .02), 41.0 + k * .19, .05, .4)
# ---------- 6. полати ----------
for k in range(5): add(wood_thud(150 + k * 10, .15, 1600), 43.2 + k * .35, .3, .2)
add(rustle(.4), 45.0, .3); add(jingle([72, 76, 79, 84], .09, 'tri', .3), 45.3, .14)
add(snore(1.5), 46.0, .25)
for k in range(5): add(rustle(.35), 47.6 + k * .32, .25 + k * .05)
add(whoosh(.4, 2000, 400, False), 49.15, .35)
add(wood_thud(55, .8, 500) * 1.6, 50.0, 1.0); add(crack(), 50.0, .3)
# ---------- 7. снова на полу ----------
add(fire(9), 51.0, .4, .1)
for k in range(6): add(glass_ping(2600 + (k % 3) * 300, .3), 51.2 + k * .35, .08, (-.3, .3)[k % 2])
add(rustle(.2), 51.6, .2)
for k in range(6): add(mouse_squeak(3800 + (k % 2) * 500, .06), 52.4 + k * .13, .25, .3)
add(jingle([84, 88, 91], .06, 'sq', .1), 54.3, .14)
for i in range(7): add(hammer_hit(), 54.45 + i * .3, .4, .2)
add(snore(1.8), 56.7, .3); add(snore(1.8), 58.5, .25)

# ---------- интерфейс ----------
CAPS = [('Ночь. Камин горит, а на полу — холодно.', 0.6), ('Спать на голых досках — как на льду.', 3.8), ('Брр... Колотун.', 7.3),
        ('Солома — мягко и тепло.', 10.2), ('Только в ней уже кто-то живёт.', 14.9),
        ('Тёплый воздух лёгкий — он поднимается к потолку.', 18.4), ('Холодный тяжелее и стелется по полу. Внизу — самый холод.', 23.0),
        ('Значит, спать — наверху. Настил у трубы, но с зазором, как разделка.', 28.3),
        ('Мешок из холста, набитый соломой, — тюфяк.', 34.2), ('Сверху — полынь. Мыши её запах не выносят.', 38.2),
        ('Полати. Тепло, мягко, и никто не кусает.', 43.2), ('Красота...', 47.4), ('Полатям нужно ещё кое-что.', 51.3), ('Бортик. Чтобы не скатиться обратно в холод.', 54.3)]
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
blk = (np.arange(N) >= int(49.5 * SR)) & (np.arange(N) < int(50.0 * SR)); mix[:, blk] *= .15   # тишина перед «бух»
fade = np.ones(N); fn = int(2.4 * SR); fade[-fn:] = np.linspace(1, 0, fn) ** 1.5
mix *= fade
peak = np.max(np.abs(mix)); mix = mix / peak * 0.85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx4.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, 'peak', round(float(peak), 3))
