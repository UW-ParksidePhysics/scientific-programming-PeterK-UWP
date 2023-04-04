"""
This is meant as an outline for those who need a good place to start with their coding projects.
Before coding make sure you have an equation for your problem, as well as an end goal for your plot.
    ie.) kinematic equations: plotting position, velocity, and acceleration verse time

I highly recommend putting everything in definition statements to make the code easier to read, and run
***You will have to do this for your final, so it is good practice***
"""

# import statements
import numpy as np
import matplotlib.pyplot as plt
import linalg as la

#global variables


# make a definition statement for your equation
def __equation_name__(arg1, agr2, ...):
    """
    Statement takling about what the def statement does
    :param arg1:
    :param agr2:
    :return:
    """
    # <equation>
    <variable> = <equation>
    return <variable>


# generate arrays to plug into your def statement, you can use for loops or linear_algebra code
# for computing these arrays depending on your problem

# for loop
x_values = # here you can use np.range(), or np.linspace() this will most likely be time for many of you
argument_values = [] # you will use this to plug in as an argument into your def
                     # statement and it depends on the x_value above
for i in x_values:
    # compute argument values with an equation
    # append y values to empty list

# linalg
x_values = # here you can use np.range(), or np.linspace() this will most likely be time for many of you
argument_values = # <definition of this argument as a function of x_values>
    # ie.) y = x^2 : argument_values = (x_values)**2 , this will return an array

# do this for your various variables


# plotting
plt.plot(<x_axis_values>, <def_statement_return>, color='red', label='function')
    # main plot(x values, y values, color, label)
plt.xlabel('x values')                                                 # x label
plt.ylabel('y values')                                                 # y label
plt.legend(["function"], loc="lower right")                            # legend (key)
plt.title('your project name')                                         # title of graph
plt.savefig('plot of <your graph>')                                    # saves graph as a png
plt.show()                                                             # display the graph


