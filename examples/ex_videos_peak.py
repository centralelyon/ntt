# pylint: disable=C0114
# TODO : Removed when this sample code will be fixed
# pylint: disable=C0103

# import os

# from dotenv import load_dotenv
from ntt.videos.peak import detect_peak_video

if __name__ == "__main__":
    # TODO : Do we want to iterate on these values or are they specific
    # to the videos
    xa, xb, ya, yb = 2355, 2519, 1062, 1149
    # xa, xb, ya, yb = 750, 820, 3590, 3670
    # xa,xb,ya,yb = 500,580,3170,3230
    # xa,xb,ya,yb = 150,220,2550,2700
    # xa,xb,ya,yb = 10,100,2350,2400

    """rep = detect_peak_video(
        "./vidéos/2021_Montpellier_freestyle_hommes_50_FinaleC_fixeDroite.mp4",
        xa,
        xb,
        ya,
        yb,
        nb_frame=1300,
        afficher_anime=True,
        afficher_hist=True,
    )"""

    # TODO : Hard coded Windows path !
    input_path = "c:/Users/thomas/Documents/GitHub/neptune-dev/samples/2023_CF_Rennes_papillon_dames_50_finaleA"  # pylint: disable=C0301
    video_name_in = "2023_CF_Rennes_papillon_dames_50_finaleA_fixeDroite.mp4"
    output_path = "c:/Users/thomas/Documents/GitHub/neptune-dev/samples/2023_CF_Rennes_papillon_dames_50_finaleA"  # pylint: disable=C0301
    video_name_out = "2023_CF_Rennes_papillon_dames_50_finaleA_fixeDroite_flash.mp4"

    rep = detect_peak_video(
        input_path,
        video_name_in,
        output_path,
        video_name_out,
        xa,
        xb,
        ya,
        yb,
        nb_frame=959,
        afficher_anime=True,
        afficher_hist=True,
    )
    print(rep)
