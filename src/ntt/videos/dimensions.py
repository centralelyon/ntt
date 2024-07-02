"""TODO : dimensions module provides ...
"""

from moviepy.editor import VideoFileClip


def get_video_dimensions(video_path):
    """Get the video width and height.

    Args:
        video_path (str or Path): Full path to the input video

    Returns:
        tuple of int: width and height of the video
    """
    width = None
    height = None

    try:
        clip = VideoFileClip(str(video_path))
        width, height = clip.size
        clip.close()

    except Exception as e:
        print(f"Error: {e}")

    return width, height
