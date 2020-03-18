#         https://www.mathsisfun.com/data/mean-deviation.html
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def mean_deviation(data):
    try:
        # 1. find the mean of the data
        calculatedMean = mean(data)
        distanceArray = []
        meanDeviationValue = 0

        for item in data:
            distanceArray.append( abs(subtraction(item, calculatedMean)) )
        # 2. find the distance of each value from that mean
        # iterate the data list, subtract it from general mean, store it in a list

        meanDeviationValue = mean(distanceArray)
        return meanDeviationValue
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")


