FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y \
    libopencv-dev \
    python3-opencv \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    ffmpeg    

RUN pip install numpy moviepy opencv-python-headless eyed3 pydub pyAudioAnalysis matplotlib scipy pandas pytest

WORKDIR /app

VOLUME /app

CMD [ "python", "script.py" ]