FROM python:3.10-slim-bullseye                                                                        
                                                                                                        
# Install system dependencies                                                                           
# libsndfile1 is required by librosa                                                                    
# The others are primarily for OpenCV and audio/video processing                                        
RUN apt-get update && apt-get install -y --no-install-recommends \                                      
    libopencv-dev \                                                                                     
    python3-opencv \                                                                                    
    libsm6 \                                                                                            
    libxext6 \                                                                                          
    libxrender-dev \                                                                                    
    libgl1-mesa-glx \                                                                                   
    libglib2.0-0 \                                                                                      
    ffmpeg \                                                                                            
    libsndfile1 \                                                                                       
    && rm -rf /var/lib/apt/lists/*                                                                      
                                                                                                        
WORKDIR /app                                                                                            
                                                                                                        
# Copy project files                                                                                    
COPY . /app                                                                                             
                                                                                                        
# Install the ntt package along with its dev dependencies                                               
# This automatically gets the requirements from pyproject.toml                                          
RUN pip install --no-cache-dir .[dev]                                                                   
                                                                                                        
ENV PYTHONPATH=/app/src                                                                                 
                                                                                                        
CMD ["pytest", "tests"] # Run tests by default