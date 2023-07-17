import random
import string
import uuid


def generate_random_string(length=8):
    """generate a string of random characters like yHgFZBrK"""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_uuid4():
    """generate random id like d6799325-ba91-4cee-9ddc-3d12464e6c52"""
    return str(uuid.uuid4())
