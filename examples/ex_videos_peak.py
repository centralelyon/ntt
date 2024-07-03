# pylint: disable=C0114
# TODO : Removed when this sample code will be fixed
# pylint: disable=C0103

import os
from pathlib import Path

import dotenv
from ntt.videos.peak import detect_peak_video

# https://peps.python.org/pep-0008/#constants
# TODO : videos not in samples folder
# VIDEO_NAME_IN = "2021_Montpellier_freestyle_hommes_50_FinaleC_fixeDroite.mp4"
# VIDEO_NAME_IN = "2023_CF_Rennes_papillon_dames_50_finaleA_fixeDroite.mp4"
VIDEO_NAME_IN = "ALEXIS-LEBRUN_vs_JANG-WOOJIN.mp4"
VIDEO_NAME_OUT = "ALEXIS-LEBRUN_vs_JANG-WOOJIN_gray.mp4"

# TODO : hard coded values not computed for the current video
XA, XB, YA, YB = 0, 100, 100, 200
THRESHOLD = 50
NB_FRAME = 150

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    # TODO : Get video real characteristics dynamically for the arguments
    rep = detect_peak_video(
        path_in,
        VIDEO_NAME_IN,
        path_out,
        VIDEO_NAME_OUT,
        XA,
        XB,
        YA,
        YB,
        nb_frame=NB_FRAME,
        seuil=THRESHOLD,
        afficher_anime=False,
        afficher_hist=False,
        write_video=False
    )

    print(f"Peak detection done at frame {rep}.")
