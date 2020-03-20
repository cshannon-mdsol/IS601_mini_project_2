from random import seed
from Random.ListItem import ListItem


class ListItemSeed:

    @staticmethod
    def rand_list_seed(series, nut):
        seed(nut)
        return ListItem.list_item(series)
