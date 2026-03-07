import os

from PIL import Image

from ntt.frames.exif import extract_exif_exifread, extract_exif_pillow


def extract_image_metadata(image_path: str) -> dict:
    """Return unified metadata for an image file."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    with Image.open(image_path) as image:
        width, height = image.size
        color_mode = image.mode

    return {
        "path": image_path,
        "file_size_bytes": os.path.getsize(image_path),
        "width": width,
        "height": height,
        "dimensions": {"width": width, "height": height},
        "color_mode": color_mode,
        "exif_pillow": extract_exif_pillow(image_path),
        "exif_exifread": extract_exif_exifread(image_path),
    }
