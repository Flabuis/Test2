"""Синтез звуков для «Каталога» (numpy/scipy, без сэмплов) + звук общего интро и аутро."""
import numpy as np
from scipy.signal import butter, lfilter

SR = 44100
rng = np.random.default_rng(13)


class Mix:
    def __init__(self, T): self.N = int(T * SR); self.L = np.zeros(self.N); self.R = np.zeros(self.N)

    def add(self, sig, t0, g=1.0, pan=0.0):
        i = int(t0 * SR)
        if i >= self.N or len(sig) == 0: return
        s = sig[:self.N - i]; gl, gr = g * np.sqrt((1 - pan) / 2), g * np.sqrt((1 + pan) / 2)
        self.L[i:i + len(s)] += s * gl; self.R[i:i + len(s)] += s * gr


def lp(x, f, o=2): b, a = butter(o, min(f, SR / 2 - 100) / (SR / 2)); return lfilter(b, a, x)
def hp(x, f, o=2): b, a = butter(o, f / (SR / 2), 'high'); return lfilter(b, a, x)
def bp(x, lo, hi, o=2): b, a = butter(o, [lo / (SR / 2), hi / (SR / 2)], 'band'); return lfilter(b, a, x)
def noise(d): return rng.uniform(-1, 1, int(d * SR))
def tt(d): return np.arange(int(d * SR)) / SR
def env(n, a=.005, d=.2, c=4):
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-c * np.maximum(0, t - a) / max(d, 1e-4))
def fade(x, a=.05, b=.1):
    n = len(x); t = np.arange(n) / SR; return x * np.minimum(1, t / max(a, 1e-4)) * np.minimum(1, (n / SR - t) / max(b, 1e-4))
def sine(f, d): return np.sin(2 * np.pi * f * tt(d))
def thud(f=80, d=.3, br=900):
    n = int(d * SR); return lp(noise(d), br) * env(n, .001, d * .25, 5) * .7 + np.sin(2 * np.pi * f * tt(d) * (1 - .3 * tt(d) / d)) * env(n, .001, d * .3, 5)
def click(): return hp(noise(.02), 2000) * env(int(.02 * SR), .0003, .004, 4)
def clack(f=1400): return bp(noise(.06), 800, 5000) * env(int(.06 * SR), .0005, .012, 5) + sine(f, .06) * env(int(.06 * SR), .001, .01, 5) * .3
def static(d): return hp(noise(d), 1500) * .5 + bp(noise(d), 300, 3000) * .3
def hum(d, f=60): t = tt(d); return (np.sin(2 * np.pi * f * t) * .5 + np.sin(2 * np.pi * f * 2 * t) * .3 + np.sin(2 * np.pi * f * 3 * t) * .15) * .4
def whine(d, f=15734 / 2): return sine(f, d) * .05   # строчник кинескопа (смягчён)
def drone(d, f=55, cut=400):
    t = tt(d); x = sum(np.sin(2 * np.pi * f * m * t * (1 + .002 * np.sin(t * .7 + m))) / m for m in (1, 1.5, 2, 3)); return lp(x + lp(noise(d), 200) * .6, cut) * .5
def whoosh(d=.6, f0=300, f1=2500):
    n = int(d * SR); x = noise(d); out = np.zeros(n); seg = 1024
    for s in range(0, n, seg):
        f = f0 + (f1 - f0) * s / n; out[s:s + seg] = bp(x[s:s + seg], max(60, f * .7), min(18000, f * 1.3), 1)[:len(out[s:s + seg])]
    return out * np.sin(np.pi * np.arange(n) / n) ** 2 * 1.4
def motor(d, f=120):
    t = tt(d); return (lp(np.sign(np.sin(2 * np.pi * f * t)), 900) * .3 + bp(noise(d), 400, 2000) * .2) * fade(np.ones(len(t)), .05, .15)
def beep(f=1000, d=.5): return sine(f, d) * fade(np.ones(int(d * SR)), .005, .01) * .6
def sting(d=2.5):
    t = tt(d); x = sum(np.sin(2 * np.pi * f * t) for f in (110, 116.5, 155.6, 233)) * np.exp(-t * 1.2); return lp(x + hp(noise(d), 3000) * np.exp(-t * 3) * .5, 3000) * .5
def reverb(x):
    y = np.zeros_like(x)
    for dl, g in [(.037, .5), (.053, .45), (.079, .4), (.131, .35)]:
        dd = int(dl * SR); b = np.zeros(dd + 1); b[0] = 1; a = np.zeros(dd + 1); a[0] = 1; a[dd] = -g; y += lfilter(b, a, x) * .25
    return lp(y, 4000)


INTRO, OUTRO = 14.0, 7.0


def intro(m):
    """Звук общего интро (время — от начала ролика)."""
    m.add(fade(lp(noise(14), 150) * .3, 1, .5), 0, .5)                          # тишина комнаты
    m.add(fade(static(6.3), 1.2, .05), 4.6, .22)                                  # белый шум телевизора
    m.add(fade(hum(9.4), 1.5, .2), 4.6, .25); m.add(fade(whine(9.4), 1.5, .2), 4.6, .5)
    m.add(thud(60, .4, 600), 5.5, .5); m.add(click(), 5.5, .6)                   # включился свет над кассетами
    m.add(fade(drone(8.5, 49, 300), 2, 1), 5.5, .5)
    m.add(whoosh(.7, 200, 900), 7.4, .15, .4)                                     # рука
    m.add(clack(900), 8.45, .5, .4); m.add(bp(noise(.5), 300, 2500) * env(int(.5 * SR), .02, .2, 3), 8.5, .12, .3)
    m.add(clack(1100), 10.0, .3)
    m.add(motor(.9, 90), 10.4, .35); m.add(thud(110, .25, 1500), 10.85, .5); m.add(clack(700), 10.9, .5)
    m.add(click(), 11.05, .5); m.add(beep(1000, .12), 11.15, .15)
    m.add(fade(motor(2.8, 60), .3, .5), 11.2, .15)
    m.add(whoosh(1.8, 200, 3000), 12.2, .25)


