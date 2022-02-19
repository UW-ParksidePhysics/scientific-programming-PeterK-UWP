import numpy as np
import matplotlib as mp
import vpython as mp
import cmath as m


def complex_roots(number_of_roots, complex_number):
    angle = np.arctan(b/a)
    modulus = np.sqrt(a**2 + b**2)
    if number_of_roots <= 2:
        two_roots = -(b + (b**2 - (4*a*c))**(1/n))/(2*a)

    elif number_of_roots > 2:
        values = [0,number_of_roots-1]
        for k in values:
            real = m.cos((angle+(2 * k * np.pi)/n))
            imaginary = m.sin((angle + (2 * k * np.pi)/n))

        return real, imaginary

    return complex_roots

complex number = [a, b, c]



#if __name__ == '__main__':

#   a*z**2 + b*z + c = 0
#n = 2
#a = complex(x,y)
#b = complex(x,y)
#c = complex(x,y)
#angle = m.arctan((z.imag/z.real)