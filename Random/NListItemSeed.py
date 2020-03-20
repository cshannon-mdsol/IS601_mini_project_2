from numpy.random import seed
from Random.NListItem import NListItem


class NListItemSeed:

    @staticmethod
    def pick_from_list_seed(series, realm, nut):
        seed(nut)
        series2 = NListItem.pick_from_list(series, realm)
        return series2
