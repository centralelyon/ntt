import cv2

from ntt.frames.metadata import extract_image_metadata
from ntt.frames.frame_generation import random_frame
from ntt.frames.io import write_frame


def test_extract_image_metadata_returns_expected_fields(tmp_path):
    image_path = tmp_path / "image.jpg"
    frame = random_frame(64, 48)
    write_frame(str(image_path), frame)

    metadata = extract_image_metadata(str(image_path))

    assert metadata["path"] == str(image_path)
    assert metadata["file_size_bytes"] > 0
    assert metadata["width"] == 64
    assert metadata["height"] == 48
    assert metadata["dimensions"] == {"width": 64, "height": 48}
    assert metadata["color_mode"] == "RGB"
    assert isinstance(metadata["exif_pillow"], dict)
    assert isinstance(metadata["exif_exifread"], dict)
