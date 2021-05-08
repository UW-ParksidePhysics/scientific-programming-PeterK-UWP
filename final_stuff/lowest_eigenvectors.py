from numpy import linalg as LA
import numpy as np

def lowest_eigenvectors(square_matrix, number_of_eigenvectors):
  w, v = LA.eig(square_matrix)
  sorted_eig_array = np.argsort(w)[0 : number_of_eigenvectors]
  lowest_eigenvectors = []
  lowest_eigenvalues = []
  for i in sorted_eig_array:
    lowest_eigenvectors.append(v[i])
    lowest_eigenvalues.append(w[:,  i])
  lowest_eigenvectors = np.array(lowest_eigenvectors)
  lowest_eigenvalues = np.array(lowest_eigenvalues)
  

  return lowest_eigenvalues, lowest_eigenvectors


if __name__ == "__main__":
  matrix = np.array([
    [1, 1, 1],
    [1, 2, 0],
    [0, 0, 1]
  ])
  eig_val, eig_vec = lowest_eigenvectors(matrix, 2)
  for i in range(len(eig_val)):
    print(f"lambda{i}={eig_val[i]}")
    print(f"e{i}={eig_vec[:, i]}")

#def lowest_eigenvector(square_matrix, number_of_eigenvectors=3):
#  m, n = square_matrix.shape
  #if m != n:
  #  raise IndexError("Matrix is not square!")

  #values, vectors = np.linalg.eig(square_matrix)
  #values_sorted = np.sort(values)
  #vectors_sorted = vectors[:, values.argsort()]

  #return values_sorted[:number_of_eigenvectors+1], vectors_sorted[:number_of_eigenvectors+1]