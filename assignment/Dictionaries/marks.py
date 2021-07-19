Students = ["jack", "jill", "david", "silva", "ronaldo"]
Marks = [55, 56, 57, 66, 76]
report = {
    "students": Students,
    "marks": Marks
}

lowestMarks = min(report["marks"])
index = report["marks"].index(lowestMarks)

#deleting the key-value (students:marks) pairs with lowest marks
del report["students"][index]
del report["marks"][index]

print(report)