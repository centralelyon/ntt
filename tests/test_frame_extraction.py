import os
import cv2
from dotenv import load_dotenv
from ntt.frames.frame_extraction import extract_first_frame, extract_last_frame


def test_extract_first_frame():
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name_in = "crop.mp4"
    frame_path_in = os.environ.get("VIDEO_PATH_IN")
    frame_name_in = "crop.jpg"

    frame_path = os.path.join(frame_path_in, frame_name_in)
    image = cv2.imread(frame_path)

    # test
    result = extract_first_frame(
        video_path_in, video_name_in, os.environ.get("VIDEO_PATH_IN"), "crop-test.jpg"
    )

    saved_image = cv2.imread(frame_path)
    assert saved_image.shape == image.shape
    assert (saved_image == image).all()


def test_extract_last_frame():
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name_in = "crop.mp4"
    frame_path_in = os.environ.get("VIDEO_PATH_IN")
    frame_name_in = "crop.jpg"

    frame_path = os.path.join(frame_path_in, frame_name_in)
    image = cv2.imread(frame_path)

    # test
    result = extract_last_frame(
        video_path_in, video_name_in, os.environ.get("VIDEO_PATH_IN"), "crop-test.jpg"
    )

    saved_image = cv2.imread(frame_path)
    assert saved_image.shape == image.shape
    assert (saved_image == image).all()


if __name__ == "__main__":
    test_extract_first_frame()
    test_extract_last_frame()
