from moviepy.editor import VideoFileClip, CompositeVideoClip
import os, cv2


def overlay_two_videos_opencv(
    path_videos, name_video1, name_video2, opacities, path_video_out
):
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
    video_clips = [VideoFileClip(path) for path in list_videos_path]
    opacities = [
        0.5 for i in range(len(list_videos_path))
    ]  # Opacity values for each video
    overlayed_clips = []

    for clip, opacity in zip(video_clips, opacities):
        overlayed_clip = clip.copy().set_opacity(opacity)
        overlayed_clips.append(overlayed_clip)

    final_clip = CompositeVideoClip(overlayed_clips)
    final_clip.write_videofile(path_video_out, codec="libx264")
    for clip in video_clips:
        clip.close()
