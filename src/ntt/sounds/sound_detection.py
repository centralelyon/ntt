from pyAudioAnalysis import MidTermFeatures as aFm
from pyAudioAnalysis import audioBasicIO as aIO
import moviepy.editor as mp
import numpy as np
from pydub import AudioSegment
import librosa
import os


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


def simple_peak_count_librosa(video_path, video_name):
    video = os.path.join(video_path, video_name)
    video = mp.VideoFileClip(video)
    fps = video.fps
    audio = os.path.join(video_path, video_name[: len(video_name) - 4] + ".mp3")
    video.audio.write_audiofile(audio)
    x, sr = librosa.load(audio)
    onset_frames = librosa.onset.onset_detect(x, sr)
    return len(onset_frames)

def detect_sound_ref_librosa(samples_path,video_name,ref_sound_name,path_out):
    # Step 1: Load the target sound effect and the audio or video file
    target_sound_file = os.path.join(samples_path,ref_sound_name)
    audio_or_video_file = os.path.join(samples_path,video_name)
    # Load the target sound effect
    target_sound,sr = librosa.load(target_sound_file)
    target_sound = np.array(target_sound)
    # Load the audio or video file
    audio, sr1 = librosa.load(audio_or_video_file)
    length_video=int(len(audio)*1000/sr1)

    segment_duration = int(len(target_sound) * 1000 / sr)
    # Step 2: Convert the target sound effect to a spectrogram
    target_sound_spec = librosa.amplitude_to_db(np.abs(librosa.stft(target_sound, hop_length=512)), ref=np.max)
    # Step 3: Split the audio into short segments and compare them with the target sound effect  # Convert milliseconds to seconds)
    segment_length = segment_duration
    l=[]
    for i in range(0, length_video - segment_length, segment_length):
        # Extract a segment from the audio
        segment = audio[i:i + segment_length]

        # Convert the segment to a spectrogram using librosa
        segment_spec = librosa.amplitude_to_db(np.abs(librosa.stft(segment, hop_length=512)), ref=np.max)

        # Compare the spectrograms of the segment and target sound effect
        resized_target_sound_spec = np.resize(target_sound_spec, segment_spec.shape)

        # Compare the spectrograms of the segment and target sound effect
        similarity = np.mean(np.abs(segment_spec - resized_target_sound_spec))

        # Set a threshold to determine if the target sound effect is present
        threshold = 16  # Adjust this value based on your requirements

        if similarity < threshold:
            l.append(i/1000)
    return(l)

