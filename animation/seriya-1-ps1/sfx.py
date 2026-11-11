"""Звук для PS1-версии серии 1: синтез SFX, эмбиента и фоновой музыки (без внешних сэмплов).
Тайминги совпадают с index.html. Выход: sfx.wav (44.1 кГц, стерео).
Запуск: python3 sfx.py
"""
import numpy as np
from scipy.signal import butter, lfilter
import wave, os

SR = 44100
T = 58.0
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


# ---------- эмбиент ----------
add(wind(21.4, 600), 0, .28, -.2); add(wind(21.4, 450), 0, .28, .2)
add(crickets(13) * np.linspace(0, 1, int(13 * SR)), 8.4, .18, .3)
add(wind(7, 450), 51, .25); add(crickets(7), 51, .2, -.3); add(fire(7), 51, .9, -.1)

# ---------- музыка: тихий синт-пэд (ля минор), колокольчики как у SPU ----------
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
prog_forest = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]   # Am F C G
prog_void = [[45, 52, 57, 60], [41, 48, 53, 57], [43, 50, 55, 59], [40, 47, 52, 56]]  # Am F G E
for i, t0 in enumerate(np.arange(0, 21.4, 4.0)):
    add(pad(prog_forest[i % 4], min(4.6, 21.6 - t0)), t0, .16)
for i, t0 in enumerate(np.arange(22.2, 50.8, 4.0)):
    add(pad(prog_void[i % 4], min(4.6, 51.0 - t0), 1100), t0, .17)
    add(bell([69, 72, 76, 71][i % 4] + 12), t0 + 1.0, .05, .4); add(bell([64, 65, 67, 68][i % 4] + 12), t0 + 3.0, .04, -.4)
for i, t0 in enumerate(np.arange(51.2, 58, 3.4)):
    add(pad([[57, 60, 64], [52, 55, 59]][i % 2], min(4.0, 58.2 - t0), 1000), t0, .15)

# ---------- интерфейс: окна диалогов и печать текста ----------
CAPS = [('Лес. Вечер.', 0.6, 3.9), ('Скоро ночь.', 4.1, 7.3), ('А дома нет.', 7.6, 10.7), ('Значит, будем строить.', 10.9, 12.9),
        ('Обычный деревянный дом, из бруса.', 13.4, 18.3), ('Маленький облом.', 18.9, 21.2),
        ('В средневековье строили не из брусков, а из брёвен.', 22.4, 25.6), ('Пилить бревно вдоль вручную — это неделя мата', 25.8, 29.0), ('и одна сломанная пила.', 29.1, 31.6),
        ('Поэтому рубили сруб из круглых брёвен.', 32.4, 36.8), ('А главный инструмент — топор.', 37.0, 41.6),
        ('Даже доски не пилили:', 42.4, 44.6), ('их кололи клиньями', 44.7, 46.6), ('и стёсывали топором.', 46.7, 50.6)]
for s, a, b in CAPS:
    add(jingle([84, 91], .04, 'sq', .05), a, .12)
    for k, ch in enumerate(s):
        if ch.strip(): add(blip(1150 + (k % 3) * 60), a + .2 + k / 30, .035)
for i, ch in enumerate('КОНЕЦ ПЕРВОЙ СЕРИИ'):
    if ch.strip(): add(blip(900), 51.8 + i / 14, .05)

# ---------- сцена A ----------
for t0 in np.arange(4.9, 10.5, .5): add(blip(2200, .015), t0, .08, -.6)                       # таймер
for t0 in np.arange(7.8, 11.0, 4 / 15): add(tone(330, .08, 'sq') * env(int(.08 * SR), .002, .05, 3), t0, .07, .4)  # мигание «ДОМ: НЕТ»
add(jingle([72, 76, 79, 84], .08), 11.0, .18, .2)                                              # «СТРОИМ!»
add(boing(), 11.2, .3)

# ---------- сцена B: брус, СТОП, развал ----------
for i in range(10):
    for s in range(4):
        add(wood_thud(160 + rng.uniform(-20, 30), .2, 2200), 13.5 + (i * 4 + s) * .085 + .3, .32, rng.uniform(-.5, .5))
add(wood_thud(120, .35, 1500), 17.3, .5)
add(buzzer(), 18.6, .55); add(wood_thud(60, .5, 600), 18.6, .9)
for k in range(26):
    add(wood_thud(rng.uniform(90, 200), .25, 2000), 19.0 + rng.uniform(0, 1.3) ** 1.5, .3, rng.uniform(-.8, .8))
add(lp(noise(1.2), 1200) * env(int(1.2 * SR), .01, .5, 3), 19.0, .4)

# ---------- «ЗАГРУЗКА» ----------
d = .8; n = int(d * SR); t = np.arange(n) / SR
add(np.sin(2 * np.pi * (180 + 900 * t) * t) * .25 * np.sin(np.pi * t / d) + bp(noise(d), 3000, 6000) * .05, 21.4, .5)
add(jingle([76, 83], .06, 'tri', .25), 22.1, .25)

# ---------- сцена C: бревно, пила, мат ----------
add(wood_thud(70, .5, 900), 22.6, .7)
add(jingle([88, 95, 88, 95], .06, 'sq', .04), 23.4, .08)
add(lp(tone(880, 1.0, 'tri') * np.linspace(0, 1, SR) * np.linspace(1, 0, SR), 4000), 24.2, .12)
st = 25.9
while st < 29.85:
    add(saw_stroke(.2, 900 + rng.uniform(-100, 150)), st, .35, .2); st += np.pi / 14
for k in range(6): add(blip(1800, .03), 26.0 + (k + 1) * 1.4 / 6, .1, .6)
add(tone(1000, .45, 'sin') * env(int(.45 * SR), .005, 1, 0.2), 28.0, .12)              # «пииип» цензуры
add(twang(), 29.85, .5); add(clank(1300), 29.85, .4); add(wood_thud(80, .4, 1200), 29.85, .4)
add(blip(500, .1), 31.95, .1)

# ---------- сцена D: сруб, топор ----------
for i in range(8):
    for k in range(4):
        tl = 32.6 + i * .42 + (0 if k < 2 else .21) + (k % 2) * .1 + .3
        add(wood_thud(rng.uniform(85, 120), .4, 1400), tl, .38, (-.6 if k % 2 else .6))
add(wood_thud(100, .4, 1600), 36.45, .5); add(jingle([67, 71, 74], .07, 'tri', .2), 36.6, .15)
add(whoosh(.55, 300, 2500), 37.0, .45, .5); add(chop(), 37.55, .9, .4)
add(jingle([72, 79], .06, 'tri', .2), 38.2, .14)
add(blip(500, .1), 41.95, .1)

# ---------- сцена E: клинья, раскол, тёс ----------
add(wood_thud(80, .45, 1100), 42.7, .6)
for th in (43.2, 43.6, 44.0): add(clank(900 + rng.uniform(-50, 50)), th, .45)
add(crack(), 44.5, .8)
add(whoosh(.4, 1200, 300, False), 45.3, .3)
for c in (46.6, 47.1, 47.6, 48.1):
    add(whoosh(.25, 600, 2200), c - .25, .2, .3); add(chop(), c, .6, .3)
add(jingle([72, 76, 79, 84, 88], .07, 'tri', .25), 48.7, .22)                                # «предмет получен»
add(blip(500, .1), 50.95, .1)

# ---------- финал ----------
add(jingle([69, 72, 76, 74, 72, 69], .32, 'tri', .6), 52.2, .16)

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
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, 'peak', round(float(peak), 3))
