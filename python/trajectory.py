from math import *
horizontal_range = eval(input('range:'))  # try,
launch_angle = eval(input('angle:'))  # try,
initial_velocity = eval(input('v0:'))  # try,
initial_height = eval(input('y0'))  # try,
standard_gravity = 9.81


def calculate_height(horizontal_displacement, angle, starting_velocity, starting_height):
    height = horizontal_displacement * tan(angle) \
             - 1 / (2 * starting_velocity ** 2) * standard_gravity + horizontal_displacement ** 2 / (cos(angle) ** 2) \
             + starting_height
    return height


projectile_height = calculate_height(horizontal_range, launch_angle, initial_velocity, initial_height)
print(f'{projectile_height} m ')

