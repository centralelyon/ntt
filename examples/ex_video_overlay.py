from ntt.videos.video_overlay import overlay_two_videos_opencv
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    path_videos = os.environ.get("PATH_IN")
    name_video1 = "point_0.mp4"
    name_video2 = "point_8.mp4"
    video_out = os.path.join(os.environ.get("PATH_OUT"), "overlayed_points.mp4")
    opacities = [0.5] * 2
    overlay_two_videos_opencv(
        path_videos, name_video1, name_video2, opacities, video_out
    )
