def powers(x, y):
    return x ** y

base = int(input("Enter the base: "))
power = int(input("Enter power: ")) 

print(base, " raised to the power", power, "is ", powers(base, power))
