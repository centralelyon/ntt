from ntt.frames.frame_overlay import overlay_two_images,overlay_n_frames
import os,cv2
from dotenv import load_dotenv
load_dotenv()
def test_overlay_two_images():
    frames_path_in=f"{os.environ.get('PATH_IN')}"
    frame1_name="frame1.jpg"
    frame2_name="frame2.jpg"
    path_output_name=f"{os.environ.get('FRAME_PATH_OUT')}overlayed.jpg"
    path_frame1=os.path.join(frames_path_in,frame1_name)
    path_frame2=os.path.join(frames_path_in,frame2_name)
    frame1=cv2.imread(path_frame1)
    frame2=cv2.imread(path_frame2)
    assert frame1.shape==frame2.shape
    opacities=[0.5]*2
    overlayed=overlay_two_images(frames_path_in,frame1_name,frame2_name,opacities,path_output_name)
def test_overlay_n_images():
    frames_path_in=f"{os.environ.get('PATH_IN')}"
    frame1_name="frame1.jpg"
    frame2_name="frame2.jpg"
    frame3_name="frame3.jpg"
    path_output_name=f"{os.environ.get('FRAME_PATH_OUT')}overlayed.jpg"
    path_frame1=os.path.join(frames_path_in,frame1_name)
    path_frame2=os.path.join(frames_path_in,frame2_name)
    path_frame3=os.path.join(frames_path_in,frame3_name)
    frame1=cv2.imread(path_frame1)
    frame2=cv2.imread(path_frame2)
    frame3=cv2.imread(path_frame3)
    frames=[frame1,frame2,frame3]
    assert frame1.shape==frame2.shape and frame1.shape==frame3.shape
    opacities=[0.5]*3
    overlayed=overlay_n_frames(frames_path_in,frames,opacities,path_output_name)


if __name__=="__main__":
    test_overlay_two_images()
    test_overlay_n_images()