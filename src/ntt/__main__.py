"""CLI dispatcher for ntt.

Usage:
    python -m ntt <command> [--json] <file>

Available commands:
    extract_exif_pillow     Extract EXIF from an image using Pillow
    extract_exif_exifread   Extract EXIF from an image using ExifRead
    extract_video_meta_cv   Extract metadata from a video using OpenCV
    extract_video_meta_ff   Extract metadata from a video using ffprobe
    extract_all_frames      Extract all frames from a video to the same folder
    generate_random_image   Generate a random JPEG with injected EXIF metadata
    change_speed            Change video speed with OpenCV, ffmpeg, or MoviePy
    change_video_speed      Backward-compatible alias for change_speed

Examples:
    python -m ntt extract_exif_pillow photo.jpg
    python -m ntt extract_exif_pillow --json photo.jpg
    python -m ntt extract_video_meta_cv video.mp4
    python -m ntt extract_all_frames video.mp4
    python -m ntt generate_random_image
    python -m ntt generate_random_image --output /app/myimage.jpg
    python -m ntt change_speed input.avi --output output.avi --factor 2 --backend ffmpeg
    python -m ntt change_video_speed input.avi --output output.avi --factor 2 --backend ffmpeg
"""

import sys
import json as _json


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _print(data: dict, as_json: bool) -> None:
    if as_json:
        print(_json.dumps(data, default=str, indent=2))
    else:
        if not data:
            print("(no data)")
        for key, value in sorted(data.items()):
            print(f"  {key}: {value}")


def _parse(argv, expected_args=1):
    """Returns (as_json, positional_args)."""
    as_json = "--json" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) < expected_args:
        return as_json, None
    return as_json, args


# ---------------------------------------------------------------------------
# Command implementations
# ---------------------------------------------------------------------------

def _cmd_extract_exif_pillow(argv):
    as_json, args = _parse(argv)
    if not args:
        print("Usage: python -m ntt extract_exif_pillow [--json] <image_path>")
        sys.exit(1)
    from ntt.frames.exif import extract_exif_pillow
    data = extract_exif_pillow(args[0])
    _print(data, as_json)


def _cmd_extract_exif_exifread(argv):
    as_json, args = _parse(argv)
    if not args:
        print("Usage: python -m ntt extract_exif_exifread [--json] <image_path>")
        sys.exit(1)
    from ntt.frames.exif import extract_exif_exifread
    data = extract_exif_exifread(args[0])
    _print(data, as_json)


def _cmd_extract_video_meta_cv(argv):
    as_json, args = _parse(argv)
    if not args:
        print("Usage: python -m ntt extract_video_meta_cv [--json] <video_path>")
        sys.exit(1)
    from ntt.videos.exif import extract_metadata_opencv
    data = extract_metadata_opencv(args[0])
    _print(data, as_json)


def _cmd_extract_video_meta_ff(argv):
    as_json, args = _parse(argv)
    if not args:
        print("Usage: python -m ntt extract_video_meta_ff [--json] <video_path>")
        sys.exit(1)
    from ntt.videos.exif import extract_metadata_ffprobe
    data = extract_metadata_ffprobe(args[0])
    _print(data, as_json)


def _cmd_extract_all_frames(argv):
    as_json, args = _parse(argv)
    if not args:
        print("Usage: python -m ntt extract_all_frames <video_path>")
        sys.exit(1)
    import os
    import cv2
    video_path = args[0]
    if not os.path.isfile(video_path):
        print(f"Error: file '{video_path}' not found.")
        sys.exit(1)
    video_dir = os.path.dirname(os.path.abspath(video_path))
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    cap = cv2.VideoCapture(video_path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Extracting {total} frames to {video_dir}...")
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(video_dir, f"{video_name}_frame_{count:04d}.jpg"), frame)
        count += 1
    cap.release()
    if as_json:
        print(_json.dumps({"frames_extracted": count, "output_dir": video_dir}))
    else:
        print(f"Done: {count} frames extracted.")


