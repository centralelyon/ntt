from ntt.frames.overlay_two_images import overlay_images
import os
from dotenv import load_dotenv
if __name__=="__main__":
    load_dotenv()
    path_frames=os.environ.get("PATH_IN")
    name_frame1="frame1.jpg"
    name_frame2="frame2.jpg"
    name_output_frame=f"{os.environ.get('FRAME_PATH_OUT')}overlayed.png"
    overlay_images(path_frames, name_frame1, name_frame2, name_output_frame)