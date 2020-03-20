from numpy.random import seed
from Random.NListItem import NListItem


def pick_from_list_seed(list, range, seed):
    seed(seed)
    list2 = NListItem.pick_from_list(list, range)
    return list2
