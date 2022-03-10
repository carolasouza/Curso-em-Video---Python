n = input('Digite algo: ')

print('\n- Tipo primitivo: {} '
      '\n- É decimal: {} '
      '\n- É numérico: {} '
      '\n- É alfabético: {} '
      '\n- É alfa-numérico: {} '.format(type(n), n.isdecimal(), n.isnumeric(), n.isalpha(), n.isalnum()))
