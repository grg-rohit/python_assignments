import numpy as np
A = np.array([0, 1, 3])
B = np.array([2, 4, 5])
print("\nOriginal array1:")
print(A)
print("\nOriginal array1:")
print(B)
print("\nCross-correlation of the said arrays:\n",np.cov(A, B))