import cv2

from ntt.draw.primitives import (
    draw_rectangle,
    write_text,
    draw_crosshair,
    draw_line,
    draw_bright_circle,
)
from ntt.frames.frame_generation import random_frame, empty_frame, number_frame

if __name__ == "__main__":
    w, h = 500, 500
    frame = empty_frame(w, h)
    x, y = 20, 20
    write_text(frame, "test", (x, y))
    draw_rectangle(frame, (20, 20, 30, 30))
    draw_crosshair(frame, 50, 50, 10, 2)
    draw_line(frame, (10, 10), (50, 50))
    draw_bright_circle(frame, (100, 100), 50, 50)
    cv2.imshow("draw primitive on image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
