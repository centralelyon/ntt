from dotenv import load_dotenv
import os
from ntt.videos.shake_video import shake_video_randomly

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name = "reference.mp4"
    video_path_out = os.environ.get("PATH_OUT") + "out.mp4"
    shake_intensity = 10
    shake_video_randomly(video_path_in, video_name, shake_intensity, video_path_out)
