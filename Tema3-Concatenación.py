datoUno = "Hola"
datoDos = "Mundo :)"

saludo = datoUno + " " +  datoDos
print(saludo)

print("El saludo es: %s %s" %(datoUno, datoDos))

saludoFinal = "Saludo {1} {0}".format(datoUno, datoDos)
print(saludoFinal)



saludoFinal = "Saludo {a} {b}".format(a = datoUno, b = datoDos)
print(saludoFinal)