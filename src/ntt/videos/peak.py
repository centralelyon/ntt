import os
import cv2
import numpy as np

from ntt.videos.io import get_writer_fourcc


def _write_peak_clip(
    video_link,
    video_file_out,
    fps,
    peak_frame,
    xa,
    xb,
    ya,
    yb,
    frame_begin,
    clip_before_seconds,
    clip_after_seconds,
):
    cap = cv2.VideoCapture(video_link)
    if not cap.isOpened():
        raise ValueError(f"Could not reopen input video for flash clip: {video_link}")

    start_frame = max(frame_begin, int(round(peak_frame - clip_before_seconds * fps)))
    end_frame = int(round(peak_frame + clip_after_seconds * fps))
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    fourcc = get_writer_fourcc(video_file_out)
    out = cv2.VideoWriter(
        video_file_out,
        fourcc,
        fps,
        (xb - xa, yb - ya),
    )
    if not out.isOpened():
        cap.release()
        raise ValueError(f"Could not open output video writer: {video_file_out}")

    current_frame = start_frame
    while cap.isOpened() and current_frame <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame[ya:yb, xa:xb], cv2.COLOR_BGR2GRAY)
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        offset_label = (current_frame - peak_frame) / fps
        color = (0, 0, 255) if current_frame == peak_frame else (255, 255, 255)
        cv2.putText(
            gray_bgr,
            f"frame {current_frame}",
            (8, 18),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            color,
            1,
        )
        cv2.putText(
            gray_bgr,
            f"t={offset_label:+.2f}s",
            (8, 38),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            color,
            1,
        )
        out.write(gray_bgr)
        current_frame += 1

    out.release()
    cap.release()


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
    frame_end=-1,
    nb_frame=-1,
    afficher_anime=True,
    afficher_hist=False,
    write_video=True,
    clip_before_seconds=1.0,
    clip_after_seconds=1.0,
):
    video_link = os.path.join(input_path, video_name_in)
    video_file_out = os.path.join(output_path, video_name_out)
    cap = cv2.VideoCapture(video_link)  # read video
    if not cap.isOpened():
        raise ValueError(f"Could not open input video: {video_link}")
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_begin))  # go to first frame
    rep = []  # optimizable by preallocation
    gray_values = []
    i = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    if isinstance(nb_frame, bool):
        nb_frame = -1

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
            if cv2.waitKey(1) == ord("q"):
                break

        if i == nb_frame or (frame_end != -1 and i + frame_begin >= frame_end):
            break

        i += 1

    if afficher_hist:
        import matplotlib.pyplot as plt

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

    cap.release()
    peak_frame = int(np.argmax(rep) + frame_begin)

    if write_video:
        _write_peak_clip(
            video_link,
            video_file_out,
            fps,
            peak_frame,
            xa,
            xb,
            ya,
            yb,
            frame_begin,
            clip_before_seconds,
            clip_after_seconds,
        )

    return peak_frame


# applies the function to be more compliant with the generate_peak_video function
def detect_peak_in_video(file_path):

    # get the videos dimensions
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()

    # call the detect_peak_video function
    return detect_peak_video(
        input_path=".",
        video_name_in=file_path,
        output_path=".",
        video_name_out="output_peak.avi",
        xa=0,
        xb=width,
        ya=0,
        yb=height,
        seuil=250,
        frame_begin=0,
        frame_end=-1,
        nb_frame=-1,
        afficher_anime=False,
        afficher_hist=False,
        write_video=False,
    )
