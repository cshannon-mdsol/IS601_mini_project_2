from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.StandardDeviation import stddev
from pprint import pprint

def skewness(data):
    try:
        distanceArray = []
        meanDeviationValue = 0

        for item in data:
            distanceArray.append(item)

            num_values = len(data)
            x = 0
            z= 0
        i=0
        for i in distanceArray:
            x = i
        pprint(distanceArray[1])
        x = 3 * (distanceArray[0] - distanceArray[1]) / distanceArray[2]
        pprint(round(x, 1))

        return x
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/skewness/
# https://study.com/academy/lesson/skewness-in-statistics-definition-formula-example.html
# 3*(mean-median)/stddev

