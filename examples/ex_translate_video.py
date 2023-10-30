import os
from dotenv import load_dotenv
from ntt.videos.shake_video import *

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name = "sample.mp4"
    translation_rate = 1
    video_path_out = os.path.join(
        os.environ.get("PATH_OUT"), "video_after_translation.mp4"
    )
    translate_video_horizontally(
        video_path_in, video_name, translation_rate, video_path_out
    )
