import subprocess, os

from ntt.videos.duration import get_video_duration


def split_video_ffmpeg(
    video_path_in: str, video_name: str, output_path: str, n: int
) -> None:
    """This function splits a video into n segments of equal duration using ffmpeg.

    Args:
        video_path_in (string): path to the folder conataining the input video
        video_name (string): name of the input video
        output_path (string): path to the folder conataining the output segments
        n (int): number of segments

    Raises:
        ValueError: if n is negative
        Exception: if the video is not found

    Returns:
        None
    """

    if n < 0:
        raise ValueError("Number of segments (n) must be greater than zero.")

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
        os.path.join(output_path, video_name[: len(video_name) - 4]) + "%03d.mp4",
    ]
    try:
        subprocess.run(command)
    except Exception as e:
        print(e)
