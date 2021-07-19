milk_carton = {}

#adding keys and values in milk Carton dictionary
milk_carton['Expiration_date'] = (20, 12, 2022)
milk_carton['Vol'] = 2
milk_carton['Cost'] = 50
milk_carton['Brand_name'] = "D.D.C"

print("\n", milk_carton, "\n")

#printing values of all of the elements of the milk_carton using the values in the dictionary
for value in milk_carton.values():
    print(value)


cost = milk_carton['Cost'] * 6
print("\nCost of 6 cartons of milk is", cost, "\n")
