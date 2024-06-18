# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.videos.video_overlay import overlay_two_videos_opencv

# https://peps.python.org/pep-0008/#constants
NAME_VIDEO1 = "point_0.mp4"
NAME_VIDEO2 = "point_8.mp4"

if __name__ == "__main__":
    load_dotenv()
    path_videos = os.environ.get("PATH_IN")
    video_out = os.path.join(os.environ.get("PATH_OUT"), "overlayed_points.mp4")
    opacities = [0.5] * 2
    overlay_two_videos_opencv(
        path_videos, NAME_VIDEO1, NAME_VIDEO2, opacities, video_out
    )
