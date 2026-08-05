from __future__ import annotations

import argparse
import json
from pathlib import Path

from ntt.frames.exif import extract_exif_exifread, extract_exif_pillow


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".tif", ".tiff", ".png", ".bmp", ".webp"}


def build_flatdir_with_exif(root: Path, depth: int | None = 0) -> list[dict[str, object]]:
    try:
        from flatdir.listing import list_entries
    except ImportError as exc:
        raise SystemExit(
            "This example requires flatdir and Python 3.10+. Install it with: "
            "python -m pip install flatdir"
        ) from exc

    root = root.resolve()
    entries = list_entries(
        root,
        depth=depth,
        match=r"\.(jpg|jpeg|tif|tiff|png|bmp|webp)$",
        ignore_typical=True,
    )

    for entry in entries:
        if entry.get("type") != "file":
            continue

        filename = str(entry.get("name", ""))
        if Path(filename).suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        image_path = root / str(entry.get("path", ".")) / filename
        try:
            entry["exif_pillow"] = extract_exif_pillow(str(image_path))
            entry["exif_exifread"] = extract_exif_exifread(str(image_path))
        except FileNotFoundError:
            entry["exif_pillow"] = {}
            entry["exif_exifread"] = {}

    return entries


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a flatdir JSON listing and enrich image entries with ntt EXIF extraction."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Folder to index with flatdir. Defaults to the current directory.",
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=0,
        help="Maximum traversal depth passed to flatdir. Use -1 for unlimited depth.",
    )
    parser.add_argument(
        "--output",
        help="Optional JSON output file. Defaults to stdout.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    depth = None if args.depth < 0 else args.depth
    data = build_flatdir_with_exif(Path(args.root), depth=depth)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, default=str)
            f.write("\n")
        print(f"Saved flatdir with EXIF: {output_path}")
    else:
        print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()
