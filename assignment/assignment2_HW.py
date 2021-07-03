import math

#to convert tuples to list using list() built in method
#initializing river as tuple
river = ("nile", "koshi", "amazon")
#converting river to list using list() method
list(river)
#confirming the river is a list
print(type(river))

#creating our own list function
def list1(tuples):
	newList = []
	for eachTuple in tuples:
		newList.append(eachTuple)
	return newList

#inititalizing tuple
countries = ('a', 'b', 'c')
#initializing a variable to store list after conversion
countries_list = list1(countries)
#confirming the conversion of tuple to list
print(type(countries_list))


A = (20, 30)
C = list(A)
B = (30, 40)
D = list(B)


slope = (D[0] - C[0])/(D[1] - C[1])

direction = math.atan(slope)
print("Direction of (20, 30) and (30, 40) is", direction, "\n")

magnitude = math.sqrt((D[1] - C[1])**2 + (D[0] - C[0])**2)
print("Magnitude of (20, 30) and (30, 40) is",magnitude, "\n")


#program to demonstrate data types that can be elements of a tuple

newTuple = ("Gorkha")
#for newTuple to be tuple it must have value >= 2 in it else it will have some other datatype that is stored in it
print(newTuple)
print(type(newTuple), "\n")

#string in tuple
stringInTuple = ("Gorkha", "karnali", "Pokhara")
print(stringInTuple)
print(type(stringInTuple), "\n")

#integer in tuple
integerInTuple = (1, 2, 3, 4)
print(integerInTuple)
print(type(integerInTuple), "\n")

#floating numbers in tuple
floatInTuple = (2.222, 3.4, 5.666)
print(floatInTuple)
print(type(floatInTuple), "\n")

#characters in tuple
charInTuple = ('a', '!', 'd', '+')
print(charInTuple)
print(type(charInTuple), "\n")

#boolean in tuple
boolInTuple = (True, False, False, True)
print(boolInTuple)
print(type(boolInTuple), "\n")

#mixed data types in a tuple
tupleCase = ('a', 12, True, "Himalayas", 445.332, '@')
print(tupleCase)
print(type(tupleCase))




