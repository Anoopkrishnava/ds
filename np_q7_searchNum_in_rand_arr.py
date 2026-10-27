
import numpy as np

arr = np.random.randint(low=-10, high=40, size=10)
print(arr)

num = int(input("Enter a number"))

res = np.where(arr == num)

print(type(res))

if len(res[0]) == 0:
    print("Number is not present in the array")
else:
    print("Number is present in the array")
