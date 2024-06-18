# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.videos.shake_video import translate_video_horizontally

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "sample.mp4"
TRANSLATION_RATE = 1

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_path_out = os.path.join(
        os.environ.get("PATH_OUT"), "video_after_translation.mp4"
    )
    translate_video_horizontally(
        video_path_in, VIDEO_NAME, TRANSLATION_RATE, video_path_out
    )
