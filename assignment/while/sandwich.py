sandwich_orders = ["American sub", "Bacon", "Bagel toast", "Baked bean", "Bauru"]

finished_sandwiches = []
i = 0
while(i < len(sandwich_orders)):
    print("I made your ", sandwich_orders[i], ".")
    finished_sandwiches.append(sandwich_orders[i])
    i += 1
    
j = 0
while(j < len(finished_sandwiches)):
    print(sandwich_orders[j], " has been made.")
    j += 1