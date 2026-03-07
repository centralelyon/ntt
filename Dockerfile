FROM python:3.12-slim-bookworm

# Install system dependencies                                                                           
# libsndfile1 is required by librosa                                                                    
# The others are primarily for OpenCV and audio/video processing                                        
RUN apt-get update && apt-get install -y --no-install-recommends \                                      
    libsm6 \                                                                                            
    libxext6 \                                                                                          
    libxrender1 \                                                                                       
    libgl1 \                                                                                            
    libglib2.0-0 \                                                                                      
    ffmpeg \                                                                                            
    libsndfile1 \                                                                                       
    && rm -rf /var/lib/apt/lists/*                                                                      
                                                                                                        
WORKDIR /app                                                                                            
                                                                                                        
# Copy project files                                                                                    
COPY . /app                                                                                             
                                                                                                        
# Install the ntt package along with its dev dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir .[dev]
                                                                                                        
ENV PYTHONPATH=/app/src                                                                                 
                                                                                                        
CMD ["pytest", "tests"] # Run tests by default
