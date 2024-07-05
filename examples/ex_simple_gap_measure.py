# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.sounds.sound_gap_measure import sound_gap_measure

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME_1 = "2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed_cut.mp4"
VIDEO_NAME_2 = "2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed_cut.mp4"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))

    # start_time = extract_time_start(
    #     args.video, bip_ref_path=args.ref, references_path=args.ref_feat
    # )

    video1 = path_in / VIDEO_NAME_1
    video2 = path_in / VIDEO_NAME_2

    start_time = sound_gap_measure(video1, video2)

    print(start_time)
