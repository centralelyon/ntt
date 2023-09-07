from moviepy.editor import VideoFileClip


def get_video_dimensions(video_path):
    try:
        clip = VideoFileClip(video_path)
        width, height = clip.size
        clip.close()
        return width, height
    except Exception as e:
        print(f"Error: {e}")
        return None
