milk_carton = {}

#adding keys and values in milk Carton dictionary
milk_carton['Expiration_date'] = (20, 12, 2022)
milk_carton['Vol'] = 2
milk_carton['Cost'] = 45
milk_carton['Brand_name'] = "D.D.C"

print(milk_carton)

#printing values of all of the elements of the milk_carton using the values in the dictionary
for value in milk_carton.values():
    print(value)
