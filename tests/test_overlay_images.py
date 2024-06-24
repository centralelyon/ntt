"""TODO : test_overlay_images ...
Should write fi
"""

import cv2
import numpy as np

from ntt.frames.frame_generation import empty_frame
from ntt.frames.frame_overlay import overlay_n_frames, overlay_two_frames


def test_overlay_two_frames(sample_path_in, sample_path_out):
    """Test ntt overlay_two_frames function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    frame1_name = "frame1.jpg"
    frame2_name = "frame2.jpg"

    frame1 = cv2.imread(sample_path_in / frame1_name)
    frame2 = cv2.imread(sample_path_in / frame2_name)

    assert frame1.shape == frame2.shape

    opacities = [0.5] * 2

    overlayed_output_path = sample_path_out / "overlayed.jpg"

    # TODO : is the a test of the overlay_two_frames function ?
    _ = overlay_two_frames(
        sample_path_in,
        frame1_name,
        frame2_name,
        opacities,
        overlayed_output_path,
    )


def test_overlay_n_frames(sample_path_in, sample_path_out):
    """Test ntt overlay_n_frames function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    frame1_name = "frame1.jpg"
    frame2_name = "frame2.jpg"
    frame3_name = "frame3.jpg"

    frame1 = cv2.imread(sample_path_in / frame1_name)
    frame2 = cv2.imread(sample_path_in / frame2_name)
    frame3 = cv2.imread(sample_path_in / frame3_name)

    frames = [frame1_name, frame2_name, frame3_name]

    assert frame1.shape == frame2.shape and frame1.shape == frame3.shape

    opacities = [0.5] * 3
    overlayed_output_path = sample_path_out / "overlayed.jpg"

    # TODO : is the a test of the overlay_n_frames function ?
    _ = overlay_n_frames(
        sample_path_in,
        frames,
        opacities,
        overlayed_output_path
        )


def test_custom(sample_path_out):
    """_summary_
    TODO : No input image here, using only sample_path_out

    Args:
        sample_path_out (Path): output path
    """
    # TODO : does empty_frame produce 3 different images ?
    # Probably not : written files have the same md5sum
    frame1 = empty_frame(width=10, height=10)
    frame2 = empty_frame(width=10, height=10)
    # TODO : computed a new way a few line later, this one is not useful ?
    frame3 = empty_frame(width=10, height=10)

    # TODO : written in PATH_IN path and commited !!!
    cv2.imwrite(sample_path_out / "image1.png", frame1)
    cv2.imwrite(sample_path_out / "image2.png", frame2)

    overlayed1_name = "overlayed1.png"
    overlayed2_name = "overlayed2.png"

    # TODO : new frame3 definition
    h, w, _ = frame3.shape
    frame3[h // 4:h // 2, w // 4:w // 2] = np.full(
        (h // 2 - h // 4, w // 2 - w // 4, 3),
        [0, 255, 0],
        dtype=np.uint8
    )

    cv2.imwrite(sample_path_out / "image3.png", frame3)

    _ = overlay_two_frames(
        sample_path_out,
        "image1.png",
        "image3.png",
        [0.5] * 2,
        sample_path_out / overlayed1_name
        )

    _ = overlay_two_frames(
        sample_path_out,
        "image2.png",
        "image3.png",
        [0.5] * 2,
        sample_path_out / overlayed2_name
        )

    res_output_path = sample_path_out / "res.png"

    overlayed = overlay_two_frames(
        sample_path_out,
        overlayed1_name,
        overlayed2_name,
        [1, 1],
        res_output_path
        )

    assert (frame3 == overlayed).all()
