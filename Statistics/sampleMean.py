from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.GetSample import get_sample


def samplemean(data, sample_size):
    try:
        total = 0
        sample = get_sample(data, sample_size)
        num_values = len(sample)
        for num in sample:
            total = addition(total, num)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")
