#### RENAME from mini_project.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing mini-project ~ 100-200 words
#
# We will be solving for the currents of a two resistor parallel circuit, given a source voltage
# and the values of the two resistors (as shown bellow). Next we will construct two kirchhoff loops enveloping
# the two resistors, and another around the voltage source and resistor one. These two equations will provide us
# a matrix to which we can solve for the currents flowing through the two resistors. Next, we will take the two
# currents and ad them up to produce the total current (i1). With the total current, we can graph it with the source
# voltage, and graph the inverse of the total resistance (conductance). This graph will show the total
# current of the circuit and what happens to the conductance as the total current goes to zero. Plugging in
# any values of voltage and resistance will yield the conductance shown graphically.
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
# no imports used
#
# 3. Function definitions
#
# function currents = calculate_currents(voltage, resistances):
#    matrix = diag(resistances);
#    vector = voltage * ones([2, 1]);
#    currents = matrix / vector;
# end
#
# function conductance = calculate_conductance(voltage, current)
#    conductance = current / voltage;
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
import numpy as np
import matplotlib.pyplot as plt

def initialize_parameters():
    voltage_source = 6    # inputs (Voltage as whole number)
    resistor_one = 13
    resistor_two = 7
    resistances = [resistor_one, resistor_two]
    return voltage_source, resistances


def calculate_currents(voltage, resistance):
    matrix = np.linalg.inv(np.diag(resistance));
    vector = voltage * np.ones([2, 1]);
    currents = vector * matrix
    return currents


def calculate_conductance(voltage, current):
    conductance = current / voltage;
    return conductance


def calculate_power(voltage, current):
    power = current * voltage
    return power


"""
   this equation... (doc string)
"""


def setup_arrays(voltage_source, resistances):

    currents_get = calculate_currents(voltage_source, resistances)
    total_current = (currents_get[0][0] + currents_get[1][1])
    # currents_get.append(total_current)
    # print(currents_get)
    # print(total_current)

    # spaceing = total_current / voltage_source
    # spaceing1 = currents_get[0][0] / voltage_source
    number_of_points = 100
    # spaceing2 = currents_get[1][1] / voltage_source
    V_array = np.linspace(0, voltage_source, number_of_points)
    I_array = [
        np.linspace(0, total_current, number_of_points),
        np.linspace(0, currents_get[0][0], number_of_points),
        np.linspace(0, currents_get[1][1], number_of_points)
    ]

    currentM = [
        total_current,
        currents_get[0][0],
        currents_get[1][1]
    ]
    return V_array, I_array, currentM


# Total_Resistance = 1/calculate_conductance(voltage_source, total_current)
# Power = calculate_power(voltage_source, total_current)

def plot_conductances(
        v_array, i_array, given_voltage, current
):
    labels = [
        'total conductance',
        'conductance R1',
        'conductance R2'
    ]
    colors = [
        'r',
        'b',
        'g'
    ]


    for i in i_array:
        plt.plot(v_array, i,)        # c=colors[i_array.index(i)], label=labels[i_array.index(i)])
        plt.scatter(given_voltage * np.ones(len(current)), current)
    plt.show()


plt.xlabel('voltage source')
plt.ylabel('total current')
plt.legend('labels')

if __name__ == '__main__':
    voltage_source, resistances = initialize_parameters()
    voltages, currents, max_currents = setup_arrays(voltage_source, resistances)
    plot_conductances(voltages, currents, voltage_source, max_currents)
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

