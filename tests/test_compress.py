"""Test videos/compress.py ffmeg functions"""

from pathlib import Path

from ntt.videos.compress import compress_video_ffmpeg_cmd, convert_video


def test_compress_video_ffmpeg_cmd(sample_path_in, sample_path_out):
    """Test ntt compress_video_ffmpeg_cmd function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_name_in = "AMIGO-ROBOT_COTE.mp4"
    video_path_out = sample_path_out / "AMIGO-ROBOT_COTE_comp35.mp4"

    ret = compress_video_ffmpeg_cmd(sample_path_in / video_name_in, video_path_out)

    # TODO : Test that it worked as expected
    assert ret == 0
    assert video_path_out.exists()


def test_convert_video(sample_path_in, sample_path_out):
    """Test ntt convert_video function.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """
    video_name_in = "AMIGO-ROBOT_COTE.mp4"
    video_name_out = "AMIGO-ROBOT_COTE_converted.mp4"

    ret = convert_video(sample_path_in, video_name_in, sample_path_out, video_name_out)

    # TODO : Test that it worked as expected
    assert ret == 0
    assert Path(sample_path_out / video_name_out).exists()
