import subprocess,os,ffmpeg

def split_video(video_path_in,video_name,n,path_out):
    # Get the duration of the input video
    video=os.path.join(video_path_in,video_name)
    # Open the input video
    input_stream = ffmpeg.input(video)

    # Split the video into equal parts
    split_streams = ffmpeg.split(input_stream, n)

    # Output files
    output_files = [f"{os.environ.get('PATH_OUT')}/clip{i+1}.mp4" for i in range(num_parts)]

    # Save each part to a separate file
    for i, stream in enumerate(split_streams):
        output_file = output_files[i]
        ffmpeg.output(stream, output_file).run()