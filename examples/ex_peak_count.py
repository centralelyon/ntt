from ntt.sounds.sound_detection import simple_peak_count
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    video_path = os.environ.get("VIDEO_PATH_IN")
    video_name = "2_bounces_ping.mp4"
    print(simple_peak_count(video_path, video_name))