def _cmd_generate_random_image(argv):
    """Generate a random image with EXIF metadata.

    Uses ntt.frames.frame_generation.random_frame to create the image.
    Saves as JPEG (PNG does not support EXIF).
    Default output: ./random_img.jpg
    """
    import datetime
    import os
    import cv2
    from ntt.frames.frame_generation import random_frame
    from ntt.frames.exif import inject_exif

    as_json, _ = _parse(argv)

    # Parse optional --output flag
    output_path = "random_img.jpg"
    for i, arg in enumerate(argv):
        if arg == "--output" and i + 1 < len(argv):
            output_path = argv[i + 1]
            break

    # Ensure .jpg extension (EXIF requires JPEG)
    if not output_path.lower().endswith((".jpg", ".jpeg")):
        output_path = os.path.splitext(output_path)[0] + ".jpg"

    # Use ntt random frame generator (returns a BGR numpy array, width x height x 3)
    frame = random_frame(width=256, height=256)
    cv2.imwrite(output_path, frame)

    # Inject EXIF metadata
    metadata = {
        "Make":             "ntt",
        "Model":            "random_frame_generator",
        "DateTime":         datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S"),
        "ImageDescription": "Randomly generated image by ntt",
        "Software":         "ntt/__main__.py",
    }
    inject_exif(output_path, metadata)

    if as_json:
        print(_json.dumps({"output": output_path, "metadata": metadata}))
    else:
        print(f"Saved: {output_path}")
        for k, v in metadata.items():
            print(f"  {k}: {v}")


def _cmd_change_speed(argv):
    if not argv:
        print(
            "Usage: python -m ntt change_speed <video_path> --output <out_path> "
            "[--factor <speed_factor>] [--backend opencv|ffmpeg|moviepy]"
        )
        sys.exit(1)

    video_path_in = argv[0]
    video_path_out = "video_speed_changed.avi"
    speed_factor = 1.0
    backend = "opencv"

    for i, arg in enumerate(argv):
        if arg == "--output" and i + 1 < len(argv):
            video_path_out = argv[i + 1]
        elif arg == "--factor" and i + 1 < len(argv):
            speed_factor = float(argv[i + 1])
        elif arg == "--backend" and i + 1 < len(argv):
            backend = argv[i + 1]

    from ntt.videos.change_speed import change_speed

    output = change_speed(
        video_path_in=video_path_in,
        video_path_out=video_path_out,
        speed_factor=speed_factor,
        backend=backend,
    )
    print(f"Saved: {output}")


def _cmd_enrich_exif(argv):
    """Read a JSON array of file entries and enrich image entries with EXIF data.

    Each entry must have ``path`` (directory) and ``name`` (filename) fields.
    EXIF data is added under ``exif_pillow`` and ``exif_exifread`` keys.
    Non-image files or files with no EXIF are enriched with empty dicts.

    Usage:
        python -m ntt enrich_exif [--json] <file.json>
        python -m ntt enrich_exif [--json] -   (read from stdin)
    """
    import os
    import sys
    from ntt.frames.exif import extract_exif_pillow, extract_exif_exifread

    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".tiff", ".tif", ".png", ".bmp", ".webp"}

    as_json, _ = _parse(argv)
    sources = [a for a in argv if not a.startswith("--")]

    if not sources:
        print("Usage: python -m ntt enrich_exif [--json] <file.json | ->")
        sys.exit(1)

    src = sources[0]
    if src == "-":
        raw = sys.stdin.read()
    else:
        if not os.path.isfile(src):
            print(f"Error: file '{src}' not found.")
            sys.exit(1)
        with open(src, "r", encoding="utf-8") as f:
            raw = f.read()

    entries = _json.loads(raw)
    if not isinstance(entries, list):
        entries = [entries]

    for entry in entries:
        if entry.get("type") != "file":
            continue
        name = entry.get("name", "")
        ext = os.path.splitext(name)[1].lower()
        if ext not in IMAGE_EXTENSIONS:
            continue
        file_path = os.path.join(entry.get("path", "."), name)
        try:
            entry["exif_pillow"]   = extract_exif_pillow(file_path)
            entry["exif_exifread"] = extract_exif_exifread(file_path)
        except FileNotFoundError:
            entry["exif_pillow"]   = {}
            entry["exif_exifread"] = {}

    print(_json.dumps(entries, default=str, indent=2))


# ---------------------------------------------------------------------------
# Dispatch table
# ---------------------------------------------------------------------------

COMMANDS = {
    "extract_exif_pillow":   _cmd_extract_exif_pillow,
    "extract_exif_exifread": _cmd_extract_exif_exifread,
    "extract_video_meta_cv": _cmd_extract_video_meta_cv,
    "extract_video_meta_ff": _cmd_extract_video_meta_ff,
    "extract_all_frames":    _cmd_extract_all_frames,
    "generate_random_image": _cmd_generate_random_image,
    "change_speed":          _cmd_change_speed,
    "change_video_speed":    _cmd_change_speed,
    "enrich_exif":           _cmd_enrich_exif,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Commands:")
        for name in COMMANDS:
            print(f"  {name}")
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd not in COMMANDS:
        print(f"Unknown command: '{cmd}'")
        print(f"Available: {', '.join(COMMANDS)}")
        sys.exit(1)

    try:
        COMMANDS[cmd](sys.argv[2:])
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
