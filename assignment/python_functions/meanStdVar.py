
def mean(data):
  
  n = len(data)

  mean = sum(data) / n
  
  return mean


#creating a function to calculate standard deviation
def stdeviation(y):
  mean = sum(y)/len(y)
  total = 0

  for i in range(len(y)):
    diff = (y[i] - mean) ** 2
    total += diff
  stdv = math.sqrt(total/len(y))
  return stdv




#creating a function to calculate mean deviation of Numbers
def meandev(y):
  mean = sum(y)/len(y)
  total = 0

  for i in range(len(y)):
    diff = abs(y[i] - mean)
    total += diff

  meanDev = total/len(y)
  return meanDev

print("Standard deviation of", Numbers, ": %.2f"%stdeviation(Numbers))

print("Mean deviation of", Numbers, ": %.2f"%meandev(Numbers));