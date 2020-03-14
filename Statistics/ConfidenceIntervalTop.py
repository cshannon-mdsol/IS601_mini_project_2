from Calculator.SquareRoot import square_root
from Statistics.PopulationMean import population_mean
from Statistics.StandardDeviation import stddev


def confidence_interval_top(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = stddev(num)
        avg = population_mean(num)
        return round(avg + (z * sd / square_root(num_values)), 5)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")
