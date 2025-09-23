from ntt.videos.video_generation import generate_peak_video
from ntt.videos.peak import detect_peak_in_video


def test_detect_peak_in_video(tmp_path):
    duration, fps = 10, 2
    generate_peak_video("peak_video.mp4", 640, 480, duration, fps)
    assert detect_peak_in_video("peak_video.mp4") == duration


if __name__ == "__main__":
    test_detect_peak_in_video(".")
