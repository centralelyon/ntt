import os
import sys

import cv2

from ntt.frames.frame_extraction import extract_first_frame
from ntt.videos.video_generation import generate_video_numbers


def main() -> None:
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    video_path = os.path.join(output_dir, "numbered_video.avi")
    frame_path = os.path.join(output_dir, "numbered_video_first_frame.jpg")

    generate_video_numbers(t=2, fps=5, size=(320, 240), out_path=video_path)
    extracted = extract_first_frame(
        video_path_in=output_dir,
        video_name_in=os.path.basename(video_path),
        frame_path_out=output_dir,
        frame_name_out=os.path.basename(frame_path),
    )

    frame = cv2.imread(extracted)
    print(f"Saved video: {video_path}")
    print(f"Saved first frame: {extracted}")
    print(f"First frame shape: {frame.shape}")


if __name__ == "__main__":
    main()
