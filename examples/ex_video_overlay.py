from ntt.videos.overlay_videos import video_fusion_image
from dotenv import load_dotenv
import os
if __name__=="__main__":
    load_dotenv()
    path_videos=os.environ.get("PATH_IN")
    name_video1="point_0.mp4"
    name_video2="point_8.mp4"
    video_out=f"{os.environ.get('PATH_OUT')}overlayed_points.mp4"
    video_fusion_image(path_videos,name_video1,name_video2,video_out)
    