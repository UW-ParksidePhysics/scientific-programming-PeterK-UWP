from math import *
horizontal_range = eval(input('range:'))  # try, 2.5m
launch_angle = eval(input('angle:'))  # try, 60degree
initial_velocity = eval(input('v0:'))  # try, 15km
initial_height = eval(input('y0'))  # try, 1.0m


def calculate_height(horizontal_displacement, angle, starting_velocity, starting_height,
                     gravitational_acceleration=9.80665):
    height = horizontal_displacement * tan(angle) \
             - 1 / (2 * starting_velocity ** 2) * gravitational_acceleration + horizontal_displacement ** 2 / (cos(angle) ** 2) \
             + starting_height
    return height


projectile_height = calculate_height(horizontal_range, launch_angle, initial_velocity, initial_height,
                                     )
print(f'{projectile_height} m ')

