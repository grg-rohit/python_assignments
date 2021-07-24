import re
pi = open('pi_million_digits.txt', 'r')

data = pi.read()
lists = str(data).split('.')

#removing all the white spaces using regex in python
digits = re.sub(r"\s+", "", lists[1])


total = 0

for digit in digits:
    total += int(digit)



print("Sum of all the digits after decimal in Pi: ",total)

