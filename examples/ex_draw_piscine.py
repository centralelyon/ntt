# pylint: disable=C0114

import json
import os
from pathlib import Path

import cv2
import dotenv
from ntt.draw.polygone import draw_polygones

# https://peps.python.org/pep-0008/#constants
JSON_FILE_NAME = "2023_CF_Rennes_freestyle_hommes_50_finaleA.json"
VIDEO_NAME_IN = "2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4"
VIDEO_NAME_OUT = "output_piscine.mp4"


def extract_piscine(json_file):
    """This function finds the 4 edges of the swimming pool given the json
    file of a competition.

    Args:
        json_file (Path): Path to the json file containing the competition annotation

    Returns:
        list[list]: list of the pixel coordinates of the four edges od the swimming pool
    """
    with json_file.open("rb") as f:
        data = json.load(f)

    x0, y0 = map(int, data["videos"][1]["srcPts"][0])
    x1, y1 = map(int, data["videos"][1]["srcPts"][1])
    x2, y2 = map(int, data["videos"][1]["srcPts"][2])
    x3, y3 = map(int, data["videos"][1]["srcPts"][3])

    return [[y0, x0], [y1, x1], [y2, x2], [y3, x3]]


if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    jsonfile = path_in / JSON_FILE_NAME

    piscine = extract_piscine(jsonfile)

    # Draw swimming pool with ntt
    # ---------------------------
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
            draw_polygones(frame, piscine, couleur=[0, 255, 0], epaisseur=3)

            # Write the processed frame to the output video
            output_video.write(frame)

    # Free resources
    video.release()
    output_video.release()
