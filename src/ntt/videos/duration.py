"""TODO : duration module provides ...
"""

import subprocess
from pathlib import Path

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def remove_duration_ffmpeg(input_file, output_file, start_time):
    """_summary_

    Args:
        input_file (str or Path): Full path to the input video file
        output_file (str or Path): Full Path to the output video file
        start_time (_type_): _description_
    """
    if start_time < 10e-3:
        start_time = 0

    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        Path(input_file),
        "-y",
        "-ss",
        str(start_time),
        "-vcodec",
        "libx264",
        "-g",
        "10",
        "-crf",
        "24",
        "-preset",
        "superfast",
        "-vf",
        "format=yuv420p",
        "-acodec",
        "aac",
        "-strict",
        "experimental",
        Path(output_file),
    ]

    # TODO : could pass check=True to trigger an exception if the command fails
    subprocess.run(ffmpeg_cmd)


def remove_duration_movieclip(input_file, output_file, duration):
    """_summary_

    Args:
        input_file (str or Path): Full path to the input video file
        output_file (str or Path): Full Path to the output video file
        duration (_type_): _description_
    """
    video_clip = VideoFileClip(str(input_file))

    if video_clip.duration >= duration:
        start_time = duration
        # Float computing : the end_time may be like 3.5199999999999996
        end_time = video_clip.duration - duration
        ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
        print(f"{duration=} removed successfully ({start_time=}, {end_time=}).")
    else:
        print(f"{duration=} is longer than the video clip "
              f"duration={video_clip.duration}.")


def get_video_duration(video_path_in, video_name):
    """_summary_

    Args:
        video_path_in (str or Path): Path to the folder containing the input video
        video_name (string): Name of the input video

    Returns:
        float: Duration of the input video
    """
    video = Path(video_path_in) / video_name

    ffprobe_cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        video,
    ]

    result = subprocess.run(ffprobe_cmd, capture_output=True, text=True)

    duration = float(result.stdout)

    return duration
