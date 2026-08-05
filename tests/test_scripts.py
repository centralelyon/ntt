import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def _run_script(script_name: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script_name), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )


def test_example_generate_random_image_script(tmp_path):
    output_path = tmp_path / "random_image.jpg"

    result = _run_script("example_generate_random_image.py", str(output_path))

    assert output_path.is_file()
    assert "Saved random image" in result.stdout


def test_example_inject_and_extract_exif_scripts(tmp_path):
    output_path = tmp_path / "image_with_exif.jpg"

    inject = _run_script("example_inject_exif_into_image.py", str(output_path))
    extract = _run_script("example_extract_exif_from_image.py", str(output_path))
    payload = json.loads(extract.stdout)

    assert output_path.is_file()
    assert "Saved image with EXIF" in inject.stdout
    assert payload["image"] == str(output_path)
    assert payload["pillow"]["Make"] == "ntt"


def test_example_flatdir_exif_script(tmp_path):
    pytest.importorskip("flatdir")

    image_path = tmp_path / "image_with_exif.jpg"
    output_path = tmp_path / "files_with_exif.json"

    _run_script("example_inject_exif_into_image.py", str(image_path))
    result = _run_script(
        "example_flatdir_exif.py",
        str(tmp_path),
        "--output",
        str(output_path),
    )
    payload = json.loads(output_path.read_text(encoding="utf-8"))

    assert "Saved flatdir with EXIF" in result.stdout
    assert payload[0]["name"] == "image_with_exif.jpg"
    assert payload[0]["exif_pillow"]["Make"] == "ntt"


def test_generate_primitives_showcase_script(tmp_path):
    output_path = tmp_path / "primitives_showcase.png"

    result = _run_script("generate_primitives_showcase.py", str(output_path))

    assert output_path.is_file()
    assert "Primitives showcase saved" in result.stdout
