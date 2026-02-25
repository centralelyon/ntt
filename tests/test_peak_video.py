import os
from ntt.videos.video_generation import generate_peak_video
from ntt.videos.peak import detect_peak_in_video

from ntt.videos.video_generation import random_video


def test_detect_peak_in_video(tmp_path):
    duration, fps = 10, 2
    generate_peak_video("peak_video.mp4", 640, 480, duration, fps)
    assert detect_peak_in_video("peak_video.mp4") == duration

    # remove generated video
    os.remove("peak_video.mp4")


def test_no_peak_in_video():
    import cv2
    fps = 30
    video_frames = random_video(width=640, height=480, fps=fps, duration=2)
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    out = cv2.VideoWriter("no_peak_video.mp4", fourcc, fps, (640, 480))
    for frame in video_frames:
        out.write(frame)
    out.release()

    res = detect_peak_in_video("no_peak_video.mp4")
    print(res)

    os.remove("no_peak_video.mp4")

if __name__ == "__main__":
    #   test_detect_peak_in_video(".")
    test_no_peak_in_video()
