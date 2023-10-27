from ntt.videos.create_clip import cut_video
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    path_in = os.path.join(
        os.environ.get("VIDEO_PATH_IN"),
        "2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed.mp4",
    )
    path_out = os.path.join(
        os.environ.get("PATH_OUT"),
        "2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed_cut.mp4",
    )
    start = 10
    end = 13
    cut_video(path_in, path_out, start, end)
    path_in = os.path.join(
        os.environ.get("VIDEO_PATH_IN"),
        "2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed.mp4",
    )
    path_out = os.path.join(
        os.environ.get("PATH_OUT"),
        "2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed_cut.mp4",
    )
    start = 10
    end = 13
    cut_video(path_in, path_out, start, end)
