from numpy.random import randint


class NListItem:

    @staticmethod
    def pick_from_list(realm):
        series = []
        length = len(series)
        for each in range(realm):
            position = randint(0, length-1)
            series.append(series[position])
        return series


