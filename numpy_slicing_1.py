#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Create an array of 10 zeros
zeros = np.zeros(10)

# Create an array of 10 ones
ones = np.ones(10)

# Create an array of 10 fives
fives = np.full(10, 5)

# Concatenate the arrays
result = np.concatenate((zeros, ones, fives))

print(result)

"""Output:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5.
 5. 5. 5. 5. 5. 5.
 """
