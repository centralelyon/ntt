"""Test get_fourcc.py module functions.
"""

import cv2
from ntt.videos.get_fourcc import get_fourcc


def test_get_fourcc(sample_path_in):
    """Test ntt get_fourcc function.

    Args:
        sample_path_in (Path): input path
    """
    video_file_in = sample_path_in / "ALEXIS-LEBRUN_vs_JANG-WOOJIN.mp4"

    cap = cv2.VideoCapture(video_file_in)

    codec = get_fourcc(cap)

    assert codec == "h264"