def outro(m, t0):
    """Звук общего аутро; t0 — начало аутро в ролике."""
    m.add(whoosh(2.4, 2500, 200), t0, .25)
    m.add(fade(static(1.8), .05, .05), t0 + 1.0, .22); m.add(fade(hum(4.0), .3, 1.5), t0, .25)
    m.add(motor(.6, 80), t0 + 2.6, .3); m.add(thud(120, .2, 1500), t0 + 2.8, .5); m.add(clack(800), 2.85 + t0, .4)
    m.add(click(), t0 + 4.2, .6); m.add(thud(50, .3, 400), t0 + 4.2, .3)
    m.add(fade(drone(3.0, 41, 250), .5, 2.5), t0 + 4.0, .4)


# ---------- «кинематографичные» хоррор-звуки (с тома 6) ----------
def saw(f, d):
    t = tt(d); return 2 * ((f * t) % 1) - 1
def braam(d=3.0, f=41.2):
    """Тяжёлый «брам»: расстроенные пилы внизу, перегруз, раскрывающийся фильтр."""
    n = int(d * SR); x = sum(saw(f * m * (1 + dt), d) for m, dt in ((1, 0), (1, .006), (2, -.004), (1.5, .003), (.5, 0)))
    x = np.tanh(x * 1.5); out = np.zeros(n); seg = 2048
    for s in range(0, n, seg):
        k = s / n; c = 300 + 2200 * np.sin(np.pi * min(1, k * 1.6)) ** 2; out[s:s + seg] = lp(x[s:s + seg], c, 1)[:len(out[s:s + seg])]
    return out * env(n, .04, d * .45, 2.2) * .7
def impact(d=2.5):
    """Резкое появление: суб-удар с падением высоты + шумовой взрыв + металлический призвук."""
    t = tt(d); n = len(t)
    sub = np.sin(2 * np.pi * np.cumsum(30 + 90 * np.exp(-t * 6)) / SR) * np.exp(-t * 2.2)
    burst = lp(noise(d), 4000) * np.exp(-t * 9)
    metal = sum(np.sin(2 * np.pi * f * t) * a for f, a in ((523, .3), (1371, .2), (2219, .12), (3203, .08))) * np.exp(-t * 3)
    return np.tanh((sub * 1.2 + burst * .8 + metal * .5) * 1.4) * .8
def riser(d=6.0, f0=60, f1=900):
    """Нарастание: тон, уходящий вверх (с октавными слоями), и шум, который раскрывается."""
    t = tt(d); k = t / d; out = np.zeros(len(t))
    for o in (1, 2, 4):
        f = f0 * o * (f1 / f0) ** k; out += np.sin(2 * np.pi * np.cumsum(f) / SR) / o
    nz = noise(d); out2 = np.zeros(len(t)); seg = 2048
    for s in range(0, len(t), seg):
        c = 200 + 6000 * (s / len(t)) ** 2; out2[s:s + seg] = lp(nz[s:s + seg], c, 1)[:len(out2[s:s + seg])]
    return (out * .4 + out2 * .5) * k ** 2
def choir(d, notes=(50, 57, 62, 65), bright=1.0):
    """Хор «ааа»: пилы через формантные полосы гласной А, медленное вибрато."""
    t = tt(d); x = np.zeros(len(t))
    for m in notes:
        f = 440 * 2 ** ((m - 69) / 12)
        for dt in (-.004, 0, .005):
            ph = np.cumsum(f * (1 + dt) * (1 + .006 * np.sin(2 * np.pi * 5.2 * t + m))) / SR; x += 2 * (ph % 1) - 1
    y = bp(x, 650, 1100) * 1.0 + bp(x, 1000, 1500) * .5 * bright + bp(x, 2400, 3000) * .2 * bright
    return fade(y / len(notes) * .5, 1.5, 1.5)
def dark_amb(d, base=36):
    """Пугающий эмбиент: низкий гул с биениями, «дыхание» фильтрованного шума, редкие металлические стоны."""
    t = tt(d); f = 440 * 2 ** ((base - 69) / 12)
    hum_ = sum(np.sin(2 * np.pi * f * m * t * (1 + .0015 * np.sin(t * .3 + m))) / m for m in (1, 1.01, 1.5, 2.02))
    breath_ = lp(noise(d), 300) * (.5 + .5 * np.sin(2 * np.pi * .11 * t)) * 1.5
    out = lp(hum_, 500) * .4 + breath_ * .5
    for k in range(int(d / 7)):
        t0 = rng.uniform(0, max(.1, d - 4)); m = int(3.5 * SR); tm = np.arange(m) / SR; ff = rng.uniform(180, 420)
        moan = np.sin(2 * np.pi * np.cumsum(ff * (1 + .08 * np.sin(2 * np.pi * .4 * tm))) / SR) * np.sin(np.pi * tm / 3.5) ** 2 * .12
        i = int(t0 * SR); out[i:i + m] += moan[:len(out) - i]
    return fade(out, 2, 2)
def reverse_swell(x):
    """Обратный реверб-нарост перед ударом."""
    y = reverb(np.concatenate([x, np.zeros(int(1.5 * SR))]))[::-1]; return y / (np.max(np.abs(y)) + 1e-9) * .6
