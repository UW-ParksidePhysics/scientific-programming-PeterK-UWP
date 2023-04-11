"""
This will contain the equations needed for my three plots:
position v time
velocity v time
acceleration v time
mass v time (data allowing)
"""
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

rocket_mass_array = [mass_saturn, mass_falcon, mass_block]
thrust_array = [thrust_saturn, thrust_falcon, thrust_block]


def total_mass(rocket_mass_array):
    payload = 8300  # kg, the largest payload possible that can be used by all three rockets
    total_mass_array = int(rocket_mass_array + payload)
    return total_mass_array


# position as a function of time
def rocket_simulation(total_mass_array, thrust_array):
    gravity = -9.81  # m/s/s
    t = 0
    dt = 0.01
    dm = 0.1
    m = total_mass_array
    position_array = []
    velocity_array = []
    acceleration_array = []
    mass_array = []
    time_array = []
    while m > m - 8300:
        for i in thrust_array:
            acceleration = (i - (m - dm) * gravity) / (m - dm)
            velocity = acceleration * t
            position = velocity * t
            position_array.append(position)
            velocity_array.append(velocity)
            acceleration_array.append(acceleration)
            mass_array.append(m)
            time_array.append(t)
            # dm = dm + 0.1
            m = m - dm
            t = t + dt
    rocket_data = [position_array, velocity_array, acceleration_array, mass_array, time_array]
    return rocket_data


def plot_graphs(rocket_data):
    plt.plot(rocket_data[4], rocket_data[0])
    plt.plot(rocket_data[4], rocket_data[1])
    plt.plot(rocket_data[4], rocket_data[2])
    plt.plot(rocket_data[4], rocket_data[3])
    plt.show()


print(plot_graphs(rocket_simulation(total_mass(rocket_mass_array), thrust_array)))


"""
plot 3 graphs: x vs t, v vs t, a vs t, m vs t.
"""