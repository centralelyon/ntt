import sys
import cv2


def get_fourcc(cap: cv2.VideoCapture) -> str:
    """Return the 4-letter string of the codec the camera is using."""
    return (
        int(cap.get(cv2.CAP_PROP_FOURCC)).to_bytes(4, byteorder=sys.byteorder).decode()
    )
