"""
Background watcher: auto-detects Zoom/Teams/Lark running on this laptop, records system audio
(loopback = what you hear, i.e. everyone on the call) + your mic while detected, then mixes and
hands the result to transcribe.py when the app closes. No cloud bot, nothing leaves this machine,
and it never depends on the meeting host sharing a recording.

CAVEAT — read before trusting this unattended: detection is by PROCESS NAME, not "actually in an
active call." Zoom/Teams/Lark can be running in the background with no meeting happening, and
this will start recording anyway. Watch the console log for unexpected start/stop lines during
your first few real uses before you leave this running unsupervised. If it misfires, Ctrl+C stops
it immediately and safely.

CAVEAT 2 — the Lark process name below (`lark.exe`) is an inferred best guess, not verified on
your machine. Confirm it before relying on this: open Task Manager during a Lark call → Details
tab → find Lark's row → check the exact "Name" column value → update MEETING_PROCESS_NAMES below
if it differs (e.g. some regions ship it as `feishu.exe`).

Usage: python watch_and_record.py     (leave the window open/minimized while you work)
Stop:  Ctrl+C — finishes and transcribes whatever's in progress, then exits.

Requires: psutil, soundcard, numpy, ffmpeg on PATH, faster-whisper. See setup.md.
"""

import subprocess
import sys
import time
import wave
import threading
import datetime
from pathlib import Path

import numpy as np
import psutil
import soundcard as sc

POLL_INTERVAL_SECONDS = 5
MEETING_PROCESS_NAMES = {"zoom.exe", "teams.exe", "ms-teams.exe", "lark.exe"}  # desktop apps only — browser-based Meet/Zoom-web is NOT detected. "lark.exe" unverified, see CAVEAT 2 above — some regions ship it as "feishu.exe"
SAMPLE_RATE = 16000

REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_ROOT / "scripts" / "transcribe" / "_raw_recordings"


def meeting_app_running() -> bool:
    for proc in psutil.process_iter(["name"]):
        if (proc.info.get("name") or "").lower() in MEETING_PROCESS_NAMES:
            return True
    return False


class LoopbackMicRecorder:
    """Records default speaker output (loopback, via WASAPI) and default mic in parallel threads."""

    def __init__(self):
        self._stop_event = threading.Event()
        self._mic_frames = []
        self._loop_frames = []
        self._threads = []

    def _record_loopback(self):
        speaker = sc.default_speaker()
        loopback_mic = sc.get_microphone(id=str(speaker.name), include_loopback=True)
        with loopback_mic.recorder(samplerate=SAMPLE_RATE) as rec:
            while not self._stop_event.is_set():
                self._loop_frames.append(rec.record(numframes=SAMPLE_RATE))

    def _record_mic(self):
        mic = sc.default_microphone()
        with mic.recorder(samplerate=SAMPLE_RATE) as rec:
            while not self._stop_event.is_set():
                self._mic_frames.append(rec.record(numframes=SAMPLE_RATE))

    def start(self):
        self._threads = [
            threading.Thread(target=self._record_loopback, daemon=True),
            threading.Thread(target=self._record_mic, daemon=True),
        ]
        for t in self._threads:
            t.start()

    def stop_and_save(self, loop_path: Path, mic_path: Path):
        self._stop_event.set()
        for t in self._threads:
            t.join(timeout=5)
        _write_wav(loop_path, self._loop_frames)
        _write_wav(mic_path, self._mic_frames)


def _write_wav(path: Path, frames: list) -> None:
    if not frames:
        return
    audio = np.concatenate(frames, axis=0)
    audio_int16 = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    channels = audio_int16.shape[1] if audio_int16.ndim > 1 else 1
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_int16.tobytes())


def mix_and_transcribe(loop_path: Path, mic_path: Path, meeting_name: str) -> None:
    if not loop_path.exists() and not mic_path.exists():
        print("No audio captured (recording was too short) — skipping.")
        return
    mixed_path = loop_path.with_name(loop_path.stem.replace("-loopback", "-mixed") + ".wav")
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", str(loop_path), "-i", str(mic_path),
            "-filter_complex", "amix=inputs=2:duration=longest:dropout_transition=0",
            str(mixed_path),
        ],
        check=True,
    )
    transcribe_script = Path(__file__).resolve().parent / "transcribe.py"
    subprocess.run([sys.executable, str(transcribe_script), str(mixed_path), meeting_name], check=True)
    print(f"Raw recordings kept at {loop_path.parent} — delete once the transcript is confirmed good (see setup.md).")


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Watching for {sorted(MEETING_PROCESS_NAMES)} every {POLL_INTERVAL_SECONDS}s. Ctrl+C to stop.")
    recording = False
    recorder = None
    loop_path = mic_path = None

    try:
        while True:
            running = meeting_app_running()
            if running and not recording:
                ts = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
                loop_path = RAW_DIR / f"{ts}-loopback.wav"
                mic_path = RAW_DIR / f"{ts}-mic.wav"
                print(f"[{ts}] Meeting app detected — recording started.")
                recorder = LoopbackMicRecorder()
                recorder.start()
                recording = True
            elif not running and recording:
                ts = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
                print(f"[{ts}] Meeting app closed — recording stopped, transcribing...")
                recorder.stop_and_save(loop_path, mic_path)
                mix_and_transcribe(loop_path, mic_path, meeting_name=f"auto-meeting-{ts}")
                recording = False
                recorder = None
            time.sleep(POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nStopped by user.")
        if recording and recorder:
            ts = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
            print("Finishing in-progress recording before exit...")
            recorder.stop_and_save(loop_path, mic_path)
            mix_and_transcribe(loop_path, mic_path, meeting_name=f"auto-meeting-{ts}")


if __name__ == "__main__":
    main()
