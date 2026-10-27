
import numpy as np

arr = np.array([
    complex(7, 5),
    complex(4, 3),
    complex(12, 2),
    complex(1, 8),
    complex(1, 9)
])

sorted = np.sort(arr)  #np.sort(arr, descending=True) if descending order

print("Array before sorting=", arr)
print("After sorting=", sorted)
