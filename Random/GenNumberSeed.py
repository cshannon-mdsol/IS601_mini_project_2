from random import seed
from random import randint
from random import uniform


class GenNumberSeed:

    @staticmethod
    def rand_num(x, y, nut):
        seed(nut)
        number = randint(x, y)
        if isinstance(x, float):
            return GenNumberSeed.rand_float(x, y, nut)
        return number

    @staticmethod
    def rand_float(x, y, nut):
        seed(nut)
        number = uniform(x, y)
        return number
