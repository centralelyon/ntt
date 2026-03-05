import cv2
import os
from dotenv import load_dotenv

load_dotenv()


def extract_n_frame(video_path_in, video_name_in, n):
    """This function extracts the nth  frame of a given video.

    Args:
        video_path_in (string): path to the folder conataining the input video
        video_name_in (string): name of the input video
        n (int): the number of the frame to be extracted

    Returns:
        string: full path of the output frame
    """
    video_name = os.path.join(video_path_in, video_name_in)

    vidcap = cv2.VideoCapture(video_name)
    success, image = vidcap.read()
    i = 0
    while i < n and success:
        i = i + 1
        success, image = vidcap.read()

    if i == n and success:
        cv2.imwrite(os.path.join(video_path_in, str(n) + "th_frame" + ".jpg"), image)
        vidcap.release()
    else:
        vidcap.release()
        return None

    path_out = os.environ.get("PATH_OUT")
    if path_out is None:
        raise EnvironmentError("Environment variable 'PATH_OUT' is not set.")
    frame_path_out = os.path.join(path_out, str(n) + "th_frame")

    return frame_path_out


def extract_frame_opencv(video_path, frame_number):
    """This function extracts a frame given its number from a video with opencv

    Args:
        video_path (string): path to the folder conataining the input video
        frame_number (int, optional): the number of the frame to extract. Defaults to 1.

    Returns:
        np.ndarray: the frame with number = frame_number
    """
    if not os.path.isfile(video_path):
        return None

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_number < 1 or frame_number > total_frames:
        return None

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
    ret, frame = cap.read()
    cap.release()

    if ret:
        return frame
    else:
        return None
