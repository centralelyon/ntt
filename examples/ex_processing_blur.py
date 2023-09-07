import numpy as np
import cv2
import matplotlib.pyplot as plt
from ntt.frames.processing import blur_frame

input_frame = np.random.randint(
    0, 256, size=(480, 640, 3), dtype=np.uint8
)  # Example random frame
blurred_frame = blur_frame(
    input_frame, kernel_size=(15, 15), region=(100, 100, 200, 150)
)


# Display the original and blurred images side by side
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(input_frame)

plt.subplot(1, 2, 2)
plt.title("Blurred Image")
plt.imshow(blurred_frame)

plt.tight_layout()
plt.show()
