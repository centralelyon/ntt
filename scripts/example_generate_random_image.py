import os
import sys
from ntt.frames.frame_generation import random_frame
from ntt.frames.io import write


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else "/app/output/random_image.jpg"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    frame = random_frame(640, 480)
    write(output_path, frame)
    print(f"Saved random image: {output_path}")


if __name__ == "__main__":
    main()
