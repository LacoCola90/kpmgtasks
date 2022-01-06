import numpy as np

# using numpy.fill_diagonal() method
array = np.zeros((3, 3), int)
np.fill_diagonal(array, 1)

print(array)