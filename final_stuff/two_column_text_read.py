"""
This function reads a readable file inputed into it. In this case(volumes_energies). It will then arrange the values into two data sets and continues this process until the list is complete
__author__ = "Peter & Lena"
"""

import numpy as np


def two_column_text_read(file_name):

  try:
    file = open (file_name)  
  except OSError as error:
    print(error)
    return

  content = file.readlines()
  data = np.zeros([2, (len(content))], float)
  n = 0

  for line in content:
    elements = line.split()
    data[0, n] = float(elements[0])
    data[1, n] = float(elements[1])
    n += 1
    
  return data


#try:
#  infile = open('final_stuff/final_review/volumes_energies.dat', 'r')
#  infile.readline()  #skips line "volumes energies"
#  infile.readline()  #skips line "----------------"
#  print('%12s %12s' %('Volume', 'Energy'))  
#  print('-----------------------')

#  for line in infile:
#   v = float(line.split()[0])
#   u = float(line.split()[1])
#   print('%12.4f %12.4f' %(v, u))

#except OSError as error:
#  print(error)
#  print('That file was not found')



 


