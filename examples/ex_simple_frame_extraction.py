# pylint: disable=C0114

import os
from pathlib import Path

import dotenv
from ntt.frames.frame_extraction import extract_first_frame

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    if not path_out.exists():
        path_out.mkdir()

    output = extract_first_frame(
        video_path_in=path_in,
        video_name_in="crop.mp4",
        frame_path_out=path_out,
        frame_name_out="crop-ex.jpg",
    )

    if output is None:
        print("Frame extraction failed")
    else:
        print(f"Frame successfully extracted at {output}")
