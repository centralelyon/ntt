# pylint: disable=C0114

import cv2
import numpy as np
from ntt.draw.polygone import draw_polygones

# https://peps.python.org/pep-0008/#constants
DIMX = 400
DIMY = 600

if __name__ == "__main__":
    # build initial frame
    image = np.full((DIMX, DIMY, 3), (0, 0, 0), dtype=np.uint8)

    # draw rectangle
    points = [
        [DIMX / 4, DIMY / 4],
        [3 * DIMX / 4, DIMY / 4],
        [3 * DIMX / 4, 3 * DIMY / 4],
        [DIMX / 4, 3 * DIMY / 4],
    ]
    couleur = [255, 0, 0]  # blue
    draw_polygones(image, points=points, couleur=couleur, epaisseur=3)

    # draw n-points d'un polygone regulier
    n = 8  # pylint: disable=C0103
    r = min(DIMX, DIMY) / 3
    points = []
    for x in range(n):
        points.append(
            [
                DIMX / 2 + r * np.cos(2 * x * np.pi / n),
                DIMY / 2 + r * np.sin(2 * x * np.pi / n),
            ]
        )
    couleur = [0, 255, 0]  # vert
    draw_polygones(image, points=points, couleur=couleur, epaisseur=2)

    # draw n-points d'un polygone random
    n = 3  # pylint: disable=C0103
    points = []
    for x in range(n):
        points.append([np.random.randint(0, DIMX), np.random.randint(0, DIMY)])
    couleur = [0, 0, 255]  # rouge
    draw_polygones(image, points=points, couleur=couleur, epaisseur=1)

    cv2.imshow("Black frame", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
