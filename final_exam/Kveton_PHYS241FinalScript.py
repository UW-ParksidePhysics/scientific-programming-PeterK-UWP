import numpy as np
import matplotlib.pyplot as plt

def parse_file_name(file_name):
  symbol = file_name[0]+ file_name[1]
  structure = file_name[3] + file_name[4] + file_name[5] + file_name[6] + file_name[7]
  acronym = file_name[10] + file_name[11] + file_name[12] + file_name[13] + file_name[14] + file_name[15]
  #parse_file_name = np.linspace(file_name)
  parse_file_name = symbol, structure, acronym
  return parse_file_name

print(parse_file_name('Al.Fm-3m.GGA-PBE.dat'))

from two_column_text_read import two_column_text_read
array = two_column_text_read("Al.Fm-3m.GGA-PBE.dat")
#print(array)

from bivariate_statistics import bivariate_statistics
statistics = bivariate_statistics(array)
#mean_of_y, standard_deviation_of_y, x_min, x_max, y_min, y_max
#print(statistics)
min_x = statistics[2]
max_x = statistics[3]

from quadratic_fit import quadratic_fit
quadratic_coefficients = quadratic_fit(array)
#print(quadratic_coefficients)

from equations_of_state import fit_eos
volumes = array[0]
energy = array[1]
fit_eos = fit_eos(array[0], array[1], quadratic_coefficients)
#print(fit_eos)

#from convert_units import convert_values
#converted_array = convert_values(array)
#converted_fit = convert_values(fit_eos)
#print(converted_array)
#print(converted_fit)


from generate_matrix import generate_matrix # Harmonic 120,100
matrix = generate_matrix(min_x, max_x, 120, 'Harmonic', 100)
#print(matrix)

from lowest_eignevectors import lowest_eigenvectors #0, 1, 2
matrix = np.array([
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 2]
  ])
values_sorted, vectors_sorted = lowest_eigenvectors(matrix, 3)
#print(values_sorted)
#print(vectors_sorted)

from fit_curve_array import fit_curve_array
fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
#print(fit_curve)
print('your gay')


from plot_data_with_fit import plot_data_with_fit
scatter_plot, curve_plot = plot_data_with_fit(array, fit_curve, data_format="b", fit_format="k")

print('your gay')


