from Calculator.SquareRoot import square_root
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Statistics.Mean import mean
from Statistics.StandardDeviation import stddev
from pprint import pprint


def confidence_intervals(data):
    try:
        zvalue = 1.960
        nLenght = len(data)
        nMean = mean(data)
        sd = stddev(data)
        pprint(sd)
        CI = multiplication(zvalue, (division(square_root(nLenght), sd)))
        x = round(float(CI), 1)
        pprint(str(str(nMean) + "+" + str(x)))
        return str(str(nMean) + "+" + str(x))
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")

        # https://www.mathsisfun.com/data/confidence-interval.html
