import cv2
import time


def show_video(video_path, window_name="Video"):
    """Show a video in a window at its native frame rate.

    Args:
        video_path (str): Path to the video file.
        window_name (str): Title of the display window.

    Press Esc or Q to quit early.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_duration = 1.0 / fps if fps > 0 else 1.0 / 30

    while cap.isOpened():
        t0 = time.perf_counter()
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(window_name, frame)

        # subtract decode+display time from the target frame duration
        elapsed = time.perf_counter() - t0
        wait_ms = max(1, int((frame_duration - elapsed) * 1000))
        key = cv2.waitKey(wait_ms) & 0xFF
        if key in (27, ord('q')):  # Esc or Q
            break

    cap.release()
    cv2.destroyAllWindows()
