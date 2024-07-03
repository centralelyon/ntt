"""Test videos/video_generation.py functions"""

import cv2
from ntt.videos.video_generation import generate_peak_video, generate_video_numbers


def test_generate_peak_video(sample_path_out):
    """Test ntt generate_peak_video function.

    Args:
        sample_path_out (Path): output path
    """
    video_path_out = sample_path_out / "generated-peak-video.mp4"

    width = 200
    height = 150
    fps = 40
    duration = 7

    generate_peak_video(video_path_out, width, height, fps, duration)

    assert video_path_out.exists()

    video = cv2.VideoCapture(video_path_out)

    width_g = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height_g = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_g = video.get(cv2.CAP_PROP_FPS)

    assert width_g == width and height_g == height
    assert fps_g == fps


def test_generate_video_numbers(sample_path_out):
    """Test ntt generate_video_numbers function.

    Args:
        sample_path_out (Path): output path
    """
    video_path_out = sample_path_out / "generated-video-numbers-video.mp4"

    width = 200
    height = 150
    fps = 15
    duration = 6

    generate_video_numbers(duration, fps, (width, height), video_path_out)

    assert video_path_out.exists()

    video = cv2.VideoCapture(video_path_out)

    width_g = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height_g = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_g = video.get(cv2.CAP_PROP_FPS)

    assert width_g == width and height_g == height
    assert fps_g == fps
