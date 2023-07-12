import cv2
import numpy as np
from ntt.frames.frame_generation import full_frame


def generate_peak_video(file_path, width, height, fps, duration):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(file_path, fourcc, fps, (width, height))
    frame_count = int(fps * duration)

    for i in range(frame_count):
        time = i / fps
        if time < duration / 2:
            intensity = int((time / (duration / 2)) * 255)
        else:
            intensity = int(((duration - time) / (duration / 2)) * 255)

        frame = full_frame(width, height, (intensity, intensity, intensity))

        out.write(frame)

    out.release()
