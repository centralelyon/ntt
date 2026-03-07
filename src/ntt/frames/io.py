import os

import cv2
import numpy as np


def read(image_path: str) -> np.ndarray:
    """Read an image from disk as a BGR frame."""
    frame = cv2.imread(image_path)
    if frame is None:
        raise FileNotFoundError(f"Could not open image: {image_path}")
    return frame


def write(image_path: str, frame: np.ndarray) -> str:
    """Write a frame to disk and return the output path."""
    os.makedirs(os.path.dirname(image_path) or ".", exist_ok=True)

    ok = cv2.imwrite(image_path, frame)
    if not ok:
        raise ValueError(f"Could not write image: {image_path}")

    return image_path
