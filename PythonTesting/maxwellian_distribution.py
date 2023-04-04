"""
Lets plot a distribution function with various energies taking k_b*T to be the energy in eV represented by E
"""
import numpy as np
import matplotlib.pyplot as plt

temperatures = np.linspace(0, 2.0 * 10 ** 9, 1000)  # 150million - 200million C


# 1.5 * 10 ** 8, 2.0 * 10 ** 9, 100


def distribution(temperature_array):
    """
    the distribution function requires an energy E and a velocity v. Electrons and Ions have typical thermal velocities
    for Maxwellian Distributions, and depend on the energy. v = (E/m)^1/2, we will assume the electrons and ions, have
    a constant shared temperature (room for small fluctuations)
    v_e = 4.19x10^7 T^1/2 cm/s = 4.19x10^5 T^1/2 m/s: T = E/k_b
    v_i = 9.79x10^5 T^1/2 cm/s = 9.79x10^3 T^1/2 m/s: T = E/k_b
    """
    boltzmann_constant = 8.62 * 10 ** -5
    m_i = 1.67 * 10 ** -27
    m_e = 9.11 * 10 ** -31
    m_t = m_i + m_e
    energy_array = temperature_array * boltzmann_constant
    electron_velocity_array = 4.19 * 10 ** 5 * temperature_array ** (1 / 2)
    ion_velocity_array = 9.79 * 10 ** 3 * temperature_array ** (1 / 2)
    velocities = [electron_velocity_array, ion_velocity_array]
    density_of_particles = 10 ** 6
    y_values = []
    for v in velocities:
        f = density_of_particles * (m_t / (2 * np.pi * energy_array)) ** (1 / 2) * np.e ** (
                -m_t * v ** 2 / (2 * energy_array))
        # f = (m_t / (2 * np.pi * energy_array)) ** (3 / 2) * 4 * np.pi * v ** 2 * \
        #    np.e ** (-m_t * v ** 2 / (2 * energy_array))
        y_values.append(f)
    return velocities, y_values


def plot_distribution(velocity_array, y_values):
    for v in velocity_array:
        plt.plot(velocity_array, y_values)
    plt.xlabel('velocity')
    plt.ylabel('f(v)')
    plt.show()


import numpy as np


def quadratic_fit(velocity_array, y_values):
    electron_velocity_values = velocity_array[0]
    ion_velocity_values = velocity_array[1]
    electron_quadratic_coefficients = np.polyfit(electron_velocity_values, y_values, 2)
    ion_quadratic_coefficients = np.polyfit(ion_velocity_values, y_values, 2)
    quadratic_coefficients = [electron_quadratic_coefficients, ion_quadratic_coefficients]
    return quadratic_coefficients


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
    if max_x < min_x:  # max values cannot be less than min values
        raise ArithmeticError
    if number_of_points <= 2:  # need more than 2 points
        raise IndexError

    x_array = np.linspace(min_x, max_x, number_of_points)  # 2 parameters
    y_array = np.polyval(quadratic_coefficients, x_array)  #
    fit_curve = np.array((x_array, y_array))  # np.column_stack((x_array, y_array))

    return fit_curve


print(plot_distribution(distribution(temperatures)[0], distribution(temperatures)[1]))
