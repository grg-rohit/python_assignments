import numpy as np
from numpy import linalg as LA

B = np.array([[1, 2, 3], [55, 66, 7], [6, 7, 12]])

w, v =LA.eig(B)

print("eigenvalues:\n {}".format(w))
print("eigenvector:\n {}".format(v))