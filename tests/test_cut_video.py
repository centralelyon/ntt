"""TODO : test_cut_video ...
"""

from moviepy.editor import VideoFileClip
from ntt.videos.create_clip import cut_video


def test_cut_video(sample_path_in, sample_path_out):
    """Test ntt cut_video function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    # Conversion to str need for ffmpeg underlying functions
    video_path_in = str(sample_path_in / "ping.mp4")
    video_path_out = str(sample_path_out / "ping_clip.mp4")
    start = 0
    end = 1

    # appel de la fonction de creation de cut
    cut_video(video_path_in, video_path_out, 0, 1)

    video = VideoFileClip(video_path_out)
    assert video.duration == end - start
    video.close()
