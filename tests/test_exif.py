"""Tests for EXIF / metadata extraction.

Image tests use a synthetic JPEG with minimal EXIF embedded via Pillow.
Video tests use a synthetic MP4 generated with OpenCV (consistent with
the approach in test_frame_extraction.py).
"""

import io
import os
import struct

import cv2
import numpy as np
import pytest

from ntt.frames.exif import extract_exif_pillow, extract_exif_exifread
from ntt.videos.exif import extract_metadata_opencv, extract_metadata_ffprobe


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_jpeg_with_exif(path: str) -> None:
    """Create a minimal JPEG with EXIF data using Pillow + raw TIFF bytes (no piexif)."""
    import struct
    from PIL import Image

    # Build a minimal EXIF/APP1 payload in TIFF format (little-endian).
    # Structure: TIFF header + 1 IFD with a single ASCII tag (Make = 0x010F)
    make_value = b"TestMake\x00"            # must be null-terminated
    make_len = len(make_value)

    # TIFF header: byte order (II = little-endian), magic 42, offset of IFD0 = 8
    tiff_header = b"II" + struct.pack("<H", 42) + struct.pack("<I", 8)

    # IFD entry: tag, type (ASCII=2), count, value-or-offset
    # value/offet: if <= 4 bytes it is inline; here make_len > 4 → offset
    ifd_count = 1
    # IFD starts at byte 8; its payload = 2 (count) + 12*entries + 4 (next IFD offset) = 18 bytes
    # So make_value lives at offset 8 + 18 = 26
    value_offset = 8 + 2 + 12 * ifd_count + 4
    ifd_entry = struct.pack("<HHII", 0x010F, 2, make_len, value_offset)
    ifd = struct.pack("<H", ifd_count) + ifd_entry + struct.pack("<I", 0)  # next IFD = 0
    tiff_data = tiff_header + ifd + make_value

    # APP1 marker: FF E1, length (2 bytes, includes itself), "Exif\x00\x00", then TIFF
    app1_body = b"Exif\x00\x00" + tiff_data
    app1_len = struct.pack(">H", len(app1_body) + 2)  # +2 for the length field itself
    app1 = b"\xFF\xE1" + app1_len + app1_body

    # Save a plain JPEG first, then insert APP1 right after SOI (FF D8)
    buf = io.BytesIO()
    img = Image.new("RGB", (64, 64), color=(100, 150, 200))
    img.save(buf, "JPEG")
    jpeg_bytes = buf.getvalue()

    # SOI is the first 2 bytes; APP1 goes right after
    with open(path, "wb") as f:
        f.write(jpeg_bytes[:2] + app1 + jpeg_bytes[2:])


def _make_jpeg_no_exif(path: str) -> None:
    """Create a plain JPEG with no EXIF."""
    from PIL import Image
    img = Image.new("RGB", (64, 64), color=(200, 100, 50))
    img.save(path, "JPEG")


