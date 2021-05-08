import matplotlib.pyplot as plt

from two_column_text_read import two_column_text_read
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from bivariate_statistics import bivariate_statistics
from plot_data_with_fit import plot_data_with_fit

array = two_column_text_read("volumes_energies.dat")
#plt.show(plot_data_with_fit(array, fit_curve_array))
print(fit_curve_array(quadratic_fit(array), 0, 10,))
print(bivariate_statistics(array))

#def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):