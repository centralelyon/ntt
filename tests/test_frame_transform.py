import numpy as np

from ntt.frames.frame_generation import random_frame
from ntt.frames.transform import (
    annotate_frame,
    blur_frame,
    flip_frame,
    grayscale_frame,
    resize_frame,
    rotate_frame,
    transform_frame,
)


def test_resize_rotate_flip_and_grayscale_transformations():
    frame = random_frame(64, 48)

    resized = resize_frame(frame, 32, 24)
    rotated = rotate_frame(frame, 10)
    flipped = flip_frame(frame, "horizontal")
    gray = grayscale_frame(frame)

    assert resized.shape == (24, 32, 3)
    assert rotated.shape == frame.shape
    assert flipped.shape == frame.shape
    assert gray.shape == frame.shape
    assert np.any(gray[:, :, 0] == gray[:, :, 1])


def test_annotate_and_blur_modify_frame():
    frame = random_frame(64, 48)

    annotated = annotate_frame(
        frame,
        text="ntt",
        rectangle=((5, 5), (20, 20)),
        line=((0, 0), (30, 30)),
        crosshair={"x": 32, "y": 24, "text": "x"},
    )
    blurred = blur_frame(frame, kernel_size=(7, 7))

    assert annotated.shape == frame.shape
    assert blurred.shape == frame.shape
    assert np.any(annotated != frame)


def test_transform_frame_pipeline_applies_operations():
    frame = random_frame(64, 48)

    result = transform_frame(
        frame,
        [
            {"name": "resize", "params": {"width": 40, "height": 30}},
            {"name": "grayscale"},
            {"name": "annotate", "params": {"text": "pipeline"}},
            {"name": "crop", "params": {"x1": 5, "y1": 5, "x2": 35, "y2": 25}},
        ],
    )

    assert result.shape == (20, 30, 3)
