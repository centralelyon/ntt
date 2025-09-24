from ntt.frames.frame_generation import random_frame
from ntt.frames.frame_crop import crop


def test_crop_identity():
    frame = random_frame()  # default 640x480
    result = crop(frame, 0, 0, 640, 480)
    assert result.shape == frame.shape


def test_crop_partial():
    frame = random_frame()  # default 640x480
    result = crop(frame, 100, 100, 500, 400)
    assert result.shape == (500 - 100, 400 - 100, 3)


def test_crop_empty():
    frame = random_frame()  # default 640x480
    result = crop(frame, 100, 100, 100, 100)
    assert result.shape == (0, 0, 3)


if __name__ == "__main__":
    test_crop_identity()
    test_crop_partial()
    test_crop_empty()
