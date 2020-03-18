import random

# Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
random.randint(1, 1000)

random.uniform(1, 1000)

# Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
random.seed(555)
random.randint(1, 1000)

random.seed(555)
random.uniform(1, 1000)

# Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
random.seed(555)
[random.randint(1, 1000) for _ in range(5)]

random.seed(555)
[random.uniform(1, 1000) for _ in range(5)]

# Select a random item from a list
stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
random.choice(stats)

# Set a seed and randomly.select the same value from a list
stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
random.seed(555)
random.choice(stats)

# Select N number of items from a list without a seed
stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
random.choices(stats, k=3)

# Select N number of items from a list with a seed
stats = ['mean', 'median', 'mode', 'quartiles', 'skewness', 'variance', 'zscore']
random.seed(555)
random.choices(stats, k=3)

# https://docs.python.org/3.1/library/random.html
