"""TODO : test_change_video_speed ...
"""

from moviepy.editor import VideoFileClip
from ntt.videos.change_speed import change_video_speed


def test_change_video_speed(sample_path_in, sample_path_out):
    """Test change_video_speed funtion.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_file_in = sample_path_in / "ping.mp4"
    video_file_out = sample_path_out / "ping_speed.mp4"

    change_video_speed(video_file_in, video_file_out, 1)

    # Conversion to str need for ffmpeg underlying functions
    video_in = VideoFileClip(str(video_file_in))
    video_out = VideoFileClip(str(video_file_out))

    # info video_in.reader.nframes does not give the sama values of nb frames
    nb_frames_video_in = video_in.fps * video_in.duration
    nb_frames_video_out = video_out.fps * video_out.duration

    # change of speed 1x does not change videos
    assert nb_frames_video_in == nb_frames_video_out

    change_video_speed(video_file_in, video_file_out, 2)
    
    video_in = VideoFileClip(str(video_file_in))
    video_out = VideoFileClip(str(video_file_out))

    nb_frames_video_in = video_in.fps * video_in.duration
    nb_frames_video_out = video_out.fps * video_out.duration

    # change of speed 2x has less frames
    assert nb_frames_video_in > nb_frames_video_out

    change_video_speed(video_file_in, video_file_out, 0.5)

    video_in = VideoFileClip(str(video_file_in))
    video_out = VideoFileClip(str(video_file_out))

    nb_frames_video_in = video_in.fps * video_in.duration
    nb_frames_video_out = video_out.fps * video_out.duration

    # change of speed .5x has more frames
    assert nb_frames_video_in < nb_frames_video_out
