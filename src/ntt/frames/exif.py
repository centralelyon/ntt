"""EXIF metadata extraction and injection for images.

Two extraction backends are provided with the same interface:

* ``extract_exif_pillow``   – uses Pillow  (built-in EXIF support via _getexif)
* ``extract_exif_exifread`` – uses ExifRead (richer tag coverage, raw strings)

One injection function:

* ``inject_exif`` – embeds a metadata dict into a JPEG file (pure stdlib, no piexif)

All functions:
- Accept an image file path (JPEG, TIFF for extraction; JPEG only for injection).
- Raise ``FileNotFoundError`` if the file does not exist.
"""

import os
import struct


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


# ---------------------------------------------------------------------------
# EXIF injection
# ---------------------------------------------------------------------------

# Supported ASCII tag IDs (TIFF/EXIF standard), sorted by tag ID numerically.
# Entries MUST be written to the IFD in ascending tag ID order.
_ASCII_TAGS = {
    "ImageDescription": 0x010E,  # 270
    "Make":             0x010F,  # 271
    "Model":            0x0110,  # 272
    "Software":         0x0131,  # 305
    "DateTime":         0x0132,  # 306
    "Artist":           0x013B,  # 315
    "Copyright":        0x8298,  # 33432
}


def inject_exif(image_path: str, metadata: dict) -> None:
    """Embed EXIF metadata into a JPEG file (in-place).

    Supports ASCII string tags: ImageDescription, Make, Model, Software,
    DateTime, Artist, Copyright.

    Per the TIFF spec, ASCII values whose byte count (including null
    terminator) fits in 4 bytes are stored inline in the IFD entry value
    field; longer values are stored in a separate data area and referenced
    by offset.

    Args:
        image_path (str): Path to the JPEG file to modify.
        metadata (dict): Tag name to string value mapping.
            Unknown keys are silently ignored.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a JPEG.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    with open(image_path, "rb") as f:
        jpeg_bytes = f.read()

    if jpeg_bytes[:2] != b"\xFF\xD8":
        raise ValueError(f"Not a JPEG file: {image_path}")

    # Build (tag_id, raw) pairs for recognised, non-empty values.
    # Sort ascending by tag_id, as required by the TIFF/IFD spec.
    pairs = []
    for name, value in metadata.items():
        tag_id = _ASCII_TAGS.get(name)
        if tag_id is not None and value:
            raw = value.encode("utf-8") + b"\x00"  # null-terminated ASCII
            pairs.append((tag_id, raw))
    if not pairs:
        return
    pairs.sort(key=lambda x: x[0])

    n = len(pairs)
    # Each IFD entry = 12 bytes.
    # IFD block = 2 (entry count) + n*12 (entries) + 4 (next-IFD offset).
    ifd_block_size = 2 + n * 12 + 4
    data_area_start = 8 + ifd_block_size  # TIFF header is 8 bytes

    # Assign offsets for out-of-line strings (count > 4 bytes).
    # In-line strings (count <= 4) are embedded directly in the value field.
    ool_cursor = data_area_start
    entry_meta = []  # (tag_id, raw, is_inline, offset)
    for tag_id, raw in pairs:
        if len(raw) <= 4:
            entry_meta.append((tag_id, raw, True, 0))
        else:
            entry_meta.append((tag_id, raw, False, ool_cursor))
            ool_cursor += len(raw)

    # --- Assemble TIFF bytes ---
    # Header: byte-order mark "II" (little-endian), magic 42, IFD offset = 8
    tiff_header = b"II" + struct.pack("<H", 42) + struct.pack("<I", 8)

    # IFD entries
    ifd = struct.pack("<H", n)
    for tag_id, raw, is_inline, offset in entry_meta:
        if is_inline:
            value_field = raw + b"\x00" * (4 - len(raw))  # left-justify, zero-pad
            ifd += struct.pack("<HHI", tag_id, 2, len(raw)) + value_field
        else:
            ifd += struct.pack("<HHII", tag_id, 2, len(raw), offset)
    ifd += struct.pack("<I", 0)  # next IFD pointer = null

    data_area = b"".join(raw for _, raw, is_inline, _ in entry_meta if not is_inline)

    tiff_data = tiff_header + ifd + data_area

    # Wrap in JPEG APP1 segment
    app1_body = b"Exif\x00\x00" + tiff_data
    app1_len = struct.pack(">H", len(app1_body) + 2)  # big-endian, includes itself
    app1 = b"\xFF\xE1" + app1_len + app1_body

    # Strip existing APP1 EXIF segments (if any), insert new one after SOI (FF D8)
    rest = jpeg_bytes[2:]
    while rest[:2] == b"\xFF\xE1":
        seg_len = struct.unpack(">H", rest[2:4])[0]
        rest = rest[2 + seg_len:]

    with open(image_path, "wb") as f:
        f.write(b"\xFF\xD8" + app1 + rest)
