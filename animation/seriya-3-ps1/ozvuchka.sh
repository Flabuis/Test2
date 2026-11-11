#!/usr/bin/env bash
# Серия 3: закадр RHVoice (aleksandr-hq, строки N) + реплики мужика (pavel, строки G) + sfx3.wav.
# Темп каждой фразы подгоняется под окно её субтитра (не быстрее x1.3).
# Нужно: apt-get install rhvoice rhvoice-russian; сначала python3 sfx3.py и node render.js
set -euo pipefail
cd "$(dirname "$0")/vo"
D=60; inputs=""; filt=""; i=0
while IFS=$'\t' read -r a b who s; do
  i=$((i+1)); f=$(printf "l%02d.wav" $i)
  if [ "$who" = G ]; then echo "$s" | RHVoice-test -p pavel -r 115 -t 125 -o "$f" 2>/dev/null; fx=",volume=1.25,aecho=0.8:0.5:90:0.25"
  else echo "$s" | RHVoice-test -p aleksandr-hq -o "$f" 2>/dev/null; fx=""; fi
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  tempo=$(echo "t=$dur/($b-$a); if(t<1)t=1; if(t>1.3)t=1.3; t" | bc -l)
  ms=$(echo "$a*1000/1" | bc)
  inputs="$inputs -i $f"
  filt="$filt[$((i-1)):a]aresample=44100,atempo=$tempo,silenceremove=start_periods=1:start_threshold=-45dB$fx,adelay=${ms}|${ms},apad=whole_dur=$D[v$i];"
  printf "%2d %s tempo=%.2f %s\n" $i $who $tempo "$s"
done < lines.tsv
mix=""; for k in $(seq 1 $i); do mix="$mix[v$k]"; done
ffmpeg -loglevel error -y $inputs -filter_complex "${filt}${mix}amix=inputs=$i:normalize=0,apad=whole_dur=$D,lowpass=f=9000,aformat=channel_layouts=stereo,atrim=0:$D[out]" -map "[out]" voice.wav
cd ..
ffmpeg -loglevel error -y -i seriya-3-ps1.mp4 -i sfx3.wav -i vo/voice.wav -filter_complex \
 "[1:a]acompressor=threshold=-24dB:ratio=4:attack=5:release=120,volume=0.55[bed];[2:a]loudnorm=I=-16:TP=-2,asplit=2[vo][sc];[bed][sc]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=350[duck];[duck][vo]amix=inputs=2:normalize=0,alimiter=limit=0.89,loudnorm=I=-15:TP=-1.5,afade=t=out:st=56.4:d=3.4[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 44100 -t $D seriya-3-ps1-ozvuchka.mp4
echo done
