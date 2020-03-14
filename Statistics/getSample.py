from random import random


def get_sample(data, sample_size):
    random_values = random.sample(data, k=sample_size)
    return random_values
