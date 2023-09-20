import subprocess,os,ffmpeg
from moviepy.editor import VideoFileClip
def split_video_ffmpeg(video_path_in,video_name,n,path_out):
    # Get the duration of the input video
    video=os.path.join(video_path_in,video_name)
    clip = VideoFileClip(video)
    duration = clip.duration
    clip.close()
    # Open the input video
    output_template = f"{os.path.join(path_out,'clip%d.mp4')}"
    start_time=0

    # FFmpeg command
    command = [
        'ffmpeg',
        '-i', video,
        '-ss', str(start_time),
        '-f', 'segment',
        '-segment_time', str(duration/n),
        '-vcodec', 'copy',
        '-reset_timestamps', '1',
        '-map', '0:0',
        '-an',
        output_template
    ]

    # Execute the FFmpeg command
    subprocess.run(command)