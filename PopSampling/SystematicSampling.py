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

# https://www.statisticshowto.datasciencecentral.com/systematic-sampling/
