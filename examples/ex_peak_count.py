# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.sounds.sound_detection import simple_peak_count_librosa

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "2_bounces_ping.mp4"

if __name__ == "__main__":
    load_dotenv()
    video_path = os.environ.get("VIDEO_PATH_IN")
    print(simple_peak_count_librosa(video_path, VIDEO_NAME))
