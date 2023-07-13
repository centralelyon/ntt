import cv2
import numpy as np
from typing import Tuple

def draw_polygones(frame: np.ndarray,
                   points: Tuple[Tuple] = [[0,0],[0,1],[1,1],[1,0]], 
                   couleur: Tuple[int, int, int] = (0, 0, 255),
                   epaisseur : int = 2
) -> None:
    """Ajoute a la frame un polygone du degrès de la taille de points, à l'epaisseur et couleur choisit.
    Les points seront relier dans leurs ordre dans le paramètre points.

    Args:
        frame (np.ndarray): _description_
        points (Tuple[Tuple], optional): _description_. Defaults to [[0,0],[0,1],[1,1],[1,0]].
        couleur (Tuple[int, int, int], optional): _description_. Defaults to (0, 0, 255).
        epaisseur(int) : epaisseur du tracé
    """
        
    n_lines = len(points)
    for i in range(n_lines):
        point1 = (int(points[i][1]),int(points[i][0]))
        point2 = (int(points[(i+1) % n_lines][1]),int(points[(i+1) % n_lines][0]))
        cv2.line(frame, point1, point2, color=couleur,thickness = epaisseur)