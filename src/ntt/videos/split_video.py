import subprocess, os, ffmpeg
from moviepy.editor import VideoFileClip
from ntt.videos.duration import get_video_duration


def split_video_ffmpeg(video_path_in, video_name, output_path, n):
    video = os.path.join(video_path_in, video_name)
    duration = get_video_duration(video_path_in, video_name)
    segment_duration = duration / n

    command = [
        "ffmpeg",
        "-i",
        video,
        "-c:v",
        "libx264",
        "-crf",
        "22",
        "-map",
        "0",
        "-segment_time",
        str(segment_duration),
        "-reset_timestamps",
        "1",
        "-g",
        "30",
        "-sc_threshold",
        "0",
        "-force_key_frames",
        "expr:gte(t,n_forced*1)",
        "-f",
        "segment",
        os.path.join(output_path, video_name[:len(video_name)-4]) + "%03d.mp4",
    ]

    subprocess.run(command)
