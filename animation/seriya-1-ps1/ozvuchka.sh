#!/usr/bin/env bash
# Озвучка RHVoice (голос aleksandr-hq) + сведение с sfx.wav.
# Нужно: apt-get install rhvoice rhvoice-russian; сначала python3 sfx.py
set -euo pipefail
cd "$(dirname "$0")/vo"
inputs=""; filt=""; i=0
while IFS=$'\t' read -r a b s; do
  i=$((i+1)); f=$(printf "l%02d.wav" $i)
  echo "$s" | RHVoice-test -p aleksandr-hq -o "$f" 2>/dev/null
  tempo=1.0; [ $i -eq 7 ] && tempo=1.2; [ $i -eq 8 ] && tempo=1.15   # не влезают в окно субтитра
  ms=$(echo "$a*1000/1" | bc)
  inputs="$inputs -i $f"
  filt="$filt[$((i-1)):a]aresample=44100,atempo=$tempo,silenceremove=start_periods=1:start_threshold=-45dB,adelay=${ms}|${ms},apad=whole_dur=58[v$i];"
done < lines.tsv
mix=""; for k in $(seq 1 $i); do mix="$mix[v$k]"; done
ffmpeg -loglevel error -y $inputs -filter_complex "${filt}${mix}amix=inputs=$i:normalize=0,lowpass=f=9000,aformat=channel_layouts=stereo,atrim=0:58[out]" -map "[out]" voice.wav
cd ..
ffmpeg -loglevel error -y -i seriya-1-ps1.mp4 -i sfx.wav -i vo/voice.wav -filter_complex \
 "[1:a]acompressor=threshold=-24dB:ratio=4:attack=5:release=120,volume=0.55[bed];[2:a]loudnorm=I=-16:TP=-2,asplit=2[vo][sc];[bed][sc]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=350[duck];[duck][vo]amix=inputs=2:normalize=0,alimiter=limit=0.89,loudnorm=I=-15:TP=-1.5[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 44100 -shortest seriya-1-ps1-ozvuchka.mp4
echo done
