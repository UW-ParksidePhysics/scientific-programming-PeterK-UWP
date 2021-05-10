import matplotlib.pyplot as plt

from two_column_text_read import two_column_text_read
array = two_column_text_read("volumes_energies.dat")
#print(array)

from bivariate_statistics import bivariate_statistics
statistics = bivariate_statistics(array)
print(statistics)
min_x = statistics[2]
max_x = statistics[3]
print(min_x)
print(max_x)

from quadratic_fit import quadratic_fit
quadratic_coefficients = quadratic_fit(array)
#print(quadratic_coefficients)

from fit_curve_array import fit_curve_array
data = fit_curve_array(quadratic_coefficients, min_x, max_x)
plt.plotshow()

from plot_data_with_fit import plot_data_with_fit

from lowest_eigenvectors import lowest_eigenvectors






#plt.show(plot_data_with_fit(array, fit_curve_array))
#print(fit_curve_array(quadratic_fit(array), 0, 10,))
#print(bivariate_statistics(array))

#def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):