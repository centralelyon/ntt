import os

import ffmpeg

from ntt.videos.exif import extract_metadata_ffprobe, extract_metadata_opencv


def extract_video_info_opencv(video_path: str) -> dict:
    """Return unified video info using OpenCV only."""
    metadata = extract_metadata_opencv(video_path)
    width = metadata.get("width", 0)
    height = metadata.get("height", 0)
    return {
        **metadata,
        "resolution": {"width": width, "height": height},
        "audio_present": None,
    }


def extract_video_info_ffprobe(video_path: str) -> dict:
    """Return unified video info using ffprobe."""
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    metadata = extract_metadata_ffprobe(video_path)
    probe = ffmpeg.probe(video_path)
    streams = probe.get("streams", [])
    audio_present = any(stream.get("codec_type") == "audio" for stream in streams)
    width = metadata.get("width", 0)
    height = metadata.get("height", 0)

    return {
        **metadata,
        "resolution": {"width": width, "height": height},
        "audio_present": audio_present,
    }


def extract_video_info(video_path: str, backend: str = "auto") -> dict:
    """Return unified video info with optional backend selection."""
    if backend == "opencv":
        return extract_video_info_opencv(video_path)
    if backend == "ffprobe":
        return extract_video_info_ffprobe(video_path)
    if backend != "auto":
        raise ValueError(f"Unknown backend: {backend}")

    try:
        return extract_video_info_ffprobe(video_path)
    except Exception:
        return extract_video_info_opencv(video_path)
