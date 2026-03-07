import os

import cv2

from ntt.utils.constants import DEFAULT_FOURCC, FOURCC_MP4V


def get_writer_fourcc(video_path: str) -> int:
    """Return a container-compatible fourcc for the output path."""
    if video_path.lower().endswith(".mp4"):
        return FOURCC_MP4V
    return DEFAULT_FOURCC


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


def write(video_path: str, frames: list, fps: int = 30) -> str:
    if not frames:
        raise ValueError("No frames to write.")

    height, width, _ = frames[0].shape
    os.makedirs(os.path.dirname(video_path) or ".", exist_ok=True)
    out = cv2.VideoWriter(
        video_path, get_writer_fourcc(video_path), fps, (width, height)
    )

    if not out.isOpened():
        raise ValueError(f"Could not open video writer for: {video_path}")

    for frame in frames:
        if frame.shape[:2] != (height, width):
            raise ValueError("All frames must have the same width and height.")
        out.write(frame)

    out.release()
    return video_path


if __name__ == "__main__":
    from ntt.videos.video_generation import random_video
    video_path = "path_to_your_video.mp4"
    frames = random_video(320, 240, 10, 30)
    write("output_video.mp4", frames)
    frames = read("output_video.mp4")
    print(f"Total frames extracted: {len(frames)}")
