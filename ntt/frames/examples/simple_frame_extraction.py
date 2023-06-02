
from ntt.frames.frame_extraction import extract_first_frame

if __name__ == "__main__":

    extract_first_frame(video_path_in = "samples/", 
                    video_name_in = "crop.MP4",
                    frame_path_out = "samples/",
                    frame_name_out = "crop-ex.jpg" 
                    )
