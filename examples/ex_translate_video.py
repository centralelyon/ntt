# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.videos.shake_video import translate_video_horizontally

# from ntt.videos.shake_video import translate_video_vertically

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME_IN = "reference.mp4"
VIDEO_NAME_OUT_H = "reference_translated_horizontally.mp4"
# VIDEO_NAME_OUT_V = "reference_translated_vertically.mp4"
TRANSLATION_RATE = 1

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    translate_video_horizontally(
        path_in, VIDEO_NAME_IN, TRANSLATION_RATE, path_out / VIDEO_NAME_OUT_H
    )

    # TODO : Added a call to this function but got an OpenCV error
    # cv2.error: OpenCV(4.10.0) /io/opencv/modules/videoio/src/cap_ffmpeg.cpp:169:
    # error: (-215:Assertion failed) image.depth() == CV_8U || image.depth() == CV_16U
    # in function 'write'

    # translate_video_vertically(
    #     path_in, VIDEO_NAME_IN, TRANSLATION_RATE, path_out / VIDEO_NAME_OUT_V
    # )
