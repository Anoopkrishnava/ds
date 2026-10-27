import numpy as np
from numpy import linalg

def matrixread(n):
    matrix = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            num = int(input("Enter element " + str(i) + "," + str(j)+" "))
            temp.append(num)
        matrix.append(temp)
    return matrix

n = int(input("Enter the order of the matrix"))

print("Matrix 1")
matrix1 = np.array(matrixread(n))

print("Matrix 2")
matrix2 = np.array(matrixread(n))

print("Matrices are")
print(matrix1)
print(matrix2)

print("Transpose of matrix 1 =", np.transpose(matrix1))  #transpose

print("Trace of matrix 1 =", np.trace(matrix1))   # trace of matrix ie. sum of diagonal elements

print("Rank of matrix 1 =", linalg.matrix_rank(matrix1)) # rank of matrix

print("Determinant of matrix 1=", linalg.det(matrix1))   #determinant

print("Inverse of matrix 1=", linalg.inv(matrix1))  # inverse of matrix

print("Eigen values and Eigen vectors of matrix 1")
print(linalg.eig(matrix1))