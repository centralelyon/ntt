"""TODO : test_split_video ...
"""

import pytest
from ntt.videos.split_video import split_video_ffmpeg


def test_split_video_negative_n(sample_path_in, sample_path_out):
    """Test ntt split_video_ffmpeg function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_name = "swimming_start_small.mp4"
    n = -5  # Test with a negative value for n

    with pytest.raises(ValueError) as e:
        split_video_ffmpeg(sample_path_in, video_name, sample_path_out, n)

    assert str(e.value) == "Number of segments (n) must be greater than zero."
