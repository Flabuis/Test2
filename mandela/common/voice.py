"""Озвучка серии: python3 ../common/voice.py <папка серии> <сдвиг_сек> <длина_сек>
Читает vo/lines.tsv (начало, конец, кто, текст; время — от начала серии без интро), пишет vo/voice.wav.
R — диктор: RHVoice aleksandr-hq, огрублённый (ниже, хрипотца, лёгкий перегруз), интонация живая.
A — альтернат: низкий, плавающий по высоте, с «неправильными» формантами и эхом.
M — живой человек на любительской записи: mikhail, полоса микрофона видеокамеры, без огрубления.
X — диктор с искажениями: местами проседает по высоте, заикается, хрустит (сигнал «захватывают»).
S — диктор, который всё сильнее замедляется и проседает (предупреждение «выключите кассету»).
F — голос по телефону (автоответчик): elena, телефонная полоса. W — тот же голос, но «не тот»: ниже, плывёт, медленнее.
Нужно: rhvoice rhvoice-russian, pip install pyworld soundfile, numpy, scipy.
"""
import sys, os, subprocess, tempfile
import numpy as np, soundfile as sf, pyworld as pw
from scipy.signal import butter, lfilter, resample_poly

SR = 44100
VOICE = {'R': 'aleksandr-hq', 'A': 'yuriy', 'M': 'mikhail', 'F': 'elena', 'W': 'elena', 'X': 'aleksandr-hq', 'S': 'aleksandr-hq'}


def bp(x, lo, hi, sr):
    b, a = butter(2, [lo / (sr / 2), hi / (sr / 2)], 'band'); return lfilter(b, a, x)


def tts(text, voice):
    w = tempfile.mktemp(suffix='.wav')
    subprocess.run(['RHVoice-test', '-p', voice, '-o', w], input=text.encode(), stderr=subprocess.DEVNULL, check=True)
    x, sr = sf.read(w); os.remove(w)
    return x.astype(np.float64), sr


def rough(x, sr, pitch=.82, warp=.93, comp=.6, drive=2.2):
    """Грубый мужской голос: ниже, интонация живая, но сжатая, форманты чуть ниже, хрипотца и лёгкий перегруз."""
    f0, t = pw.harvest(x, sr, f0_floor=50, f0_ceil=400, frame_period=5)
    sp = pw.cheaptrick(x, f0, t, sr); ap = pw.d4c(x, f0, t, sr)
    v = f0 > 0; m = np.log(f0[v]).mean(); f1 = f0.copy()
    f1[v] = np.exp((np.log(f0[v]) - m) * comp + m + np.log(pitch))
    n = sp.shape[1]; src = np.clip(np.arange(n) / warp, 0, n - 1)
    sp = np.stack([np.interp(src, np.arange(n), r) for r in sp])
    ap = np.clip(ap + .08, 0, 1)
    y = pw.synthesize(f1, sp, ap, sr, frame_period=5); y = y / (np.max(np.abs(y)) + 1e-9)
    y = np.tanh(y * drive) / np.tanh(drive)
    return bp(y, 90, 6500, sr)


def camcorder(x, sr):
    y = bp(x, 180, 5200, sr); y = y / (np.max(np.abs(y)) + 1e-9); return np.tanh(y * 1.4) / np.tanh(1.4)


def phone(x, sr):
    y = bp(x, 320, 3300, sr); y = y / (np.max(np.abs(y)) + 1e-9); return np.tanh(y * 2.0) / np.tanh(2.0)


def wrong(x, sr):
    f0, t = pw.harvest(x, sr, f0_floor=80, f0_ceil=500, frame_period=5)
    sp = pw.cheaptrick(x, f0, t, sr); ap = pw.d4c(x, f0, t, sr)
    n = sp.shape[1]; src = np.clip(np.arange(n) / .9, 0, n - 1); sp = np.stack([np.interp(src, np.arange(n), r) for r in sp])
    k = np.arange(len(f0)); f1 = np.where(f0 > 0, f0 * .82 * (1 + .06 * np.sin(k * .04)), 0)
    y = pw.synthesize(f1, sp, ap, sr, frame_period=6.5)        # медленнее: синтез с более длинным шагом кадра
    return phone(y, sr)


