from ntt.frames.overlay_two_images import overlay_images
import os,cv2
from dotenv import load_dotenv
load_dotenv()
def test_overlay_images():
    frames_path_in=os.environ.get('PATH_IN')
    frame1_name="frame1.jpg"
    frame2_name="frame2.jpg"
    path_output_name=f"{os.environ.get('FRAME_PATH_OUT')}overlayed.jpg"
    path_frame1=os.path.join(frames_path_in,frame1_name)
    path_frame2=os.path.join(frames_path_in,frame2_name)
    frame1=cv2.imread(path_frame1)
    frame2=cv2.imread(path_frame2)
    assert frame1.shape==frame2.shape
    overlayed=overlay_images(frames_path_in,frame1_name,frame2_name,path_output_name)

if __name__=="__main__":
    test_overlay_images()