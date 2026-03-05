"""Technical metadata extraction for videos.

Two backends with the same interface so they can be used interchangeably:

* ``extract_metadata_opencv``  – uses cv2.VideoCapture (no subprocess).
* ``extract_metadata_ffprobe`` – uses ffmpeg-python (already a project dependency).

Both functions:
- Accept a video file path.
- Return a ``dict`` with consistent keys:
  ``width``, ``height``, ``fps``, ``frame_count``, ``duration_s``, ``codec``.
- Raise ``FileNotFoundError`` if the file does not exist.
"""

import os


# ---------------------------------------------------------------------------
# OpenCV backend
# ---------------------------------------------------------------------------

def extract_metadata_opencv(video_path: str) -> dict:
    """Extract technical metadata from a video using OpenCV.

    Args:
        video_path (str): Path to the video file.

    Returns:
        dict: Keys: ``width``, ``height``, ``fps``, ``frame_count``,
              ``duration_s``, ``codec``.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    import cv2

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video: {video_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc_int = int(cap.get(cv2.CAP_PROP_FOURCC))
    codec = "".join(chr((fourcc_int >> (8 * i)) & 0xFF) for i in range(4))
    duration_s = frame_count / fps if fps > 0 else 0.0

    cap.release()

    return {
        "width": width,
        "height": height,
        "fps": fps,
        "frame_count": frame_count,
        "duration_s": duration_s,
        "codec": codec,
    }


# ---------------------------------------------------------------------------
# ffprobe backend
# ---------------------------------------------------------------------------

def extract_metadata_ffprobe(video_path: str) -> dict:
    """Extract technical metadata from a video using ffprobe (via ffmpeg-python).

    Args:
        video_path (str): Path to the video file.

    Returns:
        dict: Keys: ``width``, ``height``, ``fps``, ``frame_count``,
              ``duration_s``, ``codec``.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    import ffmpeg

    probe = ffmpeg.probe(video_path)
    video_stream = next(
        (s for s in probe.get("streams", []) if s.get("codec_type") == "video"),
        None,
    )
    if video_stream is None:
        return {}

    # fps may be encoded as "30/1" or "30000/1001"
    fps_raw = video_stream.get("avg_frame_rate", "0/1")
    try:
        num, den = fps_raw.split("/")
        fps = float(num) / float(den) if float(den) != 0 else 0.0
    except (ValueError, ZeroDivisionError):
        fps = 0.0

    frame_count_raw = video_stream.get("nb_frames")
    frame_count = int(frame_count_raw) if frame_count_raw is not None else 0

    duration_raw = video_stream.get("duration") or probe.get("format", {}).get("duration", "0")
    try:
        duration_s = float(duration_raw)
    except (ValueError, TypeError):
        duration_s = 0.0

    return {
        "width": int(video_stream.get("width", 0)),
        "height": int(video_stream.get("height", 0)),
        "fps": fps,
        "frame_count": frame_count,
        "duration_s": duration_s,
        "codec": video_stream.get("codec_name", ""),
    }
