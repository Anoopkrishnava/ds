
import numpy as np

arr = np.array([4, 5, 4, 6, 11, 2235, 56])

print("Writing the array to the file")
np.savetxt(fname="test.txt", X=arr)  #writes the values of arr to a file

print("File content is")
loaded_arr = np.loadtxt(fname="test.txt")  #reads the numerical data from the file and returns it
print(loaded_arr)
