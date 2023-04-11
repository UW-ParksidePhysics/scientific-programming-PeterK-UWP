import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
"""
2 -1 0 0 0
-1 2 -1 0 0
0 -1 2 -1 0
0 0 -1 2 -1
0 0 0 -1 2
"""

twos = np.ones(5) * 2
two_diagonal = np.diagflat(twos)
print(two_diagonal)

four_negative_ones = np.ones(4) * -1

upper_negative_ones = np.diagflat(four_negative_ones, 1)  # offset by 1
print(f'up_neg_one = {upper_negative_ones}')

lower_negative_ones = np.diagflat(four_negative_ones, -1) # offset by -1
print(f'low_neg_one = {lower_negative_ones}')

matrix_again = two_diagonal + upper_negative_ones + lower_negative_ones
print(f'A = {matrix_again}')

five_by_five_matrix = (two_diagonal + upper_negative_ones + lower_negative_ones)*1/(2*(1/6)**2)
print(five_by_five_matrix)

eigenvalues5, eigenvectors5 = np.linalg.eig(five_by_five_matrix)
print(f'values = {eigenvalues5}')
print(f'vectors = {eigenvectors5}')

# plot
x_values = np.linspace(1/6, 5/6, 5)
fifth_vector = eigenvectors5[4]

plt.plot(x_values, fifth_vector)
plt.show()
function = np.sqrt(2)*np.sin(np.pi * x_values)
plt.plot(x_values, function)
plt.show()

###

tens = np.ones(10) * 2
two_diagonal = np.diagflat(tens)
print(two_diagonal)

nein_negative_ones = np.ones(9) * -1

upper_negative_ones = np.diagflat(nein_negative_ones, 1)  # offset by 1
print(f'up_neg_one = {upper_negative_ones}')

lower_negative_ones = np.diagflat(nein_negative_ones, -1) # offset by -1
print(f'low_neg_one = {lower_negative_ones}')

matrix_again = two_diagonal + upper_negative_ones + lower_negative_ones
print(f'A = {matrix_again}')

ten_by_ten_matrix = (two_diagonal + upper_negative_ones + lower_negative_ones)*1/(2*(1/6)**2)
print(ten_by_ten_matrix)

eigenvalues10, eigenvectors10 = np.linalg.eig(ten_by_ten_matrix)
print(f'values = {eigenvalues10}')
print(f'vectors = {eigenvectors10}')

# plot
x_values = np.linspace(1/6, 5/6, 10)
tenth_vector = eigenvectors10[9]

plt.plot(x_values, tenth_vector)
plt.show()
function = np.sqrt(2)*np.sin(np.pi * x_values)
plt.plot(x_values, function)
plt.show()
