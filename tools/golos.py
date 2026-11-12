"""Перенос тембра закадра (RHVoice aleksandr-hq) на живую запись: интонация, паузы и темп остаются от записи,
высота и тембр подтягиваются к голосу закадра. Без нейросетей: вокодер WORLD (pyworld) + сдвиг F0 + деформация спектра.
  python3 tools/golos.py profile                 — один раз: собрать профиль голоса закадра из RHVoice
  python3 tools/golos.py convert in.wav out.wav  — переделать запись
Нужно: pip install pyworld soundfile; apt-get install rhvoice rhvoice-russian; ffmpeg.
"""
import sys, os, glob, subprocess, tempfile
import numpy as np, soundfile as sf, pyworld as pw
from scipy.ndimage import uniform_filter1d

SR = 24000
HERE = os.path.dirname(os.path.abspath(__file__))
PROF = os.path.join(HERE, 'golos_profile.npz')


def load(path):
    tmp = tempfile.mktemp(suffix='.wav')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', path, '-ac', '1', '-ar', str(SR), tmp], check=True)
    x, _ = sf.read(tmp); os.remove(tmp)
    return x.astype(np.float64)


def analyze(x):
    f0, t = pw.harvest(x, SR, f0_floor=60, f0_ceil=500, frame_period=5)
    sp = pw.cheaptrick(x, f0, t, SR); ap = pw.d4c(x, f0, t, SR)
    return f0, sp, ap


def stats(f0, sp):
    v = f0 > 0; lf = np.log(f0[v])
    e = np.log(sp + 1e-12); en = e.max(axis=1); voiced = v & (en > np.percentile(en, 30))
    return np.median(lf), lf.std(), e[voiced].mean(axis=0)


def warp(sp, a):
    n = sp.shape[1]; src = np.clip(np.arange(n) / a, 0, n - 1)
    return np.stack([np.interp(src, np.arange(n), row) for row in sp])


def profile():
    lines = []
    for f in sorted(glob.glob(os.path.join(HERE, '..', 'animation', 'seriya-*-ps1', 'vo', 'lines.tsv'))):
        for l in open(f, encoding='utf-8'):
            p = l.rstrip('\n').split('\t')
            if len(p) == 4 and p[2] == 'N': lines.append(p[3])
    F, S = [], []
    for i, s in enumerate(lines[:40]):
        w = tempfile.mktemp(suffix='.wav')
        subprocess.run(['RHVoice-test', '-p', 'aleksandr-hq', '-o', w], input=s.encode(), stderr=subprocess.DEVNULL, check=True)
        f0, sp, _ = analyze(load(w)); os.remove(w); F.append(f0); S.append(sp)
    m, sd, env = stats(np.concatenate(F), np.concatenate(S))
    np.savez(PROF, m=m, sd=sd, env=env)
    print(f'профиль: {len(F)} фраз, F0 ~ {np.exp(m):.0f} Гц')


def convert(src, dst, keep_expr=.6):
    P = np.load(PROF); x = load(src); x = x / (np.max(np.abs(x)) + 1e-9) * .9
    f0, sp, ap = analyze(x); m, sd, env = stats(f0, sp)
    # высота: среднее — как у закадра, размах интонации — в основном свой
    v = f0 > 0; f1 = f0.copy()
    f1[v] = np.exp((np.log(f0[v]) - m) / sd * (keep_expr * sd + (1 - keep_expr) * P['sd']) + P['m'])
    # форманты: подобрать растяжение спектра, ближе всего к закадру
    def dist(a):
        d = (stats(f0, warp(sp, a))[2] - P['env'])[8:220]; return np.mean((d - d.mean()) ** 2)
    best = min(np.arange(.88, 1.16, .01), key=dist)
    sp1 = warp(sp, best)
    # остаточная окраска: эквалайзер по среднему спектру
    eq = uniform_filter1d(P['env'] - stats(f0, sp1)[2], 15); eq = np.clip(eq, -2.5, 2.5)
    sp1 = sp1 * np.exp(eq)[None, :]
    y = pw.synthesize(f1, sp1, ap, SR, frame_period=5)
    y = y / (np.max(np.abs(y)) + 1e-9) * .9
    sf.write(dst, y, SR)
    print(f'{os.path.basename(src)}: F0 {np.exp(m):.0f} -> {np.exp(P["m"]):.0f} Гц, форманты x{best:.2f}')


if __name__ == '__main__':
    if sys.argv[1] == 'profile': profile()
    else: convert(sys.argv[2], sys.argv[3])
