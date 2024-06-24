"""TODO : test_draw_swimming_pool ...
"""

import json

import cv2
from ntt.draw.polygone import draw_polygones


def extract_polygone(json_file_path):
    """Extracting polygone coordinates.

    Args:
        json_file_path (Path or str): json file path

    Returns:
        list of lists: Polygone coordinates
    """
    try:
        with open(json_file_path, "rb") as f:
            data = json.load(f)

        x0, y0 = map(int, data["videos"][1]["srcPts"][0])
        x1, y1 = map(int, data["videos"][1]["srcPts"][1])
        x2, y2 = map(int, data["videos"][1]["srcPts"][2])
        x3, y3 = map(int, data["videos"][1]["srcPts"][3])

        return [[y0, x0], [y1, x1], [y2, x2], [y3, x3]]

    except Exception as e:
        print(f"Exception when trying to open {json_file_path} : {e}")


def test_draw_swimming_pool(sample_path_in, sample_path_out):
    """Draw swimming pool with ntt.

    Args:
        sample_path_in (Path): input path
        sample_path_out (Path): output path
    """

    jsonfile = sample_path_in / "2023_CF_Rennes_freestyle_hommes_50_finaleA.json"
    video_path_in = (
        sample_path_in / "2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4"
    )  # noqa - E501 # pylint: disable=C0301

    # open video
    piscine = extract_polygone(jsonfile)
    try:
        video = cv2.VideoCapture(video_path_in)

        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)

        for coords in piscine:
            assert (
                coords[0] >= 0
                and coords[0] < height
                and coords[1] >= 0
                and coords[1] < width
            )

    except Exception as e:
        print(
            "Exception when trying to extract swimming pool from"
            "{video_path_in} : {e}",
            e,
        )

    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    video_path_out = sample_path_out / "output_piscine.mp4"
    output_video = cv2.VideoWriter(video_path_out, fourcc, fps, (width, height))

    while True:
        # read frame from video
        ret, frame = video.read()
        draw_polygones(frame, piscine, couleur=[0, 255, 0], epaisseur=3)

        # Write the processed frame to the output video
        output_video.write(frame)

        # verify if video reading process is finished
        if not ret:
            break

        # Wait for the 'q' key to quit

    # liberate resources
    video.release()
    output_video.release()
