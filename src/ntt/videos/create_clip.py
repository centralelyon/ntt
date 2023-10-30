import os
from moviepy import editor
import cv2 as cv
from dotenv import load_dotenv

load_dotenv()


def cut_video(
    video_file_in: str = os.path.join(os.environ.get("VIDEO_PATH_IN"), "crop.mp4"),
    video_file_out: str = os.path.join(os.environ.get("PATH_OUT"), "crop_clip.mp4"),
    start: int = 0,
    end: int = 0,
) -> str:
    """Cut video during a given time interval in seconds"""

    myclip_in = editor.VideoFileClip(video_file_in)
    myclip_out = myclip_in.subclip(start, end)
    myclip_out.write_videofile(video_file_out)
    myclip_in.close()
    myclip_out.close()

    return video_file_out


def cut_video_opencv(
    video_file_in: str = os.path.join(os.environ.get("VIDEO_PATH_IN"), "crop.mp4"),
    video_file_out: str = os.path.join(os.environ.get("PATH_OUT"), "crop_clip.mp4"),
    start: int = 0,
    end: int = 10,
) -> str:
    """Cut video during a given time interval in frame"""

    if start < 0:
        print("Error: negativ start")
        return 0
    elif start >= end:
        print(start)
        print(end)
        print("Error: start >= end")
        return 0

    if not os.path.isfile(video_file_in):
        print("Wrong video path")
        return 0
    cap = cv.VideoCapture(video_file_in)
    length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    ret, frame = cap.read()
    fps = cap.get(cv.CAP_PROP_FPS)
    if start > length:
        print("Error: start > video length")
        return 0
    if end > length:
        print("Error: end > video length")
        return 0

    cap.set(cv.CAP_PROP_POS_FRAMES, int(start))

    height, width, layers = frame.shape
    frameSize = (width, height)
    fourcc = cv.VideoWriter_fourcc("M", "J", "P", "G")
    out = cv.VideoWriter(video_file_out, fourcc, fps, frameSize)
    for i in range(end - start):
        ret, frame = cap.read()
        out.write(frame)
    out.release()

    return video_file_out
