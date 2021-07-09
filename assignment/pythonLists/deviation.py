#from statistics import stdev
#calculate standard deviation using stdev() 

#import numpy as np
#calculate standard deviation using np.std()

import math

Numbers = [1, 2, 3, 5, 88, 99, 55, 33, 41, 52]

#creating a function to calculate standard deviation
def stdeviation(y):
  mean = sum(y)/len(y)
  total = 0

  for i in range(len(y)):
    diff = (y[i] - mean) ** 2
    total += diff
  stdv = math.sqrt(total/len(y))
  return stdv

print("Standard deviation of", Numbers, ": %.2f"%stdeviation(Numbers))


#creating a function to calculate mean deviation of Numbers
def meandev(y):
  mean = sum(y)/len(y)
  total = 0

  for i in range(len(y)):
    diff = abs(y[i] - mean)
    total += diff

  meanDev = total/len(y)
  return meanDev

print("Mean deviation of", Numbers, ": %.2f"%meandev(Numbers));