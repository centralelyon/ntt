from scipy import signal
import numpy as np
import moviepy.editor as mp

def Sound_gap_measure(video1:str,video2:str)->float:
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
    y1 = my_clip1.audio.to_soundarray(fps=samplerate1)
    y2 = my_clip2.audio.to_soundarray(fps=samplerate2)

    # take only the left channel
    size_analysed = min(len(y1), len(y2))
    y1 = y1[:size_analysed, 0]
    y2 = y2[:size_analysed, 0]

    # for noisy data and with a lot of points, we normalize the data
    y1 = y1 - y1.mean()
    y2 = y2 - y2.mean()
    y1 = y1 / y1.std()
    y2 = y2 / y2.std()

    # Calculation of the cross-correlation
    corr = signal.correlate(y1, y2) # , mode="same")
    time = np.arange(1 - size_analysed, size_analysed)
    shift_calculated = time[corr.argmax()] * 1.0 * (1/samplerate1)

    return(shift_calculated)