import math
import random

#function to calculate permutation
def permutation(n, r):
	permutationAns = math.factorial(n)/math.factorial((n - r))
	#math.perm() for permutation in python 3.8
	return permutationAns

#function to calculate combination
def combination(n, r):
	combinationAns = math.factorial(n)/(math.factorial((n - r)) * math.factorial(r))
	#math.comb() for combination in python 3.8
	return combinationAns

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

#function to enter two numbers (say a and b) and generating 2 random number between them to find their combination
def randomCombination():
	a = int(input("Enter first number "))
	b = int(input("Enter second number "))
	rand1 = random.randint(a, b)
	rand2 = random.randint(a, b)
	print(rand1)
	print(rand2)
	if rand1 > rand2:
		combinationAns = math.factorial(rand1)/(math.factorial((rand1 - rand2)) * math.factorial(rand2))
		print("combination of the two random numbers given by the user is : ", combinationAns, "\n")
	else:
		combinationAns = math.factorial(rand2)/(math.factorial((rand2 - rand1)) * math.factorial(rand1))
		print("combination of the two random numbers given by the user is : ", combinationAns, "\n") 

#permutation of (5,3)
print("Permutation of (5, 3) is %.2f \n"% permutation(5, 3))

#combination of (15, 3)
print("Combination of (15, 3) is %.2f \n"% combination(15, 3))

#code that takes degrees as input from user and conver it into radian
degrees = int(input("Enter degrees: "))
radian = math.radians(degrees)
print("Radian is : %d \n"% radian)

#code to calculate square root given by the user
print("For square root")
num = int(input("Enter a number: "))
sqrt = math.sqrt(num)
print(sqrt, "\n")

#lcm of (25, 55)
print("lcm is ", lcm(25, 55), "\n")

#combination of two random numbers given by user
randomCombination()

#code to divide 1000 by 3 and print the answer with only 5 numbers after decimal
num1 = 1000
divAns = num1 / 3
print("1000 divided by 3 is %.3f \n" % divAns)

#code to convert 108 to binary
decNum = 108
binAns = bin(decNum)
print("Binary of 108 is: ", binAns, "\n")

#code to convert 1008 to hexadecimal
decNum1 = 1008
hexAns = hex(decNum1)
print("Hexadecimal value of 1008 is ", hexAns, "\n")

