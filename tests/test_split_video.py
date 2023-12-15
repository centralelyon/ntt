from ntt.videos.split_video import split_video_ffmpeg
import os
from dotenv import load_dotenv
import pytest

load_dotenv()


def test_split_video_negative_n():
    video_path_in = os.environ.get("NTT_SAMPLES_PATH_IN")
    video_name = "swimming_start_small.mp4"
    output_path = os.environ.get("PATH_OUT")
    n = -5  # Test with a negative value for n

    with pytest.raises(ValueError) as e:
        split_video_ffmpeg(video_path_in, video_name, output_path, n)

    assert str(e.value) == "Number of segments (n) must be greater than zero."


if __name__ == "__main__":
    test_split_video_negative_n()
