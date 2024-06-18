# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.videos.shake_video import shake_video_randomly

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "reference.mp4"
SHAKE_INTENSITY = 10

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_path_out = os.environ.get("PATH_OUT") + "out.mp4"
    shake_video_randomly(video_path_in, VIDEO_NAME, SHAKE_INTENSITY, video_path_out)
