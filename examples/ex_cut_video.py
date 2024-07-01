# pylint: disable=C0114,C0103
# TODO : start and end are constants or not ?

import os
from pathlib import Path

import dotenv
from ntt.videos.create_clip import cut_video


# https://peps.python.org/pep-0008/#constants
# TODO : videos not in samples folder
VIDEO_IN_NAME_1 = "2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed.mp4"  # noqa - E501 # pylint: disable=C0301
VIDEO_OUT_NAME_1 = "2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed_cut.mp4"  # noqa - E501 # pylint: disable=C0301
VIDEO_IN_NAME_2 = "2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed.mp4"  # noqa - E501 # pylint: disable=C0301
VIDEO_OUT_NAME_2 = "2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed_cut.mp4"  # noqa - E501 # pylint: disable=C0301

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    start = 10
    end = 13
    cut_video(path_in / VIDEO_IN_NAME_1, path_out / VIDEO_OUT_NAME_1, start, end)

    start = 10
    end = 13
    cut_video(path_in / VIDEO_IN_NAME_2, path_out / VIDEO_OUT_NAME_2, start, end)
