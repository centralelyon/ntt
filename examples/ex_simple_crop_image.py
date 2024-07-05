# pylint: disable=C0114

import os
from pathlib import Path

import cv2
import dotenv
import numpy
from ntt.frames.crop_image import crop

# https://peps.python.org/pep-0008/#constants
FRAME_NAME = "exemple_crop.jpg"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    w, h = 100, 100
    imarray = numpy.random.rand(w, h, 3) * 255

    im = crop(imarray, 20, 20, 30, 30)

    cv2.imwrite(path_out / FRAME_NAME, im)
    cv2.imshow("Original Image", imarray)

    cv2.rectangle(im, (20, 20, 20, 20), (30, 30))
    cv2.imshow("Cropped Image", im)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
