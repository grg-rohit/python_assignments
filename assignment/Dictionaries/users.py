users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}

usernames = []
names = []
ages = []
poisons = []

for keys in users.keys():
    usernames += [keys]
    names += [users[keys]['name']]
    ages += [users[keys]['age']]
    poisons += [users[keys]['poison']]
        


print("usernames: ", usernames)
print("names: ", names)
print("ages: ",ages)
print("poisons: ",poisons)

#taking the above list and arranging it in order

print("\nAfter arranging in order: \n")

usernames.sort()
names.sort()
ages.sort()
poisons.sort()
print("usernames ",usernames)
print("names", names)
print("ages: ", ages)
print("poisons: ", poisons)