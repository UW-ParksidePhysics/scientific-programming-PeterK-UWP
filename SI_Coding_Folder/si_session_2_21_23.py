"""
Today we will cover matrix equations (how to use them in python)
 - writing a matrix
 - using a definition statement
 - performing calculations
 - looping over matrix terms
"""
import numpy as np

matrix_A = np.array([[1, 0], [0, 1]])  # identity
matrix_B = np.array([[2, 4], [6, 8]])  # example matrix


def matrix_manipulations(matrix_one, matrix_two):
    summ = np.add(matrix_one, matrix_two)
    difference = np.subtract(matrix_one, matrix_two)
    product = np.multiply(matrix_one, matrix_two)
    quotient = np.divide(matrix_one, matrix_two)
    return summ, difference, product, quotient


summ = matrix_manipulations(matrix_A, matrix_B)[0]  # 3 4 6 9
difference = matrix_manipulations(matrix_A, matrix_B)[1]
product = matrix_manipulations(matrix_A, matrix_B)[2]
quotient = matrix_manipulations(matrix_A, matrix_B)[3]

ft = []
st = []
tt = []
fot = []

for i in matrix_manipulations(matrix_A, matrix_B):
    first_terms = i[0][0]
    second_terms = i[0][1]
    third_terms = i[1][0]
    fourth_terms = i[1][1]
    ft.append(first_terms)
    st.append(second_terms)
    tt.append(third_terms)
    fot.append(fourth_terms)
print(f'first_terms {ft}')
print(f'second_terms {st}')
print(f'third_terms {tt}')
print(f'fourth_terms {fot}')

"""
print(f'The sum of matrix A to B is')
print(matrix_manipulations(matrix_A, matrix_B)[0])
print(f'The difference of matrix A to B is')
print(matrix_manipulations(matrix_A, matrix_B)[1])
print(f'The product of matrix A to B is')
print(matrix_manipulations(matrix_A, matrix_B)[2])
print(f'The quotient of matrix A to B is')
print(matrix_manipulations(matrix_A, matrix_B)[3])
"""

"""
Meet/plan for the week 2/20 - 2/24

functions and branching
solving matrix eq (finding inverse)

shell: manipulating files and directories

suggested topics:
circuit, projectile motion, spring system, orbits, collisions (contact check)(elastic), kinetic energy
"""