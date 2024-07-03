"""TODO : shake_video module provides ...
"""

from pathlib import Path

import cv2
import numpy as np

from ntt.frames.processing import rotate, translate_horizontally, translate_vertically
from ntt.utils.random import random_translate_direction


def shake_video_randomly(video_path_in, video_name, shake_intensity, video_path_out):
    """_summary_

    Args:
        video_path_in (str or Path): Path to the folder containing the input video
        video_name (string): Name of the input video
        shake_intensity (_type_): _description_
        video_path_out (str or Path): Full path to the output video
    """
    video = Path(video_path_in) / video_name

    video = cv2.VideoCapture(video)

    # TODO : Depends of the input video type and the platform ? see peak.py
    # "MJPG" did not work on Ubuntu 22.04 for an .mp4 output
    # fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))

    # TODO : explain the algorithm, the logic
    got_frame = True
    while got_frame:
        got_frame, frame = video.read()

        if got_frame:
            h, w, _ = frame.shape
            direction = random_translate_direction()
            frame1 = np.zeros_like(frame)

            if direction == "up":
                frame1[: h - shake_intensity] = frame[shake_intensity:h]
            elif direction == "left":
                frame1[:, : w - shake_intensity] = frame[:, shake_intensity:w]
            elif direction == "down":
                frame1[shake_intensity:h] = frame[: h - shake_intensity]
            else:
                frame1[:, shake_intensity:w] = frame[:, : w - shake_intensity]

            video_writer.write(frame1)

    video_writer.release()
    video.release()


def rotate_video(video_path_in, video_name, rotation_increment, video_path_out):
    """_summary_
    TODO : random rotation ? why ?
    TODO : it seems that rotation_increment are degree ?

    Args:
        video_path_in (str or Path): Path to the folder containing the input video
        video_name (string): Name of the input video
        rotation_increment (_type_): _description_
        video_path_out (str or Path): Full path to the output video
    """
    video = Path(video_path_in) / video_name

    video = cv2.VideoCapture(video)

    # TODO : Depends of the input video type and the platform ?
    # fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))

    got_frame = True
    while got_frame:
        got_frame, frame = video.read()

        if got_frame:
            # TODO : What is the aim of a random rotation ???
            direction = np.random.choice([-1, 1])
            result = rotate(frame, rotation_increment * direction)
            rotation_increment = rotation_increment * direction

            video_writer.write(result)

    video_writer.release()
    video.release()


def translate_video_horizontally(
    video_path_in, video_name, translation_rate, video_path_out
):
    """_summary_
    TODO: Unit, explanation of translation_rate

    Args:
        video_path_in (str or Path): Path to the folder containing the input video
        video_name (string): Name of the input video
        translation_rate (_type_): _description_
        video_path_out (str or Path): Full path to the output video
    """
    video = Path(video_path_in) / video_name

    video = cv2.VideoCapture(video)

    # TODO : Depends of the input video type and the platform ?
    # fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))

    got_frame = True
    while got_frame:
        got_frame, frame = video.read()

        if got_frame:
            result = translate_horizontally(frame, translation_rate)
            translation_rate += 5

            video_writer.write(result)

    video_writer.release()
    video.release()


def translate_video_vertically(
    video_path_in, video_name, translation_rate, video_path_out
):
    """_summary_
    TODO : Does not work ?
    TODO : Unit, explanation of translation_rate

    Args:
        video_path_in (str or Path): Path to the folder containing the input video
        video_name (string): Name of the input video
        translation_rate (_type_): _description_
        video_path_out (str or Path): Full path to the output video
    """
    video = Path(video_path_in) / video_name

    video = cv2.VideoCapture(video)

    # TODO : Depends of the input video type and the platform ?
    # fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))

    got_frame = True
    while got_frame:
        got_frame, frame = video.read()

        if got_frame:
            result = translate_vertically(frame, translation_rate)
            translation_rate += 5

            video_writer.write(result)

    video_writer.release()
    video.release()
