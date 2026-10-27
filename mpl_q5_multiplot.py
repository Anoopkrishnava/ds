import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y_1 = np.array([30, 32, 31, 32, 33])
y_2 = np.array([27, 26, 29, 28, 29])

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y_1, color="red", marker=".", mfc="red",
         label="Highest Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Highs")

plt.subplot(1, 2, 2)
plt.plot(x, y_2, color="blue", marker=".", mfc="blue",
         label="Lowest Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Lows")

plt.suptitle("Temperature Difference Over 5 Days")
plt.show()