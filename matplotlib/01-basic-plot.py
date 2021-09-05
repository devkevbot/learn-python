import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([0, 6])
y_points = np.array([0, 250])

plt.plot(
    x_points,
    y_points,
    marker="o",
    ms=10,
    linestyle="dotted",
    linewidth="3",
    color="orange"
)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("simple-graph")

plt.grid(
    color="green",
    linestyle="--",
    linewidth="0.5",
    axis="y"
)

plt.show()
