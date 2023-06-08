import os
from ntt.sounds.Sound_generation import One_seconde_square_frequencies,Random_to_start,No_to_start
from ntt.sounds.Sound_gap_measure import sound_gap_measure

def test_same_video():
    frequency1 = 440
    frequency2 = 680
    percentage = 0.5
    filename = "video"
    One_seconde_square_frequencies(percentage, frequency1, frequency2, filename)

    path="samples/video.mp4"
    res=sound_gap_measure(path,path)
    os.remove(path)
    assert res == 0

def test_decalage():
    start1=0.1
    start2=2.6
    t=5.0
    f=680
    filename1 = "video1"
    filename2 = "video2"
    Random_to_start(start1, t, f, filename1)
    Random_to_start(start2, t, f, filename2)

    path1="samples/video1.mp4"
    path2="samples/video2.mp4"
    res=sound_gap_measure(path1,path2)
    os.remove(path1)
    os.remove(path2)

    assert res == start2-start1

def test_local():
    path1="samples/2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed.mp4"
    path2="samples/2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed.mp4"
    res=sound_gap_measure(path1,path2)

    assert res == 1.7841043083900228

if __name__ == "__main__":
    test_same_video()
    test_decalage()
    test_local()

