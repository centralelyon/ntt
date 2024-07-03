"""TODO : peak module provides ...

https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

FourCC is a 4-byte code used to specify the video codec.
The list of available codes can be found in fourcc.org.
It is platform dependent.

The following codecs work fine for me :

- In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable.
  MJPG results in high size video. X264 gives very small size video)
- In Windows: DIVX (More to be tested and added)
- In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv)

TODO : fourcc depends on the video type ?

I had the following error on Ubuntu 22.04 :

OpenCV: FFMPEG: tag 0x47504a4d/'MJPG' is not supported with codec id 7
        and format 'mp4 / MP4 (MPEG-4 Part 14)'
OpenCV: FFMPEG: fallback to use tag 0x7634706d/'mp4v'

As specified in the message, I have to use 'mp4v' instead of 'MJPG'
for .mp4 video types : https://stackoverflow.com/a/72954514/481719

Some system drivers may be needed : https://stackoverflow.com/a/30106506/481719
"""

from pathlib import Path

import cv2

import matplotlib.pyplot as plt
import numpy as np


def detect_peak_video(
    input_path,
    video_name_in,
    output_path,
    video_name_out,
    xa,
    xb,
    ya,
    yb,
    seuil=200,
    frame_begin=0,
    nb_frame=-1,
    afficher_anime=True,
    afficher_hist=True,
    write_video=True,
):
    """_summary_
    TODO : A library should not display graphic interface. This function should
    return more results or write more data to disk.

    Args:
        input_path (str or Path): Path to the folder containing the input video
        video_name_in (string): Name of the input video
        output_path (str or Path): Path to the folder that will contain the output
        video_name_out (_type_): Name of the output video
        xa (_type_): _description_
        xb (_type_): _description_
        ya (_type_): _description_
        yb (_type_): _description_
        seuil (int, optional): _description_. Defaults to 200.
        frame_begin (int, optional): _description_. Defaults to 0.
        nb_frame (int, optional): _description_. Defaults to -1.
        afficher_anime (bool, optional): _description_. Defaults to False.
        afficher_hist (bool, optional): _description_. Defaults to False.
        write_video (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    """
    video_path_in = Path(input_path) / video_name_in
    video_path_out = Path(output_path) / video_name_out

    # Read video
    cap = cv2.VideoCapture(video_path_in)

    # Go to first frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_begin))

    # optimizable by preallocation
    rep = []
    gray_values = []
    i = 0

    fps = cap.get(cv2.CAP_PROP_FPS)

    # TODO : We can get the number of frames in the video file
    # https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
    # cap.get(cv2.CAP_PROP_FRAME_COUNT)

    # TODO : Depends of the input video type ?
    # fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

    if write_video:
        out = cv2.VideoWriter(
            video_path_out,
            fourcc,
            fps,
            (xb - xa, yb - ya),
            isColor=False,
        )

    # Work on each video frame
    # TODO : explain the algorithm, the logic
    while cap.isOpened():
        got_frame, frame = cap.read()

        if not got_frame:
            # TODO : Can test if we got less frame than expected
            # Otherwise nothing to print
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame[ya:yb, xa:xb], cv2.COLOR_BGR2GRAY)
        rep.append(np.sum(gray > seuil))
        gray_values.append(np.mean(gray))

        cv2.putText(
            gray,
            f"{i+frame_begin}",
            (7, 7),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.3,
            (255, 255, 255),
        )

        if afficher_anime:
            cv2.imshow("f", gray)

        if write_video:
            out.write(gray)

        if cv2.waitKey(1) == ord("q"):
            break

        if i == nb_frame:
            break

        i += 1

    if write_video:
        out.release()

    cap.release()

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(rep)
    plt.xlabel("Frame")
    plt.ylabel("Sum")
    plt.title("Histogram of Sum Values")
    # Vertical red line
    plt.axvline(np.argmax(rep), color="red", linestyle="--")

    plt.subplot(1, 2, 2)
    plt.plot(gray_values, color="gray")
    plt.xlabel("Frame")
    plt.ylabel("Gray Value")
    plt.title("Gray Value over Frames")
    # Vertical red line
    plt.axvline(np.argmax(rep), color="red", linestyle="--")

    plt.tight_layout()

    if afficher_hist:
        plt.show()
    else:
        plt.savefig(video_path_out.with_suffix(".png"))

    return np.argmax(rep) + frame_begin
