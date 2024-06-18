"""TODO : test_sound_gap_measure ...
"""

import os

from dotenv import load_dotenv
from ntt.sounds.sound_gap_measure import sound_gap_measure
from ntt.sounds.sound_generation import one_second_square_frequencies

load_dotenv()


def test_same_video():
    """_summary_
    """
    frequency1 = 440
    frequency2 = 680
    percentage = 0.5
    filename = "video"
    one_second_square_frequencies(percentage, frequency1, frequency2, filename)

    path = os.path.join(os.environ.get("VIDEO_PATH_IN"), "video.mp4")
    res = sound_gap_measure(path, path)
    os.remove(path)
    assert res == 0


def test_decalage():
    """_summary_
    """
    path1 = os.path.join(
        os.environ.get("VIDEO_PATH_IN"),
        "2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed_cut.mp4",
    )
    path2 = os.path.join(
        os.environ.get("VIDEO_PATH_IN"),
        "2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed_cut.mp4",
    )
    res = sound_gap_measure(path2, path1)
    assert res == -1.7842857142857143


if __name__ == "__main__":
    # TODO : Remove this block
    test_same_video()
    test_decalage()  # missing input file
