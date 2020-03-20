from numpy.random import seed
from numpy.random import randint
from numpy.random import uniform


def list_num(x, y, seed, range):
    if instance(x, float):
        return list_float(x,y, seed, range)
    list = []
    seed(seed)
    for _ in range(range):
        number = randint(x, y)
        list.append(number)
    return list

def list_float(x, y, seed, range):
    list = []
    seed(seed)
    for _ in range(range):
        number = uniform(x, y)
        list.append(number)
    return list
