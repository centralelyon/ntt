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
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(VIDEO_PATH, fourcc, 10.0, (100, 100))
        for _ in range(10): # 10 frames
            frame = np.zeros((100, 100, 3), dtype=np.uint8)
            cv2.randu(frame, 0, 255)
            out.write(frame)
        out.release()
    yield
    if os.path.exists(VIDEO_PATH):
        os.remove(VIDEO_PATH)

def test_extract_first_frame(tmp_path):
    frame_name = tmp_path / "first_frame.jpg"
    result = frame_extraction.extract_first_frame(
        os.path.dirname(VIDEO_PATH), os.path.basename(VIDEO_PATH), tmp_path, frame_name.name
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None

def test_extract_last_frame(tmp_path):
    frame_name = tmp_path / "last_frame.jpg"
    result = frame_extraction.extract_last_frame(
        os.path.dirname(VIDEO_PATH), os.path.basename(VIDEO_PATH), tmp_path, frame_name.name
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None

def test_extract_nth_frame(tmp_path):
    frame_name = tmp_path / "nth_frame.jpg"
    result = frame_extraction.extract_nth_frame(
        os.path.dirname(VIDEO_PATH), os.path.basename(VIDEO_PATH), tmp_path, frame_name.name, 1
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None

def test_extract_frame_opencv():
    frame = frame_extraction.extract_frame_opencv(VIDEO_PATH, 1)
    assert frame is not None
    assert isinstance(frame, np.ndarray)

@pytest.mark.skipif(shutil.which('ffmpeg') is None, reason="ffmpeg is not installed")
def test_extract_frame_ffmpeg():
    frame = frame_extraction.extract_frame_ffmpeg(VIDEO_PATH, 1)
    assert frame is not None
    assert isinstance(frame, np.ndarray)

@pytest.mark.skipif(shutil.which('ffmpeg') is None, reason="ffmpeg is not installed")
def test_compare_frames():
    # On ne teste que la non-erreur, car les frames peuvent différer selon les codecs
    result = frame_extraction.compare_frames(VIDEO_PATH, 1)
    assert isinstance(result, (bool, np.bool_))
