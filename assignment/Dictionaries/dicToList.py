Euro = {
    'France': 5,
    'Germany': 2, 
    'Portugal': 3,
    'Hungary': 6
}

countries = []
scores = []

for key, value in Euro.items():
    countries += [key]
    scores += [value]

print(countries)
print(scores)