from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    try:
        num_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
        return division(num_values, total)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/statistics-definitions/mean-median-mode/
