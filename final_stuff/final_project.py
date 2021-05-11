import matplotlib.pyplot as plt
import numpy as np

from two_column_text_read import two_column_text_read
array = two_column_text_read("volumes_energies.dat")
print('----------')
print('Volumne & Energies')
print(array)
print('----------')


from bivariate_statistics import bivariate_statistics
statistics = bivariate_statistics(array)
min_x = statistics[2]
max_x = statistics[3]
print('----------')
print('mean_of_y, standard_deviation_of_y, x_min, x_max, y_min, y_max')
print(statistics)
#print(min_x), print(max_x)
print('----------')


from quadratic_fit import quadratic_fit
quadratic_coefficients = quadratic_fit(array)
#quadratic_array = [quadratic_coefficients[0], quadratic_coefficients[1]]
print('----------')
print('Quadratic Coefficients')
print(quadratic_coefficients)
#print(quadratic_array)
print('----------')


from fit_curve_array import fit_curve_array #erroring in fit_curve_array
fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
print('----------')
print('fit_curve is an eye sore')
#print(fit_curve)
print('----------')


from lowest_eigenvectors import lowest_eigenvectors
matrix = np.array([
  [1, 0, 0],
  [0, 2, 0],
  [0, 0, 3]
  ])
values_sorted, vectors_sorted = lowest_eigenvectors(matrix, 3)
print('----------')
print('Eigenvalues lowest to highest')
print(values_sorted)
print('Eigenvectors lowest to highest')
print(vectors_sorted)
print('----------')


from plot_data_with_fit import plot_data_with_fit
scatter_plot, curve_plot = plot_data_with_fit(array, fit_curve, data_format="", fit_format="")

for i in plot_data_with_fit:
  plt.plot(array)
  plt.scatter(scatter_plot, curve_plot)
  plt.xlabel('Volumes')
  plt.ylabel('Energies')
  plt.show()
