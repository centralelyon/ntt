import os
import cv2
from ntt.videos.video_generation import generate_peak_video
from ntt.videos.peak import detect_peak_in_video

from ntt.videos.video_generation import random_video
from ntt.videos.io import write_video
from ntt.frames.frame_generation import full_frame


def test_detect_peak_in_video(tmp_path):
    duration, fps = 10, 2
    video_path = "peak_video.avi"
    generate_peak_video(video_path, 640, 480, duration, fps)
    assert detect_peak_in_video(video_path) == duration

    # remove generated video
    os.remove(video_path)


def test_no_peak_in_video():
    fps = 30
    video_path = "no_peak_video.avi"
    video_frames = random_video(width=640, height=480, fps=fps, duration=2)
    write_video(video_path, video_frames, fps=fps)

    res = detect_peak_in_video(video_path)
    print(res)

    os.remove(video_path)


def test_detect_peak_video_writes_playable_output_without_animation(tmp_path):
    from ntt.videos.peak import detect_peak_video

    input_video = tmp_path / "input.avi"
    output_video = tmp_path / "flash.avi"
    frames = [full_frame(80, 60, (0, 0, 0)) for _ in range(5)]
    frames[2][:, :] = (255, 255, 255)
    write_video(str(input_video), frames, fps=5)

    frame_index = detect_peak_video(
        input_path=str(tmp_path),
        video_name_in=input_video.name,
        output_path=str(tmp_path),
        video_name_out=output_video.name,
        xa=0,
        xb=80,
        ya=0,
        yb=60,
        seuil=200,
        afficher_anime=False,
        afficher_hist=False,
        write_video=True,
    )

    assert frame_index >= 0
    assert output_video.is_file()

    cap = cv2.VideoCapture(str(output_video))
    assert cap.isOpened()
    assert int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) > 0
    assert int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) == 80
    assert int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) == 60
    cap.release()

if __name__ == "__main__":
    #   test_detect_peak_in_video(".")
    test_no_peak_in_video()
