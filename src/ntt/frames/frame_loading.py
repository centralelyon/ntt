import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import imageio.v2 as imageio
from skimage import io


# --- Pillow ---
def load_image_pil(path):
    try:
        return np.array(Image.open(path))
    except Exception as e:
        raise FileNotFoundError(f"Could not open image: {path}") from e


# --- Matplotlib ---
def load_image_matplotlib(path):
    try:
        return np.array(plt.imread(path))
    except Exception as e:
        raise FileNotFoundError(f"Could not open image: {path}") from e


# --- OpenCV ---
def load_image_cv2(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Could not open image: {path}")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# --- imageio ---
def load_image_imageio(path):
    try:
        return np.array(imageio.imread(path))
    except Exception as e:
        raise FileNotFoundError(f"Could not open image: {path}") from e


# --- scikit-image ---
def load_image_skimage(path):
    try:
        return io.imread(path)
    except Exception as e:
        raise FileNotFoundError(f"Could not open image: {path}") from e


import torch
from torchvision import io


def load_image_torch(path):
    """
    Loads an image as a PyTorch tensor (C, H, W) with values 0-1.
    Raises FileNotFoundError if the file can't be opened.
    """
    try:
        # Returns a tensor of shape (C, H, W) with dtype=torch.uint8
        img = io.read_image(path)
        return img.float() / 255.0  # convert to float [0,1]
    except Exception as e:
        raise FileNotFoundError(f"Could not open image: {path}") from e
