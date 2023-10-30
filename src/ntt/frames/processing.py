import numpy as np
import cv2
import matplotlib.pyplot as plt


def blur_frame(frame, kernel_size=(5, 5), region=None):
    """
    Apply Gaussian blur to a frame (NumPy array).

    Parameters:
        frame (numpy.ndarray): Input frame as a NumPy array.
        kernel_size (tuple): Size of the Gaussian kernel for blurring.
        region (tuple): Region of interest (x, y, width, height) to blur. If None, the entire frame will be blurred.

    Returns:
        numpy.ndarray: Blurred frame as a NumPy array.
    """

    if not isinstance(frame, np.ndarray):
        raise ValueError("Input frame must be a NumPy array.")

    blurred_frame = frame.copy()

    if region:
        x, y, width, height = region

        if x < 0 or y < 0 or x + width > frame.shape[1] or y + height > frame.shape[0]:
            raise ValueError("Specified region is out of frame bounds.")

        region_of_interest = blurred_frame[y : y + height, x : x + width]
        blurred_region = cv2.GaussianBlur(region_of_interest, kernel_size, 0)
        blurred_frame[y : y + height, x : x + width] = blurred_region
    else:
        blurred_frame = cv2.GaussianBlur(blurred_frame, kernel_size, 0)

    return blurred_frame


def experiment_blur():
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


def translate_horizontally(frame, translation_rate):
    frame1 = np.zeros_like(frame)
    h, w, _ = frame.shape

    if translation_rate > 0:
        frame1[:, translation_rate:w] = frame[:, : w - translation_rate]
    else:
        frame1[:, : w - translation_rate] = frame[:, translation_rate:w]
    return frame1


def translate_vertically(frame, translation_rate):
    frame1 = np.zeros(frame.shape)
    h, w, _ = frame.shape

    if translation_rate > 0:
        frame1[translation_rate:h, :] = frame[: h - translation_rate, :]
    else:
        frame1[: h - translation_rate, :] = frame[translation_rate:h, :]
    return frame1
