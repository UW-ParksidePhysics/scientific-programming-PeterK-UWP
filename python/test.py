# from trajectory file
from sys import argv
# argv: arguments in command line (list)
# with: can be used to avoid open and close function, with will close file without the need for the close command
for index, argument in enumerate(argv):  # enumerate returns
    print(f'i, arg = {index}, {argument}')

if len(argv): > 1:
    gravitational_acceleration = argv[1]
    initial_velocity = 1.0  # m/s
    time = 1.0  #s
    final_velocity = initial_velocity + gravitational_acceleration * time
    print(f'v(t={time} s, g={gravitational_acceleration}) = {final_velocity:.2f} m/s')

#  typeerror: float, integer list, boolean

### reading in a list ###
# from urllib import request
# url = ' insert url here '
# with request.urlopen(url) as file:
#    print(file.read())

