import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array=", arr)

# Sum of all elements
total_sum = np.sum(arr)
print("Sum of elements=", total_sum)

# Sum of each column (axis=0)
col_sum = np.sum(arr, axis=0)  #calculates the sum of each column.
print("Column wise sum=", col_sum)

# Sum of each row (axis=1)
row_sum = np.sum(arr, axis=1)   #calculates the sum of each row.
print("Row wise sum=", row_sum)