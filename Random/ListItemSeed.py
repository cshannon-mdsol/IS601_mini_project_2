from random import seed


class ListItemSeed:

    @staticmethod
    def rand_list_seed(series, nut):
        seed(nut)
        length = len(series)
        position = randint(0, length - 1)
        return series[position]
