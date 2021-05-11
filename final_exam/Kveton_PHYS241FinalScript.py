import numpy as np


def parse_file_name(file_name):
  #parse_file_name = np.linspace(file_name)
  parse_file_name = file_name[0]+ file_name[1],  file_name[3] + file_name[4] + file_name[5] + file_name[6] + file_name[7], file_name[9] + file_name[10] + file_name[11] + file_name[12] + file_name[13] + file_name[14] + file_name[15]
  return parse_file_name

print(parse_file_name('Al.Fm-3m.GGA.PBE.dat'))

from two_column_text_read import two_column_text_read
array = two_column_text_read("Al.Fm-3m.GGA-PBE.dat")
#print(array)