import matplotlib.pyplot as plt

x_data = ["Java", "Python", "PHP", "Javascript", "C#", "C++"]
y_data = [22.2, 17.6, 8.8, 8, 77, 6.7]

plt.bar(x_data, y_data, color="blue")
plt.title("Programming Languages Popularity")
plt.xlabel("Programming Language")
plt.ylabel("Popularity")
plt.show()