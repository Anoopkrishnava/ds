#Write a NumPy program to create a random array with 1000 elements and compute the average,
#variance, standard deviation of the array elements.
import numpy as np

arr = np.array([23, 55, 29, 56, 28, 86, 12])

mean = np.mean(arr)
variance = np.var(arr)
std = np.std(arr)

print("Array=", arr)
print("Mean=", mean, " Variance=", variance,
      " Standard deviation= ", std)