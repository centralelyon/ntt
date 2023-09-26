from ntt.videos.split_video import split_video_ffmpeg
from dotenv import load_dotenv
import os
if __name__=="__main__":
    load_dotenv()
    video_path_in=f"{os.environ.get('VIDEO_PATH_IN')}"
    video_name="2023_CF_Rennes_freestyle_hommes_50_finaleA_fixeDroite.mp4"
    output_path=os.environ.get('PATH_OUT')
    n=5
    split_video_ffmpeg(video_path_in,video_name,output_path,n)