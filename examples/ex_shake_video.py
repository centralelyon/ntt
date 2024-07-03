# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.videos.shake_video import shake_video_randomly

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME_IN = "reference.mp4"
VIDEO_NAME_OUT = "reference_shaked.mp4"
SHAKE_INTENSITY = 10

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    shake_video_randomly(
        path_in, VIDEO_NAME_IN, SHAKE_INTENSITY, path_out / VIDEO_NAME_OUT
    )
