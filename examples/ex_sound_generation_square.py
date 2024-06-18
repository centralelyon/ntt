# pylint: disable=C0114

from ntt.sounds.sound_generation import one_second_square_frequencies

# https://peps.python.org/pep-0008/#constants
FREQUENCY1 = 440  # audio FREQUENCY for the first PERCENTAGE
FREQUENCY2 = 680  # audio FREQUENCY for the rest PERCENTAGE
PERCENTAGE = 0.5  # PERCENTAGE of video with first PERCENTAGE
FILENAME = "video"

if __name__ == "__main__":
    # video parameters

    # generate video with audio
    one_second_square_frequencies(PERCENTAGE, FREQUENCY1, FREQUENCY2, FILENAME)
