from ntt.frames.overlay_two_images import overlay_images
if __name__=="__main__":
    path_frames="./samples"
    name_frame1="frame1.jpg"
    name_frame2="frame2.jpg"
    name_output_frame="overlayed.png"
    overlay_images(path_frames, name_frame1, name_frame2, name_output_frame)