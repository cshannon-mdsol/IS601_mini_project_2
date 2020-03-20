from random import seed
from random import randint


def rand_num(number, base, top, nut):
    seed(nut)
    rand_data = []
    i = 1
    while i < number + 1:
        rand_data.append(randint(base, top))
        i += 1
    return rand_data