def _make_video(path: str, frame_count: int = 10) -> None:
    """Create a tiny synthetic MP4 with OpenCV."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(path, fourcc, 10.0, (64, 64))
    if not out.isOpened():
        raise RuntimeError(f"OpenCV could not open a video writer for {path}")
    for _ in range(frame_count):
        frame = np.zeros((64, 64, 3), dtype=np.uint8)
        cv2.randu(frame, 0, 255)
        out.write(frame)
    out.release()


@pytest.fixture(scope="module")
def jpeg_with_exif(tmp_path_factory):
    p = str(tmp_path_factory.mktemp("exif") / "with_exif.jpg")
    _make_jpeg_with_exif(p)
    return p


@pytest.fixture(scope="module")
def jpeg_no_exif(tmp_path_factory):
    p = str(tmp_path_factory.mktemp("exif") / "no_exif.jpg")
    _make_jpeg_no_exif(p)
    return p


@pytest.fixture(scope="module")
def sample_video(tmp_path_factory):
    p = str(tmp_path_factory.mktemp("exif") / "sample.mp4")
    try:
        _make_video(p, frame_count=10)
    except RuntimeError as exc:
        pytest.skip(str(exc))

    if not os.path.isfile(p):
        pytest.skip(f"OpenCV did not create the synthetic video fixture: {p}")

    cap = cv2.VideoCapture(p)
    if not cap.isOpened():
        cap.release()
        pytest.skip(f"OpenCV cannot read the synthetic video fixture on this platform: {p}")
    cap.release()
    return p


# ---------------------------------------------------------------------------
# Image – Pillow backend
# ---------------------------------------------------------------------------

class TestExtractExifPillow:

    def test_returns_dict(self, jpeg_no_exif):
        result = extract_exif_pillow(jpeg_no_exif)
        assert isinstance(result, dict)

    def test_no_exif_returns_empty(self, jpeg_no_exif):
        result = extract_exif_pillow(jpeg_no_exif)
        assert result == {}

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            extract_exif_pillow("/nonexistent/image.jpg")

    def test_with_exif_returns_dict(self, jpeg_with_exif):
        """If piexif is installed the dict is non-empty; otherwise still a dict."""
        result = extract_exif_pillow(jpeg_with_exif)
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Image – ExifRead backend
# ---------------------------------------------------------------------------

class TestExtractExifExifRead:

    def test_returns_dict(self, jpeg_no_exif):
        result = extract_exif_exifread(jpeg_no_exif)
        assert isinstance(result, dict)

    def test_no_exif_returns_empty(self, jpeg_no_exif):
        result = extract_exif_exifread(jpeg_no_exif)
        assert result == {}

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            extract_exif_exifread("/nonexistent/image.jpg")

    def test_with_exif_returns_dict(self, jpeg_with_exif):
        result = extract_exif_exifread(jpeg_with_exif)
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Video – OpenCV backend
# ---------------------------------------------------------------------------

class TestExtractMetadataOpenCV:

    EXPECTED_KEYS = {"width", "height", "fps", "frame_count", "duration_s", "codec"}

    def test_returns_dict_with_expected_keys(self, sample_video):
        result = extract_metadata_opencv(sample_video)
        assert isinstance(result, dict)
        assert self.EXPECTED_KEYS.issubset(result.keys())

    def test_dimensions(self, sample_video):
        result = extract_metadata_opencv(sample_video)
        assert result["width"] == 64
        assert result["height"] == 64

    def test_fps_positive(self, sample_video):
        result = extract_metadata_opencv(sample_video)
        assert result["fps"] > 0

    def test_frame_count(self, sample_video):
        result = extract_metadata_opencv(sample_video)
        assert result["frame_count"] == 10

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            extract_metadata_opencv("/nonexistent/video.mp4")


# ---------------------------------------------------------------------------
# Video – ffprobe backend
# ---------------------------------------------------------------------------

class TestExtractMetadataFfprobe:

    EXPECTED_KEYS = {"width", "height", "fps", "frame_count", "duration_s", "codec"}

    def test_returns_dict(self, sample_video):
        result = extract_metadata_ffprobe(sample_video)
        assert isinstance(result, dict)

    def test_has_expected_keys(self, sample_video):
        result = extract_metadata_ffprobe(sample_video)
        assert self.EXPECTED_KEYS.issubset(result.keys())

    def test_dimensions(self, sample_video):
        result = extract_metadata_ffprobe(sample_video)
        assert result["width"] == 64
        assert result["height"] == 64

    def test_fps_positive(self, sample_video):
        result = extract_metadata_ffprobe(sample_video)
        assert result["fps"] > 0

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            extract_metadata_ffprobe("/nonexistent/video.mp4")


# ---------------------------------------------------------------------------
# Consistency: both video backends return the same keys
# ---------------------------------------------------------------------------

def test_video_backends_same_keys(sample_video):
    r1 = extract_metadata_opencv(sample_video)
    r2 = extract_metadata_ffprobe(sample_video)
    assert set(r1.keys()) == set(r2.keys())
