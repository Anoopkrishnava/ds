import matplotlib.pyplot as plt

x_data = ["Java", "Python", "PHP", "Javascript", "C#", "C++"]
y_data = [30, 40, 10, 10, 5, 5]

plt.pie(y_data, labels=x_data)
plt.show()