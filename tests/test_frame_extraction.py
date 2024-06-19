"""TODO : test_frame_extraction ...
"""

import os

import cv2
from dotenv import load_dotenv
from ntt.frames.frame_extraction import (
    extract_first_frame,
    extract_last_frame,
    extract_nth_frame,
)


def test_extract_first_frame():
    """_summary_"""
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name_in = "crop.mp4"
    frame_path_in = os.environ.get("VIDEO_PATH_IN")
    frame_name_in = "crop.jpg"
    frame_path_out = os.environ.get("FRAME_PATH_OUT")
    frame_name_out = "crop-test-first.jpg"

    frame_path = os.path.join(frame_path_in, frame_name_in)
    image = cv2.imread(frame_path)

    # test
    result = extract_first_frame(
        video_path_in, video_name_in, frame_path_out, frame_name_out
    )

    saved_image = cv2.imread(frame_path)
    assert saved_image.shape == image.shape
    assert (saved_image == image).all()
    assert result is not None


def test_extract_last_frame():
    """_summary_"""
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name_in = "crop.mp4"
    frame_path_in = os.environ.get("VIDEO_PATH_IN")
    frame_name_in = "crop.jpg"
    frame_path_out = os.environ.get("FRAME_PATH_OUT")
    frame_name_out = "crop-test-last.jpg"

    frame_path = os.path.join(frame_path_in, frame_name_in)
    image = cv2.imread(frame_path)

    # TODO: result not used
    result = extract_last_frame(
        video_path_in, video_name_in, frame_path_out, frame_name_out
    )

    saved_image = cv2.imread(frame_path)
    assert saved_image.shape == image.shape
    assert (saved_image == image).all()


def test_extract_nth_frame():
    """_summary_"""
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name_in = "crop.mp4"
    frame_path_out = os.environ.get("FRAME_PATH_OUT")
    frame_name_out = "crop-test-nth-frame.jpg"

    # get total number of frames
    cap = cv2.VideoCapture(os.path.join(video_path_in, video_name_in))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    res = extract_nth_frame(
        video_path_in,
        video_name_in,
        frame_path_out,
        frame_name_out,
        nth_frame=total_frames + 1,
    )

    assert res is None


if __name__ == "__main__":
    # TODO : Remove this block
    test_extract_first_frame()
    test_extract_last_frame()
    test_extract_nth_frame()
