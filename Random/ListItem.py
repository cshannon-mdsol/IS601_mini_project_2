from numpy.random import randint


def list_item(list):
    length = len(list)
    position = randint(0, length-1)
    return list[position]
