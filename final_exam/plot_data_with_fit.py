"""
takes in data from two_column and fit cuve from eq.of state and plots the stuff
"""
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="", fit_format=""):
  
  scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
  curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
  #plt.title((r'Fm-3m Equation of State for Al in DFT GGA-PBE'), y=1.05)
  plt.xlabel(r'$V$ (Å$^3$/atom)')
  plt.ylabel(r'$E$ (eV/atom)')

  plt.xlim([90, 137])


  #plt.show()
  
  #plt.savefig("Initial_plot.png")

  return scatter_plot, curve_plot





  

