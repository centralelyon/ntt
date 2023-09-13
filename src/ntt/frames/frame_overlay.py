import os, cv2


def overlay_two_images(path_frames, name_frame1, name_frame2, opacities, path_output_frame):
    path_frame1 = os.path.join(path_frames, name_frame1)
    path_frame2 = os.path.join(path_frames, name_frame2)

    frame1 = cv2.imread(path_frame1)
    frame2 = cv2.imread(path_frame2)
    opacity_frame1,opacity_frame2=opacities[0],opacities[1]

    overlayed_frame = cv2.addWeighted(frame1, opacity_frame1, frame2, opacity_frame2, 0)

    cv2.imwrite(path_output_frame, overlayed_frame)
    return overlayed_frame
