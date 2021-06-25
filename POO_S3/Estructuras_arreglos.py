class arrays:
    def __init__(self):
        pass

    def ordenar(self):
        numeros = []
        positivos = []
        negativos = []
        print(len(numeros))
        for i in range(0, 20):
            num = int(input("Ingrese la nota de los examenes: "))
            numeros.append(num)
            while num == 0:
                print("Numero 0, no es positivo ni negativo")
                num = int(input("Ingrese la nota de los examenes: "))
                numeros.append(num)
        for i in numeros:
            if i > 0:
                positivos.append(i)
            else:
                negativos.append(i)
        if len(positivos) == 0:
            print("No hay numeros positivos")

        elif len(negativos) == 0:
            print("No hay numeros negativos")
        print("Numeros positivos :", positivos)
        print("Numeros negativos :", negativos)


Numeros = arrays()
Numeros.ordenar()
