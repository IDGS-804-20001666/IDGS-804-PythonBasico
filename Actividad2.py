import os


class Operasbas():
    # Propiedades de clase
    numeroUno = 0
    numeroDos = 0
    resultado = 0

    # Constructor
    def __init__(self, a, b):
        self.numeroUno = a
        self.numeroDos = b

    # Métodos de clase
    def sumar(self):
        self.resultado = self.numeroUno + self.numeroDos

    def restar(self):
        self.resultado = self.numeroUno - self.numeroDos

    def multiplicar(self):
        self.resultado = self.numeroUno * self.numeroDos

    def dividir(self):
        self.resultado = self.numeroUno / self.numeroDos


def main():
    os.system('cls')
    opcion = 1
    while opcion >= 1 and opcion <= 4:
        print('Selecciona una opción: ')
        print('1.- Sumar ')
        print('2.- Restar ')
        print('3.- Multplicar ')
        print('4.- Dividir ')
        print('Presione cualquier otra tecla para salir')
        opcion = int(input('Escribe la opción: '))
        if (opcion >= 1 and opcion <= 4):
            numero1 = int(input('Escribe el primer número: '))
            numero2 = int(input('Escribe el segundo número: '))
            objOperasBas = Operasbas(numero1, numero2)
            if opcion == 1:
                objOperasBas.sumar()
            elif opcion == 2:
                objOperasBas.restar()
            elif opcion == 3:
                objOperasBas.multiplicar()
            elif opcion == 4:
                objOperasBas.dividir()
            print("El resultado es: {} \n".format(objOperasBas.resultado))
        else:
            os.system('cls')
            break

if __name__ == '__main__':
    main()
