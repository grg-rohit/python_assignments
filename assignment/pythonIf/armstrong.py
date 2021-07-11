num = int(input("Enter a number: "))

sum = 0

temp = num 

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10 #floor division to return the number before decimal

if sum == num:
    print("{} is an armstrong number.".format(num))
else:
    print("{} is not an  armstrong number.".format(num))