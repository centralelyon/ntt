# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.sounds.sound_generation import one_second_square_frequencies

# video parameters
# https://peps.python.org/pep-0008/#constants
FREQUENCY1 = 440  # audio FREQUENCY for the first PERCENTAGE
FREQUENCY2 = 680  # audio FREQUENCY for the rest PERCENTAGE
PERCENTAGE = 0.5  # PERCENTAGE of video with first PERCENTAGE

if __name__ == "__main__":
    ev_path = Path(dotenv.find_dotenv())

    dotenv.load_dotenv()

    path_out = Path(ev_path.parent / os.environ.get("PATH_OUT"))

    if not path_out.exists():
        path_out.mkdir()

    video_path = path_out / "video.mp4"

    # generate video with audio
    one_second_square_frequencies(PERCENTAGE, FREQUENCY1, FREQUENCY2, video_path)
