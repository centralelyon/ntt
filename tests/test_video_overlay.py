from ntt.videos.overlay_videos import video_fusion_image
import os,cv2
from dotenv import load_dotenv
def test_video_overlay():
    load_dotenv()
    path_videos=os.environ.get("VIDEO_PATH_IN")
    name_video1="point_0.mp4"
    name_video2="point_8.mp4"
    path_video_out=f"{os.environ.get('PATH_OUT')}overlayed_points.mp4"
    path_video1=os.path.join(path_videos,name_video1)
    path_video2=os.path.join(path_videos,name_video2)
    
    video1 = cv2.VideoCapture(path_video1)
    video2 = cv2.VideoCapture(path_video2)
    width1 = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps1 = video1.get(cv2.CAP_PROP_FPS)
    width2 = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps2 = video2.get(cv2.CAP_PROP_FPS)
    totalNoFrames1 = video1.get(cv2.CAP_PROP_FRAME_COUNT)
    totalNoFrames2=video2.get(cv2.CAP_PROP_FRAME_COUNT)
    assert width1==width2 and height1==height2
    assert fps1==fps2

    video_fusion_image(path_videos,name_video1,name_video2,path_video_out)
if __name__=="__main__":
    test_video_overlay()