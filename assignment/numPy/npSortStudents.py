import numpy as np
student_id = np.array([123, 126, 140, 152])
height = np.array([145, 155, 165, 153])
#sirt by student id then by student height
indices = np.lexsort((student_id, height))

print("Sorted indices:")
print(indices)

print("Sorted data: ")

#Printing the integer indices that describe the sort order by multiple columns and the sorted data.

for i in indices:
    print(student_id[i], height[i])