import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import lxml.html
# import modulus and strength to get stress and strain

url = 'http://www-materials.eng.cam.ac.uk/mpsite/short/OCR/ropes/default.html'
length = 10


def read_webpage(link):
    webdata = pd.read_html(link)
    rope_data = webdata[6]
    return rope_data


def stress(strains, modulus):
    stress = modulus * strains
    return stress


def strain(stress, modulus):
    strain = stress / modulus
    return strain


def calculate_stress_and_strain(youngs_moduli_array, yield_strength_array):
    stress_array = []
    strain_array = []
    for index in range(len(youngs_moduli_array)):
        yield_strength = yield_strength_array[index]
        E = youngs_moduli_array[index]
        maximum_strain = strain(yield_strength, E)
        delta_length = np.linspace(0, maximum_strain)
        epsilon = delta_length / length
        strain_array.append(epsilon)
        sigma = E * epsilon
        stress_array.append(sigma)
    return stress_array, strain_array


def plot_stress_strain(stress_data, strain_data):
    for epsilon, sigma in zip(strain_data, stress_data):
        plt.plot(epsilon, sigma)
    plt.show()
    return


if __name__ == '__main__':
    # url link troubleshoot:
    print(read_webpage(url))
    # df = pd.read_html(url)
    # print(type(df))
    # print(len(df))
    # plot_stress_strain()
