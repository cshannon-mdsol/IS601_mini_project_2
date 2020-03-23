from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.StandardDeviation import stddev
from Calculator.Subtraction import  subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication
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
        #pprint(distanceArray[1])
        a = subtraction( distanceArray[1],distanceArray[0])
        #pprint(a)
        b = division(distanceArray[2],a)
        #pprint(b)
        c = multiplication(b,3)
        #pprint(c)
        #nSkewness=float(round(x,5))
        return round(c,5)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/skewness/
# https://study.com/academy/lesson/skewness-in-statistics-definition-formula-example.html
# 3*(mean-median)/stddev

