"""
    Las tuplas son estructuras de datos propios de python (de los pocos lenguajes que las usan), 
    permiten almacenar distintos valores, no se pueden reemplazar sus datos
"""

tupla = (1, 2, 3, "Veintitrés")

print(tupla)

tuplaDos = (7, "Abril", True, 12.5, 23+7j)

tuplaTres = (1, 2, 3, (2, 0, 2, 2))


print(tuplaDos[1])

print(tuplaTres[3])

print(tuplaTres[2:])

tuplaNueva = tupla + tuplaDos

print(tuplaNueva)