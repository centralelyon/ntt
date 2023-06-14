import os
from moviepy import editor


def cut_video(
    video_file_in: str = os.path.join("samples", "crop.mp4"),
    video_file_out: str = os.path.join("output", "crop_clip.mp4"),
    start: int = 0,
    end: int = 0,
) -> str:
    """Cut video during a given time interval in seconds"""

    myclip_in = editor.VideoFileClip(video_file_in)
    myclip_out = myclip_in.subclip(start, end)
    myclip_out.write_videofile(video_file_out)
    myclip_in.close()
    myclip_out.close()

    return video_file_out
