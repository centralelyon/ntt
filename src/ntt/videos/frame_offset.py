"""Split a video into an offset clip and a synced clip at a frame boundary."""

from __future__ import annotations

import math
import os
import shutil
from fractions import Fraction
from typing import Dict, Optional

import ffmpeg


def _parse_frame_rate(raw_value: str) -> float:
    if not raw_value:
        return 0.0
    try:
        return float(Fraction(raw_value))
    except (ValueError, ZeroDivisionError):
        return 0.0


def _find_stream(streams: list, codec_type: str) -> Optional[dict]:
    return next(
        (stream for stream in streams if stream.get("codec_type") == codec_type),
        None,
    )


def _derive_output_path(video_path: str, suffix: str) -> str:
    root, ext = os.path.splitext(os.path.abspath(video_path))
    return f"{root}_{suffix}{ext}"


def _get_frame_count(video_stream: dict, format_info: dict, fps: float) -> int:
    frame_count_raw = video_stream.get("nb_frames")
    if frame_count_raw not in (None, "", "N/A"):
        try:
            return int(frame_count_raw)
        except ValueError:
            pass

    duration_raw = video_stream.get("duration") or format_info.get("duration")
    if duration_raw in (None, "", "N/A"):
        return 0

    try:
        return max(0, int(round(float(duration_raw) * fps)))
    except (TypeError, ValueError):
        return 0


def _video_codec_args(video_stream: dict) -> Dict[str, object]:
    codec_name = (video_stream.get("codec_name") or "").lower()
    frame_rate = _parse_frame_rate(
        video_stream.get("avg_frame_rate") or video_stream.get("r_frame_rate", "")
    )
    args: Dict[str, object] = {}
    if frame_rate > 0:
        args["r"] = frame_rate
    pixel_format = video_stream.get("pix_fmt")
    if pixel_format:
        args["pix_fmt"] = pixel_format

    if codec_name in {"h264", "avc1"}:
        args.update({"vcodec": "libx264", "preset": "slow", "crf": 0})
        return args
    if codec_name in {"hevc", "h265"}:
        args.update({"vcodec": "libx265", "preset": "slow", "x265-params": "lossless=1"})
        return args
    if codec_name == "mpeg4":
        args.update({"vcodec": "mpeg4", "qscale:v": 1})
        return args
    if codec_name == "mjpeg":
        args.update({"vcodec": "mjpeg", "qscale:v": 1})
        return args
    if codec_name == "vp8":
        args.update({"vcodec": "libvpx", "crf": 4, "b:v": 0})
        return args
    if codec_name == "vp9":
        args.update({"vcodec": "libvpx-vp9", "lossless": 1})
        return args
    if codec_name:
        args["vcodec"] = codec_name

    return args


def _audio_codec_args(audio_stream: Optional[dict]) -> Dict[str, object]:
    if audio_stream is None:
        return {}

    codec_name = (audio_stream.get("codec_name") or "").lower()
    if codec_name == "aac":
        return {"acodec": "aac"}
    if codec_name == "mp3":
        return {"acodec": "libmp3lame", "q:a": 0}
    if codec_name == "pcm_s16le":
        return {"acodec": "pcm_s16le"}
    if codec_name == "flac":
        return {"acodec": "flac"}
    if codec_name == "vorbis":
        return {"acodec": "libvorbis", "q:a": 10}
    if codec_name == "opus":
        return {"acodec": "libopus", "b:a": "192k"}
    if codec_name:
        return {"acodec": codec_name}
    return {}


