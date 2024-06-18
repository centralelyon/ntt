# pylint: disable=C0114

import os

import cv2
from dotenv import load_dotenv

from ntt.sounds.sound_detection import detect_sound_ref_librosa

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "AMIGO-ROBOT_COTE.mp4"
REF_SOUND_NAME = "ping.wav"
FONT_SCALE = 1
TEXT_THICKNESS = 2
OUTPUT_FILE = "out.mp4"


if __name__ == "__main__":
    load_dotenv()
    samples_path = os.environ.get("PATH_IN")
    path_out = os.environ.get("PATH_OUT")
    video = os.path.join(samples_path, VIDEO_NAME)

    target_sound_start_times = detect_sound_ref_librosa(
        samples_path, VIDEO_NAME, REF_SOUND_NAME, path_out
    )
    video = cv2.VideoCapture(video)
    ret, frame = video.read()
    height, width, _ = frame.shape
    video.release()
    video = cv2.VideoCapture(video)
    fps = video.get(cv2.CAP_PROP_FPS)
    i = 0
    j = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_color = (255, 255, 255)  # White color
    text_position = (10, 30)  # Left top corner position
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(OUTPUT_FILE, fourcc, fps, (width, height))

    while True:
        i += 1
        ret, frame = video.read()

        if not ret:
            break
        temps_en_secondes = i / fps
        if (
            j < len(target_sound_start_times)
            and temps_en_secondes >= target_sound_start_times[j]
        ):
            j = j + 1
        height, width, _ = frame.shape

        cv2.putText(
            frame, str(j), text_position, font, FONT_SCALE, text_color, TEXT_THICKNESS
        )
        video_writer.write(frame)

    video.release()
    video_writer.release()
