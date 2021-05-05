
try:
  infile = open('final_stuff/final_review/volumes_energies.dat', 'r')
  infile.readline()  #skips line "volumes energies"
  infile.readline()  #skips line "----------------"
  print('%12s %12s' %('Volume', 'Energy'))  
  print('-----------------------')

  for line in infile:
   v = float(line.split()[0])
   u = float(line.split()[1])
   print('%12.4f %12.4f' %(v, u))

except OSError as error:
  print(error)
  print('That file was not found')

