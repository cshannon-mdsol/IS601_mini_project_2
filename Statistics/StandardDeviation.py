from Calculator.SquareRoot import square_root
from Statistics.Variance import variance
from Statistics.Mean import mean
from pprint import pprint

def stddev(num):
    try:
        # 1. Goes into Variance() to get the the mean and the variance
        variance_float = variance(num)
        # 2. Gets sqrt to get the standard Deviation
        x = round(square_root(variance_float), 5)
        return int(x)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.mathsisfun.com/data/standard-deviation-formulas.html
# https://www.mathsisfun.com/data/standard-deviation.html
