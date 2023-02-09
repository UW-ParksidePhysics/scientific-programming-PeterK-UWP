import numpy as np
import matplotlib.pyplot as plt
"""
In this code, we will look into using a simple for loop to graph a plot using matplotlib
we will also look into f-formatting to make the output cleaner.
 - formatting
 - for loop
 - plot
"""
# for loop
n = eval(input('input number:'))
array = np.arange(0, n + 1)     # x values
list_of_numbers = []            # y values
for i in array:
    y = i ** 2     # y = x^2
    list_of_numbers.append(y)
print(list_of_numbers)

# plotting, (need these loops above to make plots)
plt.plot(array, list_of_numbers)
plt.show()