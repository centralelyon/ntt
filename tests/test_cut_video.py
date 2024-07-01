"""TODO : test_cut_video ...
"""

from moviepy.editor import VideoFileClip
from ntt.videos.create_clip import cut_video, cut_video_opencv


def test_cut_video(sample_path_in, sample_path_out):
    """Test ntt cut_video function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_path_in = sample_path_in / "ping.mp4"
    video_path_out = sample_path_out / "ping_clip.mp4"
    start = 0
    end = 1

    # appel de la fonction de creation de cut
    cut_video(video_path_in, video_path_out, start, end)

    assert video_path_out.exists()

    # Conversion to str need for ffmpeg underlying functions
    video = VideoFileClip(str(video_path_out))
    duration = video.duration
    video.close()

    assert duration == end - start


def test_cut_video_opencv(sample_path_in, sample_path_out):
    """Test ntt cut_video_opencv function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_path_in = sample_path_in / "ping.mp4"
    video_path_out = sample_path_out / "ping_clip_opencv.mp4"
    start = 0
    end = 1

    # appel de la fonction de creation de cut
    cut_video_opencv(video_path_in, video_path_out, start, end)

    assert video_path_out.exists()

    # TODO : add a test for that the video was really cutted
