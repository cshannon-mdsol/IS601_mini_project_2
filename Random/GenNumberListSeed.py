from random import seed
from random import random


def generate_numbers_list_seed(x, y, seed_value, list_size):
    seed(seed_value)
    the_array = []
    for i in range(list_size):
        theArray.append(random.randrange(x, y))
    return the_array
