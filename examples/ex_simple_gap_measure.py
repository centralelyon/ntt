import os

from dotenv import load_dotenv

from ntt.sounds.sound_gap_measure import sound_gap_measure

if __name__ == "__main__":
    load_dotenv()

    # start_time = extract_time_start(args.video, bip_ref_path=args.ref, references_path=args.ref_feat)
    video1=f"{os.environ.get('VIDEO_PATH_IN')}2022_CF_Limoges_papillon_dames_50_finaleA_fixeDroiteCompressed.mp4"
    video2=f"{os.environ.get('VIDEO_PATH_IN')}2022_CF_Limoges_papillon_dames_50_finaleA_fixeGaucheCompressed.mp4"
    start_time = sound_gap_measure(video1, video2)
    print(start_time)
