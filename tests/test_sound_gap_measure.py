import os
from ntt.sounds.sound_generation import one_seconde_square_frequencies,vid2_decale
from ntt.sounds.sound_gap_measure import sound_gap_measure


def test_same_video():
    frequency1 = 440
    frequency2 = 680
    percentage = 0.5
    filename = "video"
    one_seconde_square_frequencies(percentage, frequency1, frequency2, filename)

    path = "samples/video.mp4"
    res = sound_gap_measure(path, path)
    os.remove(path)
    assert res == 0


def test_decalage():
    """during = 2
    decal = 1
    name = "video"
    vid2_decale(during, decal, name)"""

    path1=f"{os.environ.get('VIDEO_PATH_IN')}2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed_cut.mp4"
    path2=f"{os.environ.get('VIDEO_PATH_IN')}2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed_cut.mp4"
    res = sound_gap_measure(path2, path1)
    assert res == -1.8091836734693878


if __name__ == "__main__":
    test_same_video()
    test_decalage()  # missing input file
