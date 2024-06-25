"""TODO : video_overlay module provides ...
"""

import os

import cv2
from moviepy.editor import CompositeVideoClip, VideoFileClip


def overlay_two_videos_opencv(
    path_videos, name_video1, name_video2, opacities, path_video_out
):
    """_summary_

    Args:
        path_videos (_type_): _description_
        name_video1 (_type_): _description_
        name_video2 (_type_): _description_
        opacities (_type_): _description_
        path_video_out (_type_): _description_
    """
    path_video1 = os.path.join(path_videos, name_video1)
    path_video2 = os.path.join(path_videos, name_video2)
    path_out = path_video_out

    video1 = cv2.VideoCapture(path_video1)
    video2 = cv2.VideoCapture(path_video2)
    width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video1.get(cv2.CAP_PROP_FPS)

    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    output_video = cv2.VideoWriter(path_out, fourcc, fps, (width, height))
    while True:
        # Lire une image de la vidéo
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()

        # Write the processed frame to the output video

        # Vérifier si la lecture de la vidéo est terminée
        if not ret1 or not ret2:
            break
        overlayed_frame = cv2.addWeighted(frame1, opacities[0], frame2, opacities[1], 0)
        output_video.write(overlayed_frame)

        # Wait for the 'q' key to quit
    # Libérer les ressources
    video1.release()
    video2.release()
    output_video.release()


def overlay_videos_moviepy(list_videos_path, opacities, path_video_out):
    """_summary_

    Args:
        list_videos_path (_type_): _description_
        opacities (_type_): _description_
        path_video_out (_type_): _description_
    """
    video_clips = []
    overlayed_clips = []

    if opacities is None:
        opacities = [0.5] * len(list_videos_path)

    for path, opacity in zip(list_videos_path, opacities):
        clip = VideoFileClip(str(path))
        video_clips.append(clip)

        overlayed_clip = clip.copy().set_opacity(opacity)
        overlayed_clips.append(overlayed_clip)

    final_clip = CompositeVideoClip(overlayed_clips)

    final_clip.write_videofile(str(path_video_out), codec="libx264")

    for clip in video_clips:
        clip.close()
