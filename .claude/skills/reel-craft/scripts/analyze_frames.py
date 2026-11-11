"""Measure every frame of every *.mp4 in REEL_DIR (default: cwd): brightness, frame-to-frame change, shift, zoom, mean colour.
Writes frames_data/<id>.csv. Needs ffmpeg, numpy."""
import subprocess,glob,os,json,sys
import numpy as np
os.chdir(os.environ.get("REEL_DIR", os.getcwd()))
os.makedirs("frames_data", exist_ok=True)
def probe(f):
    o=subprocess.check_output(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height,r_frame_rate","-of","csv=p=0",f]).decode().strip().split(",")
    w,h=int(o[0]),int(o[1]); a,b=o[2].split("/"); return w,h,float(a)/float(b)
def frames(f,W=128):
    w,h,fps=probe(f); H=int(round(W*h/w/2)*2)
    p=subprocess.Popen(["ffmpeg","-v","error","-i",f,"-vf",f"scale={W}:{H}","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
    n=W*H*3
    while True:
        b=p.stdout.read(n)
        if len(b)<n: break
        yield np.frombuffer(b,np.uint8).reshape(H,W,3)
def shift(a,b):
    A=np.fft.fft2(a);B=np.fft.fft2(b);R=A*np.conj(B);R/=np.abs(R)+1e-9
    r=np.fft.ifft2(R).real;y,x=np.unravel_index(np.argmax(r),r.shape)
    if y>a.shape[0]//2:y-=a.shape[0]
    if x>a.shape[1]//2:x-=a.shape[1]
    return x,y,r.max()
def zoom(a,b):
    # estimate scale of b relative to a via center-crop comparison
    H,W=a.shape;best=(1.0,1e9)
    for s in (0.94,0.97,1.0,1.03,1.06):
        ch,cw=int(H*0.6),int(W*0.6);y0,x0=(H-ch)//2,(W-cw)//2
        crop=a[y0:y0+ch,x0:x0+cw]
        # sample b around center scaled by s
        ys=(np.arange(ch)-ch/2)/s+H/2;xs=(np.arange(cw)-cw/2)/s+W/2
        ys=np.clip(ys.round().astype(int),0,H-1);xs=np.clip(xs.round().astype(int),0,W-1)
        e=np.abs(crop-b[np.ix_(ys,xs)]).mean()
        if e<best[1]:best=(s,e)
    return best[0]
for f in sorted(glob.glob("*.mp4")):
    i=f[:-4]; w,h,fps=probe(f); rows=[];prev=None;pg=None
    for k,fr in enumerate(frames(f)):
        g=fr.astype(np.float32).mean(2)
        if prev is None: rows.append([k,float(g.mean()),0,0,0,0,1.0,*fr.reshape(-1,3).mean(0)])
        else:
            d=float(np.abs(g-pg).mean()); x,y,c=shift(g,pg); z=zoom(pg,g)
            rows.append([k,float(g.mean()),d,x,y,float(c),z,*fr.reshape(-1,3).mean(0)])
        prev=fr;pg=g
    np.savetxt(f"frames_data/{i}.csv",np.array(rows),delimiter=",",header="frame,luma,diff,sx,sy,corr,zoom,r,g,b",fmt="%.3f")
    print(i,len(rows),fps,flush=True)
