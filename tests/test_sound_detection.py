import numpy as np

from ntt.sounds import sound_detection


class _FakeAudio:
    def write_audiofile(self, path, fps):
        with open(path, "wb") as handle:
            handle.write(b"fake wav")


class _FakeVideoFileClip:
    def __init__(self, path):
        self.path = path
        self.audio = _FakeAudio()
        self.closed = False

    def close(self):
        self.closed = True


def test_detect_sound_ref_uses_audio_basic_io_and_returns_median_time(tmp_path, monkeypatch):
    references_path = tmp_path / "ref.npy"
    np.save(references_path, np.array([[1.0, 0.0], [0.0, 1.0]]))

    clips = []

    def fake_video_file_clip(path):
        clip = _FakeVideoFileClip(path)
        clips.append(clip)
        return clip

    def fake_read_audio_file(path):
        if str(path).endswith("bip.wav"):
            return 10, np.ones(10)
        if str(path).endswith("temp_audio.wav"):
            return 10, np.array([[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]])
        raise AssertionError(f"Unexpected path: {path}")

    def fake_mid_feature_extraction(signal, fs, *args):
        assert fs == 10
        assert signal.ndim == 1
        return np.array([[1.0, 0.0], [0.0, 1.0]]), None, None

    monkeypatch.setattr(sound_detection.mp, "VideoFileClip", fake_video_file_clip)
    monkeypatch.setattr(sound_detection.aIO, "read_audio_file", fake_read_audio_file)
    monkeypatch.setattr(
        sound_detection.aFm, "mid_feature_extraction", fake_mid_feature_extraction
    )

    result = sound_detection.detect_sound_ref(
        "video.mp4", bip_ref_path="bip.wav", references_path=str(references_path)
    )

    assert np.isclose(result, 0.185)
    assert len(clips) == 1
    assert clips[0].closed is True


def test_detect_sound_ref_rejects_unexpected_sample_rate(tmp_path, monkeypatch):
    references_path = tmp_path / "ref.npy"
    np.save(references_path, np.array([[1.0, 0.0]]))

    monkeypatch.setattr(
        sound_detection.mp, "VideoFileClip", lambda path: _FakeVideoFileClip(path)
    )

    def fake_read_audio_file(path):
        if str(path).endswith("bip.wav"):
            return 10, np.ones(10)
        return 20, np.ones(10)

    monkeypatch.setattr(sound_detection.aIO, "read_audio_file", fake_read_audio_file)

    try:
        sound_detection.detect_sound_ref(
            "video.mp4", bip_ref_path="bip.wav", references_path=str(references_path)
        )
    except ValueError as exc:
        assert "Unexpected sample rate" in str(exc)
    else:
        raise AssertionError("detect_sound_ref should reject mismatched sample rates")
