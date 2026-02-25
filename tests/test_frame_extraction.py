import os
import numpy as np
import pytest
import cv2

from ntt.frames import frame_extraction

# Chemin vers une vidéo de test (à adapter si besoin)
VIDEO_PATH = os.path.join(os.path.dirname(__file__), "sample.mp4")
FRAME_OUT_DIR = os.path.dirname(__file__)


@pytest.mark.skipif(
    not os.path.isfile(VIDEO_PATH), reason="Fichier vidéo de test manquant."
)
def test_extract_first_frame(tmp_path):
    frame_name = tmp_path / "first_frame.jpg"
    result = frame_extraction.extract_first_frame(
        tmp_path, os.path.basename(VIDEO_PATH), tmp_path, frame_name.name
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None


@pytest.mark.skipif(
    not os.path.isfile(VIDEO_PATH), reason="Fichier vidéo de test manquant."
)
def test_extract_last_frame(tmp_path):
    frame_name = tmp_path / "last_frame.jpg"
    result = frame_extraction.extract_last_frame(
        tmp_path, os.path.basename(VIDEO_PATH), tmp_path, frame_name.name
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None


@pytest.mark.skipif(
    not os.path.isfile(VIDEO_PATH), reason="Fichier vidéo de test manquant."
)
def test_extract_nth_frame(tmp_path):
    frame_name = tmp_path / "nth_frame.jpg"
    result = frame_extraction.extract_nth_frame(
        tmp_path, os.path.basename(VIDEO_PATH), tmp_path, frame_name.name, 1
    )
    assert result is not None
    assert os.path.isfile(result)
    img = cv2.imread(str(result))
    assert img is not None


@pytest.mark.skipif(
    not os.path.isfile(VIDEO_PATH), reason="Fichier vidéo de test manquant."
)
def test_extract_frame_opencv():
    frame = frame_extraction.extract_frame_opencv(VIDEO_PATH, 1)
    assert frame is not None
    assert isinstance(frame, np.ndarray)


@pytest.mark.skipif(
    not os.path.isfile(VIDEO_PATH), reason="Fichier vidéo de test manquant."
)
def test_extract_frame_ffmpeg():
    frame = frame_extraction.extract_frame_ffmpeg(VIDEO_PATH, 1)
    assert frame is not None
    assert isinstance(frame, np.ndarray)


@pytest.mark.skipif(
    not os.path.isfile(VIDEO_PATH), reason="Fichier vidéo de test manquant."
)
def test_compare_frames():
    # On ne teste que la non-erreur, car les frames peuvent différer selon les codecs
    result = frame_extraction.compare_frames(VIDEO_PATH, 1)
    assert isinstance(result, bool)
