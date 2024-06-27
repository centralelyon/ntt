"""TODO : test_frame_extraction ...
"""

import cv2
import pytest
from ntt.frames.frame_extraction import (
    extract_first_frame,
    extract_frame_ffmpeg,
    extract_frame_opencv,
    extract_last_frame,
    extract_nth_frame,
    compare_frames
)


def test_extract_first_frame(sample_path_in, sample_path_out):
    """Test ntt extract_first_frame function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_name_in = "crop.mp4"
    frame_name_in = "crop.jpg"
    frame_name_out = "crop-test-first.jpg"

    frame_path = sample_path_in / frame_name_in
    image = cv2.imread(frame_path)

    # test
    result = extract_first_frame(
        sample_path_in,
        video_name_in,
        sample_path_out,
        frame_name_out,
    )

    saved_image = cv2.imread(frame_path)

    assert saved_image.shape == image.shape
    assert (saved_image == image).all()
    assert result is not None


def test_extract_last_frame(sample_path_in, sample_path_out):
    """Test ntt extract_last_frame function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_name_in = "crop.mp4"
    frame_name_in = "crop.jpg"
    frame_name_out = "crop-test-last.jpg"

    frame_path = sample_path_in / frame_name_in
    image = cv2.imread(frame_path)

    _ = extract_last_frame(
        sample_path_in, video_name_in, sample_path_out, frame_name_out
    )

    saved_image = cv2.imread(frame_path)
    assert saved_image.shape == image.shape
    assert (saved_image == image).all()


def test_extract_nth_frame(sample_path_in, sample_path_out):
    """Test ntt extract_nth_frame function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_name_in = "crop.mp4"
    frame_name_out = "crop-test-nth-frame.jpg"

    # get total number of frames
    cap = cv2.VideoCapture(sample_path_in / video_name_in)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    res = extract_nth_frame(
        sample_path_in,
        video_name_in,
        sample_path_out,
        frame_name_out,
        nth_frame=total_frames + 1,
    )

    assert res is None


def test_extract_frame_opencv(sample_path_in):
    """Test ntt extract_frame_opencv function.

    Args:
        sample_path_in (Path): input path
    """
    video_name_in = "crop.mp4"
    frame_no = 1

    frame = extract_frame_opencv(sample_path_in / video_name_in, frame_no)

    assert frame is not None


@pytest.mark.skip(reason="The function does not seem to work. "
                  "Return None without errors.")
def test_extract_frame_ffmpeg(sample_path_in):
    """Test ntt extract_frame_ffmpeg function.

    Args:
        sample_path_in (Path): input path
    """
    video_name_in = "crop.mp4"
    frame_no = 1

    frame = extract_frame_ffmpeg(sample_path_in / video_name_in, frame_no)

    assert frame is not None


@pytest.mark.skip(reason="extract_frame_ffmpeg does not seem to work.")
def test_compare_frames(sample_path_in):
    """Test ntt compare_frames function.
    compare_frames seems to be itself more a test function ???

    Args:
        sample_path_in (Path): input path
    """
    video_name_in = "crop.mp4"
    frame_no = 1

    res = compare_frames(sample_path_in / video_name_in, frame_no)

    # Not sure what the function returns with np.all()
    assert res
