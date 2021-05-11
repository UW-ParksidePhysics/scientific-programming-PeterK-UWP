"""
This function take in an array of data and another array of many small points of data
and plots a curves for each of the class
"""
__author__ = "Peter & Lena"


import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="", fit_format=""):
  
  scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
  curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
  plt.show()
  
  return scatter_plot, curve_plot
