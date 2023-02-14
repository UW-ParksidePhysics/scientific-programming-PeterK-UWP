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
n = eval(input('input number:'))
array = np.arange(0, n + 1)  # x values
list_of_numbers = []  # y values
for i in array:
    y = i ** 2  # y = x^2
    list_of_numbers.append(y)
print(list_of_numbers)

# plotting, (need these loops above to make plots)
plt.plot(array, list_of_numbers, color='red', label='y = x^2')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend(["y = x^2"], loc="lower right")
plt.title('graph of y = x^2')
plt.savefig('y = x^2')
plt.show()
