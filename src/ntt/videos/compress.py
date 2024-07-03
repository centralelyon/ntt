"""TODO : compress module provides ...
TODO : Why not using ffmpeg package as in frame_extraction.py ?
"""

# import os
import subprocess
from pathlib import Path


def compress_video_ffmpeg_cmd(video_path_in, video_path_out, ext="_comp35"):
    """_summary_

    Args:
        video_path_in (str or Path): Full path to the input video
        video_path_out (str or Path): Full path to the output video
        ext (str, optional): _description_. Defaults to "_comp35".

    Returns:
        int: Command execution return code
    """
    # TODO : Simply get video_path_out as a parameter, avoid guess
    # cmd = (
    #     "ffmpeg -y -i "
    #     + video_path_in
    #     + " -vcodec libx264 -crf 35 -preset ultrafast -acodec aac -strict experimental "
    #     + video_path_out
    #     + ext
    #     + ".mp4"
    # )
    # os.system(cmd)
    # return video_path_out

    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        Path(video_path_in),
        "-y",
        "-vcodec",
        "libx264",
        "-crf",
        "35",
        "-preset",
        "ultrafast",
        "-acodec",
        "aac",
        "-strict",
        "experimental",
        Path(video_path_out)
    ]

    # https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess
    # TODO : could pass check=True to trigger an exception if the command fails
    cp = subprocess.run(ffmpeg_cmd)

    return cp.returncode


def convert_video(file_path_in, file_name_in, file_path_out, file_name_out):
    """_summary_

    Args:
        file_path_in (str or Path): Folder input path
        file_name_in (string): Input file name
        file_path_out (str or Path): Folder output path
        file_name_out (string): Output file name

    Returns:
        int: Command execution return code
    """
    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        Path(file_path_in) / file_name_in,
        "-y",
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
        Path(file_path_out) / file_name_out,
    ]

    # https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess
    # TODO : could pass check=True to trigger an exception if the command fails
    cp = subprocess.run(ffmpeg_cmd)

    return cp.returncode
