import matplotlib.pyplot as plt
import numpy as np

x_axis = np.array([1, 2, 3, 4])
series_one = np.array([1, 2, 3, 4])
series_two = np.array([1, 4, 9, 16])

plt.plot(x_axis, series_one)
plt.plot(x_axis, series_two)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear vs. Quadratic")
plt.legend(["Linear", "Quadratic"])

plt.show()
