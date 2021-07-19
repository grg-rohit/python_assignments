#function to calculate lcm
def lcm(num1, num2):
	if num1 > num2:
		greater = num1
	else:
		greater = num2

	while(True):
		if ((greater % num1 == 0) and (greater % num2 == 0)):
			lcmAnswer = greater
			break
		greater += 1
	return lcmAnswer

# Python program to find H.C.F of two numbers

# define a function
def gcd(num1, num2):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
x = 54
y = 24 
print("lcm of", x, "&", y, "is", lcm(x,y))
print("gcd of", x, "&", y, "is", gcd(x,y))


