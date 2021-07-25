import numpy as np

A = [[0, 1, 2, 3, 4, 5], [ 6, 7, 8, 9, 10, 11]]

print("\nOriginal array:")
print(A)
r1 = np.ptp(A, 1)
r2 = np.amax(A, 1) - np.amin(A, 1)
assert np.allclose(r1, r2)
print("\nDifference between the maximum and the minimum values of the said array:")
print(r1)
