import os

import cv2
from dotenv import load_dotenv
import numpy

from ntt.frames.crop_image import crop

if __name__ == "__main__":
    load_dotenv()
    imarray = numpy.random.rand(100, 100, 3) * 255
    im = crop(imarray, 20, 20, 30, 30)
    cv2.imwrite(f"{os.environ.get('FRAME_PATH_OUT')}exemple_crop.jpg", im)
