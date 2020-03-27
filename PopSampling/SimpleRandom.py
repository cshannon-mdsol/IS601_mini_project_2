import random


def simple_random(series, itemsToReturn):
    return random.choices(series, k=itemsToReturn)
