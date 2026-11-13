#!/usr/bin/env bash
# Том 7 (финал): голос + звук в финальный ролик. Особое интро 18 с, история 420 с, особое аутро 10 с.
# Сначала: node ../render.js ep07 (из папки mandela) и python3 sfx.py
set -euo pipefail
cd "$(dirname "$0")"
INTRO=18; T=448
[ -f vo/voice.wav ] && [ "${REVOICE:-0}" = 0 ] || python3 ../common/voice.py . $INTRO $T
ffmpeg -loglevel error -y -i ep07.mp4 -i sfx.wav -i vo/voice.wav -filter_complex \
 "[1:a]volume=0.8[bed];[2:a]loudnorm=I=-17:TP=-2,asplit=2[vo][sc];[bed][sc]sidechaincompress=threshold=0.03:ratio=4:attack=15:release=300[duck];[duck][vo]amix=inputs=2:normalize=0,alimiter=limit=0.89,loudnorm=I=-16:TP=-1.5,afade=t=out:st=$((T-2)):d=2[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 44100 -t $T ep07-ozvuchka.mp4
echo done
