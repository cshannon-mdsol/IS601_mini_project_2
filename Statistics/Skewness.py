from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.StandardDeviation import stddev

def skewness(data):
    try:
        3*(mean-median)/stddev
https://www.statisticshowto.datasciencecentral.com/skewness/
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")
