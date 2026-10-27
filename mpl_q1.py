import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([1, 2, 6, 18])
y_data = np.array([3, 10, 12, 20])

plt.plot(
    x_data, y_data,
    ls=":", marker=".", ms=10,
    mfc="green", mec="green", color="red"
)

plt.show()