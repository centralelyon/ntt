import cv2
import numpy as np

from ntt.draw.primitives import draw_crosshair, draw_line, draw_rectangle, write_text
from ntt.frames.frame_crop import crop as crop_frame
from ntt.frames.processing import blur_frame as blur_frame_processing
from ntt.frames.processing import rotate as rotate_frame_processing


def resize_frame(frame: np.ndarray, width: int, height: int) -> np.ndarray:
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_LINEAR)


def rotate_frame(frame: np.ndarray, angle: float) -> np.ndarray:
    return rotate_frame_processing(frame, angle)


def flip_frame(frame: np.ndarray, mode: str = "horizontal") -> np.ndarray:
    flip_codes = {"horizontal": 1, "vertical": 0, "both": -1}
    if mode not in flip_codes:
        raise ValueError("mode must be one of: horizontal, vertical, both")
    return cv2.flip(frame, flip_codes[mode])


def grayscale_frame(frame: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def blur_frame(frame: np.ndarray, kernel_size=(5, 5), region=None) -> np.ndarray:
    return blur_frame_processing(frame, kernel_size=kernel_size, region=region)


def annotate_frame(
    frame: np.ndarray,
    text: str | None = None,
    text_position=(10, 30),
    rectangle=None,
    line=None,
    crosshair=None,
    color=(0, 255, 0),
) -> np.ndarray:
    annotated = frame.copy()
    if text is not None:
        write_text(annotated, text, text_position, color)
    if rectangle is not None:
        draw_rectangle(annotated, rectangle, color)
    if line is not None:
        draw_line(annotated, line[0], line[1], color)
    if crosshair is not None:
        draw_crosshair(
            annotated,
            x=crosshair["x"],
            y=crosshair["y"],
            text=crosshair.get("text", ""),
            color=color,
            cross_size=crosshair.get("size", 12),
            draw_circle=crosshair.get("draw_circle", True),
        )
    return annotated


def transform_frame(frame: np.ndarray, operations: list[dict]) -> np.ndarray:
    """Apply a sequential list of transform operations to a frame."""
    result = frame.copy()
    for operation in operations:
        name = operation["name"]
        params = operation.get("params", {})

        if name == "resize":
            result = resize_frame(result, params["width"], params["height"])
        elif name == "rotate":
            result = rotate_frame(result, params["angle"])
        elif name == "flip":
            result = flip_frame(result, params.get("mode", "horizontal"))
        elif name == "grayscale":
            result = grayscale_frame(result)
        elif name == "blur":
            result = blur_frame(
                result,
                kernel_size=params.get("kernel_size", (5, 5)),
                region=params.get("region"),
            )
        elif name == "annotate":
            result = annotate_frame(result, **params)
        elif name == "crop":
            result = crop_frame(
                result, params["x1"], params["y1"], params["x2"], params["y2"]
            )
        else:
            raise ValueError(f"Unknown operation: {name}")

    return result
