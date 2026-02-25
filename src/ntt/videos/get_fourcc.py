import sys
import cv2

from ntt.utils.constants import LIST_FOURCC
from ntt.videos.video_generation import random_video
from ntt.videos.io import write


def get_fourcc(cap: cv2.VideoCapture) -> str:
    """Return the 4-letter string of the codec the camera is using."""
    return (
        int(cap.get(cv2.CAP_PROP_FOURCC)).to_bytes(4, byteorder=sys.byteorder).decode()
    )


if __name__ == "__main__":
    # check if fourcc in LIST_FOURCC
    cap = cv2.VideoCapture(0)
    fourcc = get_fourcc(cap)
    print(f"Camera fourcc: {fourcc}")
    if fourcc in LIST_FOURCC:
        print("Camera fourcc is in LIST_FOURCC")
    else:
        print("Camera fourcc is NOT in LIST_FOURCC")
    cap.release()

    video = random_video()
    write("test_video.avi", video)
    cap = cv2.VideoCapture("test_video.avi")
    fourcc = get_fourcc(cap)
    print(f"Video fourcc: {fourcc}")
    if fourcc in LIST_FOURCC:
        print("Video fourcc is in LIST_FOURCC")
    else:
        print("Video fourcc is NOT in LIST_FOURCC")
    cap.release()

    # check if fourcc in LIST_FOURCC for a video file
    video_path = "path_to_your_video.mp4"
