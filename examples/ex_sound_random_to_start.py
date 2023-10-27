from ntt.sounds.sound_generation import random_to_start

if __name__ == "__main__":
    # video parameters
    start = 0.1
    t = 5.0
    f = 440
    name = "video"

    # generate video with audio
    random_to_start(start, t, f, name)
