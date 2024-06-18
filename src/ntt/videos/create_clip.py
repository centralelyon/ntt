"""TODO : create_clip module provides ...
"""

from pathlib import Path

import cv2
import dotenv
from moviepy.editor import VideoFileClip


def cut_video(
    video_file_in: str, video_file_out: str, start: int = 0, end: int = 0
) -> str:
    """Cut video during a given time interval in seconds.
    TODO : Describe parameters and returned value

    Args:
        video_file_in (str): _description_
        video_file_out (str): _description_
        start (int, optional): _description_. Defaults to 0.
        end (int, optional): _description_. Defaults to 0.

    Returns:
        str: _description_
    """
    # TODO : Loading the environment variables should be done in the calling
    # script, not in the ntt library
    env_vars = dotenv.dotenv_values()

    if video_file_in is None:
        video_file_in = Path(env_vars.get("VIDEO_PATH_IN")) / "crop.mp4"

    if video_file_out is None:
        video_file_out = Path(env_vars.get("PATH_OUT")) / "crop_clip.mp4"

    myclip_in = VideoFileClip(video_file_in)
    myclip_out = myclip_in.subclip(start, end)
    myclip_out.write_videofile(video_file_out)
    myclip_in.close()
    myclip_out.close()

    return video_file_out


def cut_video_opencv(
    video_file_in: str, video_file_out: str, start: int = 0, end: int = 10
) -> str:
    """Cut video during a given time interval in frame.
    TODO : Describe parameters and returned value

    Args:
        video_file_in (str): _description_
        video_file_out (str): _description_
        start (int, optional): _description_. Defaults to 0.
        end (int, optional): _description_. Defaults to 10.

    Returns:
        str: _description_
    """
    # TODO : Loading the environment variables should be done in the calling
    # script, not in the ntt library
    env_vars = dotenv.dotenv_values()

    if video_file_in is None:
        video_file_in = Path(env_vars.get("VIDEO_PATH_IN")) / "crop.mp4"

    if video_file_out is None:
        video_file_out = Path(env_vars.get("PATH_OUT")) / "crop_clip.mp4"

    if start < 0:
        print("Error: negativ start")
        return 0
    elif start >= end:
        print(start)
        print(end)
        print("Error: start >= end")
        return 0

    if not Path.is_file(video_file_in):
        print("Wrong video path")
        return 0
    cap = cv2.VideoCapture(video_file_in)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    ret, frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    if start > length:
        print("Error: start > video length")
        return 0
    if end > length:
        print("Error: end > video length")
        return 0

    cap.set(cv2.CAP_PROP_POS_FRAMES, int(start))

    height, width, layers = frame.shape
    frame_size = (width, height)
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    out = cv2.VideoWriter(video_file_out, fourcc, fps, frame_size)
    for _ in range(end - start):
        ret, frame = cap.read()
        out.write(frame)
    out.release()

    return video_file_out
