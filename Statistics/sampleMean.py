from Calculator.Addition import Addition
from Calculator.Division import Division
from Statistics.GetSample import GetSample


def SampleMean(data, sample_size):
    total = 0
    # check that get sample returns the proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than the population
    # https://realpython.com/python-exceptions/
    # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
    sample = GetSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = Addition(total, num)
    return Division(total, num_values)
