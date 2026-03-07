import os
import shutil

import cv2
import ffmpeg
from moviepy.editor import VideoFileClip, vfx

from ntt.videos.io import read_video, write_video


def _get_video_fps(video_path: str) -> float:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
    cap.release()
    return fps if fps > 0 else 30.0


def change_speed_opencv(
    video_path_in: str, video_path_out: str, speed_factor: float
) -> str:
    """Change video speed by resampling frames with OpenCV."""
    if speed_factor <= 0:
        raise ValueError("speed_factor must be > 0")

    frames = read_video(video_path_in)
    if not frames:
        raise ValueError(f"No frames found in video: {video_path_in}")

    fps = _get_video_fps(video_path_in)
    output_count = max(1, int(len(frames) / speed_factor))
    output_frames = [
        frames[min(int(i * speed_factor), len(frames) - 1)]
        for i in range(output_count)
    ]

    return write_video(video_path_out, output_frames, fps=int(round(fps)))


def change_speed_ffmpeg(
    video_path_in: str, video_path_out: str, speed_factor: float
) -> str:
    """Change video speed using ffmpeg setpts."""
    if speed_factor <= 0:
        raise ValueError("speed_factor must be > 0")
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg executable is not available")

    video = ffmpeg.input(video_path_in).video.filter(
        "setpts", f"{1 / speed_factor}*PTS"
    )
    ffmpeg.output(video, video_path_out, an=None).overwrite_output().run(
        quiet=True, capture_stdout=True, capture_stderr=True
    )
    return video_path_out


def change_speed_moviepy(
    video_path_in: str, video_path_out: str, speed_factor: float
) -> str:
    """Change video speed using MoviePy."""
    if speed_factor <= 0:
        raise ValueError("speed_factor must be > 0")

    clip = VideoFileClip(video_path_in)
    output = None
    try:
        output = clip.fx(vfx.speedx, speed_factor)
        codec = "libx264" if video_path_out.lower().endswith(".mp4") else "png"
        output.write_videofile(video_path_out, codec=codec, audio=False, logger=None)
    finally:
        clip.close()
        if output is not None:
            output.close()

    return video_path_out


def change_speed(
    video_path_in: str,
    video_path_out: str,
    speed_factor: float = 1.0,
    backend: str = "opencv",
) -> str:
    """Change video speed using the requested backend."""
    if not os.path.isfile(video_path_in):
        raise FileNotFoundError(f"Video file not found: {video_path_in}")

    backends = {
        "opencv": change_speed_opencv,
        "ffmpeg": change_speed_ffmpeg,
        "moviepy": change_speed_moviepy,
    }
    if backend not in backends:
        raise ValueError(f"Unknown backend: {backend}")

    return backends[backend](video_path_in, video_path_out, speed_factor)


# Preview compatibility aliases
change_video_speed_opencv = change_speed_opencv
change_video_speed_ffmpeg = change_speed_ffmpeg
change_video_speed_moviepy = change_speed_moviepy
change_video_speed = change_speed
