import os
import cv2
import pytest
import sys
sys.path.append('./')
from frames.frame_extraction import extract_first_frame

def test_extract_first_frame():

    video_path_in = "samples/" 
    video_name_in = "crop.mp4"
    frame_path_in = "samples/"
    frame_name_in = "crop.jpg" 

    video_path = os.path.join(video_path_in, video_name_in)
    frame_path = os.path.join(frame_path_in, frame_name_in)

    image = cv2.imread(frame_path)
    height, width, layers = image.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_path, fourcc, 30.0, (width, height))
    video.write(image)
    video.release()

    # call of the function to test
    result = extract_first_frame(video_path_in, video_name_in, "samples/", "crop-test.jpg")

    saved_image = cv2.imread(frame_path)
    assert saved_image.shape == image.shape
    assert (saved_image == image).all()


if __name__ == '__main__':
    test_extract_first_frame()
