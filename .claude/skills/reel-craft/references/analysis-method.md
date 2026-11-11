# Analysis method: studying new reels

How the 30-reel study was made, so it can be repeated on new references. The scripts are in `../scripts/` and read and write the folder named by the `REEL_DIR` environment variable (default: current directory). Needs Python 3 with numpy, scipy and pillow, ffmpeg and ffprobe, and `yt-dlp` for downloads (`pip install yt-dlp`).

## Pipeline (run in this order)
| Step | Command | Output |
|---|---|---|
| 1. Fetch | `python scripts/fetch_reels.py <url or shortcode> ...` | `<id>.mp4` per reel. Some reels fail with "empty media response" and need browser cookies. |
| 2. Measure every frame | `python scripts/analyze_frames.py` | `frames_data/<id>.csv`: per frame luma, frame-to-frame change, sideways and vertical shift, zoom, mean RGB (frames decoded at 128 px wide). |
| 3. Shot list | `python scripts/shot_list.py` | `frames_data/EVENTS.txt`: shots, cut times, mean change, stillness, drift and zoom flags, fade flags. |
| 4. Contact sheets | `python scripts/contact_sheets.py` | `dense/<id>_sNN.jpg` (about 5 fps, labelled with time and frame) and `dense/<id>_TNN.jpg` (every frame around the ten biggest changes). |
| 5. Audio | `python scripts/analyze_audio.py [id ...]` | `audio/<id>_summary.json`, `_timeline.csv` (per 0.5 s), `_onsets.csv`, `_cuts.csv`, and `audio/spec/<id>_NN.jpg` spectrograms (30 s each, cuts and onsets marked). |

## Reading the results
- Look at every contact sheet for the reel, a few at a time (large batches of images can be dropped by the image limit). Write a timeline table per reel: time, what changes frame to frame, how it is built.
- Cut times are detected from picture change, so flashes and fades can show up as cuts; check against the sheets.
- Audio claims come only from measurements and spectrograms: loudness (ebur128), band energy, onsets, tempo candidates (check whether candidates are harmonics of each other), key (only trust above about 0.7 correlation on tonal music), pitch and syllabic-rate evidence for speech, sweeps, silences, and the share of cuts with an onset within 80 ms against a chance baseline. Sync only counts when it clearly beats the baseline, and very few cuts make the figure meaningless.
- Lens and focal length are estimates from the picture (perspective, depth of field), never read from metadata.
- Do not transcribe lyrics or speech; describe type animation, delivery rhythm and pitch range.

## Limits of the original study
- 30 of 32 links worked; two returned empty media.
- Picture was viewed at about 5 fps plus every frame around the biggest cuts, while measurement covered every frame. One 6-minute reel was only viewed in 7 of its 26 sheets.
- Audio was never listened to; instruments and effect types are inferred from spectrograms.
- One platform, one season, 30 reels.

## Where the original data is
`C:\Users\basha\Motion Design\Training Data\Instagram Refs\`: `DETAIL-batch-01.md` (frame-by-frame notes), `STUDY-batch-01.md` (quick pass), `meta.md`, `frames_data/`, `dense/`, `audio/` (including `SOUND-STUDY-batch-01.md` and `audio/parts/<id>.md`), and the mp4s. A new batch goes in the same folder as `DETAIL-batch-02.md` and `audio/SOUND-STUDY-batch-02.md`.
