from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.StandardDeviation import stddev
from Calculator.Subtraction import  subtraction
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from pprint import pprint

def skewness(data):
    try:
        List1 = []
        List2 = []
        List3 = []
        List4 = []
        x = 0
        nStddev= stddev(data)
        #pprint(nStddev)
        nMean = mean(data)
        nCount = len(data)
        for n in data:
            List1.append(subtraction(nMean,n))
        #pprint(List1)
        for n2 in List1:
            List2.append(division(nStddev,n2))
        #pprint(List2)

        for n3 in List2:
            List3.append(n3 ** 3);
        #pprint(List3)
        for n4 in List3:
            x = x + n4
        #pprint(x)
        #pprint(nCount)
        nskewness = division(nCount,x)
        #pprint(float(nskewness))
        return nskewness
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/skewness/
# https://study.com/academy/lesson/skewness-in-statistics-definition-formula-example.html
# 3*(mean-median)/stddev
# https://sciencing.com/calculate-skew-6384014.html

