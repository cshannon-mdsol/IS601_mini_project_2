#https://www.mathsisfun.com/data/standard-deviation.html
from Calculator.Square import square
from Calculator.Division import division
from Statistics.Mean import mean
from Calculator.Subtraction import subtraction
from pprint import pprint

def variance(data):
    try:
        # 1. find the mean of the data
        calculatedMean = mean(data)
        pprint(calculatedMean)
        distanceArray = []
        meanDeviationValue = 0

        for item in data:
            distanceArray.append(abs(subtraction(item, calculatedMean)))

        num_values = len(data)
        x = 0
        for i in distanceArray:
            x = x + square(i)
        return int(division(num_values,x))
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/variance/
