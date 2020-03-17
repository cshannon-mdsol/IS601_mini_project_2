# def mean_deviation(data):
#  try:
#  except ZeroDivisionError:
#          print("Error - Cannot divide by 0")
#  except ValueError:
#          print("Error - Invalid data inputs")

#         https://www.mathsisfun.com/data/mean-deviation.html
from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Mean import mean


def mean_deviation(data):
    try:
        # 1. find the mean of the data
        general_mean = mean(data)


        # 2. find the distance of each value from that mean
        # iterate the data list, subtract it from general mean, store it in a list


        #for num in data:

        num_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
        return division(num_values, total)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")


#overloaded function if someone wants mean absolute mean deviation
def mean_deviation(data, wantsAbsolute):
    return (data)