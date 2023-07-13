from scipy import signal
import numpy as np
import moviepy.editor as mp


def sound_gap_measure(video1: str, video2: str) -> float:
    """
    Args:
        video1 (str): Path of the reference video
        video2 (str): Path of the comparison video

    Returns:
        float: gap (ms) between video1 and video2
    """
    my_clip1 = mp.VideoFileClip(video1)
    my_clip2 = mp.VideoFileClip(video2)

    # hard coded sample rate
    samplerate1 = 44100
    samplerate2 = 44100

    # extract the audio
    y1 = list(my_clip1.audio.iter_chunks(fps=samplerate1))
    y2 = list(my_clip2.audio.iter_chunks(fps=samplerate2))


    # take only the left channel
    size_analysed = min(len(y1), len(y2))
    y1 = y1[:size_analysed, 0]
    y2 = y2[:size_analysed, 0]

    # for noisy data and with a lot of points, we normalize the data
    y1 = y1 - y1.mean()
    y2 = y2 - y2.mean()
    if y1.std()!=None:
        y1 = y1 / y1.std()
    if y2.std()!=None:
        y2 = y2 / y2.std()
    # Calculation of the cross-correlation
    corr = signal.correlate(y1, y2)  # , mode="same")
    time = np.arange(1 - size_analysed, size_analysed)
    shift_calculated = time[corr.argmax()] * 1.0 * (1 / samplerate1)

    my_clip1.close()
    my_clip2.close()

    return shift_calculated
