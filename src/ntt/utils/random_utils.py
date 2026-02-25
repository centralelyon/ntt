import numpy as np


def random_translate_direction(nb_direction=4):
    direction = []
    if nb_direction == 1:
        direction = ["up"]
    elif nb_direction == 2:
        direction = ["up", "down"]
    elif nb_direction == 3:
        direction = ["up", "down", "left"]
    elif nb_direction == 4:
        direction = ["up", "down", "left", "right"]
    elif nb_direction == 8:
        direction = ["up", "down", "left", "right", "up-left", "up-right", "down-left", "down-right"]
    else:
        raise ValueError("nb_direction must be 1, 2, 3, 4 or 8")
    return np.random.choice(direction)

if __name__ == "__main__":
    print(random_translate_direction())