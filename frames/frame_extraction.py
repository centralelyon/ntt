import cv2
import os

def extract_first_frame(video_path_in, video_name_in, frame_path_out, frame_name_out): 

    video_name = os.path.join(video_path_in, video_name_in)
    frame_name = os.path.join(frame_path_out, frame_name_out)

    vidcap = cv2.VideoCapture(video_name)
    success, image = vidcap.read()

    if success:
        cv2.imwrite(frame_name, image)

    return frame_path_out

if __name__ == '__main__':
    extract_first_frame(video_path_in = "samples/", 
                        video_name_in = "crop.mp4",
                        frame_path_out = "samples/",
                        frame_name_out = "crop.jpg" 
                        )