# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.sounds.sound_generation import video2_shifted

# https://peps.python.org/pep-0008/#constants
# Video params
DURATION = 3
DECALAGE = 1.5
VIDEO_NAME = "video"

if __name__ == "__main__":
    ev_path = Path(dotenv.find_dotenv())

    dotenv.load_dotenv()

    path_out = Path(ev_path.parent / os.environ.get("PATH_OUT"))

    if not path_out.exists():
        path_out.mkdir()

    # generate video with audio
    video2_shifted(DURATION, DECALAGE, path_out, VIDEO_NAME)
