"""TODO : polygone module provides ...
"""

from typing import Tuple

import cv2
import numpy as np


def draw_polygones(
    frame: np.ndarray,
    points: Tuple[Tuple] = None,
    couleur: Tuple[int, int, int] = (0, 0, 255),
    epaisseur: int = 2,
) -> None:
    """Ajoute a la frame un polygone du degrès de la taille de points, à
    l'epaisseur et couleur choisies. Les points seront relier dans leurs
    ordre dans le paramètre points.

    Args:
        frame (np.ndarray): _description_
        points (Tuple[Tuple], optional): _description_.
            Defaults to [[0, 0], [0, 1], [1, 1], [1, 0]].
        couleur (Tuple[int, int, int], optional): _description_.
            Defaults to (0, 0, 255).
        epaisseur (int, optional): Épaisseur du tracé. Defaults to 2.
    """
    # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/dangerous-default-value.html
    if points is None:
        points = [[0, 0], [0, 1], [1, 1], [1, 0]]

    n_lines = len(points)
    for i in range(n_lines):
        point1 = (int(points[i][1]), int(points[i][0]))
        point2 = (int(points[(i + 1) % n_lines][1]), int(points[(i + 1) % n_lines][0]))
        cv2.line(frame, point1, point2, color=couleur, thickness=epaisseur)
