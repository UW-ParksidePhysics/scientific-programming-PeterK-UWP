import numpy as np


def quadratic_fit(array):
  
  undo_array = zip(*array)
  array_2 = list(undo_array)



  quadratic_coefficients = np.polyfit(array_2[0], array_2[1], 2)

  return quadratic_coefficients

  if __name__ =='__main__':
    print(quadratic_fit(sys.argv[1]))