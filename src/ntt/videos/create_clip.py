from moviepy import editor


def cut_video(
    video_file_in: str = "samples/crop.mp4",
    video_file_out: str = "output/crop_clip.mp4",
    start: int = 0,
    end: int = 0,
) -> None:
    """Cut video during a given time interval in seconds"""

    myclip_in = editor.VideoFileClip(video_file_in)
    myclip_out = myclip_in.subclip(start, end)
    myclip_out.write_videofile(video_file_out)
    myclip_in.close()
    myclip_out.close()
    return
