from ntt.frames.frame_overlay import overlay_two_frames
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    path_frames = os.environ.get("PATH_IN")
    name_frame1 = "frame1.jpg"
    name_frame2 = "frame2.jpg"
    name_output_frame = os.path.join(os.environ.get("FRAME_PATH_OUT"), "overlayed.png")
    opacities = [0.5] * 2
    overlay_two_frames(
        path_frames, name_frame1, name_frame2, opacities, name_output_frame
    )
