import cv2

# A complete list of available fourcc codes can be found here:
# https://www.fourcc.org/codecs.php
FOURCC_MJPG = cv2.VideoWriter_fourcc(*"MJPG")
FOURCC_XVID = cv2.VideoWriter_fourcc(*"XVID")
FOURCC_MP4V = cv2.VideoWriter_fourcc(*"mp4v")
FOURCC_FLV1 = cv2.VideoWriter_fourcc(*"FLV1")

LIST_FOURCC = [FOURCC_MJPG, FOURCC_XVID, FOURCC_MP4V, FOURCC_FLV1]

DEFAULT_FOURCC = FOURCC_MJPG
