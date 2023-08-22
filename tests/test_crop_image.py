import os
import cv2
import pytest
import numpy as np
from ntt.frames.crop_image import crop
from dotenv import load_dotenv


def test_crop():
    load_dotenv()
    frame_name_in = os.path.join(os.environ.get("VIDEO_PATH_IN"), "crop.jpg")
    image = cv2.imread(frame_name_in)
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


if __name__ == "__main__":
    test_crop()
