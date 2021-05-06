
from two_column_text_read import two_column_text_read
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from bivariate_statistics import bivariate_statistics

array = two_column_text_read("volumes_energies.dat")

print(fit_curve_array(quadratic_fit(array), 0, 10))
print(bivariate_statistics(array))
