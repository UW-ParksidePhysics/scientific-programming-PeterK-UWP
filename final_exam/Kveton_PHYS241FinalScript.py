import numpy as np


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

from quadratic_fit import quadratic_fit
quadratic_coefficients = quadratic_fit(array)
#print(quadratic_coefficients)

from equations_of_state import fit_eos
fit_eos = fit_eos(array[0], array[1], quadratic_coefficients)
#print(fit_eos)