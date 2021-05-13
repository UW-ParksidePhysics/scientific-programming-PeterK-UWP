from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from convert_units import convert_units
from numpy import linspace
import matplotlib.pyplot as plt


display_graph = True 

def parse_file_name(file_name):
  to_parse = file_name.split(".")
  symbol = to_parse[0]
  structure = to_parse[1]
  acronym = to_parse[2]
  return symbol, structure, acronym


file_name = "Al.Fm-3m.GGA-PBE.dat"
symbol, structure, acronym = parse_file_name(file_name)
array = two_column_text_read("Al.Fm-3m.GGA-PBE.dat")
statistics = bivariate_statistics(array)
quadratic_coefficients = quadratic_fit(array)
quadratic_coefficients = [quadratic_coefficients[0], quadratic_coefficients[1]]
print(quadratic_coefficients)


undo_array = zip(*array)
array_2 = list(undo_array)

fit_eos_curve, bulk_modulus = fit_eos(array_2[0], array_2[1], quadratic_coefficients,                                         eos='murnaghan', number_of_points=50)

#print(array)
#mean_of_y, standard_deviation_of_y, x_min, x_max, y_min, y_max
#print(statistics)
min_x = statistics[2]
max_x = statistics[3]

#print(fit_eos, bulk_modulus)

def annotate_graph(symbol, structure):
  ax.annotate(symbol, xy=(min(array_2[1]) - (min(array_2[0]) * 0.07), 
                          max(array_2[1]) + max(array_2[0]) * 0.00007))

  ax.annotate(r'$ {}\overline{{{}}} {}$'.format(structure[0:2],
                                                structure[3], 
                                                structure[1]), 
              xy=(eq_vol, (max(array_2[1]) + min(array_2[1])) / 2))

  ax.annotate('K_0={:.6f}GPa'.format(bulk_modulus_gpa), 
              xy=(eq_vol, (max(array_2[1]) + min(array_2[1])) / 1.99997))

  ax.annotate('V_0={:.3f}A^3/atom'.format(eq_vol), 
              xy=(eq_vol, (max(array_2[1]) + min(array_2[1])) / 2.00001))
  plt.axvline(eq_vol - array_2[0][array_2[1].index(min(array_2[1]))] * 0.01, color="black", linestyle='--')

  plt.text(83.5226, -1032.86, "created by Peter Kveton May/12/21")
  plt.title("{} Equationof State for {} in DFT {}".format('murnaghan, symbol, acronym'))
  return ax, plt

fig = plt.figure()
ax = fig.add_subplot(111)


volumes = linspace(min(array_2[0]), max(array_2[0]), len(fit_eos_curve))
line1, = ax.plot(array_2[0], array_2[1], 'o')  # 8
line2, = ax.plot(volumes, fit_eos_curve, color="black")

x_min = (min(array_2[0]) - (min(array_2[0]) * 0.10))
x_max = (max(array_2[0]) + (max(array_2[0]) * 0.10))
y_min = (min(array_2[1]) - (min(array_2[0]) * 0.00010))
y_max = (max(array_2[1]) + (max(array_2[0]) * 0.00010))

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r'$ \mathit{Å^3/atom}\ $')
plt.ylabel(r'$ \mathcal{eV/atom}\ $')
bulk_modulus_gpa = convert_units(bulk_modulus, "rb/cb")
eq_vol = array_2[0][array_2[1].index(min(array_2[1]))]
annotate_graph(symbol, structure)
if display_graph:  # 10
    plt.show(display_graph)
elif not display_graph:
    plt.savefig("Peter.Al.Fm-3m.GGA-PBEsol.murnaghanEquationOfState.png")



fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
plot_graph = (plot_data_with_fit(array, fit_curve, data_format="bo", fit_format="k")) #scatter_plot, curve_plot

#plt.savefig("plot.png")
###########################################
from generate_matrix import generate_matrix
from lowest_eigenvectors import lowest_eigenvectors
from numpy import linspace
import matplotlib.pyplot as plt


display_graph = False
potential_name = 'harmonic'
N_dim = 120
potential_parameter = 100

matrix = generate_matrix(-10, 10, N_dim, potential_name, potential_parameter) 
#print(matrix)
eigenvalues, eigenvectors = lowest_eigenvectors(matrix, 3)

x = linspace(-10, 10, N_dim)  # 3
line1, = plt.plot(x, eigenvectors[0][0:N_dim])  # 4
line2, = plt.plot(x, eigenvectors[1][0:N_dim])  # 4
line3, = plt.plot(x, eigenvectors[2][0:N_dim])  # 4

plt.xlabel("x [a.u.]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.legend((line1, line2, line3), ('ψ1, Ε1 = 0.62414396 a.u.', 'ψ2, Ε2 = 0.87335307 a.u.', 'ψ3, Ε3 = 1.12229893 a.u.'))
plt.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])
plt.axhline(color="black")  # 5
plt.text(-9.5, -1.75, "Created by Peter Kveton May/12/21")  # 6
plt.title("Select Wavefunctions for a Harmonic Potential on a Spatial Grid of 0, 1, 2 Points")  # 7


if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Kveton.harmonic.Eigenvector0, 1, 2.png")
