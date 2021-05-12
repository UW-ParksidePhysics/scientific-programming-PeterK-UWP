def convert_units(value_to_convert, units_before_conversion, unit_after_conversion):
  if unit_before_conversion == cubic_bohr_per_atom:
    volume = value_to_convert * 0.529**3('unit_after_conversion') 
    #cubic angstrom^3s/atom

  else unit_before_conversion == rydberg_per_atom:
    energy = value_to_convert * 13.61('unit_after_conversion')
    #eV/atom

  else unit_before_conversion == rydberg_per_cubic_bohr:
    bulk_modulus = energy / volume 
    #eV/atom * atom/angstrom^3 = eV/angstrom^3
 
  return converted_value
 
print(convert_units(10, cubic_bohr_per_atom, 16))