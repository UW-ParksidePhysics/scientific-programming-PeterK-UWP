"""
taking data (two_column) and fit (eq. of states) and converting their units
"""
 
def convert_volume(value): #, "unit", "new unit"):
  if "unit" != "cubic_bohr_per_atom":
    raise ValueError #(must use "cubic_bohr_per_atom" for "unit")
  elif "new unit" != "cubic_angstrom_per_atom":
    raise ValueError #(must use "cubic_angstrom_per_atom" for "new unit")
  else:
    volume = value * 0.529**3 
  return volume, "new unit"


def convert_energy(value, unit="", new_unit=""):
  if unit="" != rydberg_per_atom:
    raise IndexError("must use rydberg_per_atom for unit")
  elif new_unit="" != "eV_per_atom":
    raise IndexError("must use eV_per_atom for new unit")
  else:
    energy = value * 13.61
  return energy, new_unit=""


def convert_bulk_modulus(value): #, "unit", "new unit"):
  if "unit" != "rydberg_per_cubic_bohr":
    raise ValueError #(must use "rydberg_per_cubic_bohr" for "unit")
  elif "new unit" != "gigapascal":
    raise ValueError #(must use "gigapascal" for "new unit")
  else:
    volume = value * 0.529**3  #Ang^3/atom
    energy = value * 13.61    #eV/atom
    bulk_modulus = energy / volume
  return bulk_modulus, "new unit"

print(convert_energy(10, "rydberg_per_atom", "eV_per_atom")) #, "rydberg_per_atom", "eV_per_atom"))

