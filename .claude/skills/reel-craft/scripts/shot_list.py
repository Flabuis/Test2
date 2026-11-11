"""Turn frames_data/*.csv into frames_data/EVENTS.txt: per-reel shot list with cut detection, brightness, motion, stillness."""
import glob,os,numpy as np
os.chdir(os.environ.get("REEL_DIR", os.getcwd()))
import subprocess
def fps(f):
    a,b=subprocess.check_output(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=r_frame_rate","-of","csv=p=0",f]).decode().split()[0].strip(",").split("/");return float(a)/float(b)
out=[]
for c in sorted(glob.glob("frames_data/*.csv")):
    i=os.path.basename(c)[:-4];F=fps(i+".mp4")
    d=np.loadtxt(c,delimiter=",",skiprows=1);n=len(d)
    diff=d[:,2];luma=d[:,1];sx=d[:,3];sy=d[:,4];corr=d[:,5];z=d[:,6]
    med=np.median(diff[1:])+1e-6
    cuts=[k for k in range(2,n) if diff[k]>max(14,6*med) and diff[k]>1.8*max(diff[k-1],1e-6)]
    # merge cuts closer than 3 frames
    m=[]
    for k in cuts:
        if not m or k-m[-1]>3:m.append(k)
    bounds=[0]+m+[n]
    lines=[f"## {i}  frames={n} fps={F:.0f} dur={n/F:.1f}s median_diff={med:.2f} shots={len(bounds)-1}"]
    for s,e in zip(bounds[:-1],bounds[1:]):
        seg=slice(s+1,e) if e-s>2 else slice(s,e)
        L=luma[seg];dd=diff[seg];ok=corr[seg]>0.12
        mx=np.median(sx[seg][ok]) if ok.any() else 0;my=np.median(sy[seg][ok]) if ok.any() else 0
        zz=np.median(z[seg]);still=(dd<0.8).mean()
        mv=[]
        if abs(mx)>=0.5 or abs(my)>=0.5:mv.append(f"drift({mx:+.1f},{my:+.1f})px/f")
        if zz>1.005:mv.append(f"zoom-in x{zz:.3f}/f")
        elif zz<0.995:mv.append(f"zoom-out x{zz:.3f}/f")
        fade="fade-up" if len(L)>6 and L[-3:].mean()-L[:3].mean()>25 else ("fade-down" if len(L)>6 and L[:3].mean()-L[-3:].mean()>25 else "")
        lines.append(f"  {s/F:6.2f}-{e/F:6.2f}s ({e-s:3d}f) luma {L.mean():5.1f} avgD {dd.mean():5.2f} still {still*100:3.0f}% {' '.join(mv)} {fade}")
    out+=lines
open("frames_data/EVENTS.txt","w",encoding="utf-8").write("\n".join(out));print(len(out))
