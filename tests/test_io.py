import os

from ntt.frames.frame_generation import random_frame
from ntt.frames.io import read_frame
from ntt.frames.io import write_frame
from ntt.videos.io import read_video
from ntt.videos.io import write_video
from ntt.videos.video_generation import random_video


def test_write_and_read_frame(tmp_path):
    frame_path = tmp_path / "frame.jpg"
    frame = random_frame(64, 48)

    written = write_frame(str(frame_path), frame)
    loaded = read_frame(written)

    assert written == str(frame_path)
    assert os.path.isfile(written)
    assert loaded.shape == frame.shape


def test_write_and_read_video(tmp_path):
    video_path = tmp_path / "video.avi"
    frames = random_video(width=64, height=48, fps=5, duration=2)

    written = write_video(str(video_path), frames, fps=5)
    loaded = read_video(written)

    assert written == str(video_path)
    assert os.path.isfile(written)
    assert len(loaded) == len(frames)
    assert loaded[0].shape == frames[0].shape


def test_write_video_rejects_empty_frames(tmp_path):
    video_path = tmp_path / "empty.avi"

    try:
        write_video(str(video_path), [])
    except ValueError as exc:
        assert "No frames to write" in str(exc)
    else:
        raise AssertionError("write_video should reject empty frame lists")


def test_write_video_rejects_inconsistent_frame_shapes(tmp_path):
    video_path = tmp_path / "bad.avi"
    frames = [random_frame(64, 48), random_frame(80, 48)]

    try:
        write_video(str(video_path), frames, fps=5)
    except ValueError as exc:
        assert "same width and height" in str(exc)
    else:
        raise AssertionError("write_video should reject inconsistent frame sizes")
