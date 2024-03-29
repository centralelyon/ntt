import cv2
import numpy as np
from typing import Tuple


def write_text(
    frame: np.ndarray,
    text: str = "Text",
    posXY: Tuple[int, int] = (10, 50),
    color: Tuple[int, int, int] = (0, 0, 255),
    thickness : int =2
) -> None:
    """write some text at a given position"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, posXY, font, 1, color, thickness, cv2.LINE_4)
    return frame


def draw_rectangle(
    frame: np.ndarray,
    posXY: Tuple[int, int] = (10, 10, 30, 30),
    color: Tuple[int, int, int] = (0, 0, 255),
) -> None:
    """draw a rectangle given 2 points"""
    thickness = 1
    cv2.rectangle(frame, posXY, color, thickness)
    return frame


def draw_line(
    frame: np.ndarray,
    start_point: Tuple[int, int] = (10, 10),
    end_point: Tuple[int, int] = (100, 100),
    color: Tuple[int, int, int] = (0, 0, 255),
) -> None:
    """draw a line given 2 points"""
    cv2.line(frame, start_point, end_point, color, thickness=2)


def draw_crosshair(
    frame: np.ndarray, x: int, y: int, size=20, thickness=2, color=(0, 255, 0)
):
    """draw a crosshair on the image"""
    cv2.line(frame, (x, y - size), (x, y + size), color, thickness)
    cv2.line(frame, (x - size, y), (x + size, y), color, thickness)


def draw_bright_circle(
    image: np.ndarray, center: Tuple, radius: int, brightness_factor=50
):
    """enhance a given circular region in the image with a brightness factor"""

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
    frame_size = (frame.shape[1], frame.shape[0])

    for row in range(rows + 1):
        y = int(row * frame_size[1] / rows)
        draw_line(frame, (0, y), (frame_size[0], y))

    for col in range(cols + 1):
        x = int(col * frame_size[0] / cols)
        draw_line(frame, (x, 0), (x, frame_size[1]))

    return frame
