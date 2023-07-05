import os
import cv2
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
    nb_frame=-1,
    afficher_anime=True,
    afficher_hist=True,
):
    video_link = os.path.join(input_path, video_name_in)
    video_file_out = os.path.join(output_path, video_name_out)
    cap = cv2.VideoCapture(video_link)  # lecture de la video
    rep = []  # (optimisable par préallocation)
    i = 0
    directory_path = os.path.dirname(video_link)

    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    out = cv2.VideoWriter(
        video_file_out,
        fourcc,
        50,
        (xb - xa, yb - ya),
        isColor=False,
    )

    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame[ya:yb, xa:xb], cv2.COLOR_BGR2GRAY)
        rep.append(np.sum(gray > seuil))

        if afficher_anime:
            cv2.putText(
                gray, f"{i}", (7, 7), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255)
            )
            cv2.imshow("f", gray)

            out.write(gray)

        if cv2.waitKey(1) == ord("q"):
            break

        if i == nb_frame:
            break

        i += 1

    out.release()
    cap.release()
    return np.argmax(rep)
