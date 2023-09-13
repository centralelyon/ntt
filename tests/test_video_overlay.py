from ntt.videos.video_overlay import overlay_videos_moviepy,overlay_two_videos_opencv
import os,cv2
from dotenv import load_dotenv
load_dotenv()
def test_video_overlay_opencv():
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

    overlay_two_videos_opencv(path_videos,name_video1,name_video2,path_video_out)
def test_video_overlay_moviepy():
    list_videos_path=os.listdir(f"{os.environ.get('VIDEO_PATH_IN')}")
    opacities = [0.5 for i in range(len(list_videos_path))]
    path_video_out=f"{os.environ.get('PATH_OUT')}overlayed.mp4"
    overlay_videos_moviepy(list_videos_path,opacities,path_video_out)

if __name__=="__main__":
    test_video_overlay_opencv()
    test_video_overlay_moviepy()