# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.sounds.sound_generation import random_to_start

# Video parameters
# https://peps.python.org/pep-0008/#constants
START_TIME = 0.1
DURATION = 5.0
FREQUENCY = 440

if __name__ == "__main__":
    ev_path = Path(dotenv.find_dotenv())

    dotenv.load_dotenv()

    path_out = Path(ev_path.parent / os.environ.get("PATH_OUT"))

    if not path_out.exists():
        path_out.mkdir()

    video_path = path_out / "video.mp4"

    # generate video with audio
    random_to_start(START_TIME, DURATION, FREQUENCY, video_path)
