import os
import cv2
from ntt.frames.crop_image import crop


def test_crop():
    frame_name_in = "samples/crop.jpg"
    image = cv2.imread(frame_name_in)
    shape = image.shape
    result = crop(image, 0, 0, shape[0], shape[1])
    assert result.shape == image.shape
    assert (result == image).all()


if __name__ == "__main__":
    test_crop()
