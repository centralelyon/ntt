import cv2
import os
import numpy as np
from dotenv import load_dotenv


def extract_last_frame(video_path_in, video_name_in, frame_path_out, frame_name_out):
    video_name = os.path.join(video_path_in, video_name_in)
    frame_name = os.path.join(frame_path_out, frame_name_out)

    vidcap = cv2.VideoCapture(video_name)

    total_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    vidcap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)

    success, image = vidcap.read()

    if success:
        cv2.imwrite(frame_name, image)
    else:
        return None

    return frame_name


def extract_first_frame(video_path_in, video_name_in, frame_path_out, frame_name_out):
    return extract_nth_frame(
        video_path_in, video_name_in, frame_path_out, frame_name_out, 0
    )


def extract_nth_frame(
    video_path_in, video_name_in, frame_path_out, frame_name_out, nth_frame=0
):
    video_name = os.path.join(video_path_in, video_name_in)
    frame_name = os.path.join(frame_path_out, frame_name_out)

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
        else:
            return None

        i = i + 1

    return frame_name


def extract_frame_opencv(video_path, frame_number=1):
    if not os.path.isfile(video_path):
        return None

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_number < 1 or frame_number > total_frames:
        return None

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
    ret, frame = cap.read()

    if ret:
        return frame
    else:
        return None


# Extract a frame using FFmpeg
def extract_frame_ffmpeg(video_path, frame_number):
    stream = ffmpeg.input(video_path)
    stream = ffmpeg.filter(stream, "select", f"eq(n,{frame_number-1})")
    stream = ffmpeg.output(stream, "pipe:", format="rawvideo", pix_fmt="rgb24")
    output, _ = ffmpeg.run(stream, capture_stdout=True, quiet=True)
    frame = cv2.imdecode(np.frombuffer(output, dtype=np.uint8), cv2.IMREAD_COLOR)
    return frame


# Compare the frames extracted by OpenCV and FFmpeg
def compare_frames(video_path, frame_number):
    frame_opencv = extract_frame_opencv(video_path, frame_number)
    frame_ffmpeg = extract_frame_ffmpeg(video_path, frame_number)
    if frame_opencv is None or frame_ffmpeg is None:
        return False
    diff = cv2.absdiff(frame_opencv, frame_ffmpeg)
    return np.all(diff == 0)


if __name__ == "__main__":
    load_dotenv()
    extract_first_frame(
        video_path_in=os.environ.get("VIDEO_PATH_IN"),
        video_name_in="crop.mp4",
        frame_path_out=os.environ.get("FRAME_PATH_OUT"),
        frame_name_out="crop.jpg",
    )
