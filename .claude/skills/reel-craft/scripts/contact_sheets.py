"""Build labelled contact sheets in dense/: ~5 fps grids plus every-frame windows around the 10 biggest picture changes. Needs frames_data/ first."""
import subprocess,glob,os,shutil,numpy as np
from PIL import Image,ImageDraw
os.chdir(os.environ.get("REEL_DIR", os.getcwd()))
OUT="dense";os.makedirs(OUT,exist_ok=True);TMP="tmp_frames"
def info(f):
    o=subprocess.check_output(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height,r_frame_rate","-of","csv=p=0",f]).decode().split()[0].strip(",").split(",")
    a,b=o[2].split("/");return int(o[0]),int(o[1]),float(a)/float(b)
def grab(f,fps,sel,W):
    shutil.rmtree(TMP,ignore_errors=True);os.makedirs(TMP)
    subprocess.run(["ffmpeg","-v","error","-i",f,"-vf",f"select='{sel}',scale={W}:-2","-fps_mode","passthrough",f"{TMP}/%05d.jpg"])
    return sorted(glob.glob(TMP+"/*.jpg"))
def sheet(paths,labels,cols,name):
    ims=[Image.open(p) for p in paths];w,h=ims[0].size;rows=(len(ims)+cols-1)//cols
    S=Image.new("RGB",(cols*w,rows*h),(0,0,0))
    for k,(im,l) in enumerate(zip(ims,labels)):
        x,y=(k%cols)*w,(k//cols)*h;S.paste(im,(x,y));d=ImageDraw.Draw(S);d.rectangle([x,y,x+78,y+12],fill=(0,0,0));d.text((x+2,y+1),l,fill=(255,255,0))
    S.save(name,quality=82)
for f in sorted(glob.glob("*.mp4")):
    i=f[:-4];w,h,fps=info(f);d=np.loadtxt(f"frames_data/{i}.csv",delimiter=",",skiprows=1);n=len(d);dur=n/fps
    rate=5 if dur<=40 else 3 if dur<=110 else 1.5
    step=max(1,round(fps/rate));W=200 if h>w else 260 if h==w else 280
    cols=9 if h>w else 7 if h==w else 6
    per=cols*4 if h>w else cols*4
    paths=grab(f,fps,f"not(mod(n\\,{step}))",W);idx=[k*step for k in range(len(paths))]
    for s in range(0,len(paths),per):
        sheet(paths[s:s+per],[f"{k/fps:.2f}s f{k}" for k in idx[s:s+per]],cols,f"{OUT}/{i}_s{s//per+1:02d}.jpg")
    # transition windows: top diff spikes
    diff=d[:,2];peaks=[]
    for k in np.argsort(-diff):
        if k<2 or k>n-3:continue
        if all(abs(k-p)>10 for p in peaks):peaks.append(int(k))
        if len(peaks)>=10:break
    peaks.sort()
    if peaks and diff[peaks].max()>12:
        sel="+".join(f"between(n\\,{max(0,p-4)}\\,{p+4})" for p in peaks)
        tp=grab(f,fps,sel,150 if h>w else 190);lab=[]
        for p in peaks:lab+= [f"f{k} {k/fps:.2f}s" for k in range(max(0,p-4),p+5) if k<n]
        tp=tp[:len(lab)]
        for s in range(0,len(tp),9*5):
            sheet(tp[s:s+45],lab[s:s+45],9,f"{OUT}/{i}_T{s//45+1:02d}.jpg")
    print(i,len(paths),flush=True)
shutil.rmtree(TMP,ignore_errors=True)
