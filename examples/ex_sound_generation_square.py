from ntt.sounds.sound_generation import one_seconde_square_frequencies

if __name__ == "__main__":
    # Paramètres de la vidéo
    frequency1 = 440  # audio frequency for the first percentage
    frequency2 = 680  # audio frequency for the rest percentage
    percentage = 0.5  # percentage of video with first percentage
    filename = "video"

    # generate video with audio
    one_seconde_square_frequencies(percentage, frequency1, frequency2, filename)
