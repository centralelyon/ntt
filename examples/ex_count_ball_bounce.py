from moviepy.editor import VideoFileClip, TextClip
import cv2,os
from dotenv import load_dotenv
from ntt.sounds.sound_detection import detect_sound_ref_librosa
if __name__=="__main__":
    load_dotenv()
    samples_path=os.environ.get('PATH_IN')
    video_name = "AMIGO-ROBOT_COTE.mp4"
    ref_sound_name="ping.wav"
    path_out=os.environ.get('PATH_OUT')
    video=os.path.join(samples_path,video_name)


    target_sound_start_times = detect_sound_ref_librosa(samples_path,video_name,ref_sound_name,path_out)
    video = cv2.VideoCapture(video)
    ret,frame=video.read()
    height, width, _ = frame.shape
    video.release()
    video = cv2.VideoCapture(video)
    fps = video.get(cv2.CAP_PROP_FPS)
    i=0
    j=0
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    text_color = (255, 255, 255)  # White color
    text_thickness = 2
    text_position = (10, 30)  # Left top corner position
    output_file = "out.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
    while True:
        i+=1
        ret,frame=video.read()
        
        if not ret:
            break
        temps_en_secondes=(i/fps)
        if j<len(target_sound_start_times) and temps_en_secondes>=target_sound_start_times[j]:
            j=j+1
        height, width, _ = frame.shape
        text=str(j)
        cv2.putText(frame, text, text_position, font, font_scale, text_color, text_thickness)
        video_writer.write(frame)


    video.release()
    video_writer.release()