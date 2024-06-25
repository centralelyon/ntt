"""TODO : test_sound_gap_measure ...
"""

from ntt.sounds.sound_gap_measure import sound_gap_measure
from ntt.sounds.sound_generation import one_second_square_frequencies


def test_same_video(sample_path_out):
    """Test ntt sound_gap_measure function with identical synthetic videos.
    Convert Path to str because of ffmpeg.

    Args:
        sample_path_out (Path): output path
    """
    frequency1 = 440
    frequency2 = 680
    percentage = 0.5

    video_path = sample_path_out / "video.mp4"

    one_second_square_frequencies(percentage, frequency1, frequency2, video_path)

    res = sound_gap_measure(video_path, video_path)

    video_path.unlink()

    assert res == 0


def test_decalage(sample_path_in):
    """Test ntt sound_gap_measure function with real videos.

    Args:
        sample_path_in (Path): input path
    """
    path1 = sample_path_in / "2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed_cut.mp4"  # noqa - E501 # pylint: disable=C0301
    path2 = sample_path_in / "2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed_cut.mp4"  # noqa - E501 # pylint: disable=C0301

    res = sound_gap_measure(path2, path1)

    assert res == -1.7842857142857143
