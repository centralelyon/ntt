import argparse
from pathlib import Path

from ntt.videos.frame_offset import split_video_at_frame_offset


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Split a video into <name>_offset and <name>_synced by moving the first "
            "N frames, or the first duration converted to frames from the source fps, "
            "into the _offset file without touching the source file."
        )
    )
    parser.add_argument("video_path", help="Path to the source video")
    parser.add_argument(
        "frame_offset",
        nargs="?",
        type=int,
        help="Number of leading frames to move",
    )
    parser.add_argument(
        "--remove-duration-s",
        type=float,
        default=None,
        help="Remove this many seconds from the beginning by converting it to frames using the source fps",
    )
    parser.add_argument(
        "--offset-path",
        default=None,
        help="Optional explicit path for the _offset output",
    )
    parser.add_argument(
        "--synced-path",
        default=None,
        help="Optional explicit path for the _synced output",
    )
    return parser


def _derive_output_path(video_path: str, suffix: str) -> str:
    path = Path(video_path).resolve()
    return str(path.with_name(f"{path.stem}_{suffix}{path.suffix}"))


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if (args.frame_offset is None) == (args.remove_duration_s is None):
        parser.error("Provide exactly one of frame_offset or --remove-duration-s")

    planned_offset_path = args.offset_path or _derive_output_path(args.video_path, "offset")
    planned_synced_path = args.synced_path or _derive_output_path(args.video_path, "synced")

    print("Step 1/4: validate inputs")
    print(f"Input video: {Path(args.video_path).resolve()}")
    if args.frame_offset is not None:
        print(f"Leading frames to move: {args.frame_offset}")
    else:
        print(f"Leading duration to remove (s): {args.remove_duration_s}")

    print("Step 2/4: prepare output files")
    print(f"Offset clip will be written to: {planned_offset_path}")
    print(f"Synced clip will be written to: {planned_synced_path}")

    print("Step 3/4: split video with ffmpeg")
    result = split_video_at_frame_offset(
        args.video_path,
        args.frame_offset,
        offset_path_out=args.offset_path,
        synced_path_out=args.synced_path,
        remove_duration_s=args.remove_duration_s,
    )

    print("Step 4/4: done")
    print(f"Source video left unchanged: {result['input_path']}")
    print(f"Saved offset clip: {result['offset_path']}")
    print(f"Saved synced clip: {result['synced_path']}")
    print(f"Removed leading frames: {result['frame_offset']}")
    if result["requested_remove_duration_s"] is not None:
        print(f"Requested remove duration (s): {result['requested_remove_duration_s']:.6f}")
    print(f"Split timestamp (s): {result['split_time_s']:.6f}")


if __name__ == "__main__":
    main()
