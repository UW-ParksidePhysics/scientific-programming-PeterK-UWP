import matplotlib.pyplot as plt
import numpy as np

from two_column_text_read import two_column_text_read
array = two_column_text_read("volumes_energies.dat")
#print(array)

from bivariate_statistics import bivariate_statistics
statistics = bivariate_statistics(array)
#print(statistics)
min_x = statistics[2]
max_x = statistics[3]
#print(min_x), print(max_x)

from quadratic_fit import quadratic_fit
quadratic_coefficients = quadratic_fit(array)
#print(quadratic_coefficients)
quadratic_array = [quadratic_coefficients[0], quadratic_coefficients[1]]
#print(quadratic_array)

from fit_curve_array import fit_curve_array #erroring in fit_curve_array
fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
#print(fit_curve)

from lowest_eigenvectors import lowest_eigenvectors
matrix = np.array([
  [5, 0, 0],
  [0, 2, 0],
  [0, 0, 3]
  ])
values_sorted, vectors_sorted = lowest_eigenvectors(matrix, 3)
print(values_sorted, vectors_sorted)

from plot_data_with_fit import plot_data_with_fit
scatter_plot, curve_plot = plot_data_with_fit(array, fit_curve, data_format="", fit_format="")
for i in plot_data_with_fit:
  plt.plot(array)
  plt.scatter(scatter_plot, curve_plot)
  plt.xlabel('Volumes')
  plt.ylabel('Energies')
  plt.show()
