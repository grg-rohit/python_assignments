
#initalizing 3X3 matrices
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[111, 22, 33], [44, 55, 56], [47, 86, 19]]

C = [[111, 22, 33, 44], [44, 55, 556, 1], [47, 86, 19, 2], [1, 2, 22, 3]]

D = [[11, 22, 3, 4], [4, 5, 6, 1], [7, 6, 19, 2], [1, 2, 22, 3]]


def matrixMultiplication(matrix1, matrix2):
    result = [] #variable to store final result of the operation

    for i in range(len(matrix1)): #runs the loop for the number of rows
        row = []
        for j in range(len(matrix2[0])): 
            product = 0
            for k in range(len(matrix1[i])):
                product += matrix1[i][k] * matrix2[k][j]

            row.append(product)

        result.append(row)

    return result

print(matrixMultiplication(A, B))

print(matrixMultiplication(C, D))