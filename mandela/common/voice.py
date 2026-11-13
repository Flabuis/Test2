"""Озвучка серии: python3 ../common/voice.py <папка серии> <сдвиг_сек> <длина_сек>
Читает vo/lines.tsv (начало, конец, кто, текст; время — от начала серии без интро), пишет vo/voice.wav.
R — диктор: RHVoice aleksandr-hq, огрублённый (ниже, хрипотца, лёгкий перегруз), интонация живая.
A — альтернат: низкий, плавающий по высоте, с «неправильными» формантами и эхом.
M — живой человек на любительской записи: mikhail, полоса микрофона видеокамеры, без огрубления.
Нужно: rhvoice rhvoice-russian, pip install pyworld soundfile, numpy, scipy.
"""
import sys, os, subprocess, tempfile
import numpy as np, soundfile as sf, pyworld as pw
from scipy.signal import butter, lfilter, resample_poly

SR = 44100
VOICE = {'R': 'aleksandr-hq', 'A': 'yuriy', 'M': 'mikhail'}


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
        y = rough(x, sr) if who == 'R' else alternate(x, sr) if who == 'A' else camcorder(x, sr)
        y = resample_poly(y, SR, sr)
        # подогнать под окно субтитра, но не быстрее x1.25 (через ffmpeg atempo)
        win = b - a; dur = len(y) / SR; tempo = min(1.25, max(1.0, dur / win))
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
