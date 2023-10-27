from moviepy.editor import *
from scipy.io.wavfile import write
import numpy as np
import tempfile
from dotenv import load_dotenv

load_dotenv()


def one_second_square_frequencies(p: float, f1: int, f2: int, filename: str):
    """Generates a black video with a duration of 1 second, where p percent
    of the video has frequency f1, and the rest has frequency f2. The video
    is saved at the path: samples/filename.mp4

    Args:
        p (float [0:1]): Percentage of the video with frequency f1
        f1 (int [20:20k]): Frequency in the first part of the video
        f2 (int [20:20k]): Frequency in the second part of the video
        filename (str): Name of the video (without the '.mp4' extension)
    """
    path = os.environ.get("PATH_IN")

    # Total duration of the video
    duration = 1.0

    # Create a temporary audio file for the first clip
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # Generate audio data for the first clip
    sample_rate = 44100
    t = np.linspace(0, duration * p, int(duration * p * sample_rate), endpoint=False)
    audio1_data = np.sin(2 * np.pi * f1 * t)

    # Save the audio data to the temporary file
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # Create a temporary audio file for the second clip
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # Generate audio data for the second clip
    t = np.linspace(
        0, (1 - p) * duration, int((1 - p) * duration * sample_rate), endpoint=False
    )
    audio2_data = np.sin(2 * np.pi * f2 * t)

    # Save the audio data to the temporary file
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # Create video clips with the corresponding audio files
    clip1 = ColorClip((1, 1), duration=duration * p, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip((1, 1), duration=(1 - p) * duration, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio2_filename)
    )

    # Concatenate the clips to form the final video
    final_clip = concatenate_videoclips([clip1, clip2])

    final_clip = final_clip.resize((1280, 720))

    # Save the video in .mp4 format with a frame rate of 30
    final_clip.write_videofile(
        path + filename + ".mp4", codec="libx264", audio_codec="aac", fps=50
    )

    # Close the temporary audio files
    audio1_file.close()
    audio2_file.close()


