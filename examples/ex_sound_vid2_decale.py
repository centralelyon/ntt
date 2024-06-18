# pylint: disable=C0114

from ntt.sounds.sound_generation import vid2_decale

# https://peps.python.org/pep-0008/#constants
# Video params
DURATION = 3
DECALAGE = 1.5
VIDEO_NAME = "video"

if __name__ == "__main__":
    # generate video with audio
    vid2_decale(DURATION, DECALAGE, VIDEO_NAME)
