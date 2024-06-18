# pylint: disable=C0114

import os

from dotenv import load_dotenv
from ntt.videos.dimensions import get_video_dimensions
from ntt.videos.zoom import zoom_xy

if __name__ == "__main__":
    load_dotenv()
    input_video_path = os.path.join(os.environ.get("VIDEO_PATH_IN"), "ping_clip.mp4")
    output_video_path = os.path.join(
        os.environ.get("VIDEO_PATH_IN"), "ping_clip_zoom.mp4"
    )

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
