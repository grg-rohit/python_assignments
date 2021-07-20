rows = 6

for i in range(0,rows+1):  

  for j in range(i):  
    print("F", end = "")  
  for j in range(i-1, 0, -1):
    print('F', end = "")
  print()

"""
final = 0

initial = 1

for i in range(1,10):

  for j in range(0,initial):

    print("F",end='')

  temporary = final

  previous = initial

  initial = initial + temporary

  print('')

  """

prev = 0

curr = 1

for i in range(1,10):

  for j in range(0,curr):

    print("F",end='')

  temp = prev

  prev = curr

  curr = curr + temp

  print('')



