import cv2

from ntt.draw.primitives import draw_rectangle, write_text
from ntt.frames.frame_generation import random_frame, empty_frame, number_frame

if __name__ == "__main__":
    w, h = 100, 100
    frame = empty_frame(w, h)
    x, y = 20, 20
    write_text(frame, "test", (x, y))
    draw_rectangle(frame, (20, 20, 30, 30))
    cv2.imshow("draw primitive on image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
