class Superficie_circulo:
    pi = 3.14159

    def __init__(self):
        pass

    def area_circ(self):
        radio = float(input("Ingrese el radio del circulo: "))
        superficie = Superficie_circulo.pi * (radio**2)
        print("La superficie del circulo es: {}" .format(superficie))


area = Superficie_circulo()
area.area_circ()
