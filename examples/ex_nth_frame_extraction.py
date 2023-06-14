import os

from dotenv import load_dotenv

from ntt.frames.n_frame_extraction import extract_n_frame

if __name__ == "__main__":
    load_dotenv()
    extract_n_frame(
        video_path_in=os.environ.get("VIDEO_PATH_IN"),
        video_name_in="crop.mp4",
        n=2350,
    )
