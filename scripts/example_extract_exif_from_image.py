import json
import sys

from ntt.frames.exif import extract_exif_exifread, extract_exif_pillow


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python /app/scripts/example_extract_exif_from_image.py /app/output/image_with_exif.jpg"
        )

    image_path = sys.argv[1]
    data = {
        "image": image_path,
        "pillow": extract_exif_pillow(image_path),
        "exifread": extract_exif_exifread(image_path),
    }
    print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()
