from math import *
from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt

N = 100


def n_array(big_n):
    n_ray = []
    for i in range(0, N + 1, 2):
        if i <= N + 1:
            n_ray.append(i)
            # i = n + 2
        elif i > N + 1:
            break
    return n_ray


def factorial(n_input):
    if type(n_input) != int:
        factorial_n_array = []
        fact = 1
        for i in n_input:
            for k in range(1, i + 1):
                fact = fact * k
            factorial_n_array.append(fact)
        return factorial_n_array
    else:
        fact = 1
        for k in range(1, n_input + 1):
            fact = fact * k
        return fact


def probability_function(n_ray_ray):
    probability_array = []
    for i in n_ray_ray:
        probability = (1 / 2 ** N) * (factorial(N)) / (factorial(i) * factorial(N - i))
        probability_array.append(probability)
    return probability_array


# print(n_array(N))
# print(factorial(N))
# print(factorial(n_array(N)))
# print(probability_function(n_array(N)))

plt.plot((n_array(N)), probability_function(n_array(N)), color='black')
plt.xlabel(r'n-value')
plt.ylabel(r'probability')
plt.show()

