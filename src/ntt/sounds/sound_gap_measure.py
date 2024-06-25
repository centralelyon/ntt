"""TODO : sound_gap_measure module provides ...
"""

import os

import numpy as np
from moviepy.editor import VideoFileClip
from scipy import signal


def sound_gap_measure(video1: str | os.PathLike, video2: str | os.PathLike) -> float:
    """
    Args:
        video1 (Path or str): Path of the reference video
        video2 (Path or str): Path of the comparison video

    Returns:
        float: gap (ms) between video1 and video2
    """
    my_clip1 = VideoFileClip(str(video1))
    my_clip2 = VideoFileClip(str(video2))

    # hard coded sample rate
    samplerate1 = 44100
    samplerate2 = 44100

    # extract the audio
    audio1 = my_clip1.audio
    audio2 = my_clip2.audio

    # get the duration of the audio (in seconds)
    duration1 = audio1.duration
    duration2 = audio2.duration

    # calculate the number of frames to extract
    n_frames1 = int(duration1 * samplerate1)
    n_frames2 = int(duration2 * samplerate2)

    # extract the audio frames as a numpy array
    y1 = np.array(
        [audio1.get_frame(t) for t in np.linspace(0, duration1, num=n_frames1)]
    )
    y2 = np.array(
        [audio2.get_frame(t) for t in np.linspace(0, duration2, num=n_frames2)]
    )

    # take only the left channel
    y1 = y1[:, 0]
    y2 = y2[:, 0]

    # for noisy data and with a lot of points, we normalize the data
    y1 = y1 - y1.mean()
    y2 = y2 - y2.mean()
    y1 = y1 / y1.std()
    y2 = y2 / y2.std()

    # Calculation of the cross-correlation
    corr = signal.correlate(y1, y2)

    time = np.arange(1 - len(y1), len(y1))
    shift_calculated = time[corr.argmax()] * 1.0 * (1 / samplerate1)

    my_clip1.close()
    my_clip2.close()

    return shift_calculated
