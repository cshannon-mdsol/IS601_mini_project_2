#source https://pynative.com/python-random-choice/

import random
#
#
# class SimpleRandom(NListItemSeed):
#
#     @staticmethod
#     def simple_random(series, realm, nut):
#         seed(nut)
#         return NListItemSeed.pick_from_list_seed(series, realm, nut)

from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.SquareRoot import square_root
from pprint import pprint


def simple_random(series, itemsToReturn, nut):
    pprint("Hello hello hello ")
    print(series)
    #return random.choice(series)
    return random.choices(series, k=itemsToReturn)


