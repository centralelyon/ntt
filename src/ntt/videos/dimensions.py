"""TODO : dimensions module provides ...
"""

from moviepy.editor import VideoFileClip


def get_video_dimensions(video_path):
    """_summary_

    Args:
        video_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        clip = VideoFileClip(video_path)
        width, height = clip.size
        clip.close()
        return width, height
    
    except Exception as e:
        print(f"Error: {e}")
        return None, None
