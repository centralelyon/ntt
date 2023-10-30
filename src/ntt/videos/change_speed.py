import os
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv

load_dotenv()


def change_video_speed(
    video_file_in: str = os.path.join(os.environ.get("VIDEO_PATH_IN"), "ping.mp4"),
    video_file_out: str = os.path.join(os.environ.get("PATH_OUT"), "ping_speed.mp4"),
    speed_factor: int = 1,
) -> str:
    """change the video speed with a factor > 1 accelerates, <1 slows down"""

    video_in = VideoFileClip(video_file_in)
    video_out = video_in.fx(VideoFileClip.speedx, speed_factor)
    video_out.write_videofile(video_file_out)
    video_in.close()
    video_out.close()

    return video_file_out
