from Calculator.Square import square
from Calculator.Division import division
from Statistics.PopulationCorrelation import population_mean


def variance(num):
    try:
        pop_mean = population_mean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + square(i-pop_mean)
        return division(x, num_values)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")
