import subprocess
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip


def remove_duration(input_file, output_file, start_time):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        input_file,
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
        output_file,
    ]

    subprocess.run(ffmpeg_cmd)


def remove_duration_movieclip(input_file, output_file, duration):
    video_clip = VideoFileClip(input_file)

    if video_clip.duration >= duration:
        start_time = duration
        end_time = video_clip.duration - duration
        ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
        print(f"Duration {duration} removed successfully.")
    else:
        print("Duration is longer than the video clip.")
