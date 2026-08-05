import os
import shutil
import numpy as np
import pytest
import cv2

from ntt.frames import frame_extraction

# Chemin vers une vidéo de test (à adapter si besoin)
VIDEO_PATH = os.path.join(os.path.dirname(__file__), "sample.mp4")
FRAME_OUT_DIR = os.path.dirname(__file__)


@pytest.fixture(scope="module", autouse=True)
def setup_test_video():
    if not os.path.exists(VIDEO_PATH):
        # Generate a dummy video for tests
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(VIDEO_PATH, fourcc, 10.0, (100, 100))
        if not out.isOpened():
            pytest.skip(f"OpenCV could not open a video writer for {VIDEO_PATH}")
        for _ in range(10):  # 10 frames
            frame = np.zeros((100, 100, 3), dtype=np.uint8)
            cv2.randu(frame, 0, 255)
            out.write(frame)
        out.release()
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        cap.release()
        pytest.skip(
            f"OpenCV cannot read the synthetic test video on this platform: {VIDEO_PATH}"
        )
    cap.release()
    yield
    if os.path.exists(VIDEO_PATH):
        os.remove(VIDEO_PATH)


def test_extract_first_frame(tmp_path):
    frame_name = tmp_path / "first_frame.jpg"
    result = frame_extraction.extract_first_frame(
        os.path.dirname(VIDEO_PATH),
        os.path.basename(VIDEO_PATH),
        tmp_path,
        frame_name.name,
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None


def test_extract_last_frame(tmp_path):
    frame_name = tmp_path / "last_frame.jpg"
    result = frame_extraction.extract_last_frame(
        os.path.dirname(VIDEO_PATH),
        os.path.basename(VIDEO_PATH),
        tmp_path,
        frame_name.name,
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None


def test_extract_nth_frame(tmp_path):
    frame_name = tmp_path / "nth_frame.jpg"
    result = frame_extraction.extract_nth_frame(
        os.path.dirname(VIDEO_PATH),
        os.path.basename(VIDEO_PATH),
        tmp_path,
        frame_name.name,
        1,
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None


def test_extract_frame_opencv():
    frame = frame_extraction.extract_frame_opencv(VIDEO_PATH, 1)
    assert frame is not None
    assert isinstance(frame, np.ndarray)


def test_cli_extract_first_frame(tmp_path, capsys):
    # exercise the new ``python -m ntt extract_first_frame`` command
    video = VIDEO_PATH
    out_file = tmp_path / "cli_frame.jpg"
    # copy test video into temp directory so the command can write next to it
    import shutil, subprocess, sys

    shutil.copy(video, tmp_path)
    cmd = [
        sys.executable,
        "-m",
        "ntt",
        "extract_first_frame",
        str(tmp_path / os.path.basename(video)),
    ]
    # run and capture output
    completed = subprocess.run(cmd, capture_output=True, text=True)
    assert completed.returncode == 0, completed.stderr
    # output should mention saved path
    assert "Saved:" in completed.stdout
    assert os.path.exists(
        str(tmp_path / (os.path.splitext(os.path.basename(video))[0] + ".jpg"))
    )


def test_shell_helper(tmp_path, monkeypatch, capsys):
    # verify the shell script refuses to overwrite an existing jpg
    script = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "shortcut_firstframe.sh")
    )
    # create dummy video and existing jpg
    video = tmp_path / "vid.mp4"
    video.write_text("dummy")
    jpg = tmp_path / "vid.jpg"
    jpg.write_text("exists")
    # call script
    completed = subprocess.run([script, str(video)], capture_output=True, text=True)
    assert completed.returncode == 0
    assert "output file already exists" in completed.stdout


@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg is not installed")
def test_extract_frame_ffmpeg():
    frame = frame_extraction.extract_frame_ffmpeg(VIDEO_PATH, 1)
    assert frame is not None
    assert isinstance(frame, np.ndarray)


@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg is not installed")
def test_compare_frames():
    # On ne teste que la non-erreur, car les frames peuvent différer selon les codecs
    result = frame_extraction.compare_frames(VIDEO_PATH, 1)
    assert isinstance(result, (bool, np.bool_))

def test_list_dirs_util(tmp_path):
    # create some subdirectories, some matching pattern, some not
    (tmp_path / "2022-foo").mkdir()
    (tmp_path / "2023-bar").mkdir()
    (tmp_path / "not-a-year").mkdir()
    from ntt.utils.index import list_directories
    all_dirs = list_directories(str(tmp_path))
    assert len(all_dirs) == 3
    matched = list_directories(str(tmp_path), r"^[0-9]{4}")
    assert all(os.path.basename(p).startswith(tuple(str(y) for y in range(2000, 3000))) for p in matched)
    assert len(matched) == 2


def test_cli_list_dirs(tmp_path):
    # using the command-line interface
    (tmp_path / "2022-foo").mkdir()
    (tmp_path / "other").mkdir()
    import subprocess, sys
    cmd = [sys.executable, "-m", "ntt", "list_dirs", str(tmp_path), "--pattern", "^[0-9]{4}"]
    completed = subprocess.run(cmd, capture_output=True, text=True)
    assert completed.returncode == 0
    lines = [l for l in completed.stdout.splitlines() if l.strip()]
    assert len(lines) == 1
    assert lines[0].endswith("2022-foo")
