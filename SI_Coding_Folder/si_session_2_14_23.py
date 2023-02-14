"""
Today we will be creating a for loop and using the loop to create graphs
we will then format the graphs to make them more refurbished
 - for loop intro
 - creating a graph
 - formatting
"""
import numpy as np
import matplotlib.pyplot as plt

# for loop
n = eval(input('input number:'))     # this will prompt you with a max x value for the graph
array = np.arange(0, n + 1)          # x values (need n above to work)
list_of_numbers = []                 # y values,  empty list that we will append values to
for i in array:                      # for loop, 'i' can be any variable/word (whatever you want)
    y = i ** 2                       # y = x^2, function to loop over with our x values
    list_of_numbers.append(y)        # appending y values to list
print(list_of_numbers)               # not necessary but shows our code works

# plotting, (need these loops above to make plots)
plt.plot(array, list_of_numbers, color='red', label='y = x^2')     # main plot(x values, y values, color, label)
plt.xlabel('x values')                                             # x label
plt.ylabel('y values')                                             # y label
plt.legend(["y = x^2"], loc="lower right")                         # legend (key)
plt.title('graph of y = x^2')                                      # title of graph
plt.savefig('y = x^2')                                             # saves graph as a png
plt.show()                                                         # display the graph
