# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.frames.frame_overlay import overlay_two_frames

# https://peps.python.org/pep-0008/#constants
NAME_FRAME1 = "frame1.jpg"
NAME_FRAME2 = "frame2.jpg"
NAME_OVERLAYED = "overlayed.png"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    overlayed_path_out = Path(ev_path_parent / os.environ.get("PATH_OUT") / NAME_OVERLAYED)

    opacities = [0.5] * 2
    overlay_two_frames(
        path_in, NAME_FRAME1, NAME_FRAME2, opacities, overlayed_path_out
    )
