"""EXIF metadata extraction for images.

Two backends are provided with the same interface so they can be used
interchangeably in pipelines:

* ``extract_exif_pillow``   – uses Pillow  (built-in EXIF support via _getexif)
* ``extract_exif_exifread`` – uses ExifRead (richer tag coverage, raw strings)

Both functions:
- Accept an image file path (JPEG, TIFF, …).
- Return a ``dict`` of human-readable tag → value pairs.
- Return an **empty dict** when the image carries no EXIF data (e.g. PNG, synthetic).
- Raise ``FileNotFoundError`` if the file does not exist.
"""

import os
from typing import Optional


# ---------------------------------------------------------------------------
# Pillow backend
# ---------------------------------------------------------------------------

def extract_exif_pillow(image_path: str) -> dict:
    """Extract EXIF metadata from an image using Pillow.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict: Mapping of EXIF tag names to values, or ``{}`` if no EXIF is present.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        from PIL import Image
        from PIL.ExifTags import TAGS

        img = Image.open(image_path)
        raw = img._getexif()
        if raw is None:
            return {}
        return {TAGS.get(tag_id, tag_id): value for tag_id, value in raw.items()}
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# ExifRead backend
# ---------------------------------------------------------------------------

def extract_exif_exifread(image_path: str) -> dict:
    """Extract EXIF metadata from an image using ExifRead.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict: Mapping of tag keys (e.g. ``"Image Make"``) to string values,
              or ``{}`` if no EXIF is present.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        import exifread

        with open(image_path, "rb") as f:
            tags = exifread.process_file(f, details=False)
        return {key: str(value) for key, value in tags.items()}
    except Exception:
        return {}
