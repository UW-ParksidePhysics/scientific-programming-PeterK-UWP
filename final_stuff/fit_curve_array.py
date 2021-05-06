import numpy as numpy


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
  if max_x < min_x:
    raise ArithmeticError
  if number_of_points <= 2:
    raise IndexError
