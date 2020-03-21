from Statistics.Mean import mean
from Statistics.StandardDeviation import stddev
from pprint import pprint


def z_score(num):
    try:
        z_mean = mean(num)
        sd = stddev(num)
        z_list = []

        for x in num:
            z = round(((float(x) - float(z_mean)) / float(sd)), 6)
            z_list.append(z)

        return z_list

    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/z-score/
