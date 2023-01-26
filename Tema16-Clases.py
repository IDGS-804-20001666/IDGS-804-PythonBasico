class Operasbas():
    # Propiedades de clase
    numeroUno = 0
    numeroDos = 0
    resultado = 0

    # Constructor -> self es equivalente a el this en Java
    def __init__(self, a, b):
        self.numeroUno = a
        self.numeroDos = b

    # Métodos de clase -> Mientras los metodos sean parte de una clase llevan self
    def sumar(self):
        self.resultado = self.numeroUno + self.numeroDos

    def restar(self):
        self.resultado = self.numeroUno - self.numeroDos


def main():
    objOperasBas = Operasbas(3, 4)
    objOperasBas.sumar()
    print("La suma es: {}".format(objOperasBas.resultado))


if __name__ == '__main__':
    main()
