import shutil

import cv2
import pytest

from ntt.videos.change_speed import (
    change_speed,
    change_speed_ffmpeg,
    change_speed_moviepy,
    change_speed_opencv,
    change_video_speed,
)
from ntt.videos.io import write_video
from ntt.videos.video_generation import random_video


def _make_input_video(tmp_path):
    input_path = tmp_path / "input.avi"
    frames = random_video(width=64, height=48, fps=6, duration=2)
    write_video(str(input_path), frames, fps=6)
    return input_path


def _frame_count(video_path):
    cap = cv2.VideoCapture(str(video_path))
    assert cap.isOpened()
    count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return count


def test_change_video_speed_opencv_creates_faster_output(tmp_path):
    input_path = _make_input_video(tmp_path)
    output_path = tmp_path / "opencv.avi"

    changed = change_speed_opencv(str(input_path), str(output_path), 2.0)

    assert changed == str(output_path)
    assert output_path.is_file()
    assert _frame_count(output_path) < _frame_count(input_path)


@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg is not installed")
def test_change_video_speed_ffmpeg_creates_output(tmp_path):
    input_path = _make_input_video(tmp_path)
    output_path = tmp_path / "ffmpeg.mp4"

    changed = change_speed_ffmpeg(str(input_path), str(output_path), 2.0)

    assert changed == str(output_path)
    assert output_path.is_file()
    assert output_path.stat().st_size > 0


def test_change_video_speed_moviepy_creates_output(tmp_path):
    input_path = _make_input_video(tmp_path)
    output_path = tmp_path / "moviepy.mp4"

    changed = change_speed_moviepy(str(input_path), str(output_path), 2.0)

    assert changed == str(output_path)
    assert output_path.is_file()
    assert output_path.stat().st_size > 0


def test_change_video_speed_dispatch_rejects_unknown_backend(tmp_path):
    input_path = _make_input_video(tmp_path)
    output_path = tmp_path / "bad.avi"

    with pytest.raises(ValueError):
        change_speed(str(input_path), str(output_path), 2.0, backend="bad")


def test_preview_change_video_speed_alias_still_works(tmp_path):
    input_path = _make_input_video(tmp_path)
    output_path = tmp_path / "alias.avi"

    changed = change_video_speed(str(input_path), str(output_path), 2.0, backend="opencv")

    assert changed == str(output_path)
    assert output_path.is_file()
