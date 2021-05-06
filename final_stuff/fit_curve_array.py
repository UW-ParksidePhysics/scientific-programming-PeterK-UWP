import numpy as numpy


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
  if max_x < min_x:   #max values cannot be less than min values
    raise ArithmeticError
  if number_of_points <= 2:   #need more than 2 points
    raise IndexError
