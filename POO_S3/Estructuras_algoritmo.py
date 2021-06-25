class Superficie_circulo:

    def __init__(self):
        self.pi = 3.14159

    def area_circ(self):
        radio = float(input("Ingrese el radio del circulo: "))
        superficie = Superficie_circulo.pi * (radio**2)
        print("""La superficie del circulo con un radio de {} es de: {} metros cuadrados""".format(radio, superficie))


area = Superficie_circulo()
area.area_circ()
