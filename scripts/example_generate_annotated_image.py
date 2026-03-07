import os
import sys

import cv2

from ntt.draw.primitives import draw_rectangle, write_text
from ntt.frames.frame_generation import random_frame


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else "/app/output/annotated_image.jpg"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    frame = random_frame(640, 480)
    frame = cv2.resize(frame, (320, 240))
    write_text(frame, "ntt example", (20, 40), (255, 255, 255))
    draw_rectangle(frame, ((40, 60), (280, 200)), (0, 255, 0))

    cv2.imwrite(output_path, frame)
    print(f"Saved annotated image: {output_path}")


if __name__ == "__main__":
    main()
