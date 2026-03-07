import cv2

from ntt.frames.frame_generation import full_frame
from ntt.videos.crop import _validate_crop_box, crop_video, crop_video_opencv
from ntt.videos.io import write_video


def test_validate_crop_box():
    assert _validate_crop_box(10, 20, 110, 220) == (100, 200)


def test_validate_crop_box_rejects_invalid_dimensions():
    try:
        _validate_crop_box(10, 20, 10, 220)
    except ValueError as error:
        assert "Invalid crop box" in str(error)
    else:
        raise AssertionError("Expected ValueError for invalid crop box.")


def test_crop_video_opencv_preserves_requested_output_size(tmp_path):
    input_path = tmp_path / "input.avi"
    output_path = tmp_path / "cropped.avi"
    frames = [full_frame(120, 80, (10, 20, 30)) for _ in range(4)]
    write_video(str(input_path), frames, fps=5)

    crop_video_opencv(str(input_path), str(output_path), 20, 10, 90, 60)

    cap = cv2.VideoCapture(str(output_path))
    assert cap.isOpened()
    assert int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) == 70
    assert int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) == 50
    cap.release()


def test_crop_video_dispatches_to_opencv_backend(tmp_path):
    input_path = tmp_path / "input.avi"
    output_path = tmp_path / "cropped.avi"
    frames = [full_frame(120, 80, (10, 20, 30)) for _ in range(4)]
    write_video(str(input_path), frames, fps=5)

    result = crop_video(
        str(input_path), str(output_path), 20, 10, 90, 60, backend="opencv"
    )

    assert result == str(output_path)
