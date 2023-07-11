import cv2
import numpy as np

# Video properties
width = 640
height = 480
fps = 30
duration = 5

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
out = cv2.VideoWriter(
    "samples/peak_black_gray_2500ms.mp4", fourcc, fps, (width, height)
)

# Calculate frame count
frame_count = int(fps * duration)

# Generate the frames
for i in range(frame_count):
    # Calculate the current time in seconds
    time = i / fps

    # Calculate the current intensity based on time
    if time < 2.5:
        intensity = int((time / 2.5) * 255)
    else:
        intensity = int(((5 - time) / 2.5) * 255)

    # frame = generate_frame(intensity, width, height)
    # Create a frame with gradually increasing intensity for each color channel
    frame = np.full(
        (height, width, 3), (intensity, intensity, intensity), dtype=np.uint8
    )

    # Write the frame to the video file
    out.write(frame)

# Release the VideoWriter
out.release()
