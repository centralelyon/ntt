from ntt.sounds.sound_detection import count_sound_occurence,detect_sound_ref
from dotenv import load_dotenv
import os

if __name__=="__main__":
    load_dotenv()
    video_path=os.path.join(f"{os.environ.get('VIDEO_PATH_IN')}","ALEXIS-LEBRUN_vs_JANG-WOOJIN.mp4")
    sound_path=os.path.join(f"{os.environ.get('PATH_IN')}","archivo.mp3")
    print(detect_sound_ref(video_path,sound_path))
