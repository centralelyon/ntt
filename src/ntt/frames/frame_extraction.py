import cv2
import os
import ffmpeg
import numpy as np


def extract_last_frame(
    video_path_in: str, video_name_in: str, frame_path_out: str, frame_name_out: str, video_URL=None
) -> str:
    """Extracts the last frame of a given video.

    Args:
        video_path_in (string): path to the folder conataining the input video
        video_name_in (string): name of the input video
        frame_path_out (string): path to the folder conataining the output frame
        frame_name_out (string): name of the output frame
        video_URL (string, optional): URL of the video if it is not stored locally

    Returns:
        string: full path of the output frame
    """
    video_name = os.path.join(video_path_in, video_name_in)
    frame_name = os.path.join(frame_path_out, frame_name_out)
    if (video_URL is not None) and (video_URL != ""):
        video_name = video_URL

    vidcap = cv2.VideoCapture(video_name)

    total_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    vidcap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)

    success, image = vidcap.read()

    if success:
        cv2.imwrite(frame_name, image)
    else:
        return None

    vidcap.release()

    return frame_name


def extract_first_frame(
        video_path_in:str, video_name_in:str, frame_path_out:str, frame_name_out:str, video_URL=None
) -> str:
    """This function extracts the first frame of a given video.

    Args:
        video_path_in (string): path to the folder conataining the input video
        video_name_in (string): name of the input video
        frame_path_out (string): path to the folder conataining the output frame
        frame_name_out (string): name of the output frame
        video_URL (string, optional): URL of the video if it is not stored locally

    Returns:
        string: full path of the output frame
    """
    return extract_nth_frame(
        video_path_in, video_name_in, frame_path_out, frame_name_out, 0, video_URL
    )


def extract_nth_frame(
    video_path_in:str, video_name_in:str, frame_path_out:str, frame_name_out:str, nth_frame=0, video_URL=None
) -> str :
    """This function extracts the nth  frame of a given video.

    Args:
        video_path_in (string): path to the folder conataining the input video
        video_name_in (string): name of the input video
        frame_path_out (string): path to the folder conataining the output frame
        frame_name_out (string): name of the output frame
        nth_frame (int): the number of the frame to be extracted
        video_URL (string, optional): URL of the video if it is not stored locally

    Returns:
        string: full path of the output frame
    """
    video_name = os.path.join(video_path_in, video_name_in)
    frame_name = os.path.join(frame_path_out, frame_name_out)
    if (video_URL is not None) and (video_URL != ""):
        video_name = video_URL

    vidcap = cv2.VideoCapture(video_name)
    success = True

    i = 0

    total_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    if nth_frame > total_frames:
        print("nth_frame is greater than total_frames")
        return None

    while i <= nth_frame and success != False:
        success, image = vidcap.read()

        if i == nth_frame and success:
            cv2.imwrite(frame_name, image)
            vidcap.release()
            return frame_name

        i = i + 1

    vidcap.release()

    return frame_name


def extract_frame_opencv(video_path, frame_number=1):
    """Extracts a frame given its number from a video with opencv

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


def extract_frame_ffmpeg(video_path, frame_number):
    """Extracts a frame given its number from a video with ffmpeg

    Args:
        video_path (string): path to the folder conataining the input video
        frame_number (int): the number of the frame to extract.

    Returns:
        np.ndarray: the frame with number = frame_number
    """
    stream = ffmpeg.input(video_path)
    stream = ffmpeg.filter(stream, "select", f"eq(n,{frame_number-1})")
    stream = ffmpeg.output(stream, "pipe:", format="rawvideo", pix_fmt="rgb24")
    output, _ = ffmpeg.run(stream, capture_stdout=True, quiet=True)
    frame = cv2.imdecode(np.frombuffer(output, dtype=np.uint8), cv2.IMREAD_COLOR)
    return frame


def compare_frames(video_path, frame_number):
    """This function compares the frames extracted by extract_frame_ffmpeg and extract_frame_opencv

    Args:
        video_path (string): path to the folder conataining the input video
        frame_number (int): the number of the frame to extract.

    Returns:
        Boolean: True if all pixels are alike between frame_opencv and frame_ffmpeg else False
    """
    frame_opencv = extract_frame_opencv(video_path, frame_number)
    frame_ffmpeg = extract_frame_ffmpeg(video_path, frame_number)
    if frame_opencv is None or frame_ffmpeg is None:
        return False
    diff = cv2.absdiff(frame_opencv, frame_ffmpeg)
    return np.all(diff == 0)