def _run_output(
    video_stream,
    audio_stream,
    output_path: str,
    codec_args: Dict[str, object],
) -> None:
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    streams = [video_stream]
    if audio_stream is not None:
        streams.append(audio_stream)

    try:
        (
            ffmpeg.output(*streams, output_path, **codec_args)
            .overwrite_output()
            .run(quiet=True, capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as exc:
        stderr = exc.stderr.decode("utf-8", errors="replace") if exc.stderr else str(exc)
        raise RuntimeError(f"ffmpeg failed for {output_path}: {stderr.strip()}") from exc


def _resolve_frame_offset(
    frame_offset: Optional[int],
    remove_duration_s: Optional[float],
    fps: float,
) -> int:
    has_frame_offset = frame_offset is not None
    has_remove_duration = remove_duration_s is not None
    if has_frame_offset == has_remove_duration:
        raise ValueError("Provide exactly one of frame_offset or remove_duration_s")

    if has_frame_offset:
        if frame_offset <= 0:
            raise ValueError("frame_offset must be > 0")
        return frame_offset

    if remove_duration_s <= 0:
        raise ValueError("remove_duration_s must be > 0")

    # Align duration-based trimming to the next frame boundary so the kept clip
    # never starts before the requested timestamp.
    resolved_frame_offset = int(math.ceil((remove_duration_s * fps) - 1e-9))
    return max(1, resolved_frame_offset)


def split_video_at_frame_offset(
    video_path_in: str,
    frame_offset: Optional[int] = None,
    offset_path_out: Optional[str] = None,
    synced_path_out: Optional[str] = None,
    *,
    remove_duration_s: Optional[float] = None,
) -> dict:
    """Split a video into ``_offset`` and ``_synced`` files at ``frame_offset``.

    The source video is never modified. The split is frame-accurate for the video
    stream and, when audio exists, trims audio at the matching timestamp.

    Provide either ``frame_offset`` directly or ``remove_duration_s`` to remove a
    duration from the start of the video. Duration-based trimming is converted to
    a frame count using the source fps before the split is applied.
    """

    if not os.path.isfile(video_path_in):
        raise FileNotFoundError(f"Video file not found: {video_path_in}")
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg executable is not available")

    probe = ffmpeg.probe(video_path_in)
    streams = probe.get("streams", [])
    format_info = probe.get("format", {})
    video_stream_info = _find_stream(streams, "video")
    audio_stream_info = _find_stream(streams, "audio")
    if video_stream_info is None:
        raise ValueError(f"No video stream found in: {video_path_in}")

    fps = _parse_frame_rate(
        video_stream_info.get("avg_frame_rate") or video_stream_info.get("r_frame_rate", "")
    )
    if fps <= 0:
        raise ValueError(f"Could not determine a valid fps for: {video_path_in}")

    frame_offset = _resolve_frame_offset(frame_offset, remove_duration_s, fps)
    frame_count = _get_frame_count(video_stream_info, format_info, fps)
    if frame_count and frame_offset >= frame_count:
        raise ValueError(
            f"frame_offset must be smaller than the total frame count ({frame_count})"
        )

    offset_path_out = os.path.abspath(offset_path_out or _derive_output_path(video_path_in, "offset"))
    synced_path_out = os.path.abspath(synced_path_out or _derive_output_path(video_path_in, "synced"))
    input_path_abs = os.path.abspath(video_path_in)
    if input_path_abs in {offset_path_out, synced_path_out}:
        raise ValueError("Output paths must be different from the source video path")
    if offset_path_out == synced_path_out:
        raise ValueError("offset_path_out and synced_path_out must be different")

    split_time_s = frame_offset / fps
    input_stream = ffmpeg.input(video_path_in)

    offset_video = (
        input_stream.video
        .filter("trim", start_frame=0, end_frame=frame_offset)
        .filter("setpts", "PTS-STARTPTS")
    )
    synced_video = (
        input_stream.video
        .filter("trim", start_frame=frame_offset)
        .filter("setpts", "PTS-STARTPTS")
    )

    offset_audio = None
    synced_audio = None
    if audio_stream_info is not None:
        offset_audio = (
            input_stream.audio
            .filter("atrim", start=0, end=split_time_s)
            .filter("asetpts", "PTS-STARTPTS")
        )
        synced_audio = (
            input_stream.audio
            .filter("atrim", start=split_time_s)
            .filter("asetpts", "PTS-STARTPTS")
        )

    codec_args = {
        **_video_codec_args(video_stream_info),
        **_audio_codec_args(audio_stream_info),
    }
    _run_output(offset_video, offset_audio, offset_path_out, codec_args)
    _run_output(synced_video, synced_audio, synced_path_out, codec_args)

    return {
        "input_path": input_path_abs,
        "offset_path": offset_path_out,
        "synced_path": synced_path_out,
        "frame_offset": frame_offset,
        "fps": fps,
        "split_time_s": split_time_s,
        "requested_remove_duration_s": remove_duration_s,
        "frame_count": frame_count,
        "video_codec": video_stream_info.get("codec_name", ""),
        "audio_codec": audio_stream_info.get("codec_name", "") if audio_stream_info else "",
    }
