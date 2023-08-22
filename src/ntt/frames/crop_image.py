import numpy as np


def crop(image: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> np.ndarray:
    """Crops an image given 2 points

    Args:
        image (np.ndarray): the image to crop
        x1 (int): top left x coordinate
        y1 (int): top left y coordinate
        x2 (int): bottom right x coordinate
        y2 (int): bottom right y coordinate

    Raises:
        ValueError: if the coordinates are out of bounds

    Returns:
        np.ndarray: the cropped image
    """
    w, h = image.shape[:2]

    # raise an error if the coordinates are out of bounds
    if x1 < 0 or y1 < 0 or x2 > w or y2 > h:
        raise ValueError("Coordinates out of bounds")

    return image[x1:x2, y1:y2]
