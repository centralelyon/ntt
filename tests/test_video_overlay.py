"""TODO : test_video_overlay ...
"""

import os

import cv2
from dotenv import load_dotenv
from ntt.videos.video_overlay import overlay_two_videos_opencv, overlay_videos_moviepy

load_dotenv()


def test_video_overlay_opencv():
    """_summary_"""
    path_videos = os.environ.get("VIDEO_PATH_IN")
    name_video1 = "point_0.mp4"
    name_video2 = "point_8.mp4"
    path_video_out = os.path.join(os.environ.get("PATH_OUT"), "overlayed_points.mp4")
    path_video1 = os.path.join(path_videos, name_video1)
    path_video2 = os.path.join(path_videos, name_video2)
    opacities = [0.5] * 2

    video1 = cv2.VideoCapture(path_video1)
    video2 = cv2.VideoCapture(path_video2)
    width1 = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps1 = video1.get(cv2.CAP_PROP_FPS)
    width2 = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps2 = video2.get(cv2.CAP_PROP_FPS)
    _ = video1.get(cv2.CAP_PROP_FRAME_COUNT)
    _ = video2.get(cv2.CAP_PROP_FRAME_COUNT)
    assert width1 == width2 and height1 == height2
    assert fps1 == fps2

    overlay_two_videos_opencv(
        path_videos, name_video1, name_video2, opacities, path_video_out
    )


def test_video_overlay_moviepy():
    """_summary_"""
    list_videos_path = os.listdir(
        os.path.join(os.environ.get("VIDEO_PATH_IN"), "videos")
    )
    opacities = [0.5 for i in range(len(list_videos_path))]
    path_video_out = os.path.join(os.environ.get("PATH_OUT"), "overlayed.mp4")
    list_videos_path = [
        os.path.join(
            os.environ.get("VIDEO_PATH_IN"), os.path.join("videos", list_videos_path[i])
        )
        for i in range(len(list_videos_path))
    ]
    overlay_videos_moviepy(list_videos_path, opacities, path_video_out)


if __name__ == "__main__":
    # TODO : Remove this block
    test_video_overlay_opencv()
    test_video_overlay_moviepy()
