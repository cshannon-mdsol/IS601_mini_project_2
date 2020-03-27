# from Random.GenNumberSeed import GenNumberSeed
#
#
# class SystematicSampling:
#
#     @staticmethod
#     def systematic_sampling(series):
#         size = len(series)
#         number = round((GenNumberSeed.rand_num(size, 2, size))/4)
#         if number == 1:
#             number = 3
#         series2 = []
#         temp = number - 1
#         while temp <= size-1:
#             value = series[temp]
#             series2.append(value)
#             temp += number
#         return series2

# source https://pynative.com/python-random-choice/

import random


def systematic_sampling(series, itemsToReturn, interval):
    # shuffle the series
    random.shuffle(series)
    returnedArray = []

    # start at a random point, then choose n number of itemsToReturn
    i = 0
    n = 0
    while i < itemsToReturn:
        if i == 0:
            returnedArray.append(series[i])
            n = n + interval
            i += 1
        else:
            returnedArray.append(series[n])
            n = n + interval
            if n > len(series):
                n = 0
            i += 1

    return returnedArray
