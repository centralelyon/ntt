# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.utils.temporal import calculate_temporal_accuracy
from ntt.videos.peak import detect_peak_video

# https://peps.python.org/pep-0008/#constants
# TODO : video not in samples folder
# VIDEO_NAME_IN = "peak_black_gray_2500ms.mp4"
VIDEO_NAME_IN = "ALEXIS-LEBRUN_vs_JANG-WOOJIN.mp4"
VIDEO_NAME_OUT = "ALEXIS-LEBRUN_vs_JANG-WOOJIN_gray.mp4"

# TODO : hard coded values not computed for the current video
XA, XB, YA, YB = 0, 100, 100, 200
NB_FRAME = 150
THRESHOLD = 50
FPS = 30

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    # TODO : Get video real characteristics dynamically for the arguments
    output = detect_peak_video(
        path_in,
        VIDEO_NAME_IN,
        path_out,
        VIDEO_NAME_OUT,
        XA,
        XB,
        YA,
        YB,
        seuil=THRESHOLD,
        nb_frame=NB_FRAME,
        afficher_anime=True,
        afficher_hist=True,
        write_video=True,
    )

    print(f"Peak detection done at frame {output} or at {output / FPS} seconds")

    accuracy = calculate_temporal_accuracy(2500, output / FPS)

    print(f"{accuracy=} or {accuracy=:.2%}")
