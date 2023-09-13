from ntt.frames.frame_overlay import overlay_two_frames,overlay_n_frames
from ntt.frames.frame_generation import empty_frame
import os,cv2
import numpy as np
from dotenv import load_dotenv
load_dotenv()
def test_overlay_two_frames():
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
    overlayed=overlay_two_frames(frames_path_in,frame1_name,frame2_name,opacities,path_output_name)
def test_overlay_n_frames():
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
    frames=[frame1_name,frame2_name,frame3_name]
    assert frame1.shape==frame2.shape and frame1.shape==frame3.shape
    opacities=[0.5]*3
    overlayed=overlay_n_frames(frames_path_in,frames,opacities,path_output_name)
def test_custom():
    frames_path_in=f"{os.environ.get('PATH_IN')}"
    frame1=empty_frame(width=10,height=10)
    frame2=empty_frame(width=10,height=10)
    frame3=empty_frame(width=10,height=10)
    
    cv2.imwrite(f"{os.environ.get('PATH_IN')}image1.jpg",frame1)
    cv2.imwrite(f"{os.environ.get('PATH_IN')}image2.jpg",frame2)
    path_output_name1=f"{os.environ.get('FRAME_PATH_OUT')}overlayed1.jpg"
    path_output_name2=f"{os.environ.get('FRAME_PATH_OUT')}overlayed2.jpg"
    path_output_name3=f"{os.environ.get('FRAME_PATH_OUT')}res.jpg"
    h,w,_=frame3.shape
    frame3[h//4:h//2,w//4:w//2]=np.full((h//2-h//4,w//2-w//4,3),[0,255,0],dtype=np.uint8)
    cv2.imwrite(f"{os.environ.get('PATH_IN')}image3.jpg",frame3)
    overlayed_frame1=overlay_two_frames(frames_path_in,"image1.jpg","image3.jpg",[0.5]*2,path_output_name1)
    overlayed_frame2=overlay_two_frames(frames_path_in,"image2.jpg","image3.jpg",[0.5]*2,path_output_name2)
    overlayed=overlay_two_frames(f"{os.environ.get('FRAME_PATH_OUT')}","overlayed1.jpg","overlayed2.jpg",[0.5,0.5],path_output_name3)
    assert(frame3==overlayed).all()




if __name__=="__main__":
    test_overlay_two_frames()
    test_overlay_n_frames()
    test_custom()