from pyAudioAnalysis import MidTermFeatures as aFm
from pyAudioAnalysis import audioBasicIO as aIO
import moviepy.editor as mp
import numpy as np
from pydub import AudioSegment


def detect_sound_ref(
    video_path,
    bip_ref_path="ref_bip_isolated.wav",
    references_path="ref_features_bip.npy",
):
    mt = np.load(references_path)
    fs, s_ref = aIO.read_audio_file(bip_ref_path)
    duration = len(s_ref) / float(fs)
    win, step = 0.05, 0.05
    win_mid, step_mid = duration, 0.5

    # extraction on the long signal
    my_clip1 = mp.VideoFileClip(video_path)
    fs = 44100
    s_long = my_clip1.audio.to_soundarray(fps=fs)
    s_long = s_long[:, 0]
    duration_long = len(s_long) / float(fs)

    # extract short-term features using a 50msec non-overlapping windows
    win, step = 0.05, 0.05
    win_mid, step_mid = 0.4, 0.05
    mt_long, st_long, mt_n_long = aFm.mid_feature_extraction(
        s_long, fs, win_mid * fs, step_mid * fs, win * fs, step * fs
    )

    # normalization
    mt_long = mt_long.T
    for i in range(len(mt_long)):
        mt_long[i] = mt_long[i] / np.linalg.norm(mt_long[i])

    temps_possible = []

    for i in range(len(mt)):
        arg_min_dist = 0
        min_dist = 1000
        for j in range(len(mt_long)):
            if np.linalg.norm(mt[i] - mt_long[j]) < min_dist:
                arg_min_dist = j
                min_dist = np.linalg.norm(mt[i] - mt_long[j])
        temps_possible.append(arg_min_dist * duration_long / mt_long.shape[0])

    median_time = np.median(temps_possible)
    temps_possible_non_aberrant = []
    aberration = 0.5
    for i in range(len(temps_possible)):
        if median_time - aberration <= temps_possible[i]:
            if temps_possible[i] <= median_time + aberration:
                temps_possible_non_aberrant.append(temps_possible[i])

    if temps_possible_non_aberrant != []:
        # 0.11s de silence avant le bip dans les sons de références
        start = np.median(temps_possible_non_aberrant) + 0.11

    else:
        # Erreur
        start = -1
    return start


def count_sound_occurence(video_path, sound_path):
    # Load the video and extract the audio
    video_clip = mp.VideoFileClip(video_path)
    video_audio = video_clip.audio

    # Load the sound file
    sound = AudioSegment.from_file(sound_path)

    # Convert sound to mono if it's stereo
    if sound.channels > 1:
        sound = sound.set_channels(1)

    # Normalize sound
    sound = sound.apply_gain(-sound.max_dBFS)

    # Convert video audio to numpy array
    video_audio_array = np.array(video_audio.to_soundarray())

    # Convert sound to numpy array
    sound_array = np.array(sound.get_array_of_samples())

    # Normalize sound array
    sound_array = sound_array / np.max(np.abs(sound_array))

    # Compute cross-correlation
    cross_correlation = np.correlate(
        video_audio_array[:, 0],
        sound_array,
        mode="valid"
    )

    # Set a threshold to identify matches
    threshold = 0.7 * np.max(cross_correlation)

    # Find start times where the cross-correlation exceeds the threshold
    start_time_indices = np.where(cross_correlation > threshold)[0]

    # Filter start times to be spaced at least the length of the sound apart
    start_times = [start_time_indices[0] / video_audio.fps]
    for idx in start_time_indices[1:]:
        if idx / video_audio.fps - start_times[-1] > sound.duration_seconds:
            start_times.append(idx / video_audio.fps)

    return start_times