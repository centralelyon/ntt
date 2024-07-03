"""TODO : video_generation module provides ...
"""

import cv2
import numpy as np

from ntt.frames.frame_generation import full_frame


def generate_peak_video(video_path_out, width, height, fps, duration):
    """_summary_

    Args:
        video_path_out (str or Path): Full path to the output video
        width (_type_): _description_
        height (_type_): _description_
        fps (_type_): _description_
        duration (_type_): _description_
    """
    # TODO : Depends of the input video type ?
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")

    out = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))

    frame_count = int(fps * duration)

    for i in range(frame_count):
        time = i / fps
        if time < duration / 2:
            intensity = int((time / (duration / 2)) * 255)
        else:
            intensity = int(((duration - time) / (duration / 2)) * 255)

        frame = full_frame(width, height, (intensity, intensity, intensity))

        out.write(frame)

    out.release()


def generate_video_numbers(t=5, fps=25, size=(800, 600), video_path_out="myvideo.mp4"):
    """_summary_
    TODO : Standardize the parameter list for these 2 functions

    Args:
        t (int, optional): _description_. Defaults to 5.
        fps (int, optional): _description_. Defaults to 25.
        size (tuple, optional): _description_. Defaults to (800, 600).
        video_path_out (str or Path, optional): Full path to the output video.
        Defaults to "myvideo.mp4".

    Returns:
        _type_: _description_
    """
    num_frames = int(t * fps)

    # TODO : Depends of the input video type ?
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    out = cv2.VideoWriter(video_path_out, fourcc, fps, size)

    for frame_num in range(num_frames):
        frame = np.zeros((size[1], size[0], 3), dtype=np.uint8)  # Black background

        # Display the frame number as text
        text = str(frame_num)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_color = (255, 255, 255)  # White
        text_size = cv2.getTextSize(text, font, font_scale, 2)[0]
        text_x = (size[0] - text_size[0]) // 2
        text_y = (size[1] + text_size[1]) // 2
        cv2.putText(
            frame, text, (text_x, text_y), font, font_scale, font_color, 2, cv2.LINE_AA
        )

        out.write(frame)

    out.release()

    return video_path_out
