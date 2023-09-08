from moviepy.editor import VideoFileClip, CompositeVideoClip
import os,cv2
def video_fusion_image(path_videos,name_video1,name_video2,video_out):
    path_video1=os.path.join(path_videos,name_video1)
    path_video2=os.path.join(path_videos,name_video2)
    path_out=os.path.join(path_videos,video_out)
    
    video1 = cv2.VideoCapture(path_video1)
    video2 = cv2.VideoCapture(path_video2)
    width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video1.get(cv2.CAP_PROP_FPS)

    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video = cv2.VideoWriter(
        path_out, fourcc, fps, (width, height)
    )
    while True:
        # Lire une image de la vidéo
        ret1, frame1 = video1.read()
        ret2,frame2=video2.read()
        overlayed_frame = cv2.addWeighted(frame1, 0.5, frame2, 0.5, 0)

        # Write the processed frame to the output video
        output_video.write(overlayed_frame)

        # Vérifier si la lecture de la vidéo est terminée
        if not ret1 or not ret2:
            break

        # Wait for the 'q' key to quit
    # Libérer les ressources
    video1.release()
    video2.release()
    output_video.release()