"""Generate Hertzsprung-Russell diagram like:
    https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram#/media/File:HRDiagram.png"""
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

astronomical_unit = 1.495978707e11  # meters
meters_to_light_years = 1. / 9.4607e15


def star_colormap(star_b_minus_vs):
    # Create color map from B-V = -0.33 (#7070ff) to 1.40 (#ff7f7f)
    # yellow = #ffff7f at B-V = 0.81
    number_of_gradient_points = 256
    white_index = int((0.33 / (0.33 + 1.40)) * number_of_gradient_points)
    yellow_index = int(((0.81 + .33) / (0.33 + 1.40)) * number_of_gradient_points)
    print(white_index, yellow_index, number_of_gradient_points)
    color_values = np.ones((number_of_gradient_points, 4))
    # Red values
    color_values[:white_index, 0] = np.linspace(112 / number_of_gradient_points,
                                                255 / number_of_gradient_points,
                                                white_index)
    color_values[white_index:yellow_index, 0] = np.linspace(255 / number_of_gradient_points,
                                                            255 / number_of_gradient_points,
                                                            yellow_index - white_index)
    color_values[yellow_index:, 0] = np.linspace(255 / number_of_gradient_points,
                                                 255 / number_of_gradient_points,
                                                 number_of_gradient_points - yellow_index)
    # Green values
    color_values[:white_index, 1] = np.linspace(112 / number_of_gradient_points,
                                                255 / number_of_gradient_points,
                                                white_index)
    color_values[white_index:yellow_index, 1] = np.linspace(255 / number_of_gradient_points,
                                                            255 / number_of_gradient_points,
                                                            yellow_index - white_index)
    color_values[yellow_index:, 1] = np.linspace(255 / number_of_gradient_points,
                                                 127 / number_of_gradient_points,
                                                 number_of_gradient_points - yellow_index)
    # Blue values
    color_values[:white_index, 2] = np.linspace(255 / number_of_gradient_points,
                                                255 / number_of_gradient_points,
                                                white_index)
    color_values[white_index:yellow_index, 2] = np.linspace(255 / number_of_gradient_points,
                                                            127 / number_of_gradient_points,
                                                            yellow_index - white_index)
    color_values[yellow_index:, 2] = np.linspace(127 / number_of_gradient_points,
                                                 127 / number_of_gradient_points,
                                                 number_of_gradient_points - yellow_index)
    new_colormap = ListedColormap(color_values)

    # Scale B-V values from 0 to 1
    scaled_b_minus_vs = (star_b_minus_vs - np.amin(star_b_minus_vs)) / (
            np.amax(star_b_minus_vs) - np.amin(star_b_minus_vs))

    return scaled_b_minus_vs, new_colormap


def parallax_to_distance(parallax):
    """Take parallax in milliarcseconds and convert to distance in meters"""
    parallax_in_radians = (parallax / 1000. / 3600.) * (2 * np.pi / 360.)
    distance = astronomical_unit / np.tan(parallax_in_radians)
    return distance


def apparent_to_absolute_magnitude(apparent_magnitude, distance):
    """Calculate absolute magnitude from apparent magnitude and distance in meters"""
    distance_in_parsecs = distance / (648000. * astronomical_unit / np.pi)
    absolute_magnitude = apparent_magnitude - 5 * np.log10(distance_in_parsecs) + 5
    return absolute_magnitude


def read_file(filename):
    """Read four column data from HIPPARCOS satellite and return a nested dictionary"""
    # Read in as nested dictionary
    infile = open(filename, 'r')
    hipparcos_read = infile.readlines()
    hipparcos_dictionary = {}
    for line in hipparcos_read:
        values = line.split()
        star_catalog_number = float(values[0])
        parallax = float(values[1])
        apparent_magnitude = float(values[2])
        blue_minus_visual = float(values[3])
        hipparcos_dictionary[star_catalog_number] = \
            {'parallax': parallax, 'apparent_magnitude': apparent_magnitude,
             'blue_minus_visual': blue_minus_visual}
    infile.close()
    return hipparcos_dictionary


# Apply read function to the data file and produce a nested dictionary
hipparcos_dictionary_read = read_file('hipparcos_data.txt')  # list, each term inside is also a list, values are float
# Loop over star catalog number key
star_absolute_magnitudes = []
star_b_minus_vs = []
parallax_value = []
a = np.arange(1, 1038, 1)
"""
for value in a:
    p_value = parallax_to_distance(hipparcos_dictionary[value][1])
    a_value = apparent_to_absolute_magnitude(hipparcos_dictionary[value][2],
                                             parallax_to_distance(hipparcos_dictionary[value][1]))
    parallax_value.append(p_value)
    star_absolute_magnitudes.append(a_value)
#       Call parallax_to_distance on parallax value and assign to new value
#       Call apparent_to_absolute_magnitude on apparent magnitude value and assign to new value
#       Append absolute magnitude for current star into NumPy array of absolute magnitudes
#           named star_absolute_magnitudes = []
#       Append B-V value for current star into NumPy array of B-V values
#           named star_b_minus_vs = []
"""
print(hipparcos_dictionary_read)
print(parallax_value)
print(star_absolute_magnitudes)
# Use dark style for plot
plt.style.use('dark_background')

# Reverse the absolute magnitude so that negative values appear on top
star_absolute_magnitudes = np.negative(star_absolute_magnitudes)

# Get color map to match star colors
scaled_b_minus_v, hr_diagram_colormap = star_colormap(star_b_minus_vs)

# Create axes labels
plt.xlabel('Colour (B-V)')
plt.ylabel('Luminosity (Sun=1)')
# Make the axes identical to the model figure referenced at the top of this file

# Define the scatter marker size in points squared (make it similar to the model figure)

# Scatter plot of B-V vs absolute magnitude
plt.scatter(star_b_minus_vs, star_absolute_magnitudes, c=scaled_b_minus_v, cmap=hr_diagram_colormap)
plt.show()
