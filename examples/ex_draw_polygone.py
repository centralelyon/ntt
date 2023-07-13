import numpy as np
import cv2
from ntt.draw.polygone import draw_polygones

if __name__=="__main__":
    #constructin image initiale
    dimx=400
    dimy=600
    image = np.full((dimx,dimy, 3), (0,0,0), dtype=np.uint8)

    #draw rectangle
    points=[[dimx/4, dimy/4],
            [3*dimx/4, dimy/4],
            [3*dimx/4, 3*dimy/4],
            [dimx/4, 3*dimy/4]]
    couleur=[255,0,0] #bleu
    draw_polygones(image,points=points,couleur=couleur,epaisseur=3)

    #draw n-points d'un polygone regulier
    n=8
    r=min(dimx,dimy)/3
    points=[]
    for x in range(n):
        points.append([dimx/2+r*np.cos(2*x*np.pi/n),dimy/2+r*np.sin(2*x*np.pi/n)])
    couleur=[0,255,0] #vert
    draw_polygones(image,points=points,couleur=couleur,epaisseur=2)

    #draw n-points d'un polygone random
    n=3
    points=[]
    for x in range(n):
        points.append([np.random.randint(0,dimx),np.random.randint(0,dimy)])
    couleur=[0,0,255] #rouge
    draw_polygones(image,points=points,couleur=couleur,epaisseur=1)

    cv2.imshow("Image noire", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()