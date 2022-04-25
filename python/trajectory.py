from math import *

horizontal_range = eval(input('range:'))  # try, 2.5m
launch_angle = eval(input('angle:'))  # try, 60degree
initial_velocity = eval(input('v0:'))  # try, 15km
initial_height = eval(input('y0'))  # try, 1.0m


def calculate_height(horizontal_displacement, angle, starting_velocity, starting_height,
                     gravitational_acceleration=9.80665):
    height = horizontal_displacement * tan(angle) \
             - 1 / (2 * starting_velocity ** 2) * gravitational_acceleration + horizontal_displacement ** 2 / (
                         cos(angle) ** 2) \
             + starting_height
    return height


projectile_height = calculate_height(horizontal_range, launch_angle, initial_velocity, initial_height,
                                     )
# print(f'{projectile_height} m ')

# from sys import argv

# for index, argument in enumerate(argv):  # enumerate returns
# print(f'i, arg = {index}, {argument}')

# (argv): > 1:
gravitational_acceleration = float(input('gravity value='))
initial_velocity = 1.0  # m/s
time = 1.0  # s
final_velocity = initial_velocity + gravitational_acceleration * time
print(f'v(t={time} s, g={gravitational_acceleration}) = {final_velocity:.2f} m/s')

#  typeerror: float, integer list, boolean

x = eval(input('x='))
y = x**2
print(y)