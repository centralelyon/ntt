import os
import sys

import cv2

from ntt.draw.primitives import write_text
from ntt.frames.frame_generation import random_frame


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else "/app/random_image.jpg"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    frame = random_frame(640, 480)
    write_text(frame, "ntt", (20, 40), (255, 255, 255))
    cv2.imwrite(output_path, frame)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
