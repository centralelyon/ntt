"""TODO : primitives module provides ...
"""

from typing import Tuple

import cv2
import numpy as np


def write_text(
    frame: np.ndarray,
    text: str = "Text",
    pos_x_y: Tuple[int, int] = (10, 50),
    color: Tuple[int, int, int] = (0, 0, 255),
    thickness: int = 2,
) -> None:
    """Write some text at a given position.

    Args:
        frame (np.ndarray): _description_
        text (str, optional): _description_. Defaults to "Text".
        pos_x_y (Tuple[int, int], optional): _description_. Defaults to (10, 50).
        color (Tuple[int, int, int], optional): _description_. Defaults to (0, 0, 255).
        thickness (int, optional): _description_. Defaults to 2.

    Returns:
        _type_: _description_
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, pos_x_y, font, 1, color, thickness, cv2.LINE_4)
    return frame


def draw_rectangle(
    frame: np.ndarray,
    pos_x_y: Tuple[int, int] = (10, 10, 30, 30),
    color: Tuple[int, int, int] = (0, 0, 255),
) -> None:
    """Draw a rectangle given 2 points.

    Args:
        frame (np.ndarray): _description_
        pos_x_y (Tuple[int, int], optional): _description_.
            Defaults to (10, 10, 30, 30).
        color (Tuple[int, int, int], optional): _description_.
            Defaults to (0, 0, 255).

    Returns:
        _type_: _description_
    """
    thickness = 1
    cv2.rectangle(frame, pos_x_y, color, thickness)
    return frame


def draw_line(
    frame: np.ndarray,
    start_point: Tuple[int, int] = (10, 10),
    end_point: Tuple[int, int] = (100, 100),
    color: Tuple[int, int, int] = (0, 0, 255),
) -> None:
    """Draw a line given 2 points.

    Args:
        frame (np.ndarray): _description_
        start_point (Tuple[int, int], optional): _description_. Defaults to (10, 10).
        end_point (Tuple[int, int], optional): _description_. Defaults to (100, 100).
        color (Tuple[int, int, int], optional): _description_. Defaults to (0, 0, 255).
    """
    cv2.line(frame, start_point, end_point, color, thickness=2)


def draw_crosshair(
    frame: np.ndarray, x: int, y: int, size=20, thickness=2, color=(0, 255, 0)
):
    """Draw a crosshair on the image.

    Args:
        frame (np.ndarray): _description_
        x (int): _description_
        y (int): _description_
        size (int, optional): _description_. Defaults to 20.
        thickness (int, optional): _description_. Defaults to 2.
        color (tuple, optional): _description_. Defaults to (0, 255, 0).
    """
    cv2.line(frame, (x, y - size), (x, y + size), color, thickness)
    cv2.line(frame, (x - size, y), (x + size, y), color, thickness)


def draw_bright_circle(
    image: np.ndarray, center: Tuple, radius: int, brightness_factor=50
):
    """Enhance a given circular region in the image with a brightness factor.

    Args:
        image (np.ndarray): _description_
        center (Tuple): _description_
        radius (int): _description_
        brightness_factor (int, optional): _description_. Defaults to 50.

    Returns:
        _type_: _description_
    """

    mask = np.zeros_like(image)  # mask
    cv2.circle(mask, center, radius, (255, 255, 255), -1)  # draw a circle on the mask
    mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)  # convert the mask to grayscale
    # enhanced_image = image.copy()  # copy the image
    enhanced_image = image

    enhanced_image[mask_gray > 0] = cv2.add(
        enhanced_image[mask_gray > 0], brightness_factor
    )
    # add the brightness factor to the pixels in the circular region

    return enhanced_image


def draw_grid(frame, rows: int, cols: int):
    """_summary_

    Args:
        frame (_type_): _description_
        rows (int): _description_
        cols (int): _description_

    Returns:
        _type_: _description_
    """
    frame_size = (frame.shape[1], frame.shape[0])

    for row in range(rows + 1):
        y = int(row * frame_size[1] / rows)
        draw_line(frame, (0, y), (frame_size[0], y))

    for col in range(cols + 1):
        x = int(col * frame_size[0] / cols)
        draw_line(frame, (x, 0), (x, frame_size[1]))

    return frame
