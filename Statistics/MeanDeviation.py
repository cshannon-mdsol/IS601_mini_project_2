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
from pprint import pprint


def mean_deviation(data):
    try:
        # 1. find the mean of the data
        general_mean = mean(data)
        print("________*******________ ", general_mean)

        # 2. find the distance of each value from that mean
        # iterate the data list, subtract it from general mean, store it in a list


        #for num in data:

        num_values = len(data)
        distance_array = 0
        total = 0

        for num in data:
            total = addition(total, num)


        return division(num_values, total)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")


