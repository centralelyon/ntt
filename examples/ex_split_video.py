# pylint: disable=C0114

import os
from pathlib import Path

import dotenv

from ntt.videos.split_video import split_video_ffmpeg

# https://peps.python.org/pep-0008/#constants
# TODO : video not in samples folder
# VIDEO_NAME = "swimming_start_small.mp4"
VIDEO_NAME = "ALEXIS-LEBRUN_vs_JANG-WOOJIN.mp4"
N = 5

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    split_video_ffmpeg(path_in, VIDEO_NAME, path_out, N)
