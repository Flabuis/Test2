"""Audio study per reel: loudness (ebur128), band energy, onsets, tempo candidates, key estimate, speech/pitch evidence, sweeps, silences, sync of video cuts to onsets vs chance, and spectrogram images. Needs frames_data/ first. Writes audio/."""
import subprocess, os, sys, json, re, glob
import numpy as np
from PIL import Image, ImageDraw
from concurrent.futures import ProcessPoolExecutor

ROOT = os.environ.get("REEL_DIR", os.getcwd())
OUT = os.path.join(ROOT, "audio")
SPEC = os.path.join(OUT, "spec")
os.makedirs(SPEC, exist_ok=True)

BANDS = [("sub", 20, 60), ("bass", 60, 250), ("lowmid", 250, 500), ("mid", 500, 2000), ("himid", 2000, 6000), ("air", 6000, 16000)]


def probe_sr(f):
    o = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=sample_rate", "-of", "csv=p=0", f]).decode().split()[0].strip(",")
    return int(o)


def load_audio(f, sr):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vn", "-ac", "2", "-ar", str(sr), "-f", "f32le", "-"], stdout=subprocess.PIPE)
    a = np.frombuffer(p.stdout, dtype=np.float32)
    a = a[: len(a) // 2 * 2].reshape(-1, 2)
    return a


def ebur(f):
    p = subprocess.run(["ffmpeg", "-nostats", "-i", f, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"], stderr=subprocess.PIPE)
    t = p.stderr.decode(errors="ignore")
    seg = t[t.rfind("Summary:"):] if "Summary:" in t else ""
    def g(pat):
        m = re.search(pat, seg)
        return float(m.group(1)) if m else None
    return {"lufs_integrated": g(r"I:\s+(-?[\d.]+) LUFS"), "lra": g(r"LRA:\s+(-?[\d.]+) LU"), "true_peak_dbtp": g(r"Peak:\s+(-?[\d.]+) dBFS")}


def stft_mag(x, sr, n_fft=2048, hop=None):
    hop = hop or sr // 100
    win = np.hanning(n_fft).astype(np.float32)
    n = 1 + max(0, (len(x) - n_fft)) // hop
    idx = np.arange(n_fft)[None, :] + hop * np.arange(n)[:, None]
    fr = x[idx] * win
    return np.abs(np.fft.rfft(fr, axis=1)).astype(np.float32), hop


def db(x, floor=-120.0):
    return 20 * np.log10(np.maximum(x, 1e-9)).clip(floor, None)


def video_cuts(i):
    d = np.loadtxt(os.path.join(ROOT, "frames_data", i + ".csv"), delimiter=",", skiprows=1)
    diff = d[:, 2]
    med = np.median(diff[1:]) + 1e-6
    cuts = []
    for k in range(2, len(d)):
        if diff[k] > max(14, 6 * med) and diff[k] > 1.8 * max(diff[k - 1], 1e-6):
            if not cuts or k - cuts[-1] > 3:
                cuts.append(k)
    return d, cuts


def fps_of(f):
    o = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", f]).decode().split()[0].strip(",")
    a, b = o.split("/")
    return float(a) / float(b)


LUT_PTS = [(0, (0, 0, 4)), (0.2, (40, 11, 84)), (0.4, (101, 21, 110)), (0.6, (159, 42, 99)), (0.8, (229, 92, 48)), (0.92, (250, 181, 54)), (1.0, (252, 253, 191))]


def lut():
    xs = np.linspace(0, 1, 256)
    out = np.zeros((256, 3), np.uint8)
    p = [a for a, _ in LUT_PTS]
    for c in range(3):
        out[:, c] = np.interp(xs, p, [v[c] for _, v in LUT_PTS])
    return out


def render_spec(i, S_db, hop_s, rms_db, cuts_t, onsets, dur, sr):
    # S_db: frames x bins (dB), full-resolution
    n_bins = S_db.shape[1]
    freqs = np.linspace(0, sr / 2, n_bins)
    H = 300
    fgrid = np.geomspace(30, min(16000, sr / 2 - 100), H)
    ridx = np.clip(np.searchsorted(freqs, fgrid), 0, n_bins - 1)
    cm = lut()
    win_s = 30.0
    pxs = 40
    nwin = int(np.ceil(dur / win_s))
    paths = []
    for w in range(nwin):
        t0, t1 = w * win_s, min(dur, (w + 1) * win_s)
        f0, f1 = int(t0 / hop_s), int(t1 / hop_s)
        seg = S_db[f0:f1]
        cols = int((t1 - t0) * pxs)
        if cols < 4 or len(seg) < 2:
            continue
        xi = np.clip((np.arange(cols) / pxs / hop_s).astype(int), 0, len(seg) - 1)
        img = seg[xi][:, ridx].T[::-1]
        v = ((img + 80) / 80).clip(0, 1)
        rgb = cm[(v * 255).astype(np.uint8)]
        L, T_, B_ = 46, 26, 62
        canvas = Image.new("RGB", (L + cols + 4, T_ + H + B_), (10, 10, 12))
        canvas.paste(Image.fromarray(rgb), (L, T_))
        d = ImageDraw.Draw(canvas)
        # top strips: cuts (red) and onsets (colored by band)
        for ct in cuts_t:
            if t0 <= ct < t1:
                x = L + int((ct - t0) * pxs)
                d.line([(x, 0), (x, 11)], fill=(255, 60, 60), width=2)
                d.line([(x, T_), (x, T_ + H)], fill=(255, 60, 60), width=1) if False else None
        for (ot, os_, bi) in onsets:
            if t0 <= ot < t1:
                x = L + int((ot - t0) * pxs)
                col = [(255, 80, 80), (255, 170, 60), (240, 230, 80), (90, 220, 120), (80, 170, 255), (190, 120, 255)][bi]
                hh = 4 + min(8, int(os_ * 8))
                d.line([(x, 25), (x, 25 - hh)], fill=col, width=1)
        # freq labels
        for fq in (50, 100, 250, 500, 1000, 2000, 4000, 8000, 16000):
            if fq < fgrid[-1]:
                y = T_ + H - 1 - int(np.interp(np.log(fq), np.log(fgrid), np.arange(H)))
                d.text((2, y - 5), (f"{fq//1000}k" if fq >= 1000 else str(fq)), fill=(200, 200, 200))
                d.line([(L - 4, y), (L, y)], fill=(200, 200, 200))
        # RMS strip
        y0 = T_ + H + 4
        d.rectangle([L, y0, L + cols, y0 + 40], fill=(20, 20, 24))
        r = rms_db[f0:f1]
        for x in range(cols):
            k = min(len(r) - 1, int(x / pxs / hop_s))
            lv = (r[k] + 60) / 60
            lv = max(0, min(1, lv))
            d.line([(L + x, y0 + 40), (L + x, y0 + 40 - int(lv * 40))], fill=(120, 200, 255))
        d.text((2, y0), "RMS", fill=(200, 200, 200))
        # time axis
        ya = y0 + 44
        s = int(np.ceil(t0))
        while s <= t1:
            x = L + int((s - t0) * pxs)
            d.line([(x, ya), (x, ya + (6 if s % 5 == 0 else 3))], fill=(255, 255, 255))
            if s % 5 == 0:
                d.text((x - 8, ya + 7), f"{s}s", fill=(255, 255, 255))
            s += 1
        p = os.path.join(SPEC, f"{i}_{w+1:02d}.jpg")
        canvas.save(p, quality=85)
        paths.append(p)
    return paths


def analyze(i):
    f = os.path.join(ROOT, i + ".mp4")
    sr = probe_sr(f)
    a = load_audio(f, sr)
    mono = a.mean(1)
    dur = len(mono) / sr
    mid = (a[:, 0] + a[:, 1]) / 2
    side = (a[:, 0] - a[:, 1]) / 2
    eb = ebur(f)
    S, hop = stft_mag(mono, sr)
    hop_s = hop / sr
    nfr = S.shape[0]
    freqs = np.fft.rfftfreq(2048, 1 / sr)
    # band energies (dB)
    band_db = []
    for nm, lo, hi in BANDS:
        m = (freqs >= lo) & (freqs < hi)
        band_db.append(db(np.sqrt((S[:, m] ** 2).sum(1)) / 40))
    band_db = np.array(band_db)  # 6 x frames
    # rms per frame
    idx = np.arange(2048)[None, :] + hop * np.arange(nfr)[:, None]
    fr = mono[idx]
    rms = np.sqrt((fr ** 2).mean(1))
    rms_db = db(rms)
    peak_db = db(np.abs(fr).max(1))
    fr_mid = mid[idx]; fr_side = side[idx]
    mid_e = (fr_mid ** 2).mean(1); side_e = (fr_side ** 2).mean(1)
    width = side_e / (mid_e + side_e + 1e-12)
    lc = a[:, 0][idx]; rc = a[:, 1][idx]
    corr = (lc * rc).mean(1) / (np.sqrt((lc ** 2).mean(1) * (rc ** 2).mean(1)) + 1e-12)
    # centroid
    mag = S + 1e-9
    centroid = (mag * freqs[None, :]).sum(1) / mag.sum(1)
    # spectral flux with log compression across 40 log bands
    edges = np.geomspace(40, min(16000, sr / 2 - 100), 41)
    lb = np.zeros((nfr, 40), np.float32)
    for b in range(40):
        m = (freqs >= edges[b]) & (freqs < edges[b + 1])
        if m.any():
            lb[:, b] = np.log1p(30 * S[:, m].mean(1))
    flux_b = np.maximum(0, np.diff(lb, axis=0, prepend=lb[:1]))
    flux = flux_b.sum(1)
    # onset detection
    fl = flux / (np.percentile(flux, 99) + 1e-9)
    from scipy.ndimage import uniform_filter1d, maximum_filter1d
    thr = uniform_filter1d(fl, size=int(0.5 / hop_s)) * 1.6 + 0.12
    pk = (fl > thr) & (fl >= maximum_filter1d(fl, size=int(0.06 / hop_s) | 1))
    on_idx = np.where(pk & (rms_db > -62))[0]
    onsets = []
    for k in on_idx:
        w0, w1 = max(0, k - 1), min(nfr, k + 4)
        bf = (flux_b[w0:w1].reshape(-1, 40)).sum(0)
        grp = [bf[:6].sum(), bf[6:12].sum(), bf[12:18].sum(), bf[18:26].sum(), bf[26:34].sum(), bf[34:].sum()]
        onsets.append((k * hop_s, float(min(1.0, fl[k])), int(np.argmax(grp))))
    # tempo via autocorrelation of onset envelope
    env = uniform_filter1d(flux, 3)
    env = env - env.mean()
    ac = np.correlate(env, env, "full")[len(env) - 1:]
    lag_lo, lag_hi = int(0.25 / hop_s), int(1.0 / hop_s)
    bpm = None; conf = None; cands = []
    if len(ac) > lag_hi + 2 and ac[0] > 0:
        seg = ac[lag_lo:lag_hi] / ac[0]
        order = np.argsort(-seg)
        taken = []
        for o in order:
            lg = lag_lo + o
            if all(abs(lg - t) > 0.1 * t for t in taken):
                taken.append(lg)
                cands.append((round(60 / (lg * hop_s), 1), round(float(seg[o]), 3)))
            if len(taken) >= 3:
                break
        bpm, conf = cands[0] if cands else (None, None)
    # onset regularity: coefficient of variation of inter-onset intervals
    ot = np.array([o[0] for o in onsets])
    ioi = np.diff(ot) if len(ot) > 3 else np.array([])
    ioi_cv = float(np.std(ioi) / (np.mean(ioi) + 1e-9)) if len(ioi) > 3 else None
    # chroma / key
    cb = (freqs > 60) & (freqs < 2000)
    pc = (np.round(12 * np.log2(freqs[cb] / 440.0) + 69).astype(int)) % 12
    chroma = np.zeros(12)
    spw = (S[:, cb] ** 2)
    loud = rms_db > -45
    if loud.sum() > 20:
        for c in range(12):
            chroma[c] = spw[loud][:, pc == c].sum()
        chroma /= chroma.sum() + 1e-12
        maj = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
        mnr = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
        names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        best = None
        for t in range(12):
            for nm, pr in (("major", maj), ("minor", mnr)):
                r = np.corrcoef(chroma, np.roll(pr, t))[0, 1]
                if best is None or r > best[0]:
                    best = (r, f"{names[t]} {nm}")
        key = {"key": best[1], "strength": round(float(best[0]), 3), "chroma_peak_ratio": round(float(chroma.max() / (chroma.mean() + 1e-9)), 2)}
    else:
        key = {"key": None, "strength": None}
    # speech-likelihood via 300-3400 band envelope modulation at 3-6Hz and harmonicity
    m_sp = (freqs >= 300) & (freqs < 3400)
    senv = np.sqrt((S[:, m_sp] ** 2).sum(1))
    # per-second analysis
    nsec = int(np.ceil(dur))
    fps_per = int(round(1 / hop_s))
    # resample to 16k for pitch
    x16 = mono[:: max(1, sr // 16000)] if sr % 16000 == 0 else np.interp(np.arange(0, len(mono), sr / 16000), np.arange(len(mono)), mono)
    sr16 = 16000
    hopp = 800  # 50ms
    N = 640
    f0s = []; voic = []
    for st in range(0, len(x16) - N, hopp):
        seg = x16[st: st + N] * np.hanning(N)
        if np.sqrt((seg ** 2).mean()) < 0.003:
            f0s.append(0); voic.append(0); continue
        A = np.fft.rfft(seg, 2 * N)
        r = np.fft.irfft(np.abs(A) ** 2)[:N]
        r = r / (r[0] + 1e-12)
        lo, hi = int(sr16 / 500), int(sr16 / 70)
        k = lo + int(np.argmax(r[lo:hi]))
        f0s.append(sr16 / k if r[k] > 0.35 else 0); voic.append(float(r[k]))
    f0s = np.array(f0s); voic = np.array(voic)
    # modulation energy: syllabic rate
    dvid, cuts = video_cuts(i)
    vfps = fps_of(f)
    cuts_t = [c / vfps for c in cuts]
    vdiff = dvid[:, 2]
    rows = []
    step = 0.5
    t = 0.0
    while t < dur:
        k0, k1 = int(t / hop_s), min(nfr, int((t + step) / hop_s))
        if k1 <= k0:
            break
        sl = slice(k0, k1)
        # modulation at syllabic rate in this 0.5s: use 2s context
        c0, c1 = max(0, int((t - 0.75) / hop_s)), min(nfr, int((t + 1.25) / hop_s))
        e = senv[c0:c1]
        e = e - e.mean()
        if len(e) > 50 and e.std() > 0:
            sp = np.abs(np.fft.rfft(e * np.hanning(len(e)))) ** 2
            fq = np.fft.rfftfreq(len(e), hop_s)
            tot = sp[(fq > 0.5) & (fq < 20)].sum() + 1e-9
            syl = sp[(fq >= 2.5) & (fq <= 7)].sum() / tot
        else:
            syl = 0.0
        p0, p1 = int(t / 0.05), int((t + step) / 0.05)
        ff = f0s[p0:p1]; vv = voic[p0:p1]
        vf = float((ff > 0).mean()) if len(ff) else 0
        f0m = float(np.median(ff[ff > 0])) if (ff > 0).any() else 0
        v0, v1 = int(t * vfps), min(len(vdiff), int((t + step) * vfps))
        vd = float(vdiff[v0:v1].mean()) if v1 > v0 else 0
        ncut = sum(1 for c in cuts_t if t <= c < t + step)
        non = sum(1 for o in onsets if t <= o[0] < t + step)
        rows.append({
            "t": round(t, 2), "rms_db": round(float(rms_db[sl].mean()), 1), "peak_db": round(float(peak_db[sl].max()), 1),
            "sub": round(float(band_db[0][sl].mean()), 1), "bass": round(float(band_db[1][sl].mean()), 1), "lowmid": round(float(band_db[2][sl].mean()), 1),
            "mid": round(float(band_db[3][sl].mean()), 1), "himid": round(float(band_db[4][sl].mean()), 1), "air": round(float(band_db[5][sl].mean()), 1),
            "centroid_hz": int(centroid[sl].mean()), "width": round(float(width[sl].mean()), 2), "corr": round(float(corr[sl].mean()), 2),
            "syl_mod": round(float(syl), 2), "voiced": round(vf, 2), "f0_hz": int(f0m), "onsets": non, "cuts": ncut, "vid_diff": round(vd, 1)})
        t += step
    # sweeps (risers/falls): look for 0.5-1.5 s spans with strong centroid slope while himid/air energy rises
    sweeps = []
    cen_s = uniform_filter1d(centroid.astype(np.float64), int(0.15 / hop_s) | 1)
    hi_s = uniform_filter1d((band_db[4] + band_db[5]) / 2, int(0.15 / hop_s) | 1)
    w = int(0.6 / hop_s)
    k = 0
    while k < nfr - w:
        dh = hi_s[k + w] - hi_s[k]
        dc = cen_s[k + w] - cen_s[k]
        if rms_db[k:k + w].mean() > -50 and abs(dh) > 9 and abs(dc) > 800:
            sweeps.append({"t": round(k * hop_s, 2), "dur": 0.6, "dir": "rise" if dh > 0 else "fall", "centroid_change_hz": int(dc), "hi_change_db": round(float(dh), 1)})
            k += w
        else:
            k += int(0.05 / hop_s)
    # silences
    sil = []
    cur = None
    for k in range(nfr):
        if rms_db[k] < -60:
            if cur is None:
                cur = k
        else:
            if cur is not None and (k - cur) * hop_s >= 0.2:
                sil.append([round(cur * hop_s, 2), round(k * hop_s, 2)])
            cur = None
    if cur is not None and (nfr - cur) * hop_s >= 0.2:
        sil.append([round(cur * hop_s, 2), round(nfr * hop_s, 2)])
    # sync: for each video cut, nearest onset
    sync = []
    for ct in cuts_t:
        if len(ot):
            j = int(np.argmin(np.abs(ot - ct)))
            sync.append(round(float(ot[j] - ct), 3))
    sync = np.array(sync)
    # sync of onsets-to-cuts when taking only strong onsets
    strong = np.array([o[0] for o in onsets if o[1] > 0.5])
    sync_strong = []
    for ct in cuts_t:
        if len(strong):
            j = int(np.argmin(np.abs(strong - ct)))
            sync_strong.append(float(strong[j] - ct))
    sync_strong = np.array(sync_strong)
    def pct_within(arr, w):
        return round(float((np.abs(arr) <= w).mean()), 2) if len(arr) else None
    # random baseline for sync: shift cuts by random offsets
    rng = np.random.RandomState(1)
    base = []
    for _ in range(200):
        shifted = np.sort((np.array(cuts_t) + rng.uniform(0.7, max(1.0, dur - 0.7))) % dur) if cuts_t else np.array([])
        if len(shifted) and len(ot):
            dd = np.array([np.min(np.abs(ot - s)) for s in shifted])
            base.append(float((dd <= 0.08).mean()))
    sync_info = {"n_cuts": len(cuts_t), "median_offset_s": round(float(np.median(sync)), 3) if len(sync) else None, "pct_cuts_with_onset_within_80ms": pct_within(sync, 0.08), "pct_within_40ms": pct_within(sync, 0.04), "chance_baseline_80ms": round(float(np.mean(base)), 2) if base else None,
                 "pct_cuts_with_STRONG_onset_within_80ms": pct_within(sync_strong, 0.08)}
    # section energy changes: find big moves in 1s smoothed rms
    sm = uniform_filter1d(rms_db, int(1.0 / hop_s))
    sections = []
    lastk = 0
    for k in range(int(2 / hop_s), nfr - int(2 / hop_s), int(0.25 / hop_s)):
        before = sm[k - int(1.5 / hop_s)]; after = sm[k + int(1.5 / hop_s)]
        if abs(after - before) > 9 and (not sections or k * hop_s - sections[-1]["t"] > 3):
            sections.append({"t": round(k * hop_s, 2), "change_db": round(float(after - before), 1)})
    # overall stats
    act = rms_db[rms_db > -60]
    avgbands = {nm: round(float(band_db[bi][rms_db > -60].mean()) if (rms_db > -60).any() else -120, 1) for bi, (nm, _, _) in enumerate(BANDS)}
    ons_per_s = len(onsets) / max(dur, 1e-6)
    summary = {
        "id": i, "duration_s": round(dur, 2), "sample_rate": sr, "channels": 2, **eb,
        "rms_mean_db": round(float(act.mean()), 1) if len(act) else None, "rms_p95_db": round(float(np.percentile(rms_db, 95)), 1), "rms_p10_db": round(float(np.percentile(rms_db, 10)), 1),
        "sample_peak_db": round(float(db(np.abs(a).max())), 1), "crest_db": round(float(db(np.abs(a).max()) - rms_db.mean()), 1) if len(rms_db) else None,
        "avg_band_db": avgbands, "centroid_mean_hz": int(centroid[rms_db > -60].mean()) if (rms_db > -60).any() else None,
        "stereo_side_fraction_mean": round(float(width[rms_db > -60].mean()), 3) if (rms_db > -60).any() else None, "stereo_corr_mean": round(float(corr[rms_db > -60].mean()), 3) if (rms_db > -60).any() else None,
        "onset_count": len(onsets), "onsets_per_s": round(ons_per_s, 2), "onset_ioi_cv": round(ioi_cv, 2) if ioi_cv else None,
        "tempo_candidates_bpm_conf": cands, "key_estimate": key, "silences_s": sil[:60], "silence_total_s": round(float(sum(b - a_ for a_, b in sil)), 2),
        "sections_by_loudness": sections[:60], "sweeps": sweeps[:60], "video_sync": sync_info, "voiced_fraction": round(float((f0s > 0).mean()), 2),
        "median_f0_hz": int(np.median(f0s[f0s > 0])) if (f0s > 0).any() else 0,
    }
    json.dump(summary, open(os.path.join(OUT, i + "_summary.json"), "w"), indent=1)
    with open(os.path.join(OUT, i + "_timeline.csv"), "w") as fo:
        keys = list(rows[0].keys())
        fo.write(",".join(keys) + "\n")
        for r in rows:
            fo.write(",".join(str(r[k]) for k in keys) + "\n")
    with open(os.path.join(OUT, i + "_onsets.csv"), "w") as fo:
        fo.write("t,strength,band\n")
        bn = ["sub-low", "bass-lowmid", "lowmid", "mid", "himid", "air"]
        for o in onsets:
            fo.write(f"{o[0]:.3f},{o[1]:.2f},{bn[o[2]]}\n")
    with open(os.path.join(OUT, i + "_cuts.csv"), "w") as fo:
        fo.write("t\n")
        for c in cuts_t:
            fo.write(f"{c:.3f}\n")
    S_db = db(S / 40)
    paths = render_spec(i, S_db, hop_s, rms_db, cuts_t, onsets, dur, sr)
    return i, len(paths), round(dur, 1)


if __name__ == "__main__":
    ids = sorted(os.path.basename(p)[:-4] for p in glob.glob(os.path.join(ROOT, "*.mp4")))
    if len(sys.argv) > 1:
        ids = sys.argv[1:]
    with ProcessPoolExecutor(max_workers=6) as ex:
        for r in ex.map(analyze, ids):
            print(r, flush=True)
