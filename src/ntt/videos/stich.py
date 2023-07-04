import os
import cv2
import numpy as np


def stitch_2_videos(
    video_path_in,
    video_name_in1,
    video_name_in2,
    video_path_out,
    video_name_out,
    time_difference,
    src_pts1,
    dest_pts1,
    src_pts2,
    dest_pts2,
):
    """stitches video1 and video2 based on the source and destination points"""

    video_name1 = os.path.join(video_path_in, video_name_in1)
    video_name2 = os.path.join(video_path_in, video_name_in2)
    video_out = os.path.join(video_path_out, video_name_out)

    # hard coded size of the reference image
    size_image_ref = (900, 360)

    # size of the final image
    shape_output_img = (1920, 1080)

    # we need to convert the points of the calibration to make them correspond the destination image size
    dest_pts1[:, 0] = dest_pts1[:, 0] * shape_output_img[0] / size_image_ref[0]
    dest_pts1[:, 1] = dest_pts1[:, 1] * shape_output_img[1] / size_image_ref[1]
    dest_pts2[:, 0] = dest_pts2[:, 0] * shape_output_img[0] / size_image_ref[0]
    dest_pts2[:, 1] = dest_pts2[:, 1] * shape_output_img[1] / size_image_ref[1]

    # generating the homography matrices
    hm1 = cv2.getPerspectiveTransform(src_pts1, dest_pts1)
    hm2 = cv2.getPerspectiveTransform(src_pts2, dest_pts2)

    # video reading
    cap1 = cv2.VideoCapture(video_name1)
    cap2 = cv2.VideoCapture(video_name2)
    fps = cap1.get(cv2.CAP_PROP_FPS)
    time_shift = round(time_difference * fps)

    # output video
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")

    out = cv2.VideoWriter(
        video_out, fourcc, fps, (shape_output_img[0], shape_output_img[1])
    )

    if cap1.isOpened() == False:
        print("Error opening video 1 stream or file")
    if cap2.isOpened() == False:
        print("Error opening video 2 stream or file")

    # we read frames until synchronised
    for _ in range(abs(time_shift)):
        if time_shift > 0:
            cap1.read()
        else:
            cap2.read()

    while (cap1.isOpened()) and (cap2.isOpened()):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if ret1 is not True or ret2 is not True:
            break
        else:
            # transformation of the frame
            left_trans = cv2.warpPerspective(
                frame1, hm1, (shape_output_img[0], shape_output_img[1])
            )
            right_trans = cv2.warpPerspective(
                frame2, hm2, (shape_output_img[0], shape_output_img[1])
            )

            # stitch them together
            out_top = np.where(right_trans != 0, right_trans, left_trans)
            out.write(out_top)

    # cleanup
    cap1.release()
    cap2.release()
