import os
import cv2
from moviepy import editor
from ntt.videos.create_clip import cut_video


def test_cut_video():
    video_in = os.path.join("samples", "ping.mp4")
    video_out = os.path.join("output", "ping_clip.mp4")
    start = 0
    end = 1

    if not os.path.exists("output"):
        os.makedirs("output")

    # appel de la fonction de creation de cut
    cut_video(video_in, video_out, 0, 1)

    video = editor.VideoFileClip(video_out)
    assert video.duration == end - start
    video.close()


if __name__ == "__main__":
    test_cut_video()
