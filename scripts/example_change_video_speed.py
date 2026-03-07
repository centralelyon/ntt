import os
import sys

from ntt.videos.change_speed import change_speed
from ntt.videos.io import write_video
from ntt.videos.video_generation import random_video


def main() -> None:
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/app/output/change_speed_demo"
    backend = sys.argv[2] if len(sys.argv) > 2 else "opencv"
    os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(output_dir, "input.avi")
    output_path = os.path.join(output_dir, f"speed_changed_{backend}.avi")

    frames = random_video(width=160, height=120, fps=8, duration=2)
    write_video(input_path, frames, fps=8)
    change_speed(input_path, output_path, speed_factor=2.0, backend=backend)

    print(f"Saved input video: {input_path}")
    print(f"Saved speed-changed video: {output_path}")


if __name__ == "__main__":
    main()
