report = {
    "Students": ["jack", "jill", "david", "silva", "ronaldo"],
    "Marks": [55, 56, 57, 66, 76]
}

lowestMarks = min(report["Marks"])
index = report["Marks"].index(lowestMarks)

#delete the key-value (students:marks) pairs with lowest marks
del report["Students"][index]
del report["Marks"][index]

print(report)