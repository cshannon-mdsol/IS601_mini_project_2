from random import random


def getsample(data, sample_size):
    random_values = random.sample(data, k=sample_size)
    return random_values
