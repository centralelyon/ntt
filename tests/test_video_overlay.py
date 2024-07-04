"""TODO : test_video_overlay ...
"""

import cv2
from ntt.videos.video_overlay import overlay_two_videos_opencv, overlay_videos_moviepy


def assert_similar_videos(video_path_1, video_path_2):
    """Check input videos for the overlay tests.

    Args:
        video_path_1 (Path): Full path of first video
        video_path_2 (Path): Full path of second video
    """
    video1 = cv2.VideoCapture(video_path_1)
    width1 = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps1 = video1.get(cv2.CAP_PROP_FPS)

    video2 = cv2.VideoCapture(video_path_2)
    width2 = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps2 = video2.get(cv2.CAP_PROP_FPS)

    assert width1 == width2 and height1 == height2
    assert fps1 == fps2


def test_video_overlay_opencv(sample_path_in, sample_path_out):
    """Test ntt overlay_two_videos_opencv function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    path_in = sample_path_in / "videos"

    name_video_1 = "point_0.mp4"
    name_video_2 = "point_8.mp4"

    # Sanity check, ideally should be a fixture:
    # https://github.com/pytest-dev/pytest/discussions/12572
    assert_similar_videos(path_in / name_video_1, path_in / name_video_2)

    opacities = [0.5] * 2
    path_video_out = sample_path_out / "test-overlayed-two-videos-opencv.mp4"

    overlay_two_videos_opencv(
        path_in, name_video_1, name_video_2, opacities, path_video_out
    )

    assert path_video_out.exists()
    assert_similar_videos(path_in / name_video_1, path_video_out)


def test_video_overlay_moviepy(sample_path_in, sample_path_out):
    """Test ntt overlay_videos_moviepy function.

    TODO :
    - There's a ffmpeg_reader warning on 'point_0.mp4' (fourcc pb ?)
      2764800 bytes wanted but 0 bytes read,at frame 35/37, at time 1.40/1.44 sec.
      Using the last valid frame instead.

    Simply creating a list with n times 0.5 : [0.5] * n
      https://docs.python.org/3.10/library/stdtypes.html#common-sequence-operations

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    videos_path = sample_path_in / "videos"
    list_videos_path = [videos_path / v for v in videos_path.iterdir()]

    opacities = [0.5] * len(list_videos_path)

    path_video_out = sample_path_out / "test-overlayed-multiple.mp4"

    overlay_videos_moviepy(list_videos_path, opacities, path_video_out)

    assert path_video_out.exists()
    assert_similar_videos(list_videos_path[0], path_video_out)
