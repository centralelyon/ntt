import os, cv2
import numpy as np

def overlay_two_frames(path_frames, name_frame1, name_frame2, opacities, path_output_frame):
    path_frame1 = os.path.join(path_frames, name_frame1)
    path_frame2 = os.path.join(path_frames, name_frame2)

    frame1 = np.array(cv2.imread(path_frame1),dtype=np.uint8)
    frame2 = np.array(cv2.imread(path_frame2),dtype=np.uint8)
    opacity_frame1,opacity_frame2=opacities[0],opacities[1]

    overlayed_frame = cv2.addWeighted(frame1, opacity_frame1, frame2, opacity_frame2, 0)

    cv2.imwrite(path_output_frame, overlayed_frame)
    return overlayed_frame
def overlay_n_frames(path_frames, frames,opacities,path_output_frame):
    n=len(frames)
    path_frame0=os.path.join(path_frames,frames[0])
    path_frame1=os.path.join(path_frames,frames[1])
    frame0=cv2.imread(path_frame0)
    frame1=cv2.imread(path_frame1)
    overlayed=cv2.addWeighted(frame0,opacities[0],frame1,opacities[1],0)
    for i in range(2,n):
        path_frame=os.path.join(path_frames,frames[i])
        frame=cv2.imread(path_frame)
        overlayed=cv2.addWeighted(overlayed,1-opacities[i],frame,opacities[i],0)
    cv2.imwrite(path_output_frame,overlayed)
    return(overlayed)


