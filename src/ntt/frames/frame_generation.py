import numpy as np
from ntt.draw.primitives import write_text


def empty_frame(width: int, height: int, nb_colors=3) -> np.ndarray:
    frame = np.zeros((width, height, nb_colors), dtype=np.uint8)
    return frame


def number_frame(width: int, height: int, number=123) -> np.ndarray:
    frame = empty_frame(width, height)
    x = (width) // 2
    y = (height) // 2
    write_text(frame, str(number), (x, y))
    return frame


def random_frame(width: int, height: int):
    frame = np.random.rand(width, height, 3) * 255
    return frame.astype(np.uint8)


def full_frame(width: int, height: int, color: tuple):
    frame = np.full((height, width, 3), color, dtype=np.uint8)
    return frame
