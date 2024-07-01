# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.sounds.sound_detection import simple_peak_count_librosa

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "2_bounces_ping.mp4"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()
    video_path = Path(ev_path_parent / os.environ.get("PATH_IN"))
    output_path = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    nb = simple_peak_count_librosa(video_path, VIDEO_NAME, output_path)

    print(f"{nb=} xxx detected in {VIDEO_NAME=}")
