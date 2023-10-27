from ntt.videos.show import show_video
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    input_video_path = os.path.join(os.environ.get("PATH_IN"), "ping.mp4")
    show_video(input_video_path)
