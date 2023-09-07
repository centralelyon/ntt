from ntt.frames.overlay_two_images import overlay_images
import os,cv2
def test_overlay_images():
    frames_path_in="./samples"
    frame1_name="frame1.jpg"
    frame2_name="frame2.jpg"
    output_name="overlayed.jpg"
    path_frame1=os.path.join(frames_path_in,frame1_name)
    path_frame2=os.path.join(frames_path_in,frame2_name)
    frame1=cv2.imread(path_frame1)
    frame2=cv2.imread(path_frame2)
    assert frame1.shape==frame2.shape
    overlayed=overlay_images(frames_path_in,frame1_name,frame2_name,output_name)

if __name__=="__main__":
    test_overlay_images()