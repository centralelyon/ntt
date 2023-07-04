import os
from ntt.sounds.Sound_generation import (
    One_seconde_square_frequencies,
    Random_to_start,
    No_to_start,
    Vid2_decale,
    Dirac,
)
from ntt.sounds.Sound_gap_measure import sound_gap_measure


def test_same_video():
    frequency1 = 440
    frequency2 = 680
    percentage = 0.5
    filename = "video"
    One_seconde_square_frequencies(percentage, frequency1, frequency2, filename)

    path = "samples/video.mp4"
    res = sound_gap_measure(path, path)
    os.remove(path)
    assert res == 0


def test_decalage():
    during = 2
    decal = 1
    name = "video"
    Vid2_decale(during, decal, name)

    path1 = "samples/video.mp4"
    path2 = "samples/videodecale.mp4"
    res = sound_gap_measure(path2, path1)
    os.remove(path1)
    os.remove(path2)
    assert res == decal


if __name__ == "__main__":
    test_same_video()
    # test_decalage() # missing input file
