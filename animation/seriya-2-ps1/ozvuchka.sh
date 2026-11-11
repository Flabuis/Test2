#!/usr/bin/env bash
# Серия 2: закадр RHVoice (aleksandr-hq) + реплика мужика (pavel, выше и быстрее, с эхом) + sfx2.wav.
# Нужно: apt-get install rhvoice rhvoice-russian; сначала python3 sfx2.py и node render.js
set -euo pipefail
cd "$(dirname "$0")/vo"
declare -A TEMPO=([7]=1.22 [9]=1.06 [11]=1.06 [12]=1.08)
inputs=""; filt=""; i=0
while IFS=$'\t' read -r a b s; do
  i=$((i+1)); f=$(printf "l%02d.wav" $i)
  echo "$s" | RHVoice-test -p aleksandr-hq -o "$f" 2>/dev/null
  tempo=${TEMPO[$i]:-1.0}; ms=$(echo "$a*1000/1" | bc)
  inputs="$inputs -i $f"
  filt="$filt[$((i-1)):a]aresample=44100,atempo=$tempo,silenceremove=start_periods=1:start_threshold=-45dB,adelay=${ms}|${ms},apad=whole_dur=60[v$i];"
done < lines.tsv
echo "О нет! Мой дом! Всё пропало!" | RHVoice-test -p pavel -r 125 -t 125 -o meme.wav 2>/dev/null
inputs="$inputs -i meme.wav"
filt="$filt[$i:a]aresample=44100,silenceremove=start_periods=1:start_threshold=-45dB,volume=1.3,aecho=0.8:0.6:180|360:0.35|0.2,adelay=22650|22650,apad=whole_dur=60[v$((i+1))];"
mix=""; for k in $(seq 1 $((i+1))); do mix="$mix[v$k]"; done
ffmpeg -loglevel error -y $inputs -filter_complex "${filt}${mix}amix=inputs=$((i+1)):normalize=0,apad=whole_dur=60,lowpass=f=9000,aformat=channel_layouts=stereo,atrim=0:60[out]" -map "[out]" voice.wav
cd ..
ffmpeg -loglevel error -y -i seriya-2-ps1.mp4 -i sfx2.wav -i vo/voice.wav -filter_complex \
 "[1:a]acompressor=threshold=-24dB:ratio=4:attack=5:release=120,volume=0.55[bed];[2:a]loudnorm=I=-16:TP=-2,asplit=2[vo][sc];[bed][sc]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=350[duck];[duck][vo]amix=inputs=2:normalize=0,alimiter=limit=0.89,loudnorm=I=-15:TP=-1.5[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 44100 -t 60 seriya-2-ps1-ozvuchka.mp4
echo done
