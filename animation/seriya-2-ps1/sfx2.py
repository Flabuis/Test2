"""Звук для PS1-версии серии 2 «Камин»: синтез SFX, эмбиента и фоновой музыки (без внешних сэмплов).
Тайминги совпадают с index.html. Выход: sfx.wav (44.1 кГц, стерео).
Запуск: python3 sfx.py
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

# ---------- музыка ----------
for i, t0 in enumerate(np.arange(0, 9.0, 3.0)):
    add(pad([[57, 64], [52, 59], [53, 60]][i % 3], 3.6, 900), t0, .14)
for i, t0 in enumerate(np.arange(9.0, 15.0, 3.0)):
    add(pad([[60, 64, 67], [65, 69, 72]][i % 2], 3.6, 1300), t0, .14)
add(pad([45, 46, 52], 5.5, 900), 15.0, .18)                      # тревога
add(pad([40, 41, 46], 8.6, 800), 20.0, .2)
for i, t0 in enumerate(np.arange(31.2, 51.8, 4.0)):
    add(pad([[45, 52, 57, 60], [41, 48, 53, 57], [43, 50, 55, 59], [40, 47, 52, 56]][i % 4], min(4.6, 52.0 - t0), 1100), t0, .16)
    add(bell([81, 84, 88, 83][i % 4]), t0 + 1.0, .05, .4); add(bell([76, 77, 79, 80][i % 4]), t0 + 3.0, .04, -.4)
for i, t0 in enumerate(np.arange(52.2, 60, 2.6)):
    add(pad([[60, 64, 67], [65, 69, 72], [67, 71, 74]][i % 3], min(3.2, 60.2 - t0), 1500), t0, .16)

# ---------- окружение ----------
add(wind_howl(9.4), 0, .18, -.3); add(wind_howl(9.4)[::-1].copy(), 0, .15, .3)
add(chatter(8.4), .4, .25, -.2)
add(fire(7.5), 12.5, .5); add(roar(4.5) * np.linspace(0, 1, int(4.5 * SR)), 15.5, .45)
add(roar(8.5, 900), 20, .55); add(fire(8.5), 20, .8, .2); add(wind(8.5, 400), 20, .2)
add(fire(8.0), 52, .7, -.1)

# ---------- интерфейс ----------
CAPS = [('Дом теперь есть.', 0.6), ('Но как-то холодно.', 3.0), ('Значит, нужен камин.', 6.0), ('Сложил. Затопил.', 9.6), ('Тепло...', 13.0), ('...даже слишком.', 15.2),
        ('О нет! Мой дом! Всё пропало!', 22.4),
        ('Главное правило: всё, что греется, изолировать от дерева.', 31.4), ('Камину нужен свой бетонный фундамент,', 35.6), ('не связанный с фундаментом дома.', 38.7),
        ('Между топкой и стеной — зазор и негорючий экран.', 41.6), ('Трубу через потолок ведут в разделке,', 45.6), ('а на полу перед топкой — железный лист.', 48.8), ('Вот теперь тепло.', 52.6)]
for s, a in CAPS:
    add(jingle([84, 91], .04, 'sq', .05), a, .1)
    for k, ch in enumerate(s):
        if ch.strip(): add(blip(1150 + (k % 3) * 60), a + .2 + k / 30, .03)
add(jingle([79, 84], .05, 'sq', .06), 1.0, .08); add(jingle([79, 84], .05, 'sq', .06), 52.3, .08)

# ---------- камин v1 ----------
add(jingle([72, 76, 79], .07), 9.2, .12)
nb = 6 + int(np.ceil((3.5 - 1.32) / .22))
for i in range(nb):
    k = (i + 1) / nb; add(brick(), 9.2 + 3.0 * (1 - (1 - k) ** (1 / 3)), .35, rng.uniform(-.3, .3))
add(whoosh(.5, 200, 1500), 12.4, .5)
for tt in np.arange(15.0, 19.5, .5): add(blip(1600, .03), tt, .05, -.6)    # градусник ползёт
for tt in np.arange(17.0, 20.0, .4): add(tone(880, .15, 'sq') * env(int(.15 * SR), .002, .1, 2), tt, .07)  # «ПОЖАР!»
add(wood_thud(60, .5, 500), 17.0, .5)
for tt in np.arange(17.1, 19.3, np.pi / 18): add(footstep(), tt, .4)
add(lp(noise(.6), 2000) * env(int(.6 * SR), .01, .3, 3), 19.6, .2)

# ---------- улица ----------
for tt in np.arange(20.0, 22.0, np.pi / 18): add(footstep(), tt, .5)
add(sting(), 22.2, .55)
for k in range(5): add(wood_thud(rng.uniform(60, 90), .5, 800), 23 + k * 1.1 + rng.uniform(0, .4), .3, rng.uniform(-.7, .7))  # что-то рушится

# ---------- перемотка ----------
add(tape_rewind(2.5), 28.5, .5)
add(blip(300, .08), 28.45, .2); add(blip(300, .08), 31.0, .2); add(jingle([88, 96], .03, 'sq', .05), 31.0, .15)

# ---------- справка ----------
for tt in np.arange(31.8, 35.4, 4 / 15): add(blip(1900, .03), tt, .04, .5)
for tt in np.arange(33.3, 35.4, 4 / 15): add(tone(330, .08, 'sq') * env(int(.08 * SR), .002, .05, 3), tt, .06, -.4)
for tt in np.arange(33.6, 35.4, .66): add(whoosh(.3, 800, 2400), tt, .12)
add(pour(1.6), 35.8, .35); add(wood_thud(55, .6, 500), 37.4, .7)
for tt in np.arange(38.9, 41.4, 4 / 15): add(blip(1900, .03), tt, .04, .5)
nb2 = 6 + int(np.ceil((4.1 - 1.37) / .22))
for i in range(nb2):
    k = (i + 1) / nb2; add(brick(), 41.6 + 2.0 * (1 - (1 - k) ** (1 / 3)), .3, rng.uniform(-.3, .3))
add(whoosh(.4, 200, 1400), 43.5, .3); add(fire(8.2), 43.6, .25)
add(clank(320), 44.05, .3); add(wood_thud(140, .3, 1500), 44.05, .3)
add(brick(500), 46.25, .5); add(wood_thud(120, .3, 1200), 46.25, .3)
add(clank(700), 49.75, .45)
add(blip(500, .1), 51.95, .1)

# ---------- финал ----------
add(jingle([72, 76, 79, 84, 88, 91], .09, 'tri', .3), 56.0, .2)

# ---------- мастер ----------
mix = np.stack([L, R])
mix = crush(mix[0], 12, 2), crush(mix[1], 12, 2)
mix = np.stack(mix)
# простой реверб (гребёнки) для «пещерного» SPU-звука
def verb(x):
    y = np.zeros_like(x)
    for dly, g in [(.031, .5), (.047, .45), (.071, .4), (.113, .3)]:
        dd = int(dly * SR); b = np.zeros(dd + 1); b[0] = 1; a = np.zeros(dd + 1); a[0] = 1; a[dd] = -g
        y += lfilter(b, a, x) * .25
    return lp(y, 5000)
mix = mix + np.stack([verb(mix[0]), verb(mix[1])]) * .35
fade = np.ones(N); fn = int(.8 * SR); fade[-fn:] = np.linspace(1, 0, fn)
mix *= fade
peak = np.max(np.abs(mix)); mix = mix / peak * 0.85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx2.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, 'peak', round(float(peak), 3))
