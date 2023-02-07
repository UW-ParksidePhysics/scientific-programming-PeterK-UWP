"""
This function take in an array of data and another array of many small points of data
and plots a curves for each of the class
"""
__author__ = "Peter & Lena"
import numpy as np
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="o", fit_format=""):
    scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
    curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)

    return scatter_plot, curve_plot


if __name__ == '__main__':
    info = np.array([[0, 1, 2], [0, 1, 4]])
    fit = np.empty([2, 50])
    fit[0] = np.linspace(0, 3)
    fit[1] = np.linspace(0, 3)**2
    print(fit)
    plot_data_with_fit(data, fit)
    plt.show()
