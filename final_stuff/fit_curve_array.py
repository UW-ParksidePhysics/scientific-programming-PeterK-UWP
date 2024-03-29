"""
This functioncreateas a column of data using the inputed quadratic fit( x and y arrays), 
then it creates plotable data and forms it back into an executable file for later use.
"""
__author__ = "Peter & Lena"

import numpy as np


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
    if max_x < min_x:  # max values cannot be less than min values
        raise ArithmeticError
    if number_of_points <= 2:  # need more than 2 points
        raise IndexError

    x_array = np.linspace(min_x, max_x, number_of_points)  # 2 parameters
    y_array = np.polyval(quadratic_coefficients, x_array)  #
    fit_curve = np.array((x_array, y_array))  # np.column_stack((x_array, y_array))

    return fit_curve


if __name__ == '__main__':
    array_one = np.array([0, 1, 2, 3, 4])
    coeff = np.array([1, 0, 0])
    print(fit_curve_array(coeff, 0, 4, number_of_points=5))


