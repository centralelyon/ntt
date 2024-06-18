"""TODO : change_speed module provides ...
"""
from pathlib import Path

import dotenv
from moviepy.editor import VideoFileClip


def change_video_speed(video_file_in: str, video_file_out: str,
                       speed_factor: int = 1) -> str:
    """Change the video speed with a factor > 1 accelerates, <1 slows down.
    TODO : Describe parameters

    Args:
        video_file_in (str): _description_
        video_file_out (str): _description_
        speed_factor (int, optional): _description_. Defaults to 1.

    Returns:
        str: _description_
    """
    # TODO : Loading the environment variables should be done in the calling
    # script, not in the ntt library
    env_vars = dotenv.dotenv_values()

    if video_file_in is None:
        video_file_in = Path(env_vars.get('VIDEO_PATH_IN')) / "ping.mp4"

    if video_file_out is None:
        video_file_out = Path(env_vars.get('PATH_OUT')) / "ping_speed.mp4"

    video_in = VideoFileClip(video_file_in)
    video_out = video_in.fx(VideoFileClip.speedx, speed_factor)
    video_out.write_videofile(video_file_out)
    video_in.close()
    video_out.close()

    return video_file_out
