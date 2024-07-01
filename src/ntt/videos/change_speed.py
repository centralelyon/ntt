"""TODO : change_speed module provides ...
"""

from moviepy.editor import VideoFileClip


def change_video_speed(
    video_file_in: str, video_file_out: str, speed_factor: int = 1
) -> str:
    """Change the video speed with a factor > 1 accelerates, <1 slows down.
    TODO : Describe parameters

    Args:
        video_file_in (str): _description_
        video_file_out (str): _description_
        speed_factor (int, optional): _description_. Defaults to 1.

    Returns:
        str: _description_
    """
    video_in = VideoFileClip(video_file_in)
    video_out = video_in.fx(VideoFileClip.speedx, speed_factor)
    video_out.write_videofile(video_file_out)
    video_in.close()
    video_out.close()

    return video_file_out
