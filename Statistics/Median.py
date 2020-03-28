from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
import math


def median(num):
    try:
        num_values = len(num)
        list_num = [num[i] for i in range(num_values)]
        list_num.sort()

        if num_values % 2 == 0:
            median1 = list_num[int(num_values / 2) - 1]
            median2 = list_num[int(subtraction((num_values // 2), 1))]
            median_result = division(2, addition(median1, median2))
        else:
            median_result = list_num[math.ceil(division(2, num_values)) - 1]
        return float(median_result)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/statistics-definitions/mean-median-mode/
