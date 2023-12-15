from dotenv import load_dotenv
import os

from ntt.videos.split_video import split_video_ffmpeg

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("NTT_SAMPLES_PATH_IN")
    video_name = "swimming_start_small.mp4"
    output_path = os.environ.get("PATH_OUT")
    n = 5
    split_video_ffmpeg(video_path_in, video_name, output_path, n)
