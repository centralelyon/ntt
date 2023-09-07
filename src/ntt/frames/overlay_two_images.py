import os, cv2


def overlay_images(path_frames, name_frame1, name_frame2, name_output_frame):
    path_frame1 = os.join(path_frames, name_frame1)
    path_frame2 = os.join(path_frames, name_frame2)

    frame1 = cv2.imread(path_frame1)
    frame2 = cv2.imread(path_frame2)

    overlayed_frame = cv2.addWeighted(frame1, 0.5, frame2, 0.5, 0)
    path_output_frame = os.join(path_frames, name_output_frame)
    
    cv2.imwrite(path_output_frame, overlayed_frame)
    return overlayed_frame
