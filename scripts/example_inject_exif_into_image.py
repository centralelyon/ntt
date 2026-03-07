import os
import sys
from datetime import datetime

import cv2

from ntt.frames.exif import inject_exif
from ntt.frames.frame_generation import random_frame


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else "/app/output/image_with_exif.jpg"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    frame = random_frame(640, 480)
    cv2.imwrite(output_path, frame)

    metadata = {
        "Make": "ntt",
        "Model": "example_inject_exif_into_image.py",
        "Software": "ntt",
        "ImageDescription": "Random image with EXIF injected by ntt",
        "DateTime": datetime.now().strftime("%Y:%m:%d %H:%M:%S"),
    }
    inject_exif(output_path, metadata)

    print(f"Saved image with EXIF: {output_path}")
    for key, value in metadata.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
