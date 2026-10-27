import numpy as np
import matplotlib.pyplot as plt

x_data = np.arange(1, 6) * 3
y1 = np.array([22, 30, 35, 35, 26])
y2 = np.array([25, 22, 30, 35, 29])

bar_width = 0.4

plt.bar(x_data - bar_width, y1, label="Men", color="Blue")
plt.bar(x_data + bar_width, y2, label="Women", color="Pink")

plt.legend()
plt.title("Scores by person")
plt.show()