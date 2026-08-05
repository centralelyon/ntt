import cv2
import sys
from ntt.videos.video_generation import random_video


def display_video(video):
    for frame in video:
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1000 // 30) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


def display_frames_as_video(frames: list) -> None:
    pass


if __name__ == "__main__":
    video = random_video(320, 240, 10, 2)
    print(f"Generated video: frames={len(video)}")
    if "--display" in sys.argv:
        display_video(video)
