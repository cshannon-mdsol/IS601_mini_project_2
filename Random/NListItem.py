from numpy.random import randint


def pick_from_list(list, range):
    list2 = []
    length = len(list)
    for _ in range(range):
        position = randint(0, length-1)
        list2.append(list[position])
    return list2
