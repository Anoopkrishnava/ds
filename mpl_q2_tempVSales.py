
import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([12,14,16,18,20,22,24])
y_data = np.array([100,200,250,400,300,450,500])

plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.plot(x_data,y_data,ls="-",color="green",marker="*",mfc="red",mec="red")

plt.show()
