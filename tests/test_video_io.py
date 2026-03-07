from ntt.utils.constants import DEFAULT_FOURCC, FOURCC_MP4V
from ntt.videos.io import get_writer_fourcc, read_video, write_video
from ntt.videos.video_generation import random_video


def test_get_writer_fourcc_for_mp4():
    assert get_writer_fourcc("output.mp4") == FOURCC_MP4V


def test_get_writer_fourcc_for_avi_defaults_to_default_fourcc():
    assert get_writer_fourcc("output.avi") == DEFAULT_FOURCC


def test_write_video_and_read_video_roundtrip(tmp_path):
    output_path = tmp_path / "roundtrip.avi"
    frames = random_video(width=32, height=24, fps=4, duration=2)

    write_video(str(output_path), frames, fps=4)
    loaded = read_video(str(output_path))

    assert output_path.is_file()
    assert len(loaded) == len(frames)
