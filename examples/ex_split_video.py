# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.videos.split_video import split_video_ffmpeg

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "swimming_start_small.mp4"
N = 5

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("NTT_SAMPLES_PATH_IN")
    output_path = os.environ.get("PATH_OUT")
    split_video_ffmpeg(video_path_in, VIDEO_NAME, output_path, N)
