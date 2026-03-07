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

# Copy dependency metadata first so dependency installation can be cached
COPY pyproject.toml README.md LICENSE /app/
COPY src /app/src

# Install the ntt package along with its dev dependencies.
# coverage is not needed at runtime and currently breaks numba/librosa optional
# integration under Python 3.12 in this image.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .[dev] \
    && pip uninstall -y coverage || true

# Copy the rest of the project after dependencies are installed
COPY tests /app/tests
COPY scripts /app/scripts
COPY CONTRIBUTING.md /app/
                                                                                                        
ENV PYTHONPATH=/app/src                                                                                 
                                                                                                        
CMD ["pytest", "tests"] # Run tests by default
