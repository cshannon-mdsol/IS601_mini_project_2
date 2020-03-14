from Statistics.Proportion import proportion
from Statistics.Variance import variance


def variance_of_population_proportion(num):
    variance_p = proportion(num)
    return variance(variance_p)
