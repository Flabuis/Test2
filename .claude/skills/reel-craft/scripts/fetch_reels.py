"""Download public reels with yt-dlp into REEL_DIR (default: cwd), one mp4 per reel, named by shortcode.
Usage: python fetch_reels.py <url-or-shortcode> [...]
Needs: pip install yt-dlp. Some reels return 'empty media response' without login cookies; those need --cookies-from-browser."""
import os, re, subprocess, sys
out = os.environ.get("REEL_DIR", os.getcwd())
for a in sys.argv[1:]:
    m = re.search(r"/(?:reel|p)/([A-Za-z0-9_-]+)", a)
    code = m.group(1) if m else a
    url = f"https://www.instagram.com/reel/{code}/"
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "-q", "--no-progress", "-o", os.path.join(out, "%(id)s.%(ext)s"), "-f", "mp4/best", url])
    print(code, "ok" if r.returncode == 0 else "FAILED")