def random_to_start(start_time: float, duration: float, frequency: int, filename: str):
    """Generate black video whith white sound since start_time and constant frequency sound
    to the rest of the duration.
    return None if erreur

    Args:
        start_time (float): start of constant sound
        duration (float(>start_time)): duration of the video
        frequency (int): frequence on constant sound
        filename (str): name of the video (without .mp4)
    """
    path = os.environ.get("PATH_IN")

    # create a temporary audio for the first clip
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # Générer les données audio pour le premier clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.random.random(int(start_time * sample_rate))

    # Enregistrer les données audio dans le fichier temporaire
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # Créer un fichier audio temporaire pour le deuxième clip
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # Générer les données audio pour le deuxième clip
    t = np.linspace(
        0,
        duration - start_time,
        int((duration - start_time) * sample_rate),
        endpoint=False,
    )
    audio2_data = np.sin(2 * np.pi * frequency * t)

    # Enregistrer les données audio dans le fichier temporaire
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # Créer les clips vidéo avec les fichiers audio correspondants
    clip1 = ColorClip((1, 1), duration=start_time, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip(
        (1, 1), duration=duration - start_time, color=(0, 0, 0)
    ).set_audio(AudioFileClip(audio2_filename))

    # Concaténer les clips pour former la vidéo finale
    final_clip = concatenate_videoclips([clip1, clip2])

    final_clip = final_clip.resize((1280, 720))

    # Enregistrer la vidéo au format .mp4 avec une fréquence d'images de 30
    final_clip.write_videofile(
        path + filename + ".mp4", codec="libx264", audio_codec="aac", fps=50
    )

    # Supprimer les fichiers audio temporaires
    audio1_file.close()
    audio2_file.close()


def no_to_start(start_time: float, duration: float, frequency: int, filename: str):
    """Generate black video whith no sound since start_time and constant frequency sound
    to the rest of the duration.
    return None if erreur

    Args:
        start_time (float): start of constant sound
        duration (float(>start_time)): duration of the video
        frequency (int): frequence on constant sound
        filename (str): name of the video (without .mp4)
    """
    path = os.environ.get("PATH_IN")

    # Créer un fichier audio temporaire pour le premier clip
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # Générer les données audio pour le premier clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.zeros(int(start_time * sample_rate))

    # Enregistrer les données audio dans le fichier temporaire
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # Créer un fichier audio temporaire pour le deuxième clip
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # Générer les données audio pour le deuxième clip
    t = np.linspace(
        0,
        duration - start_time,
        int((duration - start_time) * sample_rate),
        endpoint=False,
    )
    audio2_data = np.sin(2 * np.pi * frequency * t)

    # Enregistrer les données audio dans le fichier temporaire
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # Créer les clips vidéo avec les fichiers audio correspondants
    clip1 = ColorClip((1, 1), duration=start_time, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip(
        (1, 1), duration=duration - start_time, color=(0, 0, 0)
    ).set_audio(AudioFileClip(audio2_filename))

    # Concaténer les clips pour former la vidéo finale
    final_clip = concatenate_videoclips([clip1, clip2])

    final_clip = final_clip.resize((1280, 720))

    # Enregistrer la vidéo au format .mp4 avec une fréquence d'images de 30
    final_clip.write_videofile(
        path + filename + ".mp4", codec="libx264", audio_codec="aac", fps=50
    )

    # Supprimer les fichiers audio temporaires
    audio1_file.close()
    audio2_file.close()


def vid2_decale(duration: float, decalage: float, filename: str):
    """génères 2 signaux aléatoire s1 et s2.
    génére 2 vidéo noirs, la première a la bande sons s1 et la seconde s2 puis s1.
    La première video est nommée filename+".mp4" et la seconde filename+"decale.mp4"

    Args:
        duration (float): durée du signal s1
        decalage (float): durée du signal s2
        filename (str): nom du fichier en sortie
    """
    path = os.environ.get("PATH_IN")

    # Créer un fichier audio temporaire pour le clip commun
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # Générer les données audio pour le premier clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.random.random(int(duration * sample_rate))

    # Enregistrer les données audio dans le fichier temporaire
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # Créer un fichier audio temporaire pour le decalage
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # Générer les données audio pour le deuxième clip
    audio2_data = np.random.random(int(decalage * sample_rate))

    # Enregistrer les données audio dans le fichier temporaire
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # Créer les clips vidéo avec les fichiers audio correspondants
    clip1 = ColorClip((1, 1), duration=duration, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip((1, 1), duration=decalage, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio2_filename)
    )

    # Concaténer les clips pour former la vidéo finale decale
    final_clip1 = clip1.resize((1280, 720))

    # Enregistrer la vidéo au format .mp4 avec une fréquence d'images de 30
    final_clip1.write_videofile(
        path + filename + ".mp4", codec="libx264", audio_codec="aac", fps=50
    )

    # Concaténer les clips pour former la vidéo finale decale
    final_clip2 = concatenate_videoclips([clip2, clip1])

    final_clip2 = final_clip2.resize((1280, 720))

    # Enregistrer la vidéo au format .mp4 avec une fréquence d'images de 30
    final_clip2.write_videofile(
        path + filename + "decale.mp4", codec="libx264", audio_codec="aac", fps=50
    )

    # Supprimer les fichiers audio temporaires
    audio1_file.close()
    audio2_file.close()


def dirac(duration: float, decalage: float, filename: str):
    """prend un signal s1 [1 0 0 0 ... 0] et un s2 [0 ... 0]
    génère 2 vidéos noirs,
    - filename+".mp4" : bande sonore s1
    - filename+"decale.mp4" : bande sonore s2 puis s1

    Args:
        duration (float): durée du signal s1
        decalage (float): durée du signal s2
        filename (str): nom du fichier en sortie
    """
    path = os.environ.get("PATH_IN")

    # Créer un fichier audio temporaire pour le clip commun
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # Générer les données audio pour le premier clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.zeros(int(duration * sample_rate))
    audio1_data[0] = 1

    # Enregistrer les données audio dans le fichier temporaire
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # Créer un fichier audio temporaire pour le decalage
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # Générer les données audio pour le deuxième clip
    audio2_data = np.zeros(int(decalage * sample_rate))

    # Enregistrer les données audio dans le fichier temporaire
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # Créer les clips vidéo avec les fichiers audio correspondants
    clip1 = ColorClip((1, 1), duration=duration, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip((1, 1), duration=decalage, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio2_filename)
    )

    # Concaténer les clips pour former la vidéo finale decale
    final_clip1 = clip1.resize((1280, 720))

    # Enregistrer la vidéo au format .mp4 avec une fréquence d'images de 30
    final_clip1.write_videofile(
        path + filename + ".mp4", codec="libx264", audio_codec="aac", fps=50
    )

    # Concaténer les clips pour former la vidéo finale decale
    final_clip2 = concatenate_videoclips([clip2, clip1])

    final_clip2 = final_clip2.resize((1280, 720))

    # Enregistrer la vidéo au format .mp4 avec une fréquence d'images de 30
    final_clip2.write_videofile(
        path + filename + "decale.mp4", codec="libx264", audio_codec="aac", fps=50
    )

    # Supprimer les fichiers audio temporaires
    audio1_file.close()
    audio2_file.close()
