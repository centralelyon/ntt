"""Test dimensions.py functions.
"""

from ntt.videos.dimensions import get_video_dimensions


def test_get_video_dimensions(sample_path_in):
    """Test ntt get_video_dimensions function.

    Args:
        sample_path_in (Path): input path
    """
    video_path_in = sample_path_in / "ping.mp4"

    width, height = get_video_dimensions(video_path_in)

    assert width == 1280 and height == 720
