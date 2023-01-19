print('Suma de dos números')
numeroUno = input('Escribe el primer número: ')
numeroDos = input('Escribe el segundo número: ')
resultado = float(numeroUno) + float(numeroDos)

print("La suma de {} + {} = {}".format(numeroUno, numeroDos, resultado))

if (numeroUno > numeroDos):
    print("{} es mayor que {}".format(numeroUno, numeroDos))
else:
    print("{1} es mayor que {0}".format(numeroUno, numeroDos))

print("{} es mayor que {}".format(numeroUno, numeroDos)) if (numeroUno > numeroDos) else print("{1} es mayor que {0}".format(numeroUno, numeroDos))
    
print("\n-- Nuevo Programa :) -- \n")
edad = int(input("Escribe la edad: "))
if(edad > 18):
    print("Mayor de edad")
elif edad == 18:
    print("18 años cariño")
else:
    print("Menor de edad")

'''
    AND, OR, NOT, >, <, <=, ! 
'''

valorUno = 200
valorDos  = 2
valorTres = 1000

if (valorUno > 1000 and valorDos > 2) or valorTres < 2000:
    print("Resultado")