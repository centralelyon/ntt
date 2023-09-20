import subprocess,os

def split_video(video_path_in,video_name,n,path_out):
    # Get the duration of the input video
    video=os.path.join(video_path_in,video_name)
    ffprobe_command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video
    ]
    duration = float(subprocess.check_output(ffprobe_command))

    # Calculate the duration for each part
    part_duration = duration / n

    # Generate the FFmpeg command to split the video
    ffmpeg_command = [
        'ffmpeg',
        '-i', video,
        '-c', 'copy',
        '-map', '0',
        '-segment_time', str(part_duration),
        '-f', 'segment',
    ]

    # Add output file names to the command
    for i in range(n):
        output_file = os.path.join(path_out,f'clip{i+1}.mp4')
        ffmpeg_command.extend(['-reset_timestamps', '1', output_file])

    # Execute the FFmpeg command
    subprocess.run(ffmpeg_command)