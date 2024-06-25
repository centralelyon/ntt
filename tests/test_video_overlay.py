"""TODO : test_video_overlay ...
"""

import cv2
from ntt.videos.video_overlay import overlay_two_videos_opencv, overlay_videos_moviepy


def test_video_overlay_opencv(sample_path_in, sample_path_out):
    """Test ntt overlay_two_videos_opencv function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    name_video1 = "point_0.mp4"
    name_video2 = "point_8.mp4"

    path_video_out = sample_path_out / "overlayed_points.mp4"
    path_video1 = sample_path_in / name_video1
    path_video2 = sample_path_in / name_video2
    opacities = [0.5] * 2

    video1 = cv2.VideoCapture(path_video1)
    width1 = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps1 = video1.get(cv2.CAP_PROP_FPS)
    _ = video1.get(cv2.CAP_PROP_FRAME_COUNT)

    video2 = cv2.VideoCapture(path_video2)
    width2 = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps2 = video2.get(cv2.CAP_PROP_FPS)
    _ = video2.get(cv2.CAP_PROP_FRAME_COUNT)

    assert width1 == width2 and height1 == height2
    assert fps1 == fps2

    overlay_two_videos_opencv(
        sample_path_in, name_video1, name_video2, opacities, path_video_out
    )


def test_video_overlay_moviepy(sample_path_in, sample_path_out):
    """Test ntt overlay_videos_moviepy function.

    TODO :
    - 'point_0.mp4', 'point_8.mp4' are in samples folder as well as in
      samples/videos folder !
    - There's a ffmpeg_reader warning on 'point_0.mp4'
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

    path_video_out = sample_path_out / "overlayed.mp4"

    overlay_videos_moviepy(list_videos_path, opacities, path_video_out)
