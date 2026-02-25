import cv2

FOURCC_MJPG = cv2.VideoWriter_fourcc(*"MJPG")
FOURCC_XVID = cv2.VideoWriter_fourcc(*"XVID")
FOURCC_MP4V = cv2.VideoWriter_fourcc(*"mp4v")

LIST_FOURCC = [FOURCC_MJPG, FOURCC_XVID, FOURCC_MP4V]

DEFAULT_FOURCC = FOURCC_MJPG
