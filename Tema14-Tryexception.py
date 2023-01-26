numeroUno = 10
numeroDos = 0

try:
  res = numeroUno / numeroDos
except ZeroDivisionError:
  print('Error en el programa')
finally:
    print('Fin del programa (El finally siempre se ejecuta)')