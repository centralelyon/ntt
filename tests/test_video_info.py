import shutil

import pytest

from ntt.videos.info import (
    extract_video_info,
    extract_video_info_ffprobe,
    extract_video_info_opencv,
)
from ntt.videos.io import write_video
from ntt.videos.video_generation import random_video


def _make_video(tmp_path):
    video_path = tmp_path / "video.avi"
    frames = random_video(width=64, height=48, fps=5, duration=2)
    write_video(str(video_path), frames, fps=5)
    return video_path


def test_extract_video_info_opencv_returns_expected_fields(tmp_path):
    video_path = _make_video(tmp_path)

    info = extract_video_info_opencv(str(video_path))

    assert info["width"] == 64
    assert info["height"] == 48
    assert info["frame_count"] == 10
    assert info["resolution"] == {"width": 64, "height": 48}
    assert info["audio_present"] is None


@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg is not installed")
def test_extract_video_info_ffprobe_returns_expected_fields(tmp_path):
    video_path = _make_video(tmp_path)

    info = extract_video_info_ffprobe(str(video_path))

    assert info["width"] == 64
    assert info["height"] == 48
    assert info["fps"] > 0
    assert info["resolution"] == {"width": 64, "height": 48}
    assert info["audio_present"] is False


def test_extract_video_info_auto_uses_available_backend(tmp_path):
    video_path = _make_video(tmp_path)

    info = extract_video_info(str(video_path))

    assert info["width"] == 64
    assert info["height"] == 48
    assert "audio_present" in info
