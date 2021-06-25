class EstructuraSecuenciales:
    def __init__(self):
        pass
    
    def Secuencial_1(self):
        subtotal = float(input("Ingrese el total de la compra: "))
        Descuento = subtotal * 0.15
        total = subtotal-Descuento
        print("""El subtotal de la compra es {},su descuento es de {}, su valor a pagar es {}""" .format(subtotal, Descuento, total))
    
    def Secuencial_2(self):
        Sueldo_Base = float(input("Ingrese su sueldo base: "))
        venta1 = float(input("Ingrese el valor de venta 1: "))
        venta2 = float(input("Ingrese el valor de venta 2: "))
        venta3 = float(input("Ingrese el valor de venta 3: "))
        Ventas = venta1 + venta2 + venta3
        Comision = Ventas * 0.10
        Pago_total = Sueldo_Base + Comision
        print("""
        Comision venta 1 : {}
        Comision venta 2 : {}
        COmision venta 3 : {}""".format(venta1, venta2, venta3)
        print("Su sueldo base es {}, mas las ventas realizadas {}, usted recibirá un total {}" .format(Sueldo_Base, Ventas, Pago_total))

if __name__ == "__main__":
    Secuencia = EstructuraSecuenciales()
    Secuencia.Secuencial_1()
    Secuencia.Secuencial_2()
