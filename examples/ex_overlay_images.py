# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.frames.frame_overlay import overlay_two_frames

# https://peps.python.org/pep-0008/#constants
NAME_FRAME1 = "frame1.jpg"
NAME_FRAME2 = "frame2.jpg"

if __name__ == "__main__":
    load_dotenv()
    path_frames = os.environ.get("PATH_IN")
    name_output_frame = os.path.join(os.environ.get("FRAME_PATH_OUT"), "overlayed.png")
    opacities = [0.5] * 2
    overlay_two_frames(
        path_frames, NAME_FRAME1, NAME_FRAME2, opacities, name_output_frame
    )
