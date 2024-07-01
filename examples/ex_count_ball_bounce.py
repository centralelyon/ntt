# pylint: disable=C0114
# What is purpose of this example

import logging
import os
from pathlib import Path

import cv2
import dotenv
from ntt.sounds.sound_detection import detect_sound_ref_librosa

BASENAME = f"{Path(__file__).stem}"

# https://peps.python.org/pep-0008/#constants
VIDEO_NAME = "AMIGO-ROBOT_COTE.mp4"
REF_SOUND_NAME = "ping.wav"
FONT_SCALE = 1
TEXT_THICKNESS = 2
OUTPUT_FILE = "out.mp4"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()
    samples_path = Path(ev_path_parent / os.environ.get("PATH_IN"))
    ouput_path = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    logger = logging.getLogger(BASENAME)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(
        filename=ouput_path / f"{BASENAME}.log", encoding="utf-8"
    )
    # fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    video_path = samples_path / VIDEO_NAME

    # TODO : target_sound_start_times not tested ?
    target_sound_start_times = detect_sound_ref_librosa(
        samples_path, VIDEO_NAME, REF_SOUND_NAME
    )

    logger.info(
        "VIDEO_NAME=%s : target_sound_start_times=%s",
        VIDEO_NAME,
        target_sound_start_times,
    )

    video = cv2.VideoCapture(video_path)
    ret, frame = video.read()
    height, width, _ = frame.shape
    video.release()

    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)

    logger.info(
        "VIDEO_NAME=%s : height=%d, width=%d, fps=%d", VIDEO_NAME, height, width, fps
    )

    i = 0
    j = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_color = (255, 255, 255)  # White color
    text_position = (10, 30)  # Left top corner position

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    video_writer = cv2.VideoWriter(
        ouput_path / OUTPUT_FILE, fourcc, fps, (width, height)
    )

    # TODO : remplace while True by a better test
    while True:
        i += 1
        ret, frame = video.read()

        if not ret:
            break

        temps_en_secondes = i / fps

        logger.debug("\ti=%d, j=%d, temps_en_secondes=%d", i, j, temps_en_secondes)

        if (j < len(target_sound_start_times)) and (
            temps_en_secondes >= target_sound_start_times[j]
        ):
            j = j + 1

        height, width, _ = frame.shape

        cv2.putText(
            frame, str(j), text_position, font, FONT_SCALE, text_color, TEXT_THICKNESS
        )
        video_writer.write(frame)

    video.release()
    video_writer.release()
