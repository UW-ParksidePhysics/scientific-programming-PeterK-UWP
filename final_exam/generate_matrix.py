def generate_matrix(minimum_x, maximum_x, number_of_dimensions, potential_name, potential_parameter):
    """
    Generates an NxN Hamiltonian matrix for a one-dimensional potential on a spatial grid
    :param minimum_x:               float :: left endpoint of the spatial grid
    :param maximum_x:               float :: right endpoint of the spatial grid
    :param number_of_dimensions:    int :: N, number of dimensions of the matrix and number of grid points of grid
    :param potential_name:          str :: name of potential to use ('harmonic', 'sinusoidal', 'square')
    :param potential_parameter:     float :: single parameter to adjust potential (affects magnitude of potential)
    :return:                        NumPy array (N,N) :: Hamiltonian matrix created from potential
    """
    import numpy as np

    hbar = 1.0
    mass = 1.0

    grid_spacing = (maximum_x - minimum_x)/(number_of_dimensions - 1)
    units_prefactor = hbar**2 / (2 * mass * grid_spacing**2)

    horizontal_grid = np.linspace(minimum_x, maximum_x, num=number_of_dimensions)
    if potential_name == 'harmonic':
        angular_frequency = potential_parameter * hbar / (mass * (maximum_x - minimum_x)**2)
        reduced_potential = 0.5 * mass * np.power(angular_frequency * horizontal_grid, 2) / units_prefactor

    elif potential_name == 'sinusoidal':
        well_width = (maximum_x - minimum_x)
        wave_vector = np.pi / well_width
        pre_factor = 5 * potential_parameter * hbar**2 / (2. * mass * well_width**2)
        reduced_potential = pre_factor * np.sin(wave_vector * horizontal_grid) / units_prefactor

    elif potential_name == 'square':
        well_width = (maximum_x - minimum_x) / 2.
        well_depth = potential_parameter * well_width
        number_of_well_points = int(number_of_dimensions / 2.)
        number_of_outside_points = int(number_of_dimensions / 4.)
        reduced_potential = horizontal_grid
        reduced_potential[0:number_of_outside_points] = well_depth
        reduced_potential[number_of_well_points+number_of_outside_points:] = well_depth
        reduced_potential /= units_prefactor

    else:
        horizontal_grid = np.linspace(minimum_x, maximum_x, num=number_of_dimensions)
        reduced_potential = 0. * horizontal_grid

    off_diagonal_terms_array = -1. * np.ones(number_of_dimensions-1)
    diagonal_terms_array = np.full(number_of_dimensions, 2) + reduced_potential

    matrix_one = np.diagflat(off_diagonal_terms_array, -1)
    matrix_two = np.diagflat(diagonal_terms_array)
    matrix_three = np.diagflat(off_diagonal_terms_array, 1)

    matrix_total = units_prefactor*(matrix_one + matrix_two + matrix_three)

    return matrix_total

