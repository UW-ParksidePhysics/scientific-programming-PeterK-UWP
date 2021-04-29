#### RENAME from mini_project.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing mini-project ~ 100-200 words
#
# We will be solving for the currents of a two resistor parallel circuit, given a source voltage
# and the values of the two resistors (as shown bellow). Next we will construct two kirchhoff loops enveloping
# the two resistors, and another around the voltage source and resistor one. These two equations will provide us
# a matrix to which we can solve for the currents flowing through the two resistors. Next, we will take the two
# currents and add them up to produce the total current. With the total current, we can graph it with the source
# voltage, and graph the inverse of the total resistance (conductance). This graph will show the total
# current of the circuit and what happens to the conductance as the total current goes to zero. Plugging in
# any values of voltage and resistance will yield the conductance shown graphically. This grpah will also display
# the other conductances of each resistor as well.
#
#        ___i1__>>_______i2__>>___
#       |            |            |
#       |  +      i3 | +          | +
#      VOLT       \/ R1           R2
#       |  -         | -          | -
#       |____________|____________|
#
#
# 2. Module imports that are used in multiple functions
#
# import numpy, and matplotlib.pyplot
#
# 3. Function definitions
#
# define currents as a matrix
#
# define conductance and power as their simple formulas (see comments)
#

import numpy as np
import matplotlib.pyplot as plt

voltage_source = 6    # inputs
resistor_one = 13
resistor_two = 7
V = [voltage_source]
resistances = [resistor_one, resistor_two]

def calculate_currents(voltage, resistances):
    matrix = np.linalg.inv(np.diag(resistances));
    vector = voltage * np.ones([2, 1]);
    currents = vector * matrix
    return currents

def calculate_conductance(voltage, current):
    # G = I/V
    conductance = current / voltage;
    return conductance

def calculate_power(voltage, current):
    # P = I*V
    power = current * voltage
    return power

currents_get = calculate_currents(voltage_source, resistances)
total_current = currents_get[0][0] + currents_get[1][1]
# currents_get.append(total_current)
# print(currents_get)
# print(total_current)

spaceing = total_current / (voltage_source)
spaceing1 = currents_get[0][0] / (voltage_source)
spaceing2 = currents_get[1][1] / (voltage_source)
Varray = np.linspace(0, 1, voltage_source)
Iarray = [
    np.linspace(0, spaceing, total_current),
    np.linspace(0, spaceing1, currents_get[0][0]),
    np.linspace(0, spaceing2, currents_get[1][1])
]
colors = [
    'r-',
    'b-',
    'g-'
]
currentM = [
    total_current,
    currents_get[0][0],
    currents_get[1][1]
]
labels = [
    'total conductance',
    'conductance R1',
    'conductance R2'
]
Total_Resistance = 1/calculate_conductance(voltage_source, total_current)
Power = calculate_power(voltage_source,total_current)

def plot_conductances(
        Varray, Iarray, voltage_source, current, color, label
):
    for i in Iarray:
        plt(Varray, Iarray, voltage_source, currentM, colors, labels)


print(plot_conductances)
# end
#
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization

