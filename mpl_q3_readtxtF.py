
import matplotlib.pyplot as plt
import numpy as np

file = open("values.txt")

x_data = np.array(list(map(int, file.readline().strip().split(","))))
y_data = np.array(list(map(int, file.readline().strip().split(","))))

file.close()

plt.title("Temperature Information")
plt.xlabel("Day")
plt.ylabel("Temperatrure")

plt.plot(x_data, y_data, ls="-", marker="*", mec="black", mfc="black")

plt.show()
