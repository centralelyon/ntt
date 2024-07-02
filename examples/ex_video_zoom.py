# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.videos.dimensions import get_video_dimensions
from ntt.videos.zoom import zoom_xy

# https://peps.python.org/pep-0008/#constants
# TODO : videos not in samples folder
VIDEO_IN_NAME = "ping.mp4"
VIDEO_OUT_NAME = "ping_zoom.mp4"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    input_video_path = path_in / VIDEO_IN_NAME
    output_video_path = path_out / VIDEO_OUT_NAME

    width, height = get_video_dimensions(input_video_path)

    if width is not None and height is not None:
        zoom_x = width / 2
        zoom_y = height / 2
        zoom_duration = 2.0  # pylint: disable=C0103

        zoom_xy(
            input_video_path,
            output_video_path,
            zoom_x,
            zoom_y,
            zoom_duration,
            (width, height),
        )
    else:
        print(f"{width=},{height=} for {input_video_path=}")
