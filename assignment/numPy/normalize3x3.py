import numpy as np

x = np.random.random((3,3))
print("3x3 random matrix:\n", x)

xmax, xmin = x.max(), x.min()
x = (x - xmin)/(xmax - xmin) 

print("After normaliztion:\n", x)