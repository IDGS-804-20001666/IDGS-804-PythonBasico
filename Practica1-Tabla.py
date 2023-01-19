numero = int(input('Escribe el número: '))

def generarTabla(numero):
    for x in range(0, 11):
        result = x * numero
        print("{} x {} = {}".format(numero, x, result))

generarTabla(numero)
