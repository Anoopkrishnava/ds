#generating random integers and selecting values greater than 4 using NumPy

import numpy as np

arr = np.random.randint(low=-40, high=40, size=10)
print("Array=", arr)

res = np.where(arr > 4)  #finds the indices of elements satisfying the condition arr > 4.
print("Elements greater than 4")

for ele in res:
    print(arr[res])
