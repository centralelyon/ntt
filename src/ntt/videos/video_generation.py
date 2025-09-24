import cv2
import numpy as np
from ntt.frames.frame_generation import full_frame, random_frame


def random_video(width: int = 640, height: int = 480, fps: int = 30, duration: int = 1):
    return [random_frame(width, height) for _ in range(int(fps * duration))]


def generate_peak_video(file_path, width, height, fps, duration):
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
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


def generate_video_numbers(t=5, fps=25, size=(800, 600), out_path="myvideo.mp4"):
    num_frames = int(t * fps)

    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    out = cv2.VideoWriter(out_path, fourcc, fps, size)

    for frame_num in range(num_frames):
        frame = np.zeros((size[1], size[0], 3), dtype=np.uint8)  # Black background

        # Display the frame number as text
        text = str(frame_num)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_color = (255, 255, 255)  # White
        text_size = cv2.getTextSize(text, font, font_scale, 2)[0]
        text_x = (size[0] - text_size[0]) // 2
        text_y = (size[1] + text_size[1]) // 2
        cv2.putText(
            frame, text, (text_x, text_y), font, font_scale, font_color, 2, cv2.LINE_AA
        )

        out.write(frame)

    out.release()

    return out_path
