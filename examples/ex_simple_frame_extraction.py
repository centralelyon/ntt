import os

from dotenv import load_dotenv

from ntt.frames.frame_extraction import extract_first_frame

if __name__ == "__main__":
    load_dotenv()
    extract_first_frame(
        video_path_in=os.environ.get("VIDEO_PATH_IN"),
        video_name_in="crop.mp4",
        frame_path_out=os.environ.get("FRAME_PATH_OUT"),
        frame_name_out="crop-ex.jpg",
    )
