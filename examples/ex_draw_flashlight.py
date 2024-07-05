# pylint: disable=C0114

import json
import os
from pathlib import Path

import cv2
import dotenv

from ntt.draw.primitives import draw_bright_circle


# https://peps.python.org/pep-0008/#constants
JSON_FILE_NAME = "2023_CF_Rennes_freestyle_hommes_50_finaleA.json"
VIDEO_NAME_IN = "2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4"
VIDEO_NAME_OUT = "output_flash.mp4"


def extract_flash(json_file):
    """_summary_

    Args:
        json_file (Path): Path to the json file containing the competition annotation

    Returns:
        _type_: _description_
    """
    with json_file.open("rb") as f:
        data = json.load(f)

    x0, y0 = map(int, data["flash"]["pts"][0])
    x1, y1 = map(int, data["flash"]["pts"][1])
    x2, y2 = map(int, data["flash"]["pts"][2])
    x3, y3 = map(int, data["flash"]["pts"][3])

    return [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]


if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    jsonfile = path_in / JSON_FILE_NAME

    flash = extract_flash(jsonfile)

    # Open video
    video = cv2.VideoCapture(path_in / VIDEO_NAME_IN)

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    output_video = cv2.VideoWriter(
        path_out / VIDEO_NAME_OUT,
        fourcc,
        fps,
        (width, height),
    )

    got_frame = True  # pylint: disable=C0103
    while got_frame:
        # Read frame from video
        got_frame, frame = video.read()

        if got_frame:
            for x, y in flash:
                draw_bright_circle(frame, (x, y), 20, 100)

            # Write the processed frame to the output video
            output_video.write(frame)

    # Free resources
    video.release()
    output_video.release()
