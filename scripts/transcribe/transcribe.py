"""
Local meeting transcription -> inbox/transcripts/YYYY-MM-DD-<meeting-name>.md

Usage:
    python transcribe.py <audio-file> [meeting-name]

Requires: faster-whisper, ffmpeg on PATH. See setup.md.
Everything runs locally; no audio or transcript is sent anywhere.
"""

import sys
import datetime
from pathlib import Path

MODEL_SIZE = "large-v3"  # switch to "medium" for a faster, less accurate fallback
LOW_CONFIDENCE_LOGPROB_THRESHOLD = -1.0  # faster-whisper avg_logprob below this = flagged

REPO_ROOT = Path(__file__).resolve().parents[2]
TRANSCRIPTS_DIR = REPO_ROOT / "inbox" / "transcripts"


def format_timestamp(seconds: float) -> str:
    td = datetime.timedelta(seconds=int(seconds))
    return str(td) if td >= datetime.timedelta(hours=1) else f"00:{str(td)}"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio-file> [meeting-name]")
        sys.exit(1)

    audio_path = Path(sys.argv[1]).expanduser().resolve()
    if not audio_path.exists():
        print(f"Audio file not found: {audio_path}")
        sys.exit(1)

    meeting_name = sys.argv[2] if len(sys.argv) > 2 else audio_path.stem
    meeting_name_slug = meeting_name.strip().replace(" ", "-").lower()

    from faster_whisper import WhisperModel

    print(f"Loading model '{MODEL_SIZE}' (first run downloads it — this can take a while)...")
    model = WhisperModel(MODEL_SIZE, device="auto", compute_type="auto")

    print(f"Transcribing {audio_path.name} (language auto-detect)...")
    segments, info = model.transcribe(str(audio_path), language=None, vad_filter=True)

    lines = []
    low_confidence = []
    for seg in segments:
        ts = format_timestamp(seg.start)
        text = seg.text.strip()
        lines.append(f"[{ts}] {text}")
        if seg.avg_logprob < LOW_CONFIDENCE_LOGPROB_THRESHOLD:
            low_confidence.append(f"[{ts}] {text}")

    today = datetime.date.today().isoformat()
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = TRANSCRIPTS_DIR / f"{today}-{meeting_name_slug}.md"

    frontmatter = (
        "---\n"
        f"date: {today}\n"
        f"meeting_name: {meeting_name}\n"
        "attendees: UNKNOWN\n"
        f"detected_language: {info.language}\n"
        f"source_audio: {audio_path.name}\n"
        "---\n\n"
    )

    body = f"# {meeting_name} — {today}\n\n" + "\n".join(lines) + "\n"

    footer = "\n## Low-confidence segments (verify before treating as ground truth)\n"
    footer += "\n".join(f"- {line}" for line in low_confidence) if low_confidence else "- None flagged."

    out_path.write_text(frontmatter + body + footer, encoding="utf-8")
    print(f"Wrote {out_path}")
    print("Reminder: delete the source audio once this transcript is confirmed good (see setup.md).")


if __name__ == "__main__":
    main()
