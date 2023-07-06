import os
import subprocess
from moviepy.editor import VideoFileClip


def compress_video_ffmpeg_cmd(video_path_in, video_path_out, ext="_comp35"):
    cmd = (
        "ffmpeg -y -i "
        + video_path_in
        + " -vcodec libx264 -crf 35 -preset ultrafast -acodec aac -strict experimental "
        + video_path_out
        + ext
        + ".mp4"
    )
    os.system(cmd)

    return video_path_out


def convert_video(file_path_in, file_name_in, file_path_out, file_name_out):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        os.path.join(file_path_in, file_name_in),
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
        os.path.join(file_path_out, file_name_out),
    ]

    subprocess.run(ffmpeg_cmd)
