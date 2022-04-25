# calculate kinetic and potential energy
#   (one dimensional, one particle)

import numpy as np


def kinetic_energy(mass, velocity):
    """
    T = (1/2)mv^2
    :return: T (float)
    """
    kinetic = 0.5 * mass * velocity**2
    return kinetic


def gravitational_potential_energy(mass, height, gravitational_acceleration=9.81):
    """
    U_g = mgh
    :return: U_g (float)
    """
    potential = mass * gravitational_acceleration * height
    return potential


if __name__ == '__main__':
    print('running')
    test_mass = 2.0  # kg
    test_speed = 3.0  # m/s
    test_kinetic = kinetic_energy(test_mass, test_speed)
    test_height = 5.0  # m
    test_potential = gravitational_potential_energy(test_mass, test_height)
    print(f' kinetic energy = {test_kinetic:0.2f}, potential energy = {test_potential:0.2f}')
