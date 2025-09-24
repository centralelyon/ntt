import cv2
from ntt.videos.video_generation import random_video


def display_video(video):
    for frame in video:
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1000 // 30) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    display_video(random_video(320, 240, 10, 2))
