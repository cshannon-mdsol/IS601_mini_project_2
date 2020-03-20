from numpy.random import seed
from numpy.random import randint
from numpy.random import uniform


def rand_num(x, y, seed):
    seed(seed)
    number = randint(x, y)
    if instance(x, float):
        return GenNumberSeed.rand_float(x, y, seed)
    return number

def rand_float(x, y, seed):
    seed(seed)
    number = uniform(x, y)
    return number
