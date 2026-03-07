import json
import os
import sys

import cv2
import numpy as np

from ntt.draw.primitives import write_text
from ntt.frames.frame_generation import full_frame
from ntt.videos.io import write_video
from ntt.videos.stich import stitch_2_videos


REFERENCE_SIZE = (900, 360)
VIDEO_SIZE = (640, 360)
FPS = 12
DURATION = 3


def make_panel_frame(dest_pts, base_color, accent_color, label, frame_idx, total_frames):
    frame = full_frame(REFERENCE_SIZE[0], REFERENCE_SIZE[1], (0, 0, 0))

    polygon = np.array(dest_pts, dtype=np.int32)
    cv2.fillConvexPoly(frame, polygon, base_color)
    cv2.polylines(frame, [polygon], True, (255, 255, 255), 4, cv2.LINE_AA)

    x_min = int(np.min(polygon[:, 0]))
    x_max = int(np.max(polygon[:, 0]))
    y_min = int(np.min(polygon[:, 1]))
    y_max = int(np.max(polygon[:, 1]))

    progress = frame_idx / max(total_frames - 1, 1)
    bar_width = 42
    bar_x = int(x_min + 20 + progress * max((x_max - x_min) - 40 - bar_width, 1))
    bar_y0 = y_min + 18
    bar_y1 = y_max - 18

    cv2.rectangle(frame, (bar_x, bar_y0), (bar_x + bar_width, bar_y1), accent_color, -1)
    cv2.circle(
        frame,
        (bar_x + bar_width // 2, (bar_y0 + bar_y1) // 2),
        18,
        (255, 255, 255),
        -1,
    )
    write_text(frame, label, (x_min + 18, y_min + 34), (255, 255, 255), thickness=2)
    write_text(
        frame,
        f"frame {frame_idx + 1}",
        (x_min + 18, y_max - 18),
        accent_color,
        thickness=2,
    )

    return frame


def render_perspective_video(dest_pts, src_pts, base_color, accent_color, label):
    total_frames = FPS * DURATION
    homography = cv2.getPerspectiveTransform(
        np.float32(dest_pts), np.float32(src_pts)
    )

    frames = []
    for frame_idx in range(total_frames):
        reference_frame = make_panel_frame(
            dest_pts, base_color, accent_color, label, frame_idx, total_frames
        )
        warped = cv2.warpPerspective(reference_frame, homography, VIDEO_SIZE)
        frames.append(warped)

    return frames


def write_perspective_json(output_dir, left_name, right_name, left_src, left_dest, right_src, right_dest):
    metadata = {
        "name": "generated_perspective_stitch_demo",
        "videos": [
            {
                "name": left_name,
                "srcPts": left_src.tolist(),
                "destPts": left_dest.tolist(),
            },
            {
                "name": right_name,
                "srcPts": right_src.tolist(),
                "destPts": right_dest.tolist(),
            },
        ],
    }

    json_path = os.path.join(output_dir, "generated_perspective_stitch_demo.json")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(metadata, json_file, indent=2)
    return json_path


def main():
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/app/output/perspective_stitch_demo"
    os.makedirs(output_dir, exist_ok=True)

    left_video_name = "generated_left.avi"
    right_video_name = "generated_right.avi"
    stitched_video_name = "generated_stitched.avi"

    left_dest = np.float32([[60, 70], [450, 70], [450, 290], [60, 290]])
    right_dest = np.float32([[450, 70], [840, 70], [840, 290], [450, 290]])

    left_src = np.float32([[90, 55], [540, 95], [505, 315], [120, 280]])
    right_src = np.float32([[105, 105], [545, 60], [575, 300], [135, 320]])

    left_frames = render_perspective_video(
        left_dest,
        left_src,
        base_color=(35, 110, 245),
        accent_color=(0, 240, 255),
        label="left camera",
    )
    right_frames = render_perspective_video(
        right_dest,
        right_src,
        base_color=(60, 190, 70),
        accent_color=(255, 80, 190),
        label="right camera",
    )

    left_path = write_video(os.path.join(output_dir, left_video_name), left_frames, fps=FPS)
    right_path = write_video(os.path.join(output_dir, right_video_name), right_frames, fps=FPS)
    json_path = write_perspective_json(
        output_dir,
        left_video_name,
        right_video_name,
        left_src,
        left_dest,
        right_src,
        right_dest,
    )

    stitch_2_videos(
        output_dir,
        left_video_name,
        right_video_name,
        output_dir,
        stitched_video_name,
        0,
        left_src.copy(),
        left_dest.copy(),
        right_src.copy(),
        right_dest.copy(),
    )

    print(f"Saved left video: {left_path}")
    print(f"Saved right video: {right_path}")
    print(f"Saved perspective metadata: {json_path}")
    print(f"Saved stitched video: {os.path.join(output_dir, stitched_video_name)}")


if __name__ == "__main__":
    main()
