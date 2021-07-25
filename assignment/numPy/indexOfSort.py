import numpy as np

X = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
print("Original array:")
print(X)
#argsort() gives the index of sorted data
index = X.argsort()
print("Indices of the sorted elements of the given array:")
print(index)