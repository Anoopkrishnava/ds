
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y_1 = np.array([30,32,31,32,33])
y_2 = np.array([27,26,29,28,29])

plt.xlabel("Day")

plt.plot(x, y_1, color="red", marker=".", mfc="red",
         label="Highest Temperature")

plt.plot(x, y_2, color="blue", marker=".", mfc="blue",
         label="Lowest Temperature")

plt.title("Temperature Difference")
plt.legend()  # adding legend to display labels
plt.show()
