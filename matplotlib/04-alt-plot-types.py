import matplotlib.pyplot as plt
import numpy as np

x1_values = np.array([0, 1, 2, 3])
y1_values = np.array([3, 8, 1, 10])
plt.subplot(2, 2, 1)
plt.bar(x1_values, y1_values)
plt.title("Bar")

x2_values = np.array([10, 20, 30, 40])
y2_values = np.array([100, 200, 300, 400])
plt.subplot(2, 2, 2)
plt.scatter(x2_values, y2_values)
plt.title("Scatter")

x3_values = np.random.normal(170, 10, 250)
plt.subplot(2, 2, 3)
plt.hist(x3_values)
plt.title("Histogram")

x4_values = np.array([5, 25, 50, 20])
plt.subplot(2, 2, 4)
plt.pie(x4_values, labels=["Team One", "Team Two", "Team Three", "Team Four"])
plt.title("Pie")

plt.suptitle("Different graph types")
plt.show()
