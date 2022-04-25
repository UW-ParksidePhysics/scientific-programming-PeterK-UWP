"""
# given a projectile of some mass with initial velocity
#   calculate kinetic, potential and total energy over time
#   (one dimension)

from python.energy import kinetic_energy, gravitational_potential_energy
import numpy as np
import matplotlib.pyplot as plt

projectile_mass = 2.0  # kg
projectile_initial_velocity = 3.0  # m/s
projectile_initial_height = 5.0  # m
standard_gravity = 9.81
# y(t) = y0 + v0*t + 0.5*standard_gravity*t^2

final_time = (projectile_initial_velocity / standard_gravity) \
             + np.sqrt(
    projectile_initial_velocity ** 2 + standard_gravity * projectile_initial_height) / standard_gravity

# print(f' final_time(y0={projectile_initial_height:0.2f} m, v0={projectile_initial_velocity:0.2f} m/s): {final_time:0.2f} s')

times = np.linspace(0., final_time)


# print(times)
# print(len(times))
# print(type(times))  # numpy array


def height(time, initial_height, initial_velocity, acceleration):
    final_height = initial_height + initial_velocity * time + 0.5 * acceleration * time ** 2
    return final_height


# t = 1, h0 = 0, v0 = 0, a = -grav
test_height = height(1, 0, 0, -9.8)
print(f' test_height: {test_height:0.2f} m')

heights = height(times, projectile_initial_height, projectile_initial_velocity, -standard_gravity)
print(f' h_f = {heights[-1]:0.2f} m')


def velocity(time, initial_velocity, acceleration):
    final_velocity = initial_velocity * time * acceleration
    return final_velocity


velocities = velocity(times, projectile_initial_velocity, -standard_gravity)
kinetic_energies = kinetic_energy(projectile_mass, velocities)
potential_energies = gravitational_potential_energy(projectile_mass, heights,
                                                    gravitational_acceleration=standard_gravity)
total_energies = kinetic_energies + potential_energies

plt.plot(times, kinetic_energies, color='red', label='$T$')
plt.plot(times, potential_energies, color='green', label='$U$')
plt.plot(times, total_energies, color='black', label='$E$')
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$E, T, U$ (J)')
plt.legend()
plt.show()

np.matmul  # matrix mult. (optional: (a, b.transpose()), arg: (a, b)
# np.invert()
"""
# Given a projectile of some mass, initial velocity,
#   calculate the kinetic energy, potential energy, and total energy of the projectile over time
#   (in one dimension)
from python.energy import kinetic_energy, gravitational_potential_energy
import numpy as np
import matplotlib.pyplot as plt

projectile_mass = 2.0  # kg
projectile_initial_velocity = 3.0  # m/s
projectile_initial_height = 5.0  # m
standard_gravity = 9.80655  # m/s

## 4/18 class ## may distrupt other code!!!##
planetary_data = {
    'Earth': 9.80655,
    'Mars': 3.71,
}
for planet in planetary_data:
    print(planetary_data[planet])
# print(planetary_data.keys())  # data.keys(), data['Earth']
exit()

def calculate_all_energies(initial_velocity, initial_height, gravitational_acceleration, mass):
    # t_f = v_0 / g + sqrt(v_0^2 + g y_0) / g
    final_time = (initial_velocity / gravitational_acceleration) \
                 + np.sqrt(
        initial_velocity ** 2 + gravitational_acceleration * initial_height) / gravitational_acceleration
    # t = [0, t_f]
    times = np.linspace(0., final_time)
    # h = h(t)
    heights = height(times, initial_height, initial_velocity, -gravitational_acceleration)
    # v = v(t)
    velocities = velocity(times, initial_velocity, -gravitational_acceleration)
    kinetic_energies = kinetic_energy(projectile_mass, velocities)
    potential_energies = gravitational_potential_energy(projectile_mass, heights,
                                                        gravitational_acceleration=gravitational_acceleration)
    total_energies = kinetic_energies + potential_energies
    return kinetic_energies, potential_energies, total_energies

for planet in planetary_data:
    acceleration = planetary_data[planet]
    times, energies = calculate_all_energies(projectile_initial_velocity, projectile_initial_height, acceleration, projectile_mass)
    plot_all_energies(enregies, times)
## 4/18 class end ## may distrupt other code !!! ##

# t_f = v_0 / g + sqrt(v_0^2 + g y_0) / g
final_time = (projectile_initial_velocity / standard_gravity) \
             + np.sqrt(
    projectile_initial_velocity ** 2 + standard_gravity * projectile_initial_height) / standard_gravity

# print(f't_f(y0= {projectile_initial_height:.0f} m, v0 = {projectile_initial_velocity:.0f} m/s) = {final_time:.02f} s')

times = np.linspace(0., final_time)


# print(times)
# print(len(times))
# print(type(times))


def height(time, initial_height, initial_velocity, acceleration):
    final_height = initial_height + initial_velocity * time + 0.5 * acceleration * time ** 2
    return final_height


# time = 1.0 s, initial_height = 0.0, initial_velocity = 0.0 , acceleration = -9.8 m/s^2
# height = 0 + 0*1 +0.5 (-9.8) * 1^2 = -4.9 m

test_height = height(1.0, 0.0, 0.0, -9.8)
print(f'h = {test_height:.1f} m')
heights = height(times, projectile_initial_height, projectile_initial_velocity, -standard_gravity)

def velocity(time, initial_velocity, acceleration):
    final_velocity = initial_velocity + time * acceleration
    return final_velocity


velocities = velocity(times, projectile_initial_velocity, -standard_gravity)
kinetic_energies = kinetic_energy(projectile_mass, velocities)
potential_energies = gravitational_potential_energy(projectile_mass, heights, gravitational_acceleration=standard_gravity)
total_energies = kinetic_energies + potential_energies

plt.plot(times, kinetic_energies, color='red', label=r'$T$')
plt.plot(times, potential_energies, color='green', label=r'$U$')
plt.plot(times,total_energies, color='black', label=r'$E$')
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$E, T, U$ (J)')
plt.legend()
plt.show()