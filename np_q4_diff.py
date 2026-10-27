import numpy as np

arr = np.array([12, 34, 6, 28, 46, 90, 3])

diffs = np.diff(arr)

print(f"array : {arr}")
print(f"Difference : {diffs}")