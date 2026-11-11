"""Звук для PS1-версии серии 3 «Окно»: синтез SFX, эмбиента и фоновой музыки (без внешних сэмплов).
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

# ---------- музыка ----------
add(pad([60, 64, 67], 3.4, 1500), 0, .15)
for i, t0 in enumerate(np.arange(3.0, 9.4, 3.2)): add(pad([[57, 64], [52, 59]][i % 2], 3.8, 900), t0, .14)
for i, t0 in enumerate(np.arange(9.4, 17.2, 2.6)): add(pad([[60, 64, 67], [65, 69, 72], [62, 65, 69]][i % 3], 3.2, 1300), t0, .12)
for i, t0 in enumerate(np.arange(18.5, 50.0, 4.0)):
    add(pad([[45, 52, 57, 60], [41, 48, 53, 57], [43, 50, 55, 59], [40, 47, 52, 56]][i % 4], min(4.6, 50.2 - t0), 1100), t0, .16)
    add(bell([81, 84, 88, 83][i % 4]), t0 + 1.0, .05, .4); add(bell([76, 77, 79, 80][i % 4]), t0 + 3.0, .04, -.4)
for i, t0 in enumerate(np.arange(50.4, 60, 3.0)):
    add(pad([[60, 64, 67], [65, 69, 72], [67, 71, 74], [60, 64, 67, 72]][i % 4], min(3.8, 60.2 - t0), 1500), t0, .17)
add(jingle([72, 76, 79, 84], .5, 'tri', 1.2), 55.6, .07)

# ---------- комната ----------
add(fire(3.2), 0, .7, .1)
add(whoosh(1.2, 300, 2200), 2.85, .6, -.6); add(wood_thud(60, .4, 500), 3.0, .4)
add(wind_howl(14.4) * np.minimum(1, np.arange(int(14.4 * SR)) / SR / .6), 3.0, .3, -.5); add(wind_howl(14.4)[::-1].copy(), 3.0, .16, .2)
add(fire(14.2), 3.2, .3, .1)
add(chatter(5.6), 3.6, .2)
for tt in np.arange(3.3, 6.0, .45): add(blip(700 - (tt - 3.3) * 60, .04), tt, .06, -.6)   # градусник падает
add(wind_howl(3.2), 6.15, .25, 0)
add(jingle([76, 83, 88], .06, 'sq', .1), 10.6, .16); add(boing(), 10.6, .2)
add(squeak(.2), 11.5, .15)
add(sand_pour(1.1), 12.6, .45); add(lp(noise(.5), 500) * env(int(.5 * SR), .02, .3, 3), 13.0, .4)
add(jingle([79, 84], .05, 'sq', .06), 13.4, .08); add(buzzer(.3), 13.9, .25)
add(trombone(), 14.9, .4)
d = 1.0; n = int(d * SR); t = np.arange(n) / SR
add(np.sin(2 * np.pi * (180 + 900 * t) * t) * .25 * np.sin(np.pi * t / d) + bp(noise(d), 3000, 6000) * .05, 17.4, .5)
add(jingle([76, 83], .06, 'tri', .25), 18.3, .25)

# ---------- справка ----------
for t0 in (18.5, 24.55, 30.55, 37.6, 42.55): add(jingle([84, 88], .05, 'sq', .06), t0, .1)
for t0 in (19.2, 20.4, 21.6): add(sand_pour(.3), t0 + .2, .4); add(wood_thud(120, .2, 900), t0 + .3, .3)
add(wood_thud(200, .25, 1500), 22.2, .4)
for i in range(3): add(sand_pour(.6), 22.9 + i * .4, .35)
# горн
add(roar(6.0, 500) * np.linspace(.4, 1, int(6.0 * SR)), 24.6, .35); add(fire(6.0), 24.6, .4)
tt = 25.4
while tt < 30.3:
    ph0 = np.ceil(tt * 1.5) / 1.5; add(bellows(.45), ph0, .5, .5); add(squeak(.12, 500, 700), ph0 + .3, .06, .5); tt = ph0 + .01
for k in range(25): add(blip(600 + k * 40, .025), 25.6 + k * (4.0 / 25), .05, -.5)
add(jingle([84, 88, 91], .06, 'sq', .1), 29.6, .14)
# выдувание
for p in (30.9, 31.3, 31.7): add(breath(.3), p, .5); add(tone(300 + (p - 30.9) * 250, .28, 'sin') * np.sin(np.pi * np.arange(int(.28 * SR)) / int(.28 * SR)), p, .1)
n2 = int(1.2 * SR); tq = np.arange(n2) / SR
add(np.sin(2 * np.pi * np.cumsum(260 + 200 * tq / 1.2) / SR) * np.sin(np.pi * tq / 1.2) * .5 + breath(1.2)[:n2] * .5, 32.3, .16)
add(whoosh(.5, 1500, 400, False), 33.8, .25); add(glass_ping(900, .3), 34.3, .25)
for tt in np.arange(34.35, 35.0, 2 / 15): add(blip(2000, .03), tt, .08)
add(squeak(.6, 1400, 500), 34.5, .12)
add(whoosh(1.7, 500, 1500), 35.0, .22); add(wood_thud(160, .2, 1500), 36.7, .25)
# отжиг
nn = int(.8 * SR); tz = np.arange(nn) / SR
add(hp(noise(.8), 5000) * np.linspace(.2, 1, nn) * .5 + np.sin(2 * np.pi * np.cumsum(1500 + 2500 * tz / .8) / SR) * .08, 37.9, .5)   # шипение
add(shatter(), 38.7, .9); add(wood_thud(70, .3, 600), 38.7, .5)
add(wood_thud(150, .2, 1400), 40.1, .3)
for k in range(8): add(blip(900 + k * 50, .03), 40.2 + k * 2.1 / 8, .05)
add(jingle([79, 84, 88], .08, 'tri', .25), 42.3, .16)
# рама
add(wind_howl(1.4), 42.6, .22, 0)
add(whoosh(.5, 300, 1200), 43.0, .3); add(wood_thud(110, .3, 1300), 43.5, .6)
for i in range(4): add(glass_ping(2200 + i * 260, .5), 44.05 + i * .3, .35, (-.4, .4, -.4, .4)[i])
for i in range(4): add(squeak(.18, 700, 500), 45.5 + i * .2, .12)
for i in range(4): add(lp(noise(.2), 900) * env(int(.2 * SR), .01, .1, 3), 47.4 + i * .3, .45); add(wood_thud(180, .15, 1200), 47.45 + i * .3, .2)
add(jingle([72, 76, 79, 84, 88], .07, 'tri', .25), 48.8, .2)
add(blip(500, .1), 50.0, .1)

# ---------- финал ----------
add(fire(9.6), 50.4, .85, .1)
add(lp(wind_howl(9.6), 350) , 50.4, .12, -.6)          # ветер теперь глухо, за стеклом
add(jingle([79, 84], .05, 'sq', .06), 50.7, .08)
for tt in (53.0, 53.5, 54.1): add(glass_ping(3000, .15), tt, .04, -.6)   # снежинки по стеклу

# ---------- интерфейс ----------
CAPS = [('Тепло. Хорошо.', 0.6), ('Но откуда-то дует.', 3.3), ('А в окне — ничего. Просто дыра.', 6.3), ('Надо что-то делать...', 9.5),
        ('Стекло делают из песка. Насыпал в камин.', 11.5), ('Получился... тёплый песок.', 14.8),
        ('Одного песка мало. Нужны ещё зола и известь.', 18.7), ('И жар гораздо сильнее каминного: горн с мехами.', 24.7),
        ('Каплю расплава выдувают в цилиндр,', 30.7), ('разрезают и расправляют в лист.', 34.0), ('Остужать — медленно. Иначе лопнет.', 37.7),
        ('Стекло ставят в раму на замазку,', 42.7), ('а щели вокруг конопатят мхом.', 46.6), ('Теперь не дует. И видно, что на улице.', 51.0)]
for s, a in CAPS:
    add(jingle([84, 91], .04, 'sq', .05), a, .1)
    for k, ch in enumerate(s):
        if ch.strip(): add(blip(1150 + (k % 3) * 60), a + .2 + k / 30, .03)

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
fade = np.ones(N); fn = int(3.4 * SR); fade[-fn:] = np.linspace(1, 0, fn) ** 1.5
mix *= fade
peak = np.max(np.abs(mix)); mix = mix / peak * 0.85 if peak > .85 else mix
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sfx3.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix.T, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, 'peak', round(float(peak), 3))
