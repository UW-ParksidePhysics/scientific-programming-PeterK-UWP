"""
This will contain the equations needed for my three plots:
position v time
velocity v time
acceleration v time
mass v time (data allowing)
"""
import numpy as np
import matplotlib.pyplot as plt
# some constants (will eventually be moved to a text file)
# Saturn V
mass_saturn = 2800000  # kg
thrust_saturn = 34500000  # N
# Falcon 9
mass_falcon = 540054  # kg
thrust_falcon = 7607000  # N
# SLS Block 1
mass_block = 26082156  # kg
thrust_block = 3991613  # N  !!! fact check this !!!

rocket_mass_array = np.array([mass_saturn, mass_falcon, mass_block])
thrust_array = np.array([thrust_saturn, thrust_falcon, thrust_block])
payload = 8300  # kg, the largest payload possible that can be used by all three rockets
print(f'rocket_array: {type(rocket_mass_array)}')
print(f'thrust_array: {type(thrust_array)}')


def total_mass(rocket_mass_array):
    total_mass_array = rocket_mass_array + payload
    return total_mass_array


# position as a function of time
def rocket_simulation(total_mass_array, thrust_array):
    gravity = -9.81  # m/s/s
    dm = 0.1
    # a = thrust - totalmass - dm * gravity / totalmass - dm
    acceleration_array = thrust_array - ((total_mass_array - dm) * gravity) / (total_mass_array - dm)
    for mass in total_mass_array:
        while mass > mass - payload:
            mass = mass - dm
    return acceleration_array


def plot_graphs(rocket_data):
    plt.plot(rocket_data[4], rocket_data[0])
    plt.plot(rocket_data[4], rocket_data[1])
    plt.plot(rocket_data[4], rocket_data[2])
    plt.plot(rocket_data[4], rocket_data[3])
    plt.show()


print(f'total_mass_array: {type(total_mass(rocket_mass_array))}')
print(f' acceleration_array: {rocket_simulation(total_mass(rocket_mass_array), thrust_array)}')


"""
plot 3 graphs: x vs t, v vs t, a vs t, m vs t.
"""