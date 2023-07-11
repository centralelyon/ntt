import cv2
from dotenv import load_dotenv
import numpy

from ntt.draw.primitives import draw_rectangle, write_text

if __name__ == "__main__":
    load_dotenv()
    w, h = 100, 100
    im = numpy.random.rand(w, h, 3) * 255
    x, y = 20, 20
    write_text(im, "test", (x, y))
    draw_rectangle(im, (20, 20, 30, 30))
    cv2.imshow("Primitive on image", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
