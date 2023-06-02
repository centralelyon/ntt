import cv2
import os
def extract_n_frame(video_path_in,video_name_in,n):
    video_name = os.path.join(video_path_in, video_name_in)

    vidcap = cv2.VideoCapture(video_name)
    success, image = vidcap.read()
    i=0
    while i<n and success!=False:
        i=i+1
        success,image=vidcap.read()
        

    if i==n and success:
        cv2.imwrite(video_path_in+'/'+str(n)+'th_frame'+'.jpg', image)
    else:
        return None
    frame_path_out='/samples/'+str(n)+'th_frame'

    return frame_path_out

def extract_frame_opencv(video_path, frame_number ):

    if not os.path.isfile(video_path):
        return None

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_number < 1 or frame_number > total_frames:
        return None

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)
    ret, frame = cap.read()

    if ret:
        return frame
    else:
        return None