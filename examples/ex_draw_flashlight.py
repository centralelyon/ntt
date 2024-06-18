# pylint: disable=C0114

import json
import os

import cv2
from dotenv import load_dotenv
from ntt.draw.primitives import draw_bright_circle


def extract_flash(json_file):
    """_summary_

    Args:
        json_file (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(json_file, "rb") as f:
        data = json.load(f)
    x0, y0 = map(int, data["flash"]["pts"][0])
    x1, y1 = map(int, data["flash"]["pts"][1])
    x2, y2 = map(int, data["flash"]["pts"][2])
    x3, y3 = map(int, data["flash"]["pts"][3])
    return [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]


if __name__ == "__main__":
    load_dotenv()
    jsonfile = os.path.join(
        os.environ.get("PATH_IN"), "2023_CF_Rennes_freestyle_hommes_50_finaleA.json"
    )

    flash = extract_flash(jsonfile)
    # open video
    video = cv2.VideoCapture(
        os.path.join(
            os.environ.get("PATH_IN"),
            "2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4",
        )
    )
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video = cv2.VideoWriter(
        os.path.join(os.environ.get("PATH_IN"), "output_flash.mp4"),
        fourcc,
        fps,
        (width, height),
    )
    while True:
        # read frame from video
        ret, frame = video.read()
        if not ret:
            break
        for x, y in flash:
            draw_bright_circle(frame, (x, y), 20, 100)

        # Write the processed frame to the output video
        output_video.write(frame)

        # verify if reading the video is terminated

        # Wait for the 'q' key to quit
    # liberate resources
    video.release()
    output_video.release()
