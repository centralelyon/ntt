"""TODO : test_crop_image ...
"""

import cv2
import numpy as np
import pytest
from ntt.frames.crop_image import crop


def test_crop(sample_path_in):
    """Test ntt crop function.

    Args:
        sample_path_in (Path): input path
    """
    frame_file_in = str(sample_path_in / "crop.jpg")
    image = cv2.imread(frame_file_in)
    shape = image.shape

    # no crop just to check if the image is the same
    result = crop(image, 0, 0, shape[0], shape[1])
    assert result.shape == image.shape
    assert (result == image).all()

    # bad dimensions
    with pytest.raises(ValueError):
        crop(image, -1, 0, shape[0], shape[1])

    with pytest.raises(ValueError):
        crop(image, 0, -1, shape[0], shape[1])

    with pytest.raises(ValueError):
        crop(image, 0, 0, shape[0] + 1, shape[1])

    with pytest.raises(ValueError):
        crop(image, 0, 0, shape[0], shape[1] + 1)

    image = np.random.rand(100, 100, 3)  # Create a random image
    x1, y1, x2, y2 = -10, 20, 80, 110

    with pytest.raises(ValueError):
        crop(image, x1, y1, x2, y2)
