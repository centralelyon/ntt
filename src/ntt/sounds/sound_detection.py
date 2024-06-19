"""TODO : sound_detection module provides ...
"""

import os

import librosa
import numpy as np
from moviepy.editor import VideoFileClip
from pyAudioAnalysis import MidTermFeatures as aFm
from pyAudioAnalysis import audioBasicIO as aIO


def detect_sound_ref(
    video_path,
    bip_ref_path="ref_bip_isolated.wav",
    references_path="ref_features_bip.npy",
):
    """_summary_

    Args:
        video_path (_type_): _description_
        bip_ref_path (str, optional): _description_.
            Defaults to "ref_bip_isolated.wav".
        references_path (str, optional): _description_.
            Defaults to "ref_features_bip.npy".

    Returns:
        _type_: _description_
    """
    mt = np.load(references_path)
    fs, s_ref = aIO.read_audio_file(bip_ref_path)
    duration = len(s_ref) / float(fs)
    win, step = 0.05, 0.05
    win_mid, step_mid = duration, 0.5

    # extraction on the long signal
    my_clip1 = VideoFileClip(video_path)
    fs = 44100
    s_long = my_clip1.audio.to_soundarray(fps=fs)
    s_long = s_long[:, 0]
    duration_long = len(s_long) / float(fs)

    # extract short-term features using a 50msec non-overlapping windows
    win, step = 0.05, 0.05
    win_mid, step_mid = 0.4, 0.05
    mt_long, _, _ = aFm.mid_feature_extraction(
        s_long, fs, win_mid * fs, step_mid * fs, win * fs, step * fs
    )

    # normalization
    mt_long = mt_long.T
    # TODO : Find a better name for val
    for i, val in enumerate(mt_long):
        mt_long[i] = val / np.linalg.norm(val)

    temps_possible = []

    # TODO : Find better names for t_val and long_val
    for i, t_val in enumerate(mt):
        arg_min_dist = 0
        min_dist = 1000
        for j, long_val in enumerate(mt_long):
            distance = np.linalg.norm(t_val - long_val)
            if distance < min_dist:
                arg_min_dist = j
                min_dist = distance
        temps_possible.append(arg_min_dist * duration_long / mt_long.shape[0])

    median_time = np.median(temps_possible)
    temps_possible_non_aberrant = []
    aberration = 0.5

    for temps in temps_possible:
        if median_time - aberration <= temps:
            if temps <= median_time + aberration:
                temps_possible_non_aberrant.append(temps)

    # An empty sequence is falsey
    if temps_possible_non_aberrant:
        # 0.11s of silence before  bip in reference sounds
        start = np.median(temps_possible_non_aberrant) + 0.11

    else:
        # Error
        start = -1
    return start


def simple_peak_count_librosa(video_path, video_name):
    """_summary_

    Args:
        video_path (_type_): _description_
        video_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    video = os.path.join(video_path, video_name)
    video = VideoFileClip(video)
    # fps = video.fps
    audio = os.path.join(video_path, video_name[: len(video_name) - 4] + ".mp3")
    video.audio.write_audiofile(audio)
    x, sr = librosa.load(audio)
    onset_frames = librosa.onset.onset_detect(y=x, sr=sr)
    return len(onset_frames)


def detect_sound_ref_librosa(samples_path, video_name, ref_sound_name, threshold=20):
    """_summary_

    Args:
        samples_path (_type_): _description_
        video_name (_type_): _description_
        ref_sound_name (_type_): _description_
        path_out (_type_): _description_
        threshold (int, optional): _description_. Defaults to 20.

    Returns:
        _type_: _description_
    """
    # Load the target sound effect and the audio or video file
    target_sound_file = os.path.join(samples_path, ref_sound_name)
    audio_or_video_file = os.path.join(samples_path, video_name)
    # Load the target sound effect
    target_sound, sr = librosa.load(target_sound_file)
    target_sound = np.array(target_sound)
    # Load the audio or video file
    audio, sr1 = librosa.load(audio_or_video_file)
    length_video = int(len(audio) * 1000 / sr1)

    segment_duration = int(len(target_sound) * 1000 / sr)
    # Convert the target sound effect to a spectrogram
    target_sound_spec = librosa.amplitude_to_db(
        np.abs(librosa.stft(target_sound, hop_length=512)), ref=np.max
    )

    # Split the audio into short segments and compare them with the target sound effect
    # Convert milliseconds to seconds)
    segment_length = segment_duration

    # TODO : "l" replaced by "l_target_sound_effect" : is this an appropriate
    # name for this list ?
    l_target_sound_effect = []

    for i in range(0, length_video - segment_length, segment_length):
        # Extract a segment from the audio
        segment = audio[i:i + segment_length]

        # Convert the segment to a spectrogram using librosa
        segment_spec = librosa.amplitude_to_db(
            np.abs(librosa.stft(segment, hop_length=512)), ref=np.max
        )

        # Compare the spectrograms of the segment and target sound effect
        resized_target_sound_spec = np.resize(target_sound_spec, segment_spec.shape)

        # Compare the spectrograms of the segment and target sound effect
        similarity = np.mean(np.abs(segment_spec - resized_target_sound_spec))

        # Set a threshold to determine if the target sound effect is present
        if similarity < threshold:
            l_target_sound_effect.append(i / 1000)

    return l_target_sound_effect
