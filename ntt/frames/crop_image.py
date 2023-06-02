
def crop(image,x1,y1,x2,y2):
    """
        Fonction permettant d'extraire une sous image
        Entrée: l'image,coin en haut à gauche du premier point selon x, coin en haut à gauche du premier point selon y,
                coin en bas à droite du premier point selon x, coin en bas à droite du premier point selon y
        Sortie: l'image croppée
    """
    return(image[x1:x2,y1:y2])