"""TODO : test_split_video ...
"""

from pathlib import Path

import pytest
from ntt.videos.split_video import split_video_ffmpeg


def test_split_video_negative_n(sample_path_in, sample_path_out):
    """Test ntt split_video_ffmpeg function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    # TODO : video not in samples folder
    # video_name = "swimming_start_small.mp4"
    video_name = "ALEXIS-LEBRUN_vs_JANG-WOOJIN.mp4"

    # Test with a negative value for n
    n = -5

    with pytest.raises(ValueError) as e:
        split_video_ffmpeg(sample_path_in, video_name, sample_path_out, n)

    assert str(e.value) == "Number of segments (n) must be greater than zero."


def test_split_video(sample_path_in, sample_path_out):
    """Test ntt split_video_ffmpeg function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_name = "ALEXIS-LEBRUN_vs_JANG-WOOJIN.mp4"

    n = 5

    split_video_ffmpeg(sample_path_in, video_name, sample_path_out, n)

    first_output_video = sample_path_out / f"{Path(video_name).stem}_000.mp4"

    assert first_output_video.exists()
