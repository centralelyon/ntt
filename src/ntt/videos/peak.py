import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ntt.utils.temporal import calculate_temporal_accuracy


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
    video_link = os.path.join(input_path, video_name_in)
    video_file_out = os.path.join(output_path, video_name_out)
    cap = cv2.VideoCapture(video_link)  # read video
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_begin))  # go to first frame
    rep = []  # optimizable by preallocation
    gray_values = []
    i = 0
    directory_path = os.path.dirname(video_link)
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")

    if write_video:
        out = cv2.VideoWriter(
            video_file_out,
            fourcc,
            fps,
            (xb - xa, yb - ya),
            isColor=False,
        )

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv2.cvtColor(frame[ya:yb, xa:xb], cv2.COLOR_BGR2GRAY)
        rep.append(np.sum(gray > seuil))
        gray_values.append(np.mean(gray))

        if afficher_anime:
            cv2.putText(
                gray,
                f"{i+frame_begin}",
                (7, 7),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.3,
                (255, 255, 255),
            )
            cv2.imshow("f", gray)

            if write_video:
                out.write(gray)

        if cv2.waitKey(1) == ord("q"):
            break

        if i == nb_frame:
            break

        i += 1

    if afficher_hist:
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(rep)
        plt.xlabel("Frame")
        plt.ylabel("Sum")
        plt.title("Histogram of Sum Values")
        plt.axvline(np.argmax(rep), color="red", linestyle="--")  # Vertical red line

        plt.subplot(1, 2, 2)
        plt.plot(gray_values, color="gray")
        plt.xlabel("Frame")
        plt.ylabel("Gray Value")
        plt.title("Gray Value over Frames")
        plt.axvline(np.argmax(rep), color="red", linestyle="--")  # Vertical red line

        plt.tight_layout()
        plt.show()

    out.release() if write_video else None
    cap.release()
    return np.argmax(rep) + frame_begin
