from random import seed
from Random.NListItemSeed import NListItemSeed


class SimpleRandom(NListItemSeed):

    @staticmethod
    def simple_random(series, realm, nut):
        seed(nut)
        return NListItemSeed.pick_from_list_seed(series, realm, nut)
