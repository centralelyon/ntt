import numpy as np

from ntt.draw.primitives import draw_rectangle
from ntt.frames.frame_generation import empty_frame


def test_draw_rectangle_accepts_two_points():
    frame = empty_frame(100, 100)
    result = draw_rectangle(frame, ((10, 10), (40, 40)), (0, 255, 0))

    assert result.shape == (100, 100, 3)
    assert np.any(result != 0)


def test_draw_rectangle_accepts_four_coordinates():
    frame = empty_frame(100, 100)
    result = draw_rectangle(frame, (10, 10, 40, 40), (0, 255, 0))

    assert result.shape == (100, 100, 3)
    assert np.any(result != 0)
