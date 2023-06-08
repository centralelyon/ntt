from ntt.sounds.Sound_generation import One_seconde_square_frequencies,Random_to_start

if __name__ == "__main__":
# Paramètres de la vidéo
    frequency1 = 440  # Fréquence audio pour le pourcentage initial
    frequency2 = 680  # Fréquence audio pour le reste de la vidéo
    percentage = 0.5  # Pourcentage de la vidéo avec la fréquence audio 440 Hz
    filename = "video"

    # Générer la vidéo avec audio
    One_seconde_square_frequencies(percentage, frequency1, frequency2,filename)