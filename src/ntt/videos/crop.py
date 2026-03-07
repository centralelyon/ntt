import os
import subprocess

import cv2

from ntt.videos.io import get_writer_fourcc


def _validate_crop_box(x1: int, y1: int, x2: int, y2: int) -> tuple[int, int]:
    if x2 <= x1 or y2 <= y1:
        raise ValueError("Invalid crop box: x2/y2 must be greater than x1/y1.")
    return x2 - x1, y2 - y1


def _resize_with_zoom(frame, width: int, height: int, zoom_factor: float):
    if zoom_factor <= 0:
        raise ValueError("zoom_factor must be greater than 0.")

    if zoom_factor == 1:
        return frame

    resized_width = max(1, int(round(width * zoom_factor)))
    resized_height = max(1, int(round(height * zoom_factor)))
    resized = cv2.resize(
        frame, (resized_width, resized_height), interpolation=cv2.INTER_LINEAR
    )

    if zoom_factor > 1:
        start_x = max(0, (resized_width - width) // 2)
        start_y = max(0, (resized_height - height) // 2)
        return resized[start_y:start_y + height, start_x:start_x + width]

    canvas = cv2.copyMakeBorder(
        resized,
        (height - resized_height) // 2,
        height - resized_height - (height - resized_height) // 2,
        (width - resized_width) // 2,
        width - resized_width - (width - resized_width) // 2,
        cv2.BORDER_CONSTANT,
        value=(0, 0, 0),
    )
    return canvas


def crop_video_opencv(
    input_path: str,
    output_path: str,
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    zoom_factor: float = 1.0,
) -> str:
    width, height = _validate_crop_box(x1, y1, x2, y2)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open input video: {input_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    writer = cv2.VideoWriter(
        output_path, get_writer_fourcc(output_path), fps, (width, height)
    )
    if not writer.isOpened():
        cap.release()
        raise ValueError(f"Could not open output video: {output_path}")

    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break

        cropped = frame[y1:y2, x1:x2]
        if cropped.shape[:2] != (height, width):
            writer.release()
            cap.release()
            raise ValueError("Crop box is out of bounds for at least one frame.")

        writer.write(_resize_with_zoom(cropped, width, height, zoom_factor))

    cap.release()
    writer.release()
    return output_path


def crop_video_moviepy(
    input_path: str,
    output_path: str,
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    zoom_factor: float = 1.0,
) -> str:
    from moviepy.editor import VideoFileClip

    width, height = _validate_crop_box(x1, y1, x2, y2)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    clip = VideoFileClip(input_path)
    try:
        cropped = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        if zoom_factor != 1.0:
            cropped = cropped.resize(zoom_factor)
            if zoom_factor > 1:
                cropped = cropped.crop(
                    x_center=cropped.w / 2,
                    y_center=cropped.h / 2,
                    width=width,
                    height=height,
                )
            else:
                cropped = cropped.on_color(
                    size=(width, height),
                    color=(0, 0, 0),
                    pos=("center", "center"),
                )
        cropped.write_videofile(
            output_path, codec="libx264", audio_codec="aac", logger=None
        )
    finally:
        clip.close()

    return output_path


def crop_video_ffmpeg(
    input_path: str,
    output_path: str,
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    zoom_factor: float = 1.0,
) -> str:
    width, height = _validate_crop_box(x1, y1, x2, y2)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    filter_chain = [f"crop={width}:{height}:{x1}:{y1}"]
    if zoom_factor != 1.0:
        scaled_width = max(1, int(round(width * zoom_factor)))
        scaled_height = max(1, int(round(height * zoom_factor)))
        filter_chain.append(f"scale={scaled_width}:{scaled_height}")
        if zoom_factor > 1:
            offset_x = max(0, (scaled_width - width) // 2)
            offset_y = max(0, (scaled_height - height) // 2)
            filter_chain.append(f"crop={width}:{height}:{offset_x}:{offset_y}")
        else:
            pad_x = max(0, (width - scaled_width) // 2)
            pad_y = max(0, (height - scaled_height) // 2)
            filter_chain.append(f"pad={width}:{height}:{pad_x}:{pad_y}:black")

    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-vf",
        ",".join(filter_chain),
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "23",
        "-c:a",
        "copy",
        output_path,
    ]
    subprocess.run(ffmpeg_cmd, check=True)
    return output_path


def crop_video(
    input_path: str,
    output_path: str,
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    backend: str = "opencv",
    zoom_factor: float = 1.0,
) -> str:
    if backend == "opencv":
        return crop_video_opencv(input_path, output_path, x1, y1, x2, y2, zoom_factor)
    if backend == "moviepy":
        return crop_video_moviepy(input_path, output_path, x1, y1, x2, y2, zoom_factor)
    if backend == "ffmpeg":
        return crop_video_ffmpeg(input_path, output_path, x1, y1, x2, y2, zoom_factor)
    raise ValueError(f"Unknown crop backend: {backend}")
