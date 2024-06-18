"""TODO : strings module provides ...
"""

import random
import string
import uuid


def generate_random_string(length=8):
    """Generate a string of random characters like yHgFZBrK

    Args:
        length (int, optional): _description_. Defaults to 8.

    Returns:
        _type_: _description_
    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_uuid4():
    """Generate random id like d6799325-ba91-4cee-9ddc-3d12464e6c52

    Returns:
        _type_: _description_
    """
    return str(uuid.uuid4())
