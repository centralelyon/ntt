import os
from dotenv import load_dotenv
from ntt.videos.peak import detect_peak_video


if __name__ == "__main__":
    load_dotenv()

    width = 640
    height = 480
    fps = 30

    output = detect_peak_video(
        "samples/",
        "peak_black_gray_2500ms.mp4",
        "output",
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

    print(f"peak detection done at {output} frame or {output / fps} seconds")

    accuracy = calculate_temporal_accuracy(2500, output / fps)
    print(accuracy, "or {:.2%}".format(accuracy))
