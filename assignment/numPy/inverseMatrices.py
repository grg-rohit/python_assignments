import numpy as np

A = np.array([[1, 2, 3], [55, 66, 7]])

B = np.array([[1, 2, 3], [55, 66, 7], [6, 7, 12]])

C =  np.array([[1, 2, 3, 8], [5, 6, 7, 5], [6, 7, 12, 12], [11, 12, 13, 20]])


# Calculating the inverse of the matrix
try:
    print(np.linalg.inv(A))

except np.linalg.LinAlgError: 
    print("not a square matrix")


print(np.linalg.inv(B))

print(np.linalg.inv(C))
