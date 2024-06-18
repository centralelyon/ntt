# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.utils.temporal import calculate_temporal_accuracy
from ntt.videos.peak import detect_peak_video

WIDTH = 640
HEIGHT = 480
FPS = 30

if __name__ == "__main__":
    load_dotenv()

    output = detect_peak_video(
        os.environ.get("VIDEO_PATH_IN"),
        "peak_black_gray_2500ms.mp4",
        os.environ.get("PATH_OUT"),
        "peak_black_gray_2500ms_gray.mp4",
        0,
        100,
        100,
        200,
        seuil=250,
        nb_frame=150,
        afficher_anime=True,
        afficher_hist=True,
        write_video=True,
    )

    print(f"peak detection done at {output} frame or {output / FPS} seconds")

    accuracy = calculate_temporal_accuracy(2500, output / FPS)
    print(f"{accuracy} or {accuracy:.2%}")
