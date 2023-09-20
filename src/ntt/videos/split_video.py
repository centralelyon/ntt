import subprocess,os,ffmpeg
from moviepy.editor import VideoFileClip
def split_video_ffmpeg(video_path_in,video_name,n,path_out):
    # Get the duration of the input video
    video=os.path.join(video_path_in,video_name)
    clip = VideoFileClip(video)
    duration = clip.duration
    clip.close()
    # Open the input video
    output_template = os.path.join(path_out,"clip%03d.mp4")
    start_time=0

    # FFmpeg command
    command = [
        'ffmpeg',
        '-i', video,
        '-c', 'copy',
        '-map', '0',
        '-segment_time', str(duration/n),
        '-f', 'segment',
        output_template
    ]

    # Execute the FFmpeg command
    subprocess.run(command)