import random
import string


def generate_random_string(length=8):
    """generate a string of random characters like yHgFZBrK"""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
