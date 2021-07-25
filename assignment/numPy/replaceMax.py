import numpy as np
x = np.random.random(15)
print("Original array:")
print(x)
x[x.argmax()] = -1 #x.argmax gives the index of maximum value in the array
print("Maximum value replaced by -1:")
print(x)