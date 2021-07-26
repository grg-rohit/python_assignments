import numpy as np
A = [0, 1, 6, 1, 4, 1, 2, 2, 7] 
print("Original array:")
print(A)
print("Number of occurrences of each value in array: ")
print(np.bincount(A))