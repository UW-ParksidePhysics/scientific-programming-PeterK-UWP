import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

matrix = np.array([[2, -1], [-1, 2]])
print(f'A = {matrix}')

twos = np.ones(2) * 2 # 2 ones in a row times 2
twos_matrix = np.diagflat(twos) # makes a diagonal of twos from "twos"
print(f'Diagonal_Matrix = {twos_matrix}')

negative_ones = np.ones(1) * -1
print(f'neg_one = {negative_ones}')

upper_negative_ones = np.diagflat(negative_ones, 1)  # offset by 1
print(f'up_neg_one = {upper_negative_ones}')

lower_negative_ones = np.diagflat(negative_ones, -1) # offset by -1
print(f'low_neg_one = {lower_negative_ones}')

matrix_again = twos_matrix + upper_negative_ones + lower_negative_ones
print(f'A = {matrix_again}')

eigenvalues, eigenvectors = np.linalg.eig(matrix_again)
print(f'values = {eigenvalues}')
print(f'vectors = {eigenvectors}')
