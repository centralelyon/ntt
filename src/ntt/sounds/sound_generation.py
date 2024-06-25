"""TODO : sound_generation module provides ...
"""

import os
import tempfile
from pathlib import Path

import numpy as np
from moviepy.editor import AudioFileClip, ColorClip, concatenate_videoclips
from scipy.io.wavfile import write


def one_second_square_frequencies(p: float, f1: int, f2: int,
                                  video_path: str | os.PathLike):
    """Generates a black video with a duration of 1 second, where p percent
    of the video has frequency f1, and the rest has frequency f2.

    Args:
        p (float [0:1]): Percentage of the video with frequency f1
        f1 (int [20:20k]): Frequency in the first part of the video
        f2 (int [20:20k]): Frequency in the second part of the video
        video_path (Path or str): Path to the video file
    """
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
        str(video_path),
        codec="libx264", audio_codec="aac", fps=50
    )

    # Close the temporary audio files
    audio1_file.close()
    audio2_file.close()


def random_to_start(start_time: float, duration: float, frequency: int,
                    video_path: str | os.PathLike):
    """Generate black video whith white sound since start_time and constant
    frequency sound to the rest of the duration.

    Args:
        start_time (float): start of constant sound
        duration (float(>start_time)): duration of the video
        frequency (int): frequence on constant sound
        video_path (Path or str): Path to the video file
    Returns:
        None if erreur
    """
    # create a temporary audio for the first clip
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # generate audio data for the first clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.random.random(int(start_time * sample_rate))

    # save audio data in a tomporary file
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # create a temporary audio for the second clip
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # generate audio data for the second clip
    t = np.linspace(
        0,
        duration - start_time,
        int((duration - start_time) * sample_rate),
        endpoint=False,
    )
    audio2_data = np.sin(2 * np.pi * frequency * t)

    # save audio data in a tomporary file
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # create clips with the associated audio files
    clip1 = ColorClip((1, 1), duration=start_time, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip(
        (1, 1), duration=duration - start_time, color=(0, 0, 0)
    ).set_audio(AudioFileClip(audio2_filename))

    # Concatenate clips to form the final clip
    final_clip = concatenate_videoclips([clip1, clip2])

    final_clip = final_clip.resize((1280, 720))

    # save video with mp4 format and fps 30
    final_clip.write_videofile(
        str(video_path),
        codec="libx264",
        audio_codec="aac", fps=50
    )

    # delete temporary audio files
    audio1_file.close()
    audio2_file.close()


def no_to_start(start_time: float, duration: float, frequency: int,
                video_path: str | os.PathLike):
    """Generate black video whith no sound since start_time and constant frequency sound
    to the rest of the duration.
    TODO : Seems there is no return value ?
    return None if erreur

    Args:
        start_time (float): start of constant sound
        duration (float(>start_time)): duration of the video
        frequency (int): frequence on constant sound
        video_path (Path or str): Path to the video file
    """
    # create a temporary audio for the first clip
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # generate audio data for the first clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.zeros(int(start_time * sample_rate))

    # save audio data in a tomporary file
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # create a temporary audio for the second clip
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # generate audio data for the second clip
    t = np.linspace(
        0,
        duration - start_time,
        int((duration - start_time) * sample_rate),
        endpoint=False,
    )
    audio2_data = np.sin(2 * np.pi * frequency * t)

    # save audio data in a tomporary file
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # create clips with the associated audio files
    clip1 = ColorClip((1, 1), duration=start_time, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip(
        (1, 1), duration=duration - start_time, color=(0, 0, 0)
    ).set_audio(AudioFileClip(audio2_filename))

    # Concatenate clips to form the final clip
    final_clip = concatenate_videoclips([clip1, clip2])

    final_clip = final_clip.resize((1280, 720))

    # save video with mp4 format and fps 30
    final_clip.write_videofile(
        str(video_path),
        codec="libx264",
        audio_codec="aac",
        fps=50
    )

    # delete temporary audio files
    audio1_file.close()
    audio2_file.close()


def video2_shifted(duration: float, decalage: float,
                   filepath: str | os.PathLike, filename: str):
    """Generates 2 random signals s1 and s2. Then, generates 2 black videos in
    the given {filepath}:

    - first has s1 soundtrack and is named {filename}.mp4
    - second has s2 soundtrack then s1 and is named {filename}shifted.mp4

    Args:
        duration (float): s1 signal duration
        decalage (float): s2 signal duration
        filepath (Path or str): Path to the generated video files
        filename (str): Base name for the video files
    """
    # create a temporary audio for the common clip
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # generate audio data for the first clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.random.random(int(duration * sample_rate))

    # save audio data in temporary file
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # create temporary audio file for shift
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # generate audio data for the second clip
    audio2_data = np.random.random(int(decalage * sample_rate))

    # save audio data in temporary file
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # create clips with the associated audio files
    clip1 = ColorClip((1, 1), duration=duration, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip((1, 1), duration=decalage, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio2_filename)
    )

    # Concatenate clips to form the final shifted clip
    final_clip1 = clip1.resize((1280, 720))

    # save video with mp4 format and fps 30
    final_clip1.write_videofile(
        str(Path(filepath) / f"{filename}.mp4"),
        codec="libx264",
        audio_codec="aac",
        fps=50
    )

    # Concatenate clips to form the final shifted clip
    final_clip2 = concatenate_videoclips([clip2, clip1])

    final_clip2 = final_clip2.resize((1280, 720))

    # save video with mp4 format and fps 30
    final_clip2.write_videofile(
        str(Path(filepath) / f"{filename}shifted.mp4"),
        codec="libx264",
        audio_codec="aac",
        fps=50
    )

    # delete temporary audio file
    audio1_file.close()
    audio2_file.close()


def dirac(duration: float, decalage: float,
          filepath: str | os.PathLike, filename: str):
    """Takes s1 signal [1 0 0 0 ... 0] then s2 signal [0 ... 0], generates
    2 black videos :

    - {filename}.mp4 has s1 soundtrack
    - {filename}shifted.mp4 has s2 soundtrack then s1

    Args:
        duration (float): s1 signal duration
        decalage (float): s2 signal duration
        filepath (Path or str): Path to the generated video files
        filename (str): Base name for the video files
    """
    # Create temporary audio file for the common clip
    audio1_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio1_filename = audio1_file.name

    # Generate audio data for the first clip
    sample_rate = 44100
    # t = np.linspace(0, start_time, int(start_time * sample_rate), endpoint=False)
    audio1_data = np.zeros(int(duration * sample_rate))
    audio1_data[0] = 1

    # Save audio data in temporary file
    write(audio1_filename, sample_rate, audio1_data.astype(np.float32))

    # Create temporay audio file for shift
    audio2_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio2_filename = audio2_file.name

    # Generate audio data for the second clip
    audio2_data = np.zeros(int(decalage * sample_rate))

    # Save audio data in temporary file
    write(audio2_filename, sample_rate, audio2_data.astype(np.float32))

    # Generate video clips with associated audio files
    clip1 = ColorClip((1, 1), duration=duration, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio1_filename)
    )
    clip2 = ColorClip((1, 1), duration=decalage, color=(0, 0, 0)).set_audio(
        AudioFileClip(audio2_filename)
    )

    # Concatenate clips to form the final shifted video
    final_clip1 = clip1.resize((1280, 720))

    # Save video in mp4 format and fps 30
    final_clip1.write_videofile(
        str(Path(filepath) / f"{filename}.mp4"),
        codec="libx264",
        audio_codec="aac",
        fps=50
    )

    # Concatenate clips to form final shifted video
    final_clip2 = concatenate_videoclips([clip2, clip1])

    final_clip2 = final_clip2.resize((1280, 720))

    # Save video in mp4 format and with fps 30
    final_clip2.write_videofile(
        str(Path(filepath) / f"{filename}shifted.mp4"),
        codec="libx264",
        audio_codec="aac",
        fps=50
    )

    # Delete temporary audio files
    audio1_file.close()
    audio2_file.close()
