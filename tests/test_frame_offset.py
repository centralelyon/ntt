import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
import pytest

from ntt.videos.exif import extract_metadata_ffprobe
from ntt.videos.frame_offset import split_video_at_frame_offset
from ntt.videos.io import write_video


ROOT = Path(__file__).resolve().parents[1]
FFMPEG_TOOLS_AVAILABLE = (
    shutil.which("ffmpeg") is not None and shutil.which("ffprobe") is not None
)


def _make_frame_sequence(frame_count: int = 8) -> list:
    frames = []
    for index in range(frame_count):
        frame = np.full((48, 64, 3), index * 20, dtype=np.uint8)
        frame[:, :, 1] = index * 10
        frames.append(frame)
    return frames


def _read_first_frame(video_path: Path) -> np.ndarray:
    cap = cv2.VideoCapture(str(video_path))
    ok, frame = cap.read()
    cap.release()
    if not ok:
        raise AssertionError(f"Could not read first frame from {video_path}")
    return frame


def _frame_count(video_path: Path) -> int:
    cap = cv2.VideoCapture(str(video_path))
    count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return count


@pytest.mark.skipif(not FFMPEG_TOOLS_AVAILABLE, reason="ffmpeg/ffprobe is not installed")
def test_split_video_at_frame_offset_creates_offset_and_synced_outputs(tmp_path):
    input_path = tmp_path / "input.avi"
    frames = _make_frame_sequence(frame_count=8)
    write_video(str(input_path), frames, fps=4)

    result = split_video_at_frame_offset(str(input_path), frame_offset=3)

    offset_path = Path(result["offset_path"])
    synced_path = Path(result["synced_path"])
    assert input_path.is_file()
    assert offset_path.is_file()
    assert synced_path.is_file()
    assert _frame_count(input_path) == 8
    assert _frame_count(offset_path) == 3
    assert _frame_count(synced_path) == 5

    synced_first_frame = _read_first_frame(synced_path)
    expected_mean = float(frames[3].mean())
    assert float(synced_first_frame.mean()) == pytest.approx(expected_mean, abs=8.0)

    input_meta = extract_metadata_ffprobe(str(input_path))
    offset_meta = extract_metadata_ffprobe(str(offset_path))
    synced_meta = extract_metadata_ffprobe(str(synced_path))
    assert offset_meta["codec"] == input_meta["codec"]
    assert synced_meta["codec"] == input_meta["codec"]


@pytest.mark.skipif(not FFMPEG_TOOLS_AVAILABLE, reason="ffmpeg/ffprobe is not installed")
def test_split_video_at_frame_offset_can_remove_duration_using_video_fps(tmp_path):
    input_path = tmp_path / "input.avi"
    frames = _make_frame_sequence(frame_count=8)
    write_video(str(input_path), frames, fps=4)

    result = split_video_at_frame_offset(str(input_path), remove_duration_s=0.74)

    offset_path = Path(result["offset_path"])
    synced_path = Path(result["synced_path"])
    assert offset_path.is_file()
    assert synced_path.is_file()
    assert result["frame_offset"] == 3
    assert result["requested_remove_duration_s"] == pytest.approx(0.74)
    assert result["split_time_s"] == pytest.approx(0.75)
    assert _frame_count(offset_path) == 3
    assert _frame_count(synced_path) == 5

    synced_first_frame = _read_first_frame(synced_path)
    expected_mean = float(frames[3].mean())
    assert float(synced_first_frame.mean()) == pytest.approx(expected_mean, abs=8.0)


@pytest.mark.skipif(not FFMPEG_TOOLS_AVAILABLE, reason="ffmpeg/ffprobe is not installed")
def test_split_video_at_frame_offset_script(tmp_path):
    input_path = tmp_path / "input.avi"
    write_video(str(input_path), _make_frame_sequence(frame_count=6), fps=3)

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "split_video_at_frame_offset.py"),
            str(input_path),
            "2",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    assert (tmp_path / "input_offset.avi").is_file()
    assert (tmp_path / "input_synced.avi").is_file()
    assert "Step 1/4: validate inputs" in result.stdout
    assert "Step 2/4: prepare output files" in result.stdout
    assert "Step 3/4: split video with ffmpeg" in result.stdout
    assert "Step 4/4: done" in result.stdout
    assert "Source video left unchanged" in result.stdout
    assert "Saved offset clip" in result.stdout
    assert "Saved synced clip" in result.stdout


@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg is not installed")
def test_split_video_at_frame_offset_script_accepts_duration_option(tmp_path):
    input_path = tmp_path / "input.avi"
    write_video(str(input_path), _make_frame_sequence(frame_count=6), fps=4)

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "split_video_at_frame_offset.py"),
            str(input_path),
            "--remove-duration-s",
            "0.74",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    assert (tmp_path / "input_offset.avi").is_file()
    assert (tmp_path / "input_synced.avi").is_file()
    assert "Leading duration to remove (s): 0.74" in result.stdout
    assert "Removed leading frames: 3" in result.stdout
    assert "Requested remove duration (s): 0.740000" in result.stdout
    assert "Split timestamp (s): 0.750000" in result.stdout
