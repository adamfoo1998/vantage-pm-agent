# Local Transcription Setup (Windows)

Goal: turn a recorded meeting into a transcript in `inbox/transcripts/`, entirely on your PC —
no audio or transcript ever leaves the machine.

## Recommended path: faster-whisper

Faster on Windows than whisper.cpp for most setups, and easier to install if you're comfortable
with Python.

1. Install Python 3.10+ if you don't have it (winget: `winget install Python.Python.3.12`).
2. Install ffmpeg: `winget install Gyan.FFmpeg` (needed to decode m4a/mp3/mp4 audio).
3. Install faster-whisper: `pip install faster-whisper`.
4. Run a transcription: `python transcribe.py "path\to\recording.m4a" "meeting-name"` — or just
   drag the audio file onto `transcribe.ps1`.

**Model choice:**
- `large-v3` (recommended) — best accuracy for Mandarin/English code-switching, which is normal
  in these meetings. First run downloads ~3GB; runs are slow on CPU-only (roughly 3-6x real-time,
  i.e. a 1-hour meeting can take 3-6 hours on CPU) but fast on a CUDA GPU (roughly 0.1-0.3x
  real-time, i.e. a 1-hour meeting in 6-18 minutes).
- `medium` (fast fallback) — ~1.5GB download, noticeably faster on CPU (roughly 1-2x real-time)
  at some accuracy cost, especially on code-switched speech. Use this if `large-v3` is too slow
  for your machine.

Edit the `MODEL_SIZE` constant at the top of `transcribe.py` to switch between them.

## Alternative path: whisper.cpp (CPU-only, no Python)

If you'd rather not install Python, or you're on a CPU-only machine and want a leaner runtime:
1. Download a prebuilt Windows release from the whisper.cpp GitHub releases page.
2. Download a GGML model file (e.g. `ggml-large-v3.bin` or the smaller `ggml-medium.bin`) from
   the whisper.cpp model repo.
3. Run `whisper-cli.exe -m ggml-large-v3.bin -f recording.wav -l auto --output-txt`.
This path is not wired into `transcribe.py`/`transcribe.ps1` (those assume faster-whisper) — treat
it as a manual fallback if the Python path doesn't work on your machine.

## Privacy rules (non-negotiable)

- `inbox/` and all audio/video source files are git-ignored — see repo-root `.gitignore`
  (`inbox/`, `*.wav`, `*.m4a`, `*.mp3`, `*.mp4`). Never remove these entries.
- Transcripts containing client data never leave this machine — no pasting into external tools,
  no cloud transcription services.
- **Delete the source audio file once its transcript has been confirmed good** (i.e. after
  `meeting-synthesis` has processed it, or you've manually checked it reads correctly). Don't let
  raw recordings accumulate.

## Output

`transcribe.py` writes `inbox/transcripts/YYYY-MM-DD-<meeting-name>.md` with:
- Frontmatter: `date`, `meeting_name`, `attendees: UNKNOWN` (placeholder — filled in later by
  `meeting-synthesis` matching speakers against `vault/people/`, or manually).
- A timestamped transcript body (`[HH:MM:SS] text`).
- A footer listing any segment faster-whisper flagged low-confidence, so you know what to
  double-check before treating the transcript as ground truth.

Language auto-detection is on — meetings mixing English and 中文 are expected and handled per
segment, not forced to one language for the whole file.
