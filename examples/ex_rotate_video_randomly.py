# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.videos.shake_video import rotate_video

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME_IN = "video_before_rotation.mp4"
VIDEO_NAME_OUT = "video_random_rotation.mp4"
ROTATION_INCREMENT = 45

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    rotate_video(path_in, VIDEO_NAME_IN, ROTATION_INCREMENT, path_out / VIDEO_NAME_OUT)
