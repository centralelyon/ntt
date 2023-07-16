import os
import cv2
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
    result = crop(image, -1, 0, shape[0], shape[1])
    assert result is None

    result = crop(image, 0, -1, shape[0], shape[1])
    assert result is None

    result = crop(image, 0, 0, shape[0] + 1, shape[1])
    assert result is None

    result = crop(image, 0, 0, shape[0], shape[1] + 1)
    assert result is None


if __name__ == "__main__":
    test_crop()
