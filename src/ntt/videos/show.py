"""TODO : show module provides ...
"""

import cv2


def show_video(video_path, window_name="Video"):
    """Show a video in a window.
    TODO : A library should not display graphic interface.

    Args:
        video_path (str or Path): Full path to the output video
        window_name (str, optional): _description_. Defaults to "Video".
    """
    cap_output = cv2.VideoCapture(video_path)

    got_frame = True
    while cap_output.isOpened() and got_frame:
        got_frame, frame_output = cap_output.read()

        if got_frame:
            cv2.imshow(window_name, frame_output)

        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap_output.release()
    cv2.destroyAllWindows()
