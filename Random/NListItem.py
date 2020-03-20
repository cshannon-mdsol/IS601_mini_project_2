from numpy.random import randint


class NListItem:

    @staticmethod
    def pick_from_list(series, realm):
        series2 = []
        length = len(series2)
        for each in range(realm):
            position = randint(0, length-1)
            series2.append(series[position])
        return series2
