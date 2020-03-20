from random import seed
from Random.ListItem import ListItem


def rand_list_seed(list, seed):
    seed(seed)
    return ListItem.list_item(list)
