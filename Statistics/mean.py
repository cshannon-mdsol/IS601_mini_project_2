from Calculator.Addition import Addition
from Calculator.Division import Division


def Mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = Addition(total, num)
    return Division(num_values, total)
