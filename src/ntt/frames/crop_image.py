import numpy as np


def crop(image: np.ndarray, x1: int, y1: int, x2: int, y2: int):
    """
    Fonction permettant d'extraire une sous image
    Entrée: l'image,coin en haut à gauche du premier point selon x, coin en haut à gauche du premier point selon y,
            coin en bas à droite du premier point selon x, coin en bas à droite du premier point selon y
    Sortie: l'image croppée
    """
    return image[x1:x2, y1:y2]
