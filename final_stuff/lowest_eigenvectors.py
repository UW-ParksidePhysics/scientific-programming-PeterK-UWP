"""
This function calculates the eigenvalues of a given square matrix and returned the values. 
It then organizes the eigenvalues and eigenvectors from smallest to largest. It then
returns this sorted list for future computation
"""
__author__ = "Peter & Lena"

import numpy as np


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    m, n = square_matrix.shape
    if m != n:
        raise IndexError("Matrix is not square!")

    values, vectors = np.linalg.eig(square_matrix)
    values_sorted = np.sort(values)
    vectors_sorted = vectors[:, values.argsort()].transpose()

    return values_sorted[:number_of_eigenvectors], vectors_sorted[:number_of_eigenvectors]


if __name__ == '__main__':
    array = np.array([[2, -1], [-1, 2]]) #[[3, 1, 1], [0, 2, 1], [0, 0, 1]])  # given array [2, -1], [-1, 2]
    eigenvalues, eigenvectors = lowest_eigenvectors(array, number_of_eigenvectors=2)  # number of eigenvalues
    # print(lowest_eigenvectors(array)) change eigenvectors from 3 to 2
    print(eigenvalues, eigenvectors)
    print(eigenvectors[0])  # should print lowest of the three
