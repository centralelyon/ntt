import cv2

from ntt.utils.constants import DEFAULT_FOURCC
from ntt.videos.video_generation import random_video


def read(video_path: str) -> list:
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames


def write(video_path: str, frames: list) -> None:
    if not frames:
        print("No frames to write.")
        return

    height, width, _ = frames[0].shape
    out = cv2.VideoWriter(video_path, DEFAULT_FOURCC, 30, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()


if __name__ == "__main__":

    video_path = "path_to_your_video.mp4"
    frames = random_video(320, 240, 10, 30)
    write("output_video.mp4", frames)
    frames = read("output_video.mp4")
    print(f"Total frames extracted: {len(frames)}")
