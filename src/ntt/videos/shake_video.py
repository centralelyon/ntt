import os, cv2
import numpy as np
from moviepy.editor import VideoClip
from ntt.utils.random import random_translate_direction
from ntt.frames.processing import rotate


def shake_video_randomly(video_path_in, video_name, shake_intensity, video_path_out):
    video = os.path.join(video_path_in, video_name)
    video = cv2.VideoCapture(video)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))
    while True:
        ret, frame = video.read()
        if not ret:
            break
        h, w, _ = frame.shape
        direction = random_translate_direction()
        frame1 = np.zeros_like(frame)
        if direction == "up":
            frame1[: h - shake_intensity] = frame[shake_intensity:h]
        elif direction == "left":
            frame1[:, : w - shake_intensity] = frame[:, shake_intensity:w]
        elif direction == "down":
            frame1[shake_intensity:h] = frame[: h - shake_intensity]
        else:
            frame1[:, shake_intensity:w] = frame[:, : w - shake_intensity]
        video_writer.write(frame1)
    video_writer.release()
    video.release()


def rotate_video(video_path_in, video_name, rotation_increment, video_path_out):
    video = os.path.join(video_path_in, video_name)

    video = cv2.VideoCapture(video)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    video_writer = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))
    while True:
        ret, frame = video.read()
        if not ret:
            break
        direction = np.random.choice([-1, 1])
        result = rotate(frame, rotation_increment * direction)
        rotation_increment = rotation_increment * direction
        video_writer.write(result)
    video_writer.release()
    video.release()
