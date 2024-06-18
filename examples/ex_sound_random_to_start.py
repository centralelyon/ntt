# pylint: disable=C0114

from ntt.sounds.sound_generation import random_to_start

# https://peps.python.org/pep-0008/#constants
# Video parameters
START_TIME = 0.1
DURATION = 5.0
FREQUENCY = 440
VIDEO_NAME = "video"

if __name__ == "__main__":
    # generate video with audio
    random_to_start(START_TIME, DURATION, FREQUENCY, VIDEO_NAME)
