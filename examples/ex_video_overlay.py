# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.videos.video_overlay import overlay_two_videos_opencv

# https://peps.python.org/pep-0008/#constants
NAME_VIDEO1 = "point_0.mp4"
NAME_VIDEO2 = "point_8.mp4"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN") / "videos")
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    if not path_out.exists():
        path_out.mkdir()

    video_out = path_out / "overlayed_points.mp4"
    opacities = [0.5] * 2

    overlay_two_videos_opencv(
        path_in, NAME_VIDEO1, NAME_VIDEO2, opacities, video_out
    )
