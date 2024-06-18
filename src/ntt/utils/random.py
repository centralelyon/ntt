"""TODO : random module provides ...
"""

import numpy as np


def random_translate_direction():
    """_summary_

    Returns:
        _type_: _description_
    """
    direction = ["up", "down", "left", "right"]
    return np.random.choice(direction)
