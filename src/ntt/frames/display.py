import cv2
import numpy as np
import sys


def display_frame(frame: np.ndarray) -> None:
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def display_video_as_frames(video: list = None) -> None:
    for frame in video:
        display_frame(frame)


if __name__ == "__main__":
    from ntt.frames.frame_generation import random_frame
    from ntt.videos.video_generation import random_video

    frame = random_frame()
    video = random_video()
    print(f"Generated frame: shape={frame.shape}, dtype={frame.dtype}")
    print(f"Generated video: frames={len(video)}")
    if "--display" in sys.argv:
        display_frame(frame)
        display_video_as_frames(video)
