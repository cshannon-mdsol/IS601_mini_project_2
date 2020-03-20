from random import seed
from random import randint
from random import uniform


class GenNumberListSeed:

    @staticmethod
    def list_num(x, y, nut, realm):
        if isinstance(x, float):
            return list_float(x, y, nut, realm)
        series = []
        seed(nut)
        for each in range(realm):
            number = randint(x, y)
            series.append(number)
        return series

    @staticmethod
    def list_float(x, y, nut, realm):
        series = []
        seed(nut)
        for each in range(realm):
            number = uniform(x, y)
            series.append(number)
        return series
