from ntt.frames.n_frame_extraction import extract_n_frame

if __name__ == "__main__":
    extract_n_frame(
        video_path_in="samples/",
        video_name_in="crop.mp4",
        n=2350,
    )
