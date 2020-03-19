from random import seed
from random import random

# 1. generate random number without seed between a range of two numbers
def generate_number(x, y):
    #return number
    pass


# 2. generate random number with a seed between a range of two numbers
def generate_number(x, y, seedValue):
    #set the seed value. https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
    seed(seedValue)

    #return a random number between x and y
    return random.randrange(x, y)


# 3. generate a list of N random numbers with a seed between a range of two numbers
def generate_random_numbers(x, y, seedValue, listSize):
    seed(seedValue)
    theArray = []

    # loop listSize times to generate a random number and add it to the list
    for i in range(listSize):
        theArray.append(random.randrange(x, y))

    #return the newly-filled array of random numbers
    return theArray


# 4. select a random item from a list
def random_from_list(listArray):
    #return item
    pass


# 5. set a seed and randomly select the same value from a list
# (Not actually sure what this one means, need to think about it)

# 6. Select N number of items from a list without a seed
def pickFromList(listArray, howManyItems):
    #return array
    pass


# 7. Select n number of items from a list with a seed
def pickFromList(listArray, howManyItems, seedValue):
    #return array
    pass


####### Commented out this section for future reference.

# # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
# random.randint(1, 1000)
#
# random.uniform(1, 1000)
#
# # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
# random.seed(555)
# random.randint(1, 1000)
#
# random.seed(555)
# random.uniform(1, 1000)
#
# # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
# random.seed(555)
# [random.randint(1, 1000) for _ in range(5)]
#
# random.seed(555)
# [random.uniform(1, 1000) for _ in range(5)]
#
# # Select a random item from a list
# stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
# random.choice(stats)
#
# # Set a seed and randomly.select the same value from a list
# stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
# random.seed(555)
# random.choice(stats)
#
# # Select N number of items from a list without a seed
# stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
# random.choices(stats, k=3)
#
# # Select N number of items from a list with a seed
# stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
# random.seed(555)
# random.choices(stats, k=3)

# https://docs.python.org/3.1/library/random.html
