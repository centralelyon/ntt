import os
import cv2
from dotenv import load_dotenv
import numpy

from ntt.frames.crop_image import crop

if __name__ == "__main__":
    load_dotenv()
    w, h = 100, 100
    imarray = numpy.random.rand(w, h, 3) * 255
    im = crop(imarray, 20, 20, 30, 30)
    cv2.imwrite(os.path.join(os.environ.get("FRAME_PATH_OUT"), "exemple_crop.jpg"), im)
    cv2.imshow("Original Image", imarray)
    cv2.rectangle(im, (20, 20, 20, 20), (30, 30))
    cv2.imshow("Cropped Image", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
