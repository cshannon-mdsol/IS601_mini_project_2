from Calculator.SquareRoot import square_root
from Statistics.Mean import mean
from Statistics.StandardDeviation import stddev


def confidence_interval_known(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = stddev(num)
        avg = mean(num)
        return round(avg + (z * sd / square_root(num_values)), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")

        # http://www.stat.yale.edu/Courses/1997-98/101/confint.htm
        # https://math.stackexchange.com/questions/167302/when-standard-deviation-is-unknown/167307
