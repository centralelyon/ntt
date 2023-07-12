import cv2
import numpy as np
from typing import Tuple


def write_text(
    frame: np.ndarray,
    text: str = "Text",
    posXY: Tuple[int, int] = (10, 50),
    color: Tuple[int, int, int] = (0, 0, 255),
) -> None:
    """write some text at a given position"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 1
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


def draw_bright_circle(image, center, radius, brightness_factor=50):
    """enhance a given circular region in the image with a brightness factor"""

    mask = np.zeros_like(image)  # mask
    cv2.circle(mask, center, radius, (255, 255, 255), -1)  # draw a circle on the mask
    mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)  # convert the mask to grayscale
    # enhanced_image = image.copy()  # copy the image
    enhanced_image = image
    enhanced_image[mask_gray > 0] = cv2.add(
        enhanced_image[mask_gray > 0], brightness_factor
    )  # add the brightness factor to the pixels in the circular region

    return enhanced_image
