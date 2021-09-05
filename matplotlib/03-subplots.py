import matplotlib.pyplot as plt
import numpy as np

# Side-by-side plots

x1_values = np.array([0, 1, 2, 3])
y1_values = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x1_values, y1_values)
plt.title("First")

x2_values = np.array([10, 20, 30, 40])
y2_values = np.array([100, 200, 300, 400])
plt.subplot(1, 2, 2)
plt.plot(x2_values, y2_values)
plt.title("Second")

plt.suptitle("Two graphs")
plt.show()
