from numpy.random import randint
from numpy.random import uniform


def rand_num(x, y):
    if instance(x, float):
        return GenNumber.rand_float(x, y)
    return randint(x, y)

def rand_float(x, y):
    return uniform(x, y)
