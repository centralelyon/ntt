import numpy as np
from ntt.draw.primitives import write_text
import cv2


def empty_frame(width: int, height: int, nb_colors=3) -> np.ndarray:
    """Return a black frame (all zeros).

    Args:
        width (int): Frame width in pixels.
        height (int): Frame height in pixels.
        nb_colors (int): Number of color channels. Defaults to 3 (BGR).

    Returns:
        np.ndarray: Zero-filled array of shape (height, width, nb_colors).
    """
    frame = np.zeros((height, width, nb_colors), dtype=np.uint8)
    return frame


def number_frame(width: int, height: int, number=123) -> np.ndarray:
    frame = empty_frame(width, height)
    x = (width) // 2
    y = (height) // 2
    write_text(frame, str(number), (x, y))
    return frame


def random_frame(width: int = 640, height: int = 480) -> np.ndarray:
    """Return a frame filled with random pixel values.

    Args:
        width (int): Frame width in pixels. Defaults to 640.
        height (int): Frame height in pixels. Defaults to 480.

    Returns:
        np.ndarray: Random uint8 array of shape (height, width, 3).
    """
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    return frame


def full_frame(width: int, height: int, color: tuple) -> np.ndarray:
    """Return a frame filled with a solid color.

    Args:
        width (int): Frame width in pixels.
        height (int): Frame height in pixels.
        color (tuple): BGR color tuple, e.g. ``(255, 0, 0)`` for blue.

    Returns:
        np.ndarray: Constant-color array of shape (height, width, 3).
    """
    frame = np.full((height, width, 3), color, dtype=np.uint8)
    return frame


def frame_from_image_file(image_path: str) -> np.ndarray:
    frame = cv2.imread(image_path)
    return frame

if __name__ == "__main__":
    from ntt.frames.display import display_frame
    frame = random_frame()
    display_frame(frame)