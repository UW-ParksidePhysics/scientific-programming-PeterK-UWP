from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

m1 = np.array([2, 3, 4], int)
m2 = 5
g = -9.81
v0 = 2
a_list = []
t = linspace(0, 10)
h_list = []


def acceleration(mass_one):
    for i in mass_one:
        a = ((m2 - i) * g) / (i + m2)
        a_list.append(a)
        # print(a_list)
    return a_list


def height(time, accel):
    for j in accel:
        h = v0 * time + 0.5 * j * time ** 2
        h_list.append(h)
        # print(h_list)
    return h_list


heights = height(t, acceleration(m1))


def plot_accelerations(time, height_values):
    for i in heights:
        plt.plot(t, i)
    plt.show()

# print(heights[0])


if __name__ == '__main__':
    plot_accelerations(t, heights)