def glitched(x, sr):
    y = rough(x, sr); n = len(y); r = np.random.default_rng(int(abs(hash(n)) % 2**31) + 7)
    for _ in range(3):
        L = int(r.uniform(.18, .38) * sr); a = int(r.uniform(.1, .85) * max(1, n - L)); seg = y[a:a + L].copy(); kind = r.integers(0, 3)
        if kind == 0:   # просадка по высоте
            seg = resample_poly(seg, 10, 7)[:L]; seg = np.pad(seg, (0, L - len(seg)))
        elif kind == 1:  # заикание
            q = L // 4; seg = np.tile(seg[:q], 4)[:L]
        else:            # цифровой хруст
            seg = np.round(seg * 6) / 6 * (np.arange(L) % 40 < 30)
        L = min(L, len(y) - a); seg = np.pad(seg, (0, max(0, L - len(seg))))[:L]; y[a:a + L] = seg
    return y


def slowing(x, sr):
    f0, t = pw.harvest(x, sr, f0_floor=50, f0_ceil=400, frame_period=5)
    sp = pw.cheaptrick(x, f0, t, sr); ap = pw.d4c(x, f0, t, sr); n = len(f0)
    pos, out = 0.0, []
    while pos < n - 1:
        k = pos / n; step = 1.0 - .72 * k; out.append((int(pos), step)); pos += step   # чем дальше, тем медленнее
    idx = np.array([i for i, _ in out]); st = np.array([s for _, s in out])
    f1 = np.where(f0[idx] > 0, f0[idx] * .82 * (.55 + .45 * st), 0)
    y = pw.synthesize(np.ascontiguousarray(f1), np.ascontiguousarray(sp[idx]), np.ascontiguousarray(ap[idx]), sr, frame_period=5)
    y = y / (np.max(np.abs(y)) + 1e-9); return bp(np.tanh(y * 2.2) / np.tanh(2.2), 90, 6500, sr)


def alternate(x, sr):
    f0, t = pw.harvest(x, sr, f0_floor=60, f0_ceil=400, frame_period=5)
    sp = pw.cheaptrick(x, f0, t, sr); ap = pw.d4c(x, f0, t, sr)
    n = sp.shape[1]; src = np.clip(np.arange(n) / .86, 0, n - 1)
    sp = np.stack([np.interp(src, np.arange(n), r) for r in sp])                     # форманты «шире» — голос чужой
    k = np.arange(len(f0))
    f1 = np.where(f0 > 0, f0 * .62 * (1 + .08 * np.sin(k * .05) + .04 * np.sin(k * .21)), 0)
    y = pw.synthesize(f1, sp, ap, sr, frame_period=5)
    d = int(.09 * sr); e = np.zeros(len(y) + 3 * d); e[:len(y)] += y
    for i, g in enumerate((.45, .25, .12)): e[(i + 1) * d:(i + 1) * d + len(y)] += y * g
    return bp(e, 90, 5000, sr)


def main():
    ep, shift, total = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    out = np.zeros(int(total * SR))
    for ln in open(os.path.join(ep, 'vo', 'lines.tsv'), encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if len(p) != 4: continue
        a, b, who, text = float(p[0]), float(p[1]), p[2], p[3]
        x, sr = tts(text, VOICE[who])
        y = {'R': rough, 'A': alternate, 'M': camcorder, 'F': phone, 'W': wrong, 'X': glitched, 'S': slowing}[who](x, sr)
        y = resample_poly(y, SR, sr)
        # подогнать под окно субтитра, но не быстрее x1.25 (через ffmpeg atempo)
        win = b - a; dur = len(y) / SR; tempo = 1.0 if who == 'S' else min(1.25, max(1.0, dur / win))
        if tempo > 1.0:
            i, o = tempfile.mktemp(suffix='.wav'), tempfile.mktemp(suffix='.wav')
            sf.write(i, y, SR); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', i, '-af', f'atempo={tempo:.3f}', o], check=True)
            y, _ = sf.read(o); os.remove(i); os.remove(o)
        y = y / (np.max(np.abs(y)) + 1e-9) * (.8 if who == 'R' else .9)
        s = int((a + shift) * SR); out[s:s + len(y)] += y[:len(out) - s]
        print(f'{a:6.1f} {who} x{tempo:.2f} конец {a + len(y) / SR:6.2f} (окно до {b})  {text}')
    sf.write(os.path.join(ep, 'vo', 'voice.wav'), np.clip(out, -1, 1), SR)


if __name__ == '__main__':
    main()
