from random import randint
from random import uniform


class GenNumber:

    @staticmethod
    def rand_num(x, y):
        if isinstance(x, float):
            return GenNumber.rand_float(x, y)
        return randint(x, y)

    @staticmethod
    def rand_float(x, y):
        return uniform(x, y)
