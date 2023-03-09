import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


def build_array():
    period_one = 365 * 24 * 60 * 60      # sec
    period_two = 24 * 60 * 60            # sec
    delta_time = period_two / 10
    time_array = np.arange(0, period_one + 1, delta_time)
    depth_array = np.linspace(0, 20, len(time_array))
    return depth_array, time_array

# function for temperature
def temperature(depth_array, time_array):
    period_one = 365 * 24 * 60 * 60  # sec
    period_two = 24 * 60 * 60  # sec
    thermal_diffusivity = 1E-6           # m^2/s
    amplitude_one = 15                   # degreesC
    amplitude_two = 7                    # degreesC
    omega_one = 2 * np.pi / period_one   # hz
    omega_two = 2 * np.pi / period_two   # hz
    alpha_one = np.sqrt(omega_one / 2 * thermal_diffusivity)  # 1/m^2
    alpha_two = np.sqrt(omega_two / 2 * thermal_diffusivity)  # 1/m^2
    initial_temperature = 0
    function = initial_temperature + amplitude_one * np.e**(-alpha_one * depth_array) * np.sin(omega_one * time_array -
                                                                                         alpha_one * depth_array)
    + amplitude_two * np.e**(-alpha_two * depth_array) * np.sin(omega_two * time_array - alpha_two * depth_array)

    return function


frame = np.linspace(initial_time, final_time, intervals)
def update(frames):


def animate(final_time, delta_time, depth, function_array):


if __name__ == "__main__":
    print(temperature(build_array()[0], build_array()[1]))
