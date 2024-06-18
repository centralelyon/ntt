# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.videos.shake_video import rotate_video

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "video_before_rotation.mp4"
ROTATION_INCREMENT = 1

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_path_out = os.path.join(
        os.environ.get("PATH_OUT"), "video_after_rotation.mp4"
    )
    rotate_video(video_path_in, VIDEO_NAME, ROTATION_INCREMENT, video_path_out)
