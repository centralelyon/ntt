"""TODO : frame_generation module provides ...
"""

import cv2
import numpy as np

from ntt.draw.primitives import write_text


def empty_frame(width: int, height: int, nb_colors=3) -> np.ndarray:
    """_summary_

    Args:
        width (int): _description_
        height (int): _description_
        nb_colors (int, optional): _description_. Defaults to 3.

    Returns:
        np.ndarray: _description_
    """
    frame = np.zeros((width, height, nb_colors), dtype=np.uint8)
    return frame


def number_frame(width: int, height: int, number=123) -> np.ndarray:
    """_summary_

    Args:
        width (int): _description_
        height (int): _description_
        number (int, optional): _description_. Defaults to 123.

    Returns:
        np.ndarray: _description_
    """
    frame = empty_frame(width, height)
    x = (width) // 2
    y = (height) // 2
    write_text(frame, str(number), (x, y))
    return frame


def random_frame(width: int, height: int) -> np.ndarray:
    """_summary_

    Args:
        width (int): _description_
        height (int): _description_

    Returns:
        np.ndarray: _description_
    """
    frame = np.random.rand(width, height, 3) * 255
    return frame.astype(np.uint8)


def full_frame(width: int, height: int, color: tuple) -> np.ndarray:
    """_summary_

    Args:
        width (int): _description_
        height (int): _description_
        color (tuple): _description_

    Returns:
        np.ndarray: _description_
    """
    frame = np.full((height, width, 3), color, dtype=np.uint8)
    return frame


def frame_from_image_file(image_path: str):
    """_summary_

    Args:
        image_path (str): _description_

    Returns:
        _type_: _description_
    """
    frame = cv2.imread(image_path)
    return frame
