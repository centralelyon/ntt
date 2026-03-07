from ntt.utils.constants import DEFAULT_FOURCC, FOURCC_MP4V
from ntt.videos.io import get_writer_fourcc


def test_get_writer_fourcc_for_mp4():
    assert get_writer_fourcc("output.mp4") == FOURCC_MP4V


def test_get_writer_fourcc_for_avi_defaults_to_default_fourcc():
    assert get_writer_fourcc("output.avi") == DEFAULT_FOURCC
