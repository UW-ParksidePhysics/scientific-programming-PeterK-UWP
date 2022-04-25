import numpy as np
import matplotlib as mp
import vpython as vp
import cmath as m


complex_function = [
    [a][z2], [b][z1], [c][z0]
]
def complex_roots(number_of_roots, complex_function):
    angle = np.arctan(b / a)
    modulus = np.sqrt(a ** 2 + b ** 2)
    if number_of_roots <= 2:
        two_roots = -(b + (b ** 2 - (4 * a * c)) ** (1 / n)) / (2 * a)

    elif number_of_roots > 2:
        values = [0, number_of_roots - 1]
        for k in values:
            real = m.cos((angle + (2 * k * np.pi) / number_of_roots))
            imaginary = m.sin((angle + (2 * k * np.pi) / number_of_roots))

        return real, imaginary

    return complex_roots

np.plot(circle(radius=modulus))

if __name__ == '__main__':

#   a*z**2 + b*z + c = 0
# n = 2
# a = complex(x,y)
# b = complex(x,y)
# c = complex(x,y)
# angle = m.arctan((z.imag/z.real)
