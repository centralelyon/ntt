import numpy
import cv2
from ntt.frames.crop_image import crop

if __name__ == "__main__":
    imarray = numpy.random.rand(100, 100, 3) * 255
    im = crop(imarray, 20, 20, 30, 30)
    cv2.imwrite("output/exemple_crop.jpg", im)
