"""TODO : zoom module provides ...
"""

from moviepy.editor import CompositeVideoClip, VideoFileClip


def zoom_xy(
    input_video, output_video, zoom_x, zoom_y, zoom_duration=1.0, screensize=(640, 360)
):
    """_summary_

    Args:
        input_video (_type_): _description_
        output_video (_type_): _description_
        zoom_x (_type_): _description_
        zoom_y (_type_): _description_
        zoom_duration (float, optional): _description_. Defaults to 1.0.
        screensize (tuple, optional): _description_. Defaults to (640, 360).
    """
    clip = VideoFileClip(input_video)

    zoom_function = lambda t: 1 + zoom_duration * t

    zoomed_clip = (
        clip.crop(
            x1=zoom_x - screensize[0] / 2,
            x2=zoom_x + screensize[0] / 2,
            y1=zoom_y - screensize[1] / 2,
            y2=zoom_y + screensize[1] / 2,
        )
        .resize(zoom_function)
        .set_position(("center", "center"))
        .set_duration(zoom_duration)
    )

    final_video = CompositeVideoClip(
        [zoomed_clip.set_position(("center", "center"))], size=screensize
    )
    final_video.write_videofile(output_video, fps=clip.fps)
