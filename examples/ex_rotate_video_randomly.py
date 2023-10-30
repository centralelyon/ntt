import os
from dotenv import load_dotenv
from ntt.videos.shake_video import rotate_video

if __name__ == "__main__":
    load_dotenv()
    video_path_in = os.environ.get("VIDEO_PATH_IN")
    video_name = "video_before_rotation.mp4"
    rotation_increment = 1
    video_path_out = os.path.join(
        os.environ.get("PATH_OUT"), "video_after_rotation.mp4"
    )
    rotate_video(video_path_in, video_name, rotation_increment, video_path_out)
