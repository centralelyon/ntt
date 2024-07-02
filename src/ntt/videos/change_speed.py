"""TODO : change_speed module provides ...
"""

from __future__ import annotations

import os

from moviepy.editor import VideoFileClip


def change_video_speed(
    video_file_in: str | os.PathLike,
    video_file_out: str | os.PathLike,
    speed_factor: int = 1,
) -> str:
    """Change the video speed with a factor > 1 accelerates, <1 slows down.
    TODO : Describe parameters

    Args:
        video_file_in (str or Path): Full path to the input video file
        video_file_out (str or Path): Full Path to the output video file
        speed_factor (int, optional): _description_. Defaults to 1.

    Returns:
        str: _description_
    """
    video_in = VideoFileClip(str(video_file_in))
    video_out = video_in.fx(VideoFileClip.speedx, speed_factor)
    video_out.write_videofile(str(video_file_out))
    video_in.close()
    video_out.close()

    return video_file_out
