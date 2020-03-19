from random import seed
from random import random


def generate_number_seed(x, y, seed_value):
    seed(seed_value)
    return random.randrange(x, y)
