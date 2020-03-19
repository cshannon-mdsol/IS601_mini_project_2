from Calculator.SquareRoot import square_root
from Statistics.Variance import variance
from pprint import pprint

def stddev(num):
    try:
        variance_float = variance(num)

        return round(square_root(variance_float), 5)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.mathsisfun.com/data/standard-deviation-formulas.html
