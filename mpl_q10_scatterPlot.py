import numpy as np
import matplotlib.pyplot as plt

math_marks = np.array([88,92,80,89,100,80,60,100,80,34])
science_marks = np.array([35,79,79,48,100,88,32,45,20,30])
marks_range = np.array([10,20,30,40,50,60,70,80,90,100])
plt.xlabel("Marks Range")
plt.title("Math marks vs Scince marks")
plt.scatter(marks_range,math_marks,color="red",label="Maths")
plt.scatter(marks_range,science_marks,color="green",label="Science")
plt.legend()
plt.show()