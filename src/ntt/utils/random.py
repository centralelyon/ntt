import numpy as np


def random_translate_direction():
    direction = ["up", "down", "left", "right"]
    return np.random.choice(direction)