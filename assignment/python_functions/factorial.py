userInput = int(input("Enter a number: "))

def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num -= 1
    return result

print("The factorial of {0} is {1}.".format(userInput, factorial(userInput)))