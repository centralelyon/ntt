from ntt.sounds.Sound_generation import Random_to_start

if __name__ == "__main__":
    # Paramètres de la vidéo
    start=0.1
    t=5.0
    f=440
    name = "video"

    # Générer la vidéo avec audio
    Random_to_start(start,t,f,name)
