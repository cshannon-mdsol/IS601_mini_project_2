from numpy.random import seed
from numpy.random import randint


def rand_num(number, min, max, seed):
    seed(seed)
    rand_data = []
    i = 1
    while i < number + 1:
        rand_data.append(randint(min, max))
        i += 1
    return rand_data
