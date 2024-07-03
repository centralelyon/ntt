# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.videos.show import show_video

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME_IN = "ping.mp4"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))

    show_video(path_in / VIDEO_NAME_IN)
