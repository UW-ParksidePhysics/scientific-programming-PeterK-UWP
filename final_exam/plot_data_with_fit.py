"""
takes in data from two_column and fit cuve from eq.of state and plots the stuff
"""
import matplotlib.pyplot as plt
from matplotlib.axis import Axis as ax

def plot_data_with_fit(data, fit_curve, data_format="", fit_format=""):
  
  scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
  curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
  plt.title(('Fm-3m Equation of State for Al in DFT GGA-PBE'))
  plt.xlabel(r'$V$ $A^3/atom$')
  plt.ylabel(r'$E$ $eV/atom$')
  plt.xlim([90, 137])
 
  plt.show()

  return scatter_plot, curve_plot


  

