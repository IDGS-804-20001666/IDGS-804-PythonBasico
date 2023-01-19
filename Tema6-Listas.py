listaUno = ["Hassel", 1.2, 23, True]
listaUnoDef = list


print(listaUno)
print(listaUno[:])
print(listaUno[2:4])
print(listaUno[:2])
print(listaUno[3:])


listaUno.append("Jessica <3")

print(listaUno)

listaUno.insert(0, "23/04")

print(listaUno)

listaUno.extend([23, 4, 22])

print(listaUno)

print(listaUno.index("Jessica <3"))

listaUno.remove("23/04")

print(listaUno)

listaUno.pop()

print(listaUno)

