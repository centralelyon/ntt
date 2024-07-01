"""TODO : frame_overlay module provides ...
"""

from pathlib import Path

import cv2
import numpy as np


def overlay_two_frames(
    path_frames, name_frame1, name_frame2, opacities, path_output_frame
):
    """_summary_

    Args:
        path_frames (Path or str): Path to the folder containing the input frames
        name_frame1 (_type_): _description_
        name_frame2 (_type_): _description_
        opacities (_type_): _description_
        path_output_frame (Path or str): Path to the output file for the resulting
        frame

    Returns:
        array: the overlayed frame
    """
    input_path = Path(path_frames)
    output_path = Path(path_output_frame)

    path_frame1 = input_path / name_frame1
    path_frame2 = input_path / name_frame2

    frame1 = np.array(cv2.imread(path_frame1), dtype=np.uint8)
    frame2 = np.array(cv2.imread(path_frame2), dtype=np.uint8)
    opacity_frame1, opacity_frame2 = opacities[0], opacities[1]

    overlayed_frame = cv2.addWeighted(frame1, opacity_frame1, frame2, opacity_frame2, 0)

    cv2.imwrite(output_path, overlayed_frame)

    return overlayed_frame


def overlay_n_frames(path_frames, frames, opacities, path_output_frame):
    """_summary_
    TODO : Should test len(frames) >= 2

    Args:
        path_frames (Path or str): Path to the folder containing the input frames
        frames (list of string): List of frame file names
        opacities (_type_): _description_
        path_output_frame (Path or str): Path to the output file for the resulting

    Returns:
        array: the overlayed frame
    """
    input_path = Path(path_frames)
    output_path = Path(path_output_frame)

    n = len(frames)

    # TODO : What is the aim of this first overlay which is overwritten after ?
    # Seems like a test code that stayed

    path_frame0 = input_path / frames[0]
    path_frame1 = input_path / frames[1]
    frame0 = cv2.imread(path_frame0)
    frame1 = cv2.imread(path_frame1)

    overlayed = cv2.addWeighted(frame0, opacities[0], frame1, opacities[1], 0)

    for i in range(2, n):
        path_frame = input_path / frames[i]
        frame = cv2.imread(path_frame)
        overlayed = cv2.addWeighted(overlayed, 1 - opacities[i], frame, opacities[i], 0)

    cv2.imwrite(output_path, overlayed)

    return overlayed
