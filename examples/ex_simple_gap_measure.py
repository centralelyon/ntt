import argparse

from ntt.sounds.sound_gap_measure import sound_gap_measure

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parser for automatic start detection."
    )
    parser.add_argument(
        "--video1",
        help="Reference video path",
        default="2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroite.mp4",
    )
    parser.add_argument(
        "--video2",
        help="Comparison video path",
        default="2022_CF_Limoges_papillon_dames_50_finaleA_fixeGauche.mp4",
    )
    args = parser.parse_args()

    # start_time = extract_time_start(args.video, bip_ref_path=args.ref, references_path=args.ref_feat)

    start_time = sound_gap_measure(args.video1, args.video2)
    print(start_time)
