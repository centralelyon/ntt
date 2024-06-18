"""TODO : n_frame_extraction module provides ...
"""

from pathlib import Path

import cv2
import dotenv


def extract_n_frame(video_path_in, video_name_in, n):
    """This function extracts the nth  frame of a given video.

    Args:
        video_path_in (string): path to the folder conataining the input video
        video_name_in (string): name of the input video
        n (int): the number of the frame to be extracted

    Returns:
        string: full path of the output frame
    """
    # TODO : Should not be in the library but in the calling script
    # The function should have a video_path_out parameter
    env_vars = dotenv.dotenv_values()

    video_path = Path(video_path_in) / video_name_in

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    i = 0
    while (i < n) and (not success):
        i = i + 1
        success, image = vidcap.read()

    if i == n and success:
        cv2.imwrite(Path(video_path_in) / f"{n}th_frame.jpg", image)
    else:
        return None

    # TODO : Should the function return a pathlib Path (i think this should
    # be the choice) or a string ?
    frame_path_out = str(Path(env_vars.get("PATH_OUT")) / str(n) / "th_frame")

    return frame_path_out


def extract_frame_opencv(video_path, frame_number):
    """This function extracts a frame given its number from a video with opencv

    Args:
        video_path (string): path to the folder containing the input video
        frame_number (int, optional): the number of the frame to extract.
        Defaults to 1.

    Returns:
        np.ndarray: the frame with number = frame_number
    """
    # Path(video_path) is not a problem if video_path is already a path
    if not Path.is_file(Path(video_path)):
        return None

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_number < 1 or frame_number > total_frames:
        return None

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
    ret, frame = cap.read()

    if ret:
        return frame
    else:
        return None
